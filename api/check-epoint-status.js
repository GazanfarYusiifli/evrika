export default async function handler(req, res) {
  const CF_STATUS_URL = "https://evrika-api.yusifliqezenfer90.workers.dev/api/payment-status";

  const regId = req.query.regId || req.query.id || req.body?.regId || req.body?.id;
  const orderId = req.query.order_id || req.body?.order_id;

  try {
    const params = new URLSearchParams();
    if (regId) params.append("id", regId);
    if (orderId) params.append("order_id", orderId);

    const forwardRes = await fetch(`${CF_STATUS_URL}?${params.toString()}`);
    const data = await forwardRes.json();
    return res.status(forwardRes.status).json(data);
  } catch (err) {
    console.error("Status proxy error:", err);
    return res.status(500).json({ error: err.message });
  }
}
