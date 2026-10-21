import crypto from 'crypto';

const PUBLIC_KEY = "i000201608";
const PRIVATE_KEY = process.env.EPOINT_PRIVATE_KEY || "HNIbtyFLu3PbxXlVykJEwOR1";
const CF_BASE_URL = "https://evrika-api.yusifliqezenfer90.workers.dev";

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Yalnız POST sorğusuna icazə verilir' });
  }

  const { amount, order_id, description, regId, email, name } = req.body || {};
  const dbId = regId ? parseInt(String(regId).replace(/\D/g, ''), 10) : '';

  // Hər yeni cəhd üçün unikal order_id generasiya edirik (məsələn: EVR-524-...)
  const randSuffix = Math.random().toString(36).substring(2, 7).toUpperCase();
  let finalOrderId = order_id;
  if (!finalOrderId) {
    if (dbId) {
      finalOrderId = `EVR-${dbId}-${Date.now().toString(36).toUpperCase()}-${randSuffix}`;
    } else {
      finalOrderId = `EVR-${Date.now().toString(36).toUpperCase()}-${randSuffix}`;
    }
  } else if (!finalOrderId.includes('-') || finalOrderId.split('-').length === 2) {
    finalOrderId = `${finalOrderId}-${Date.now().toString(36).toUpperCase()}-${randSuffix}`;
  }

  // Real qiymətlər: Məktəbəqədər = 25 AZN, digər siniflər = 35 AZN
  let parsedAmount = 35;
  if (amount) {
    const p = parseFloat(String(amount).replace(/[^0-9.]/g, ''));
    if (!isNaN(p) && p >= 20) {
      parsedAmount = p;
    }
  }

  // 1. Öncəliklə Cloudflare Worker-ə yönləndiririk (D1 orders/payments cədvəlləri üçün)
  try {
    const cfRes = await fetch(`${CF_BASE_URL}/api/epoint-pay`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        ...req.body,
        regId: dbId || regId,
        amount: parsedAmount
      })
    });

    if (cfRes.ok) {
      const cfData = await cfRes.json();

      if (cfData.already_paid) {
        return res.status(200).json(cfData);
      }

      if (cfData.redirect_url && dbId) {
        try {
          await fetch(`${CF_BASE_URL}/api/registrations?id=${dbId}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              payment_status: "Ödəniş gözlənilir",
              epoint_transaction: cfData.transaction || "",
              last_order_id: cfData.order_number || finalOrderId,
              payment_attempt_at: new Date().toISOString()
            })
          });
        } catch (regErr) {
          console.warn("Could not update registration metadata:", regErr);
        }
      }

      return res.status(200).json(cfData);
    }
  } catch (cfErr) {
    console.warn("CF Worker forward failed, falling back to direct Epoint API:", cfErr);
  }

  // 2. Fallback: Birbaşa Epoint API (/api/1/request) ilə əlaqə
  const orderData = {
    public_key: PUBLIC_KEY,
    amount: parsedAmount,
    currency: "AZN",
    language: "az",
    order_id: finalOrderId,
    description: description || (`Evrika Liseyi Kupon № ` + (dbId ? `EV-${String(dbId).padStart(4, '0')}` : finalOrderId)),
    success_redirect_url: `https://evrikaliseyi.edu.az/success?regId=${dbId}&order_id=${encodeURIComponent(finalOrderId)}&email=${encodeURIComponent(email || '')}&name=${encodeURIComponent(name || '')}`,
    error_redirect_url: `https://evrikaliseyi.edu.az/error?regId=${dbId}&order_id=${encodeURIComponent(finalOrderId)}`,
    result_url: "https://evrikaliseyi.edu.az/result"
  };

  const json_string = JSON.stringify(orderData);
  const data = Buffer.from(json_string).toString('base64');

  const shasum = crypto.createHash('sha1');
  shasum.update(PRIVATE_KEY + data + PRIVATE_KEY);
  const signature = shasum.digest('base64');

  try {
    const response = await fetch('https://epoint.az/api/1/request', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 EvrikaPaymentClient/2.0'
      },
      body: new URLSearchParams({ data, signature })
    });

    const result = await response.json();

    if (result.redirect_url && dbId) {
      try {
        await fetch(`${CF_BASE_URL}/api/registrations?id=${dbId}`, {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            payment_status: "Ödəniş gözlənilir",
            epoint_transaction: result.transaction || "",
            last_order_id: finalOrderId,
            payment_attempt_at: new Date().toISOString()
          })
        });
      } catch (regErr) {
        console.warn("Could not update registration metadata in fallback:", regErr);
      }
    }

    return res.status(200).json({
      success: result.status === 'success',
      status: result.status,
      redirect_url: result.redirect_url,
      transaction: result.transaction,
      order_number: finalOrderId,
      registration_id: dbId,
      amount: parsedAmount,
      trace_id: result.trace_id,
      message: result.message
    });
  } catch (error) {
    console.error("Epoint xətası:", error);
    return res.status(500).json({ success: false, error: error.message });
  }
}
