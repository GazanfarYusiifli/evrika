import crypto from 'crypto';

const PUBLIC_KEY = "i000201608";
const PRIVATE_KEY = process.env.EPOINT_PRIVATE_KEY || "HNIbtyFLu3PbxXlVykJEwOR1";
const CF_BASE_URL = "https://evrika-api.yusifliqezenfer90.workers.dev";

function extractRegId(orderId) {
  if (!orderId) return null;
  const str = String(orderId).trim();
  const match =
    str.match(/EVR-(\d+)/i) ||
    str.match(/EV-0*(\d+)/i) ||
    str.match(/^(\d+)_/) ||
    str.match(/^(\d+)$/);
  return match ? parseInt(match[1], 10) : null;
}

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method === 'GET') {
    return res.status(200).json({
      status: "active",
      service: "Evrika Official Epoint Result Callback Gateway",
      public_key: PUBLIC_KEY,
      timestamp: new Date().toISOString()
    });
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ status: "error", message: "Method Not Allowed" });
  }

  try {
    let data = "";
    let signature = "";

    if (typeof req.body === "object" && req.body !== null) {
      data = req.body.data || "";
      signature = req.body.signature || "";
    } else if (typeof req.body === "string") {
      try {
        const parsed = JSON.parse(req.body);
        data = parsed.data || "";
        signature = parsed.signature || "";
      } catch {
        const params = new URLSearchParams(req.body);
        data = params.get("data") || "";
        signature = params.get("signature") || "";
      }
    }

    if (!data && req.query) {
      data = req.query.data || "";
      signature = req.query.signature || "";
    }

    if (!data || !signature) {
      return res.status(400).json({
        status: "error",
        message: "Missing data or signature parameter"
      });
    }

    // 1. Official Epoint Signature Verification: base64(sha1(private_key + data + private_key, binary))
    const expectedSignature = crypto
      .createHash("sha1")
      .update(PRIVATE_KEY + data + PRIVATE_KEY)
      .digest("base64");

    if (signature !== expectedSignature) {
      console.error("Epoint callback signature mismatch:", { received: signature, expected: expectedSignature });
      return res.status(403).json({
        status: "error",
        message: "Signature verification failed"
      });
    }

    // 2. Decode Epoint Callback Payload
    let resultPayload = {};
    try {
      const jsonStr = Buffer.from(data, "base64").toString("utf8");
      resultPayload = JSON.parse(jsonStr);
    } catch (decodeErr) {
      console.error("Epoint callback base64 decode error:", decodeErr);
      return res.status(400).json({
        status: "error",
        message: "Invalid base64 JSON payload"
      });
    }

    const {
      order_id,
      status,
      code,
      message,
      transaction,
      bank_transaction,
      bank_response,
      operation_code,
      rrn,
      card_name,
      card_mask,
      amount,
      trace_id
    } = resultPayload;

    // 3. Forward to Cloudflare Worker so orders, payments, and payment_logs tables are updated
    let workerResponse = null;
    try {
      const forwardRes = await fetch(`${CF_BASE_URL}/api/epoint-callback`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ data, signature })
      });
      workerResponse = await forwardRes.json().catch(() => null);
    } catch (cfErr) {
      console.warn("Worker callback forward warning:", cfErr);
    }

    // 4. Directly synchronize status into the D1 registrations table for CRM accuracy
    let dbId = extractRegId(order_id);
    if (!dbId && workerResponse?.data?.registration_id) {
      dbId = parseInt(String(workerResponse.data.registration_id), 10);
    }

    const isSuccess = status === "success" && (!code || String(code) === "000");

    if (dbId && !isNaN(dbId)) {
      try {
        const regGetRes = await fetch(`${CF_BASE_URL}/api/registrations?id=${dbId}`);
        const regList = regGetRes.ok ? await regGetRes.json() : [];
        const existingReg = Array.isArray(regList) && regList.length > 0 ? regList[0] : null;

        if (isSuccess) {
          const couponCode = existingReg?.coupon_code || `EV-${String(dbId).padStart(4, "0")}`;
          const paidAt = existingReg?.paid_at || new Date().toISOString();

          await fetch(`${CF_BASE_URL}/api/registrations?id=${dbId}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              payment_status: "Ödənilib",
              coupon_code: couponCode,
              paid_at: paidAt,
              amount: amount ? String(amount) : (existingReg?.amount || "35"),
              epoint_transaction: transaction || existingReg?.epoint_transaction || "",
              epoint_bank_transaction: bank_transaction || "",
              epoint_rrn: rrn || "",
              epoint_card_mask: card_mask || "",
              epoint_card_name: card_name || "",
              epoint_operation_code: operation_code || "100",
              epoint_code: code || "000",
              epoint_message: message || "Approved",
              epoint_trace_id: trace_id || "",
              last_order_id: order_id || ""
            })
          });
        } else if (status && status !== "new") {
          // Only mark as Uğursuz if the registration has not already been paid
          if (!existingReg || existingReg.payment_status !== "Ödənilib") {
            const failReason =
              message ||
              bank_response ||
              (code ? `Bank imtinası (Kod: ${code})` : "Ödəniş tamamlanmadı");

            await fetch(`${CF_BASE_URL}/api/registrations?id=${dbId}`, {
              method: "PUT",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({
                payment_status: "Uğursuz",
                payment_fail_reason: failReason,
                epoint_transaction: transaction || existingReg?.epoint_transaction || "",
                epoint_bank_transaction: bank_transaction || "",
                epoint_code: code || "",
                epoint_message: message || "",
                epoint_bank_response: bank_response || "",
                epoint_trace_id: trace_id || "",
                last_order_id: order_id || ""
              })
            });
          }
        }
      } catch (regUpdateErr) {
        console.error("Failed to update registration status in D1:", regUpdateErr);
      }
    }

    return res.status(200).json({
      status: "ok",
      received: true,
      registration_id: dbId,
      order_id,
      payment_status: isSuccess ? "Ödənilib" : "Uğursuz",
      worker: workerResponse
    });
  } catch (err) {
    console.error("Callback handler error:", err);
    return res.status(500).json({ status: "error", error: err.message });
  }
}
