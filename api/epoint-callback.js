import crypto from 'crypto';
import nodemailer from 'nodemailer';

export default async function handler(req, res) {
  // Yalnız POST sorğusuna icazə veririk
  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Yalnız POST sorğusuna icazə verilir' });
  }

  const PRIVATE_KEY = process.env.EPOINT_PRIVATE_KEY || "HNIbtyFLu3PbxXlVykJEwOR1"; 
  const SUPABASE_URL = "https://miwvdhwrmxoetszkxlzy.supabase.co";
  const SUPABASE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY || process.env.SUPABASE_ANON_KEY || "sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV";

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

    // order_id 'EV-0010' kimi gələ bilər, yalnız rəqəmi çıxarırıq
    const dbId = parseInt(String(order_id).replace(/\D/g, ''), 10) || order_id;

    // Əgər ödəniş uğurludursa Supabase bazasında statusu yeniləyirik
    if (status === 'success') {
      // 1. Mövcud datanı alırıq
      const getResponse = await fetch(`${SUPABASE_URL}/rest/v1/registrations?id=eq.${dbId}&select=payload`, {
        headers: {
          'apikey': SUPABASE_KEY,
          'Authorization': `Bearer ${SUPABASE_KEY}`
        }
      });
      
      const rows = await getResponse.json();
      if (rows && rows.length > 0) {
        let existingPayload = rows[0].payload || {};
        
        // 2. Ödəniş detallarını əlavə edirik
        existingPayload.status = 'Yeni';
        existingPayload.payment_status = 'Ödənilib';
        existingPayload.epoint_amount = result.amount;
        existingPayload.epoint_currency = result.currency;
        existingPayload.epoint_card_number = result.card_number;
        existingPayload.epoint_card_type = result.card_type;
        existingPayload.epoint_bank = result.bank;
        existingPayload.epoint_transaction = result.transaction;
        existingPayload.epoint_rrn = result.rrn;
        existingPayload.epoint_date = result.date;
        
        // Yenilər (Kart sahibinin adı və bank detalları)
        existingPayload.epoint_card_name = result.cardname || result.card_name || result.name || "Bilinmir";
        existingPayload.epoint_approval_code = result.approval_code || result.approvalCode || "";
        existingPayload.epoint_result_code = result.result_code || result.resultCode || "";
        existingPayload.epoint_3dsecure = result.secure || result['3dsecure'] || result['3DSECURE'] || result['3DSecure'] || "";
        existingPayload.epoint_bank_response = result.bank_response || result.bankResponse || "";

        // 3. Supabase-ə payload-u YENİ SƏTİR KİMİ ƏLAVƏ EDİRİK (UPDATE RLS BLOKUNU KEÇMƏK ÜÇÜN)
        const updateResponse = await fetch(`${SUPABASE_URL}/rest/v1/registrations`, {
          method: 'POST',
          headers: {
            'apikey': SUPABASE_KEY,
            'Authorization': `Bearer ${SUPABASE_KEY}`,
            'Content-Type': 'application/json',
            'Prefer': 'return=representation'
          },
          body: JSON.stringify({ payload: existingPayload })
        });

        if (!updateResponse.ok) {
          console.error("Supabase yenilənmədi:", await updateResponse.text());
        }

        // --- EMAIL GÖNDƏRİLMƏSİ (SERVER TƏRƏFDƏN) ---
        try {
            const email = existingPayload.email || existingPayload['E-mail'] || (existingPayload.note && existingPayload.note.match(/E-mail:\s*([^ |]+)/)?.[1]);
            const name = existingPayload.fullName || existingPayload['Ad Soyad'] || existingPayload['[1.Əlaqə] Valideyn Adı'] || 'Şagird';

            if (email) {
                const transporter = nodemailer.createTransport({
                    service: 'gmail',
                    auth: {
                        user: process.env.EMAIL_USER || 'yusifliqezenfer90@gmail.com',
                        pass: process.env.EMAIL_PASS || 'nnzjppmkbpbhjvow'
                    }
                });

                const verifyUrl = encodeURIComponent(`https://evrikaliseyi.edu.az/verify.html?id=${order_id}`);
                const qrUrl = `https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=${verifyUrl}`;

                const mailOptions = {
                    from: '"Evrika Portal" <' + (process.env.EMAIL_USER || 'yusifliqezenfer90@gmail.com') + '>',
                    to: email,
                    subject: 'İmtahana Giriş Kuponu - Evrika Təhsil Ekosistemi',
                    html: `
                    <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #e2e8f0; border-radius: 12px; overflow: hidden;">
                        <div style="background: #8B1A2B; padding: 30px; text-align: center; color: white;">
                            <h1 style="margin: 0; font-size: 24px;">İmtahana Giriş Kuponu</h1>
                            <p style="margin: 10px 0 0; opacity: 0.8;">Evrika Beynəlxalq Elm və Texnologiya Liseyi</p>
                        </div>
                        <div style="padding: 30px; background: #ffffff;">
                            <p style="font-size: 16px; color: #333;">Hörmətli <b>${name}</b>,</p>
                            <p style="font-size: 15px; color: #555; line-height: 1.6;">
                                Qeydiyyatınız və ödənişiniz uğurla təsdiqlənmişdir. İmtahanda iştirak etmək üçün bu QR kodu imtahan günü nəzarətçiyə təqdim etməyiniz xahiş olunur.
                            </p>
                            <div style="text-align: center; margin: 30px 0; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1;">
                                <img src="${qrUrl}" alt="QR Code" style="width: 150px; height: 150px; display: block; margin: 0 auto;">
                                <div style="margin-top: 15px; font-weight: bold; color: #0f172a; font-size: 14px; letter-spacing: 2px;">
                                    KOD: EV-${String(order_id).padStart(4, '0')}
                                </div>
                            </div>
                        </div>
                    </div>`
                };
                await transporter.sendMail(mailOptions);
                console.log("Email uğurla göndərildi: " + email);
            }
        } catch (emailErr) {
            console.error("Email göndərilərkən xəta:", emailErr);
        }
      }
    }

    return res.status(200).json({ message: 'Callback uğurla işləndi' });

  } catch (error) {
    console.error("Callback xətası:", error);
    return res.status(500).json({ error: error.message });
  }
}
