import crypto from 'crypto';

const PUBLIC_KEY = "i000201608";
const PRIVATE_KEY = process.env.EPOINT_PRIVATE_KEY || "HNIbtyFLu3PbxXlVykJEwOR1";
const CF_BASE_URL = "https://evrika-api.yusifliqezenfer90.workers.dev";

function isPayableRegistration(r) {
  if (!r || r.is_call || r.chid || r.position) return false;
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
    s.includes("imtahan") ||
    Boolean(r.last_order_id || r.epoint_transaction)
  );
}

async function fetchEpointGetStatus(paramsObj) {
  try {
    const payload = JSON.stringify({
      public_key: PUBLIC_KEY,
      ...paramsObj
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

function isEpointNotFound(epStatus) {
  if (!epStatus || epStatus.status !== "error") return false;
  const msg = String(epStatus.message || "").toLowerCase();
  return msg.includes("not found") || msg.includes("tapılmadı") || msg.includes("does not exist");
}

async function queryEpointStatus({ transaction, orderId } = {}) {
  const cleanOrder = orderId ? String(orderId).trim() : "";
  const cleanTx = transaction ? String(transaction).trim() : "";

  if (cleanOrder) {
    const byOrder = await fetchEpointGetStatus({ order_id: cleanOrder });
    if (byOrder && !isEpointNotFound(byOrder)) {
      return byOrder;
    }
  }

  if (cleanTx) {
    return await fetchEpointGetStatus({ transaction: cleanTx });
  }

  return null;
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

  const targetOrderId =
    orderId ||
    regRow?.last_order_id ||
    regRow?.payload?.last_order_id ||
    cfData?.order_number ||
    null;

  const sameOrderAsCf =
    !cfData?.order_number ||
    !targetOrderId ||
    String(cfData.order_number) === String(targetOrderId);

  const txId =
    transaction ||
    regRow?.epoint_transaction ||
    regRow?.payload?.epoint_transaction ||
    (sameOrderAsCf ? cfData?.transaction : null) ||
    null;

  let epStatus = null;
  if ((txId || targetOrderId) && regRow?.payment_status !== "Ödənilib" && !cfData?.isPaid) {
    epStatus = await queryEpointStatus({ transaction: txId, orderId: targetOrderId });
  }

  const isPaid =
    regRow?.payment_status === "Ödənilib" ||
    cfData?.isPaid === true ||
    cfData?.status === "PAID" ||
    (epStatus?.status === "success" && (!epStatus.code || String(epStatus.code) === "000"));

  const epNotFound = isEpointNotFound(epStatus);
  const epExplicitFail =
    Boolean(epStatus) &&
    !epNotFound &&
    (epStatus.status === "failed" ||
      epStatus.status === "error" ||
      epStatus.status === "returned" ||
      epStatus.status === "rejected" ||
      (epStatus.code && String(epStatus.code) !== "000" && epStatus.status !== "new"));

  const cfOrderFailed =
    sameOrderAsCf &&
    epStatus?.status !== "new" &&
    (cfData?.status === "FAILED" ||
      cfData?.status === "CANCELLED" ||
      cfData?.status === "EXPIRED");

  const explicitCancelRequested =
    (markFailed === true || markFailed === "1") && epStatus?.status !== "new";

  const isFailed =
    !isPaid &&
    (epExplicitFail || cfOrderFailed || explicitCancelRequested);

  const dbAlreadyFailed =
    !isPaid &&
    regRow?.payment_status === "Uğursuz" &&
    epStatus?.status !== "new";

  const effectiveFailed = isFailed || dbAlreadyFailed;

  const epReasonParts = [epStatus?.message, epStatus?.bank_response]
    .map(v => (v ? String(v).trim() : ""))
    .filter(v => v && v !== "Error");
  const epFailText = [...new Set(epReasonParts)].join(" — ");

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
          payment_fail_reason: "",
          coupon_code: couponCode,
          paid_at: paidAt,
          epoint_code: epStatus?.code || "000",
          epoint_message: epStatus?.message || "Approved",
          ...(epStatus?.amount ? { amount: String(epStatus.amount) } : {}),
          ...(epStatus?.order_id || targetOrderId ? { last_order_id: epStatus?.order_id || targetOrderId } : {}),
          ...(epStatus?.transaction || txId ? { epoint_transaction: epStatus?.transaction || txId } : {}),
          ...(epStatus?.rrn ? { epoint_rrn: epStatus.rrn } : {}),
          ...(epStatus?.card_mask ? { epoint_card_mask: epStatus.card_mask } : {}),
          ...(epStatus?.card_name ? { epoint_card_name: epStatus.card_name } : {})
        })
      });
    } catch (e) {
      console.warn("Failed to sync PAID status to registration:", e);
    }
  } else if (
    isFailed &&
    (!regRow || isPayableRegistration(regRow)) &&
    (!regRow ||
      (regRow.payment_status !== "Ödənilib" &&
        (regRow.payment_status !== "Uğursuz" || (epFailText && !regRow.payment_fail_reason))))
  ) {
    const failReason =
      epFailText ||
      (epStatus?.code ? `Bank imtinası (Kod: ${epStatus.code})` : "") ||
      (markFailed ? "Ödəniş istifadəçi və ya bank tərəfindən ləğv edildi" : "Ödəniş tamamlanmadı / Uğursuz");
    try {
      await fetch(`${CF_BASE_URL}/api/registrations?id=${cleanId}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          payment_status: "Uğursuz",
          payment_fail_reason: failReason,
          epoint_code: epStatus?.code || "",
          epoint_message: epStatus?.message || "",
          epoint_bank_response: epStatus?.bank_response || ""
        })
      });
    } catch (e) {
      console.warn("Failed to sync FAILED status to registration:", e);
    }
  }

  const finalStatus = isPaid
    ? "PAID"
    : effectiveFailed
      ? (sameOrderAsCf && (cfData?.status === "CANCELLED" || cfData?.status === "EXPIRED") ? cfData.status : "FAILED")
      : "PENDING";
  const finalPaymentStatusAz = isPaid ? "Ödənilib" : effectiveFailed ? "Uğursuz" : "Ödəniş gözlənilir";

  return {
    registration_id: cleanId,
    order_number: targetOrderId || null,
    transaction: epStatus?.transaction || txId || null,
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
    fail_reason: effectiveFailed
      ? (epFailText || regRow?.payment_fail_reason || "Ödəniş tamamlanmadı")
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
          .filter(r => r && r.payment_status === "Ödəniş gözlənilir" && isPayableRegistration(r))
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
