import crypto from 'crypto';

export default async function handler(req, res) {
  const PUBLIC_KEY = "i000201608";
  const PRIVATE_KEY = process.env.EPOINT_PRIVATE_KEY || "HNIbtyFLu3PbxXlVykJEwOR1";

  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Yalnız POST sorğusuna icazə verilir' });
  }

  const { amount, order_id, description, regId, email, name } = req.body;
  const dbId = regId ? parseInt(String(regId).replace(/\D/g, ''), 10) : '';
  const finalOrderId = order_id || (dbId ? ("EV-" + String(dbId).padStart(4, '0')) : ("EV-" + Date.now()));

  const orderData = {
    public_key: PUBLIC_KEY,
    amount: amount !== undefined ? amount : 35,
    currency: "AZN",
    language: "az",
    order_id: finalOrderId,
    description: "Evrika Imtahan Kuponu " + finalOrderId,
    success_redirect_url: `https://evrikaliseyi.edu.az/success.html?regId=${dbId}&order_id=${encodeURIComponent(finalOrderId)}&email=${encodeURIComponent(email || '')}&name=${encodeURIComponent(name || '')}`,
    error_redirect_url: `https://evrikaliseyi.edu.az/error.html?regId=${dbId}&order_id=${encodeURIComponent(finalOrderId)}`,
    result_url: "https://evrikaliseyi.edu.az/api/epoint-callback"
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
      },
      body: new URLSearchParams({ data, signature })
    });

    const result = await response.json();
    return res.status(200).json(result);
  } catch (error) {
    console.error("Epoint xətası:", error);
    return res.status(500).json({ error: error.message });
  }
}
