import crypto from 'crypto';

export default async function handler(req, res) {
  // Sizin Public Key Epoint-dən verilən:
  const PUBLIC_KEY = "i000201608";
  
  // Epoint-dən Məxfi Açarı (Private Key) aldıqdan sonra buraya yazılacaq
  // Və ya ən yaxşısı Vercel Environment Variables içərisinə EPOINT_PRIVATE_KEY olaraq əlavə olunacaq
  const PRIVATE_KEY = process.env.EPOINT_PRIVATE_KEY || "d3hjs138sd8kdfhbcea0be04eafde9e8e2bad2fb092d"; 

  // Yalnız POST sorğusuna icazə veririk
  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Yalnız POST sorğusuna icazə verilir' });
  }

  // Ödəniş üçün lazımi məlumatlar frontend-dən göndəriləcək:
    const { amount, order_id, description, regId, email, name } = req.body;

  const orderData = {
    public_key: PUBLIC_KEY,
    amount: amount || 0,
    currency: "AZN",
    language: "az",
    order_id: order_id || `order_${Date.now()}`,
    description: description || "Evrika Liseyi - Xidmət ödənişi",
    success_redirect_url: `https://evrikaliseyi.edu.az/success?regId=${regId || ''}&email=${email || ''}&name=${encodeURIComponent(name || '')}`,
    error_redirect_url: "https://evrikaliseyi.edu.az/error"
  };

  const json_string = JSON.stringify(orderData);

  // 2. Data parametrinin hazırlanması (base64 encode)
  const data = Buffer.from(json_string).toString('base64');
  
  // 3. Signature (İmza) parametrinin hazırlanması
  // PHP: base64_encode(sha1(private_key + data + private_key, true))
  // Node.js: crypto.createHash('sha1').update(...).digest('base64')
  const shasum = crypto.createHash('sha1');
  shasum.update(PRIVATE_KEY + data + PRIVATE_KEY);
  const signature = shasum.digest('base64');

  try {
    // 4. Epoint-ə müraciət edirik
    const response = await fetch('https://epoint.az/api/1/request', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: new URLSearchParams({ data, signature })
    });

    const result = await response.json();
    
    // Epoint cavab olaraq transaction id və redirect_url (müştərini yönləndirəcəyimiz link) qaytaracaq
    return res.status(200).json(result);
  } catch (error) {
    console.error("Epoint xətası:", error);
    return res.status(500).json({ error: error.message });
  }
}
