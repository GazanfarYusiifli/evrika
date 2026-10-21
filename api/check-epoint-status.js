import crypto from 'crypto';

const PUBLIC_KEY = "i000201608";
const PRIVATE_KEY = process.env.EPOINT_PRIVATE_KEY || "HNIbtyFLu3PbxXlVykJEwOR1";
const CF_BASE_URL = "https://evrika-api.yusifliqezenfer90.workers.dev";

async function queryEpointStatusByTransaction(transactionId) {
  if (!transactionId) return null;
  try {
    const payload = JSON.stringify({
      public_key: PUBLIC_KEY,
      transaction: String(transactionId).trim()
    });
    const data = Buffer.from(payload).toString("base64");
    const signature = crypto
      .createHash("sha1")
      .update(PRIVATE_KEY + data + PRIVATE_KEY)
      .digest("base64");

    const response = await fetch("https://epoint.az/api/1/get-status", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 EvrikaPaymentClient/2.0"
      },
      body: new URLSearchParams({ data, signature })
    });

    if (!response.ok) return null;
    return await response.json();
  } catch (err) {
    console.warn("Epoint get-status error:", err);
    return null;
  }
}

async function reconcileRegistration(dbId, { orderId, transaction, markFailed, preloadedReg } = {}) {
  const cleanId = parseInt(String(dbId).replace(/\D/g, ""), 10);
  if (!cleanId || isNaN(cleanId)) return null;

  const statusParams = new URLSearchParams({ id: String(cleanId) });
  if (orderId) statusParams.append("order_id", String(orderId));

  let regRow = preloadedReg || null;
  const [cfStatusRes, regRes] = await Promise.all([
    fetch(`${CF_BASE_URL}/api/payment-status?${statusParams.toString()}`).catch(() => null),
    regRow ? Promise.resolve(null) : fetch(`${CF_BASE_URL}/api/registrations?id=${cleanId}`).catch(() => null)
  ]);

  const cfStatusJson = cfStatusRes && cfStatusRes.ok ? await cfStatusRes.json().catch(() => null) : null;
  const cfData = cfStatusJson?.data || null;

  if (!regRow && regRes && regRes.ok) {
    const regList = await regRes.json().catch(() => []);
    regRow = Array.isArray(regList) && regList.length > 0 ? regList[0] : null;
  }

  if (!cfData && !regRow) return null;

  const txId =
    transaction ||
    regRow?.epoint_transaction ||
    regRow?.payload?.epoint_transaction ||
    null;

  let epStatus = null;
  if (txId && regRow?.payment_status !== "Ödənilib" && !cfData?.isPaid) {
    epStatus = await queryEpointStatusByTransaction(txId);
  }

  const isPaid =
    regRow?.payment_status === "Ödənilib" ||
    cfData?.isPaid === true ||
    cfData?.status === "PAID" ||
    (epStatus?.status === "success" && (!epStatus.code || String(epStatus.code) === "000"));

  // Check if session has timed out (more than 30 minutes since registration/last attempt without payment)
  let isExpiredPending = false;
  if (!isPaid && regRow) {
    const refDateStr =
      regRow.payment_attempt_at ||
      regRow.payload?.payment_attempt_at ||
      regRow.date ||
      regRow.created_at;
    if (refDateStr) {
      const refTime = new Date(refDateStr).getTime();
      if (!isNaN(refTime) && Date.now() - refTime > 30 * 60 * 1000) {
        isExpiredPending = true;
      }
    }
  }

  const isFailed =
    !isPaid &&
    (cfData?.status === "FAILED" ||
      cfData?.status === "CANCELLED" ||
      cfData?.status === "EXPIRED" ||
      epStatus?.status === "failed" ||
      epStatus?.status === "error" ||
      epStatus?.status === "returned" ||
      markFailed === true ||
      markFailed === "1" ||
      isExpiredPending);

  const couponCode =
    regRow?.coupon_code ||
    cfData?.coupon_code ||
    (isPaid ? `EV-${String(cleanId).padStart(4, "0")}` : null);

  const paidAt =
    regRow?.paid_at ||
    cfData?.paid_at ||
    (isPaid ? new Date().toISOString() : null);

  // Sync authoritative state back into D1 registrations table
  // Note: Worker's PUT /api/registrations?id=X safely merges with existing payload in D1
  if (isPaid && (!regRow || regRow.payment_status !== "Ödənilib")) {
    try {
      await fetch(`${CF_BASE_URL}/api/registrations?id=${cleanId}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          payment_status: "Ödənilib",
          coupon_code: couponCode,
          paid_at: paidAt,
          ...(epStatus?.amount ? { amount: String(epStatus.amount) } : {}),
          ...(epStatus?.transaction || txId ? { epoint_transaction: epStatus?.transaction || txId } : {}),
          ...(epStatus?.rrn ? { epoint_rrn: epStatus.rrn } : {}),
          ...(epStatus?.card_mask ? { epoint_card_mask: epStatus.card_mask } : {}),
          ...(epStatus?.card_name ? { epoint_card_name: epStatus.card_name } : {})
        })
      });
    } catch (e) {
      console.warn("Failed to sync PAID status to registration:", e);
    }
  } else if (isFailed && (!regRow || (regRow.payment_status !== "Ödənilib" && regRow.payment_status !== "Uğursuz"))) {
    const failReason =
      epStatus?.message ||
      epStatus?.bank_response ||
      (markFailed ? "Ödəniş istifadəçi və ya bank tərəfindən ləğv edildi" : "Ödəniş tamamlanmadı / Uğursuz");
    try {
      await fetch(`${CF_BASE_URL}/api/registrations?id=${cleanId}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          payment_status: "Uğursuz",
          payment_fail_reason: failReason,
          epoint_code: epStatus?.code || "",
          epoint_message: epStatus?.message || ""
        })
      });
    } catch (e) {
      console.warn("Failed to sync FAILED status to registration:", e);
    }
  }

  const finalStatus = isPaid ? "PAID" : (isFailed ? "FAILED" : (cfData?.status || "PENDING"));
  const finalPaymentStatusAz = isPaid ? "Ödənilib" : (isFailed ? "Uğursuz" : "Ödəniş gözlənilir");

  return {
    registration_id: cleanId,
    order_number: cfData?.order_number || regRow?.last_order_id || orderId || null,
    status: finalStatus,
    payment_status: finalPaymentStatusAz,
    isPaid,
    coupon_code: couponCode,
    student_name: cfData?.student_name || regRow?.name || "Şagird",
    grade: cfData?.grade || regRow?.student_grade || "",
    source: cfData?.source || regRow?.source || "",
    amount: cfData?.amount || parseFloat(regRow?.amount) || 35,
    currency: "AZN",
    paid_at: paidAt,
    fail_reason: isFailed
      ? (epStatus?.message || epStatus?.bank_response || regRow?.payment_fail_reason || "Ödəniş tamamlanmadı")
      : null,
    epoint: epStatus || undefined
  };
}

export default async function handler(req, res) {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");

  if (req.method === "OPTIONS") {
    return res.status(200).end();
  }

  try {
    const syncAll = req.query.syncAll === "1" || req.body?.syncAll === true;
    const batchIds = req.body?.ids || (req.query.ids ? String(req.query.ids).split(",") : null);

    if (syncAll || (Array.isArray(batchIds) && batchIds.length > 0)) {
      let targetItems = [];
      if (Array.isArray(batchIds) && batchIds.length > 0) {
        const cleanIds = batchIds.map(id => parseInt(String(id).replace(/\D/g, ""), 10)).filter(Boolean);
        targetItems = cleanIds.map(id => ({ id, reg: null }));
      } else {
        const allRes = await fetch(`${CF_BASE_URL}/api/registrations`);
        const allRegs = allRes.ok ? await allRes.json() : [];
        targetItems = (Array.isArray(allRegs) ? allRegs : [])
          .filter(r => {
            if (!r || r.payment_status !== "Ödəniş gözlənilir") return false;
            if (r.is_call || r.chid || r.position) return false;
            const s = String(r.source || r.student_grade || "").toLowerCase();
            if (
              s === "contact" ||
              s === "karyera" ||
              s === "career" ||
              s.includes("zəng") ||
              s.includes("phone") ||
              s.includes("survey") ||
              s.includes("səsi") ||
              s.includes("sesi") ||
              s.includes("montessori") ||
              s.includes("zumrud") ||
              s.includes("zümrüd")
            ) {
              return false;
            }
            return (
              s.includes("qeydiyyat") ||
              s.includes("lisey") ||
              s.includes("ptim") ||
              s.includes("ödəniş") ||
              s.includes("odenis") ||
              s.includes("imtahan")
            );
          })
          .map(r => ({ id: r.id, reg: r }));
      }

      const reconciled = [];
      const slice = targetItems.slice(0, 20);
      const chunkSize = 5;
      for (let i = 0; i < slice.length; i += chunkSize) {
        const chunk = slice.slice(i, i + chunkSize);
        const results = await Promise.all(
          chunk.map(item => reconcileRegistration(item.id, { preloadedReg: item.reg }))
        );
        results.forEach(r => {
          if (r) reconciled.push(r);
        });
      }

      return res.status(200).json({
        success: true,
        count: reconciled.length,
        reconciled
      });
    }

    const regId = req.query.regId || req.query.id || req.body?.regId || req.body?.id;
    const orderId = req.query.order_id || req.body?.order_id;
    const transaction = req.query.transaction || req.body?.transaction;
    const markFailed = req.query.markFailed || req.body?.markFailed;

    if (!regId && !orderId) {
      return res.status(400).json({ success: false, error: "Missing regId or order_id" });
    }

    let dbId = regId;
    if (!dbId && orderId) {
      const m =
        String(orderId).match(/EVR-(\d+)/i) ||
        String(orderId).match(/EV-0*(\d+)/i) ||
        String(orderId).match(/^(\d+)/);
      if (m) dbId = m[1];
    }

    const resultData = await reconcileRegistration(dbId, { orderId, transaction, markFailed });
    if (!resultData) {
      return res.status(404).json({ success: false, error: "Registration not found" });
    }

    return res.status(200).json({
      success: true,
      data: resultData
    });
  } catch (err) {
    console.error("Status check & reconciliation error:", err);
    return res.status(500).json({ success: false, error: err.message });
  }
}
