// Production-Grade Cloudflare Worker for Evrika Liseyi
// Handles Authoritative Registrations, Orders, Payments, Payment Events, and Epoint Gateway Integration

const PUBLIC_KEY = "i000201608";
const DEFAULT_PRIVATE_KEY = "HNIbtyFLu3PbxXlVykJEwOR1";

// Helper: UTF-8 safe Base64 encode
function utf8ToBase64(str) {
  const bytes = new TextEncoder().encode(str);
  let binary = "";
  for (let i = 0; i < bytes.length; i++) binary += String.fromCharCode(bytes[i]);
  return btoa(binary);
}

// Helper: UTF-8 safe Base64 decode
function base64ToUtf8(b64) {
  const binary = atob(b64);
  const bytes = new Uint8Array(binary.length);
  for (let i = 0; i < binary.length; i++) bytes[i] = binary.charCodeAt(i);
  return new TextDecoder().decode(bytes);
}


// Helper: Calculate Epoint SHA-1 Base64 Signature
async function calculateEpointSignature(privateKey, dataB64) {
  const enc = new TextEncoder();
  const rawStr = privateKey + dataB64 + privateKey;
  const hash = await crypto.subtle.digest("SHA-1", enc.encode(rawStr));
  let binary = "";
  const bytes = new Uint8Array(hash);
  for (let i = 0; i < bytes.byteLength; i++) {
    binary += String.fromCharCode(bytes[i]);
  }
  return btoa(binary);
}

// Helper: Log Payment Event to D1
async function logPaymentEvent(db, { registration_id, order_id, payment_id, event, status, details }) {
  try {
    await db.prepare(
      "INSERT INTO payment_events (registration_id, order_id, payment_id, event, status, details) VALUES (?, ?, ?, ?, ?, ?)"
    ).bind(
      registration_id || null,
      order_id || null,
      payment_id || null,
      event,
      status || null,
      typeof details === 'object' ? JSON.stringify(details) : (details ? String(details) : null)
    ).run();
  } catch (err) {
    console.error("Failed to log payment event:", err);
  }
}

// Helper: Safe JSON parse
function safeJsonParse(str, fallback = {}) {
  try {
    return JSON.parse(str);
  } catch {
    return fallback;
  }
}

export default {
  async fetch(request, env) {
    const corsHeaders = {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET, POST, PUT, PATCH, DELETE, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type, Authorization, apikey, Prefer, Range",
      "Access-Control-Expose-Headers": "Content-Range, Range"
    };

    if (request.method === "OPTIONS") {
      return new Response(null, { headers: corsHeaders });
    }

    const url = new URL(request.url);
    let path = url.pathname;
    if (path.startsWith("/api/")) {
      path = path.replace("/api/", "/");
    }
    if (path.startsWith("/rest/v1/")) {
      path = path.replace("/rest/v1/", "/");
    }

    const privateKey = env.EPOINT_PRIVATE_KEY || DEFAULT_PRIVATE_KEY;

    // Helper to extract ids from query
    const getIdsFromQuery = () => {
      for (const [k, v] of url.searchParams.entries()) {
        if (k === 'id' || k.startsWith('id=')) {
          if (v.includes('in.(')) {
            const inside = v.replace(/.*in\.\((.*?)\).*/, '$1');
            const matches = inside.match(/\d+/g);
            if (matches && matches.length > 0) return matches;
          }
          const match = v.match(/\d+/);
          if (match) return [match[0]];
        }
      }
      return null;
    };

    const jsonResponse = (data, status = 200) => {
      return new Response(JSON.stringify(data), {
        status,
        headers: { ...corsHeaders, "Content-Type": "application/json" }
      });
    };

    try {
      // =========================================================================
      // 1. PAYMENT GATEWAY: CREATE CHECKOUT (POST /epoint-pay or /epoint)
      // =========================================================================
      if (path === "/epoint-pay" || path === "/epoint") {
        if (request.method !== "POST") {
          return jsonResponse({ success: false, error: { code: "METHOD_NOT_ALLOWED", message: "Yalnız POST sorğusuna icazə verilir" } }, 405);
        }

        const body = await request.json();
        const { regId, description, email, name, idempotency_key } = body;

        let dbId = regId ? parseInt(String(regId).replace(/\D/g, ''), 10) : null;
        if (!dbId || isNaN(dbId)) {
          return jsonResponse({ success: false, error: { code: "INVALID_REGISTRATION_ID", message: "Qeydiyyat ID tapılmadı və ya keçərsizdir." } }, 400);
        }

        // Fetch authoritative registration from D1
        const regRow = await env.DB.prepare("SELECT * FROM registrations WHERE id = ?").bind(dbId).first();
        if (!regRow) {
          return jsonResponse({ success: false, error: { code: "REGISTRATION_NOT_FOUND", message: "Sistemdə belə bir müraciət tapılmadı." } }, 404);
        }

        const regPayload = safeJsonParse(regRow.payload);

        // Check if registration is already PAID
        if (regRow.payment_status === "Ödənilib" || regRow.payment_status === "PAID") {
          const couponCode = regRow.coupon_code || ("EV-" + String(dbId).padStart(4, '0'));
          return jsonResponse({
            success: true,
            isPaid: true,
            already_paid: true,
            message: "Bu qeydiyyat artıq ödənilib.",
            data: {
              registration_id: dbId,
              coupon_code: couponCode,
              payment_status: "Ödənilib"
            }
          });
        }

        // Determine Authoritative Amount from D1 (Never trust frontend amount)
        // Official prices: Məktəbəqədər = 25 AZN, 1-11 siniflər = 35 AZN
        let authAmount = 35;
        const gradeStr = (regPayload.student_grade || regPayload.grade || regPayload['Sinif'] || regRow.source || '').toLowerCase();
        if (gradeStr.includes('məktəbəqədər') || gradeStr.includes('məktəbə qədər') || gradeStr.includes('mektebeqeder')) {
          authAmount = 25;
        }

        if (regRow.amount) {
          const parsed = parseFloat(String(regRow.amount).replace(/[^0-9.]/g, ''));
          if (!isNaN(parsed) && parsed >= 20) {
            authAmount = parsed;
          }
        }

        // Only allow 0.01 if explicitly requested with test_mode: true
        if (body.test_mode === true) {
          authAmount = 0.01;
        }

        // Check for active PENDING order created within the last 5 minutes to prevent duplicates
        const existingOrder = await env.DB.prepare(
          "SELECT * FROM orders WHERE registration_id = ? AND status = 'PENDING' AND created_at > datetime('now', '-5 minutes') ORDER BY id DESC LIMIT 1"
        ).bind(dbId).first();

        let orderNumber;
        let orderId;

        if (existingOrder && !body.force_new) {
          orderNumber = existingOrder.order_number;
          orderId = existingOrder.id;
        } else {
          // Generate unique order number: EVR-85-TIMESTAMP-RANDOM
          const randSuffix = Math.random().toString(36).substring(2, 6).toUpperCase();
          orderNumber = `EVR-${dbId}-${Date.now().toString(36).toUpperCase()}-${randSuffix}`;

          const orderDesc = description || `Evrika Imtahan Kuponu EV-${String(dbId).padStart(4, '0')}`;
          const orderInsert = await env.DB.prepare(
            "INSERT INTO orders (registration_id, order_number, amount, currency, status, description) VALUES (?, ?, ?, 'AZN', 'PENDING', ?)"
          ).bind(dbId, orderNumber, authAmount, orderDesc).run();

          orderId = orderInsert.meta.last_row_id;
        }

        // Determine attempt number
        const attemptsCount = await env.DB.prepare(
          "SELECT COUNT(*) as count FROM payments WHERE registration_id = ?"
        ).bind(dbId).first();
        const nextAttempt = (attemptsCount ? attemptsCount.count : 0) + 1;

        // Create Payment Attempt in PENDING state
        const paymentInsert = await env.DB.prepare(
          "INSERT INTO payments (order_id, registration_id, payment_attempt, amount, currency, status, description) VALUES (?, ?, ?, ?, 'AZN', 'PENDING', ?)"
        ).bind(orderId, dbId, nextAttempt, authAmount, `Ödəniş cəhdi #${nextAttempt}`).run();

        const paymentId = paymentInsert.meta.last_row_id;

        await logPaymentEvent(env.DB, {
          registration_id: dbId,
          order_id: orderId,
          payment_id: paymentId,
          event: "CHECKOUT_CREATED",
          status: "PENDING",
          details: { order_number: orderNumber, attempt: nextAttempt, amount: authAmount }
        });

        // Construct Epoint Request Payload
        const candidateName = name || regRow.name || regPayload.student_name || regPayload.fullName || "Şagird";
        const candidateEmail = email || regPayload.email || "";

        const epointPayload = {
          public_key: PUBLIC_KEY,
          amount: authAmount,
          currency: "AZN",
          language: "az",
          order_id: orderNumber,
          description: `Evrika Liseyi Kupon № EV-${String(dbId).padStart(4, '0')} (${candidateName})`,
          success_redirect_url: `https://evrikaliseyi.edu.az/success?regId=${dbId}&order_id=${encodeURIComponent(orderNumber)}`,
          error_redirect_url: `https://evrikaliseyi.edu.az/error?regId=${dbId}&order_id=${encodeURIComponent(orderNumber)}`,
          result_url: "https://evrika-api.yusifliqezenfer90.workers.dev/api/epoint-callback"
        };

        const dataB64 = utf8ToBase64(JSON.stringify(epointPayload));
        const signature = await calculateEpointSignature(privateKey, dataB64);

        // Dispatch request to Epoint
        const epointResponse = await fetch("https://epoint.az/api/1/request", {
          method: "POST",
          headers: { "Content-Type": "application/x-www-form-urlencoded" },
          body: new URLSearchParams({ data: dataB64, signature })
        });

        if (!epointResponse.ok) {
          await logPaymentEvent(env.DB, {
            registration_id: dbId,
            order_id: orderId,
            payment_id: paymentId,
            event: "EPOINT_GATEWAY_ERROR",
            status: "FAILED",
            details: { http_status: epointResponse.status }
          });
          return jsonResponse({ success: false, error: { code: "GATEWAY_UNAVAILABLE", message: "Ödəniş şlüzü hazırda cavab vermir. Zəhmət olmasa bir az sonra yenidən cəhd edin." } }, 502);
        }

        const epointData = await epointResponse.json();

        if (epointData.redirect_url) {
          if (epointData.transaction) {
            await env.DB.prepare("UPDATE payments SET epoint_transaction = ? WHERE id = ?").bind(epointData.transaction, paymentId).run();
          }

          await logPaymentEvent(env.DB, {
            registration_id: dbId,
            order_id: orderId,
            payment_id: paymentId,
            event: "REDIRECT_CREATED",
            status: "PENDING",
            details: { redirect_url: epointData.redirect_url, transaction: epointData.transaction }
          });

          return jsonResponse({
            success: true,
            redirect_url: epointData.redirect_url,
            transaction: epointData.transaction,
            order_number: orderNumber,
            registration_id: dbId,
            amount: authAmount
          });
        } else {
          await logPaymentEvent(env.DB, {
            registration_id: dbId,
            order_id: orderId,
            payment_id: paymentId,
            event: "EPOINT_REJECTED_REQUEST",
            status: "FAILED",
            details: epointData
          });
          return jsonResponse({
            success: false,
            error: {
              code: "EPOINT_REJECTED",
              message: epointData.message || "Ödəniş səhifəsi yaradılarkən xəta baş verdi."
            }
          }, 400);
        }
      }

      // =========================================================================
      // 2. PAYMENT WEBHOOK: CALLBACK HANDLER (POST /epoint-callback or /result)
      // =========================================================================
      if (path === "/epoint-callback" || path === "/result") {
        if (request.method === "GET") {
          return jsonResponse({
            status: "active",
            service: "Evrika Production Payment Webhook Gateway",
            timestamp: new Date().toISOString()
          });
        }

        if (request.method !== "POST") {
          return jsonResponse({ message: "Yalnız POST/GET icazəlidir" }, 405);
        }

        let bodyText = "";
        let dataB64 = null;
        let incomingSig = null;

        const contentType = request.headers.get("content-type") || "";
        if (contentType.includes("application/json")) {
          const bodyJson = await request.json();
          dataB64 = bodyJson.data;
          incomingSig = bodyJson.signature;
        } else {
          bodyText = await request.text();
          const formParams = new URLSearchParams(bodyText);
          dataB64 = formParams.get("data") || url.searchParams.get("data");
          incomingSig = formParams.get("signature") || url.searchParams.get("signature");
        }

        if (!dataB64 || !incomingSig) {
          await logPaymentEvent(env.DB, {
            event: "CALLBACK_REJECTED",
            status: "FAILED",
            details: { reason: "Missing data or signature" }
          });
          return jsonResponse({ success: false, error: { code: "INVALID_CALLBACK_PAYLOAD", message: "Data və ya imza tapılmadı" } }, 400);
        }

        // Strict Signature Verification
        const expectedSig = await calculateEpointSignature(privateKey, dataB64);
        if (expectedSig !== incomingSig) {
          await logPaymentEvent(env.DB, {
            event: "SIGNATURE_INVALID",
            status: "REJECTED",
            details: { incoming: incomingSig, expected: expectedSig }
          });
          return jsonResponse({ success: false, error: { code: "SIGNATURE_MISMATCH", message: "İmza xətası" } }, 403);
        }

        // Decode Payload
        let result = {};
        try {
          const decodedJson = base64ToUtf8(dataB64);
          result = JSON.parse(decodedJson);
        } catch (parseErr) {
          return jsonResponse({ success: false, error: { code: "PAYLOAD_DECODE_ERROR", message: "Məlumat formatı düzgün deyil" } }, 400);
        }

        const { order_id, status, amount, currency, transaction, rrn, card_mask, bank_response } = result;

        // Locate Order in D1
        let order = await env.DB.prepare("SELECT * FROM orders WHERE order_number = ?").bind(order_id).first();
        let dbId = null;

        if (order) {
          dbId = order.registration_id;
        } else {
          const match = String(order_id).match(/EVR-(\d+)/i) || String(order_id).match(/EV-(\d+)/i) || String(order_id).match(/^(\d+)$/);
          if (match) {
            dbId = parseInt(match[1], 10);
            order = await env.DB.prepare("SELECT * FROM orders WHERE registration_id = ? ORDER BY id DESC LIMIT 1").bind(dbId).first();
          }
        }

        if (!dbId && !order) {
          await logPaymentEvent(env.DB, {
            event: "ORDER_NOT_FOUND",
            status: "REJECTED",
            details: { order_id, status, amount }
          });
          return jsonResponse({ success: false, error: { code: "ORDER_NOT_FOUND", message: "Sifariş tapılmadı" } }, 404);
        }

        const activeOrderId = order ? order.id : null;
        const regId = dbId || (order ? order.registration_id : null);

        let payment = null;
        if (activeOrderId) {
          payment = await env.DB.prepare("SELECT * FROM payments WHERE order_id = ? ORDER BY id DESC LIMIT 1").bind(activeOrderId).first();
        }

        const paymentId = payment ? payment.id : null;

        await logPaymentEvent(env.DB, {
          registration_id: regId,
          order_id: activeOrderId,
          payment_id: paymentId,
          event: "CALLBACK_RECEIVED",
          status: status,
          details: { order_id, amount, currency, transaction, status }
        });

        // IDEMPOTENCY CHECK: If already PAID, log duplicate and return 200 OK
        if (order && order.status === "PAID") {
          await logPaymentEvent(env.DB, {
            registration_id: regId,
            order_id: activeOrderId,
            payment_id: paymentId,
            event: "DUPLICATE_CALLBACK",
            status: "PAID",
            details: { message: "Order is already marked as PAID. Duplicate callback ignored safely." }
          });
          return jsonResponse({ status: "success", message: "Artıq ödənilib (idempotent)" }, 200);
        }

        // AMOUNT & CURRENCY VERIFICATION
        if (order && amount !== undefined) {
          const cbAmount = parseFloat(amount);
          const orderAmount = parseFloat(order.amount);
          if (Math.abs(cbAmount - orderAmount) > 0.001) {
            await logPaymentEvent(env.DB, {
              registration_id: regId,
              order_id: activeOrderId,
              payment_id: paymentId,
              event: "AMOUNT_MISMATCH",
              status: "REJECTED",
              details: { order_amount: orderAmount, callback_amount: cbAmount }
            });
            return jsonResponse({ success: false, error: { code: "AMOUNT_MISMATCH", message: "Məbləğ uyğunsuzluğu aşkarlandı." } }, 400);
          }
        }

        // PROCESS SUCCESSFUL PAYMENT
        if (status === "success") {
          const nowIso = new Date().toISOString();
          const couponCode = `EV-${String(regId).padStart(4, '0')}`;

          if (paymentId) {
            await env.DB.prepare(`
              UPDATE payments 
              SET status = 'PAID', epoint_transaction = ?, rrn = ?, card_mask = ?, bank_response = ?, paid_at = CURRENT_TIMESTAMP, updated_at = CURRENT_TIMESTAMP 
              WHERE id = ?
            `).bind(transaction || null, rrn || null, card_mask || null, bank_response || "SUCCESS", paymentId).run();
          }

          if (activeOrderId) {
            await env.DB.prepare(`
              UPDATE orders 
              SET status = 'PAID', paid_at = CURRENT_TIMESTAMP, updated_at = CURRENT_TIMESTAMP 
              WHERE id = ?
            `).bind(activeOrderId).run();
          }

          const regRow = await env.DB.prepare("SELECT * FROM registrations WHERE id = ?").bind(regId).first();
          if (regRow) {
            let p = safeJsonParse(regRow.payload);
            p.payment_status = "Ödənilib";
            p.coupon_code = couponCode;
            p.paid_at = nowIso;
            p.order_id = couponCode;
            p.epoint_amount = amount || regRow.amount;
            p.epoint_transaction = transaction || "";
            p.epoint_rrn = rrn || "";
            p.epoint_card_mask = card_mask || "";
            p.epoint_bank_response = bank_response || "APPROVED";

            if (!p.note || !p.note.includes("EPOINT VASİTƏSİLƏ ÖDƏNİLDİ")) {
              p.note = (p.note ? p.note + " | " : "") + "EPOINT VASİTƏSİLƏ ÖDƏNİLDİ. İmtahan giriş kuponu təsdiqləndi.";
            }

            await env.DB.prepare(`
              UPDATE registrations 
              SET payment_status = 'Ödənilib', coupon_code = ?, paid_at = CURRENT_TIMESTAMP, payload = ? 
              WHERE id = ?
            `).bind(couponCode, JSON.stringify(p), regId).run();
          }

          await logPaymentEvent(env.DB, {
            registration_id: regId,
            order_id: activeOrderId,
            payment_id: paymentId,
            event: "PAYMENT_SUCCESS",
            status: "PAID",
            details: { coupon: couponCode, amount, transaction, rrn }
          });

          return jsonResponse({ status: "success", message: "Ödəniş uğurla təsdiqləndi" });
        } else {
          const failStatus = (status === "cancel" || status === "cancelled") ? "CANCELLED" : "FAILED";

          if (paymentId) {
            await env.DB.prepare(`
              UPDATE payments 
              SET status = ?, bank_response = ?, updated_at = CURRENT_TIMESTAMP 
              WHERE id = ?
            `).bind(failStatus, bank_response || status, paymentId).run();
          }

          if (activeOrderId) {
            await env.DB.prepare(`
              UPDATE orders 
              SET status = ?, updated_at = CURRENT_TIMESTAMP 
              WHERE id = ?
            `).bind(failStatus, activeOrderId).run();
          }

          await logPaymentEvent(env.DB, {
            registration_id: regId,
            order_id: activeOrderId,
            payment_id: paymentId,
            event: failStatus === "CANCELLED" ? "PAYMENT_CANCELLED" : "PAYMENT_FAILED",
            status: failStatus,
            details: { reason: bank_response || status, code: result.code }
          });

          return jsonResponse({ status: "processed", payment_status: failStatus });
        }
      }

      // =========================================================================
      // 3. PAYMENT STATUS & FALLBACK RECONCILIATION (GET /payment-status or POST /epoint-status)
      // =========================================================================
      if (path === "/payment-status" || path === "/epoint-status") {
        let reqRegId = url.searchParams.get("id") || url.searchParams.get("regId");
        let reqOrderNumber = url.searchParams.get("order_id");

        if (request.method === "POST") {
          try {
            const b = await request.json();
            reqRegId = reqRegId || b.id || b.regId;
            reqOrderNumber = reqOrderNumber || b.order_id || b.orderNumber;
          } catch {}
        }

        let dbId = reqRegId ? parseInt(String(reqRegId).replace(/\D/g, ''), 10) : null;
        if (!dbId && reqOrderNumber) {
          const m = String(reqOrderNumber).match(/EVR-(\d+)/i) || String(reqOrderNumber).match(/EV-(\d+)/i) || String(reqOrderNumber).match(/^(\d+)$/);
          if (m) dbId = parseInt(m[1], 10);
        }

        if (!dbId || isNaN(dbId)) {
          return jsonResponse({ success: false, error: { code: "INVALID_PARAMS", message: "id və ya order_id tələb olunur." } }, 400);
        }

        const reg = await env.DB.prepare("SELECT * FROM registrations WHERE id = ?").bind(dbId).first();
        if (!reg) {
          return jsonResponse({ success: false, error: { code: "NOT_FOUND", message: "Qeydiyyat tapılmadı." } }, 404);
        }

        const payload = safeJsonParse(reg.payload);
        const latestOrder = await env.DB.prepare("SELECT * FROM orders WHERE registration_id = ? ORDER BY id DESC LIMIT 1").bind(dbId).first();
        const latestPayment = latestOrder ? await env.DB.prepare("SELECT * FROM payments WHERE order_id = ? ORDER BY id DESC LIMIT 1").bind(latestOrder.id).first() : null;

        // Active Fallback: Check Epoint if not marked as paid in D1
        if (reg.payment_status !== "Ödənilib" && latestOrder && latestOrder.order_number) {
          try {
            const checkData = { public_key: PUBLIC_KEY, order_id: latestOrder.order_number };
            const checkB64 = utf8ToBase64(JSON.stringify(checkData));
            const checkSig = await calculateEpointSignature(privateKey, checkB64);

            const epCheckRes = await fetch("https://epoint.az/api/1/get-status", {
              method: "POST",
              headers: { "Content-Type": "application/x-www-form-urlencoded" },
              body: new URLSearchParams({ data: checkB64, signature: checkSig })
            });

            if (epCheckRes.ok) {
              const epStatusData = await epCheckRes.json();
              if (epStatusData.status === "success") {
                const couponCode = `EV-${String(dbId).padStart(4, '0')}`;
                await env.DB.prepare("UPDATE payments SET status = 'PAID', paid_at = CURRENT_TIMESTAMP WHERE id = ?").bind(latestPayment ? latestPayment.id : 0).run();
                await env.DB.prepare("UPDATE orders SET status = 'PAID', paid_at = CURRENT_TIMESTAMP WHERE id = ?").bind(latestOrder.id).run();

                payload.payment_status = "Ödənilib";
                payload.coupon_code = couponCode;
                payload.paid_at = new Date().toISOString();
                payload.epoint_amount = epStatusData.amount || reg.amount;
                payload.epoint_transaction = epStatusData.transaction || "";

                await env.DB.prepare("UPDATE registrations SET payment_status = 'Ödənilib', coupon_code = ?, paid_at = CURRENT_TIMESTAMP, payload = ? WHERE id = ?")
                  .bind(couponCode, JSON.stringify(payload), dbId).run();

                await logPaymentEvent(env.DB, {
                  registration_id: dbId,
                  order_id: latestOrder.id,
                  payment_id: latestPayment ? latestPayment.id : null,
                  event: "PAYMENT_STATUS_RECONCILED",
                  status: "PAID",
                  details: epStatusData
                });

                reg.payment_status = "Ödənilib";
                reg.coupon_code = couponCode;
                latestOrder.status = "PAID";
              }
            }
          } catch (e) {
            console.warn("Fallback check error:", e);
          }
        }

        const isPaid = reg.payment_status === "Ödənilib" || (latestOrder && latestOrder.status === "PAID");
        const studentName = reg.name || payload.student_name || payload.fullName || payload['[2.Şagird] Adı'] || "Şagird";
        const grade = payload.student_grade || payload.grade || payload['Sinif'] || "";
        const couponCode = reg.coupon_code || (isPaid ? `EV-${String(dbId).padStart(4, '0')}` : null);

        let overallStatus = "UNPAID";
        if (isPaid) overallStatus = "PAID";
        else if (latestOrder && latestOrder.status === "PENDING") overallStatus = "PENDING";
        else if (latestOrder && latestOrder.status === "FAILED") overallStatus = "FAILED";
        else if (latestOrder && latestOrder.status === "CANCELLED") overallStatus = "CANCELLED";

        return jsonResponse({
          success: true,
          data: {
            registration_id: dbId,
            order_number: latestOrder ? latestOrder.order_number : null,
            status: overallStatus,
            isPaid,
            coupon_code: couponCode,
            student_name: studentName,
            grade,
            source: reg.source,
            amount: latestOrder ? latestOrder.amount : (parseFloat(reg.amount) || 35),
            currency: "AZN",
            paid_at: reg.paid_at || (latestOrder ? latestOrder.paid_at : null)
          }
        });
      }

      // =========================================================================
      // 4. PUBLIC VERIFICATION: GET /verify
      // =========================================================================
      if (path === "/verify") {
        const reqId = url.searchParams.get("id");
        const cleanId = reqId ? parseInt(String(reqId).replace(/\D/g, ''), 10) : null;

        if (!cleanId || isNaN(cleanId)) {
          return jsonResponse({ success: false, verified: false, error: { message: "Keçərsiz kupon kodu və ya ID" } }, 400);
        }

        const row = await env.DB.prepare("SELECT * FROM registrations WHERE id = ?").bind(cleanId).first();
        if (!row) {
          return jsonResponse({ success: false, verified: false, error: { message: "Sistemdə belə bir iştirakçı tapılmadı." } }, 404);
        }

        const isPaid = row.payment_status === "Ödənilib";
        const payload = safeJsonParse(row.payload);
        const sdName = payload['[2.Şagird] Adı'];
        const sdSurname = payload['[2.Şagird] Soyadı'] || '';
        const fullSdName = sdName ? (sdName + ' ' + sdSurname).trim() : null;
        const studentName = row.name || payload.student_name || payload.fullName || fullSdName || "Şagird";
        const grade = payload.student_grade || payload.grade || payload['Sinif'] || payload['[3.Təhsil] Qeydiyyat Səviyyəsi'] || '';
        
        let branch = 'EVRİKA Liseyi';
        const src = (row.source || payload.source || '').toLowerCase();
        if (src.includes('nərimanov') || src.includes('nerimanov')) branch = 'EVRİKA BETL (Nərimanov filialı)';
        else if (src.includes('gənclik') || src.includes('genclik')) branch = 'EVRİKA BETL (Gənclik filialı)';
        else if (src.includes('montessori')) branch = 'EVRİKA Montessori Kids';
        else if (src.includes('zumrud') || src.includes('zümrüd')) branch = 'Zümrüd İdman Kompleksi';

        const currentExamStatus = payload.exam_status || payload.status || 'Yeni';
        let isAlreadyUsed = (currentExamStatus === "QR İstifadə Edilib" || payload.qr_scanned === true);

        if (url.searchParams.get("action") === "confirm" && isPaid && !isAlreadyUsed) {
          payload.exam_status = "QR İstifadə Edilib";
          payload.qr_scanned = true;
          payload.qr_scanned_at = new Date().toISOString();
          await env.DB.prepare("UPDATE registrations SET payload = ? WHERE id = ?").bind(JSON.stringify(payload), cleanId).run();
          isAlreadyUsed = true;
        }

        return jsonResponse({
          success: true,
          verified: isPaid,
          data: {
            coupon_code: `EV-${String(cleanId).padStart(4, '0')}`,
            student_name: studentName,
            grade,
            branch,
            payment_status: row.payment_status,
            is_used: isAlreadyUsed,
            exam_status: isAlreadyUsed ? "QR İstifadə Edilib" : (isPaid ? "Girişə İcazə Verildi" : "Ödəniş Edilməyib")
          }
        });
      }

      // =========================================================================
      // 5. ADMIN ANALYTICS & EVENTS TIMELINE (GET /admin/payments, /admin/payment-stats)
      // =========================================================================
      if (path === "/admin/payment-stats") {
        const totalRegs = await env.DB.prepare("SELECT COUNT(*) as count FROM registrations").first();
        const paidRegs = await env.DB.prepare("SELECT COUNT(*) as count FROM registrations WHERE payment_status = 'Ödənilib'").first();
        const pendingOrders = await env.DB.prepare("SELECT COUNT(*) as count FROM orders WHERE status = 'PENDING'").first();
        const failedOrders = await env.DB.prepare("SELECT COUNT(*) as count FROM orders WHERE status = 'FAILED'").first();
        const totalPaidAmount = await env.DB.prepare("SELECT SUM(amount) as total FROM orders WHERE status = 'PAID'").first();
        const todayPaid = await env.DB.prepare("SELECT SUM(amount) as total FROM orders WHERE status = 'PAID' AND date(paid_at) = date('now')").first();

        return jsonResponse({
          success: true,
          stats: {
            total_registrations: totalRegs ? totalRegs.count : 0,
            paid_count: paidRegs ? paidRegs.count : 0,
            pending_count: pendingOrders ? pendingOrders.count : 0,
            failed_count: failedOrders ? failedOrders.count : 0,
            total_revenue: totalPaidAmount ? (totalPaidAmount.total || 0) : 0,
            today_revenue: todayPaid ? (todayPaid.total || 0) : 0
          }
        });
      }

      if (path === "/admin/payment-events") {
        const regId = url.searchParams.get("registration_id");
        let query = "SELECT * FROM payment_events";
        let binds = [];
        if (regId) {
          query += " WHERE registration_id = ? ORDER BY id DESC LIMIT 50";
          binds.push(regId);
        } else {
          query += " ORDER BY id DESC LIMIT 100";
        }
        const { results } = await env.DB.prepare(query).bind(...binds).all();
        return jsonResponse({ success: true, events: results });
      }

      // =========================================================================
      // 6. EXISTING REGISTRATIONS HANDLER (GET, POST, PUT, DELETE /registrations)
      // =========================================================================
      if (path === "/registrations") {
        if (request.method === "GET") {
          const ids = getIdsFromQuery();
          if (ids && ids.length > 0) {
            const placeholders = ids.map(() => '?').join(',');
            const { results } = await env.DB.prepare(`SELECT * FROM registrations WHERE id IN (${placeholders}) ORDER BY id DESC`).bind(...ids).all();
            const parsed = results.map(row => {
              let p = safeJsonParse(row.payload);
              p.id = row.id;
              p._db_id_ = row.id;
              p.created_at = row.created_at;
              p.payment_status = row.payment_status;
              p.amount = row.amount;
              p.coupon_code = row.coupon_code;
              p.paid_at = row.paid_at;
              return { ...row, payload: p, ...p };
            });
            return jsonResponse(parsed);
          }

          const { results } = await env.DB.prepare("SELECT id, created_at, name, phone, source, payment_status, amount, coupon_code, paid_at, payload FROM registrations ORDER BY id DESC").all();
          const parsed = results.map(r => {
            let p = safeJsonParse(r.payload);
            p.id = r.id;
            p._db_id_ = r.id;
            p.created_at = r.created_at;
            p.payment_status = r.payment_status;
            p.amount = r.amount;
            p.coupon_code = r.coupon_code;
            p.paid_at = r.paid_at;
            return {
              id: r.id,
              created_at: r.created_at,
              name: r.name,
              phone: r.phone,
              source: r.source,
              payment_status: r.payment_status,
              amount: r.amount,
              coupon_code: r.coupon_code,
              paid_at: r.paid_at,
              payload: p,
              ...p
            };
          });
          return jsonResponse(parsed);
        }

        if (request.method === "POST") {
          const body = await request.json();
          const pData = body.payload ? body.payload : body;
          const name = pData.name || pData.fullName || pData['[2.Şagird] Adı'] || pData['[Demo Qeydiyyat] Ad Soyad'] || '';
          const phone = pData.phone || pData.tel || pData['[1.Əlaqə] Əlaqə Nömrəsi'] || pData['[3.Ata] Nömrəsi'] || '';
          const source = pData.source || pData.student_grade || pData['[2.Şagird] Təhsil Növü'] || 'Ümumi Müraciət';
          const isPayableSource = /lisey|gənclik|nərimanov|ptim|imtahan|ödəniş|odenis/i.test(source);
          const payment_status = pData.payment_status || (isPayableSource ? 'Ödənilməyib' : null);
          const gradeVal = (pData.student_grade || pData.grade || pData['Sinif'] || '').toLowerCase();
          const defaultPrice = (gradeVal.includes('məktəbəqədər') || gradeVal.includes('məktəbə qədər')) ? '25' : '35';
          const amount = pData.amount ? String(pData.amount).replace(/[^0-9.]/g, '') : (isPayableSource ? defaultPrice : '0');
          const payloadStr = JSON.stringify(pData);

          const res = await env.DB.prepare(
            "INSERT INTO registrations (name, phone, source, payment_status, amount, payload) VALUES (?, ?, ?, ?, ?, ?)"
          ).bind(name, phone, source, payment_status, amount, payloadStr).run();

          return jsonResponse({ success: true, id: res.meta.last_row_id }, 201);
        }

        if (request.method === "DELETE") {
          const ids = getIdsFromQuery();
          if (!ids || ids.length === 0) return jsonResponse({ error: "Missing id" }, 400);
          await env.DB.prepare("DELETE FROM registrations WHERE id = ?").bind(ids[0]).run();
          return jsonResponse({ success: true });
        }

        if (request.method === "PUT" || request.method === "PATCH") {
          const ids = getIdsFromQuery();
          const body = await request.json();
          if (!ids || ids.length === 0) return jsonResponse({ error: "Missing id" }, 400);
          const id = ids[0];

          const existing = await env.DB.prepare("SELECT * FROM registrations WHERE id = ?").bind(id).first();
          if (!existing) return jsonResponse({ error: "Not found" }, 404);

          let p = safeJsonParse(existing.payload);
          const incoming = body.payload ? body.payload : body;
          Object.assign(p, incoming);

          const payment_status = incoming.payment_status || existing.payment_status;
          const amount = incoming.amount ? String(incoming.amount) : existing.amount;
          const coupon_code = incoming.coupon_code || existing.coupon_code;
          const paid_at = incoming.paid_at || existing.paid_at;

          await env.DB.prepare(
            "UPDATE registrations SET payment_status = ?, amount = ?, coupon_code = ?, paid_at = ?, payload = ? WHERE id = ?"
          ).bind(payment_status, amount, coupon_code, paid_at, JSON.stringify(p), id).run();

          return jsonResponse({ success: true });
        }
      }

      // =========================================================================
      // 7. GENERIC CRUD TABLES HANDLER
      // =========================================================================
      const dynamicTables = ['ugurlar', 'vacancies', 'news', 'mezunlar', 'management', 'popups', 'employees', 'partners', 'parent_testimonials', 'settings'];
      const tableName = path.replace('/', '');

      if (dynamicTables.includes(tableName)) {
        if (request.method === "GET") {
          const ids = getIdsFromQuery();
          if (ids && ids.length > 0) {
            const placeholders = ids.map(() => '?').join(',');
            const { results } = await env.DB.prepare(`SELECT * FROM ${tableName} WHERE id IN (${placeholders}) ORDER BY id DESC`).bind(...ids).all();
            const parsed = results.map(row => {
              let p = safeJsonParse(row.payload);
              return { ...row, payload: p, ...p, id: row.id, _db_id_: row.id };
            });
            return jsonResponse(parsed);
          }

          const { results } = await env.DB.prepare(`SELECT * FROM ${tableName} ORDER BY id DESC`).all();
          const parsed = results.map(r => {
            let p = safeJsonParse(r.payload);
            return { ...r, payload: p, ...p, id: r.id, _db_id_: r.id };
          });
          return jsonResponse(parsed);
        }

        if (request.method === "POST") {
          const body = await request.json();
          const payload = body.payload ? body.payload : body;
          const res = await env.DB.prepare(`INSERT INTO ${tableName} (payload) VALUES (?)`).bind(JSON.stringify(payload)).run();
          return jsonResponse({ success: true, id: res.meta.last_row_id }, 201);
        }

        if (request.method === "PUT" || request.method === "PATCH") {
          const ids = getIdsFromQuery();
          const body = await request.json();
          const payload = body.payload ? body.payload : body;
          if (!ids || ids.length === 0) return jsonResponse({ error: "Missing id" }, 400);
          await env.DB.prepare(`UPDATE ${tableName} SET payload = ? WHERE id = ?`).bind(JSON.stringify(payload), ids[0]).run();
          return jsonResponse({ success: true });
        }

        if (request.method === "DELETE") {
          const ids = getIdsFromQuery();
          if (!ids || ids.length === 0) return jsonResponse({ error: "Missing id" }, 400);
          await env.DB.prepare(`DELETE FROM ${tableName} WHERE id = ?`).bind(ids[0]).run();
          return jsonResponse({ success: true });
        }
      }

      return jsonResponse({ status: "Evrika Cloudflare D1 & Payment Gateway API is online", timestamp: new Date().toISOString() });
    } catch (err) {
      console.error("Worker Execution Error:", err);
      return jsonResponse({ error: err.message || "Internal Server Error" }, 500);
    }
  }
};
