import crypto from 'crypto';

export default async function handler(req, res) {
  const PUBLIC_KEY = "i000201608";
  const PRIVATE_KEY = process.env.EPOINT_PRIVATE_KEY || "HNIbtyFLu3PbxXlVykJEwOR1";

  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Yalnız POST sorğusuna icazə verilir' });
  }

  const { amount, order_id, description, regId, email, name } = req.body;
  const dbId = regId ? parseInt(String(regId).replace(/\D/g, ''), 10) : '';
  
  // Hər yeni cəhd üçün unikal order_id generasiya edirik (məsələn: EV-5074-8391)
  // Beləliklə istifadəçi bank səhifəsini bağlayıb yenidən daxil olduqda Epoint "Duplicate order_id" xətası vermir
  let finalOrderId = order_id;
  if (!finalOrderId) {
    if (dbId) {
      finalOrderId = `EV-${String(dbId).padStart(4, '0')}-${Date.now().toString().slice(-4)}`;
    } else {
      finalOrderId = `EV-${Date.now()}`;
    }
  } else if (!finalOrderId.includes('-') || finalOrderId.split('-').length === 2) {
    // Əgər sırf EV-5074 göndərilibsə, cəhd vaxtı əlavə edirik
    finalOrderId = `${finalOrderId}-${Date.now().toString().slice(-4)}`;
  }

  const parsedAmount = amount !== undefined && !isNaN(parseFloat(amount)) ? parseFloat(amount) : 35;

  const orderData = {
    public_key: PUBLIC_KEY,
    amount: parsedAmount,
    currency: "AZN",
    language: "az",
    order_id: finalOrderId,
    description: description || ("Evrika Imtahan Kuponu " + (dbId ? `EV-${String(dbId).padStart(4, '0')}` : finalOrderId)),
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
