import crypto from 'crypto';

export default async function handler(req, res) {
  // Yalnız POST sorğusuna icazə veririk
  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Yalnız POST sorğusuna icazə verilir' });
  }

  const PRIVATE_KEY = process.env.EPOINT_PRIVATE_KEY || "HNIbtyFLu3PbxXlVykJEwOR1"; 
  const SUPABASE_URL = "https://miwvdhwrmxoetszkxlzy.supabase.co";
  const SUPABASE_KEY = process.env.SUPABASE_ANON_KEY || "sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV"; // Bura öz Supabase anon keyinizi qeyd edin

  // Epoint tərəfindən göndərilən data və signature parametrlərini alırıq
  const { data, signature } = req.body;

  if (!data || !signature) {
    return res.status(400).json({ message: 'Məlumat çatışmır' });
  }

  // Signature (İmza) yoxlanılması
  const shasum = crypto.createHash('sha1');
  shasum.update(PRIVATE_KEY + data + PRIVATE_KEY);
  const mySignature = shasum.digest('base64');

  if (mySignature !== signature) {
    console.error("Epoint callback signature uyğun deyil!");
    return res.status(403).json({ message: 'İmza xətası' });
  }

  try {
    // Data dəyərini deşifrə edirik
    const resultString = Buffer.from(data, 'base64').toString('utf8');
    const result = JSON.parse(resultString);

    const { order_id, status } = result;

    console.log(`Epoint əməliyyatı: Sifariş ${order_id}, Status: ${status}`);

    // Əgər ödəniş uğurludursa Supabase bazasında statusu yeniləyirik
    if (status === 'success') {
      // Supabase-ə PATCH sorğusu göndəririk
      const updateResponse = await fetch(`${SUPABASE_URL}/rest/v1/registrations?id=eq.${order_id}`, {
        method: 'PATCH',
        headers: {
          'apikey': SUPABASE_KEY,
          'Authorization': `Bearer ${SUPABASE_KEY}`,
          'Content-Type': 'application/json',
          'Prefer': 'return=representation'
        },
        body: JSON.stringify({ 
          status: 'Ödənildi' 
        })
      });

      if (!updateResponse.ok) {
        console.error("Supabase yenilənmədi:", await updateResponse.text());
        return res.status(500).json({ message: 'Baza yenilənməsi xətası' });
      }
    }

    return res.status(200).json({ message: 'Callback uğurla işləndi' });

  } catch (error) {
    console.error("Callback xətası:", error);
    return res.status(500).json({ error: error.message });
  }
}
