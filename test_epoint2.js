import crypto from 'crypto';

async function test() {
  const PUBLIC_KEY = "i000201608";
  const PRIVATE_KEY = "HNIbtyFLu3PbxXlVykJEwOR1";
  
  const orderData = {
    public_key: PUBLIC_KEY,
    amount: 35,
    currency: "AZN",
    language: "az",
    order_id: "EV-0001",
    description: "Evrika Liseyi - Xidmət ödənişi",
    success_redirect_url: "https://evrikaliseyi.edu.az/success.html",
    error_redirect_url: "https://evrikaliseyi.edu.az/error.html",
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
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({ data, signature })
    });
    const result = await response.json();
    console.log("Epoint Response:", result);
  } catch(e) {
    console.error(e);
  }
}
test();
