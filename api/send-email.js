import nodemailer from 'nodemailer';
import crypto from 'crypto';

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Only POST requests allowed' });
  }

  const { email, name, dbId, transactionId } = req.body;

  if (!email || !dbId) {
    return res.status(400).json({ message: 'Missing required fields' });
  }

  const SUPABASE_URL = "https://miwvdhwrmxoetszkxlzy.supabase.co";
  const SUPABASE_KEY = process.env.SUPABASE_ANON_KEY || "sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV";

  try {
    // 1. Datanı alırıq
    const getRes = await fetch(`${SUPABASE_URL}/rest/v1/registrations?id=eq.${dbId}&select=payload`, {
      headers: {
        'apikey': SUPABASE_KEY,
        'Authorization': `Bearer ${SUPABASE_KEY}`
      }
    });
    
    if (getRes.ok) {
      const records = await getRes.json();
      if (records && records.length > 0) {
        const payload = records[0].payload;
        
        // Əgər artıq ödənilibsə, heç nə etmə (dublikatın qarşısını al)
        if (payload.payment_status !== 'Ödənilib') {
            payload.status = 'Ödənilib';
            payload.payment_status = 'Ödənilib';
            
            // 1.5. Epoint-dən statusu yoxla və məlumatları çək
            try {
                const PUB_KEY = "i000201608";
                const PVT_KEY = process.env.EPOINT_PRIVATE_KEY || "HNIbtyFLu3PbxXlVykJEwOR1";
                const targetTransaction = transactionId || String(dbId);
                const dataObj = { public_key: PUB_KEY, transaction: targetTransaction };
                const dataJson = JSON.stringify(dataObj);
                const dataB64 = Buffer.from(dataJson).toString('base64');
                const shasum = crypto.createHash('sha1');
                shasum.update(PVT_KEY + dataB64 + PVT_KEY);
                const signatureStr = shasum.digest('base64');

                const epointRes = await fetch("https://epoint.az/api/1/get-status", {
                    method: "POST",
                    headers: { "Content-Type": "application/x-www-form-urlencoded" },
                    body: new URLSearchParams({ data: dataB64, signature: signatureStr }).toString()
                });
                
                if (epointRes.ok) {
                    const epointData = await epointRes.json();
                    if (epointData.status === 'success') {
                        payload.epoint_amount = epointData.amount;
                        payload.epoint_currency = epointData.currency;
                        payload.epoint_card_number = epointData.card_number || epointData.CARD_NUMBER || epointData.cardnumber || "";
                        payload.epoint_card_name = epointData.cardname || epointData.CARDNAME || epointData.card_name || epointData.name || "Bilinmir";
                        payload.epoint_approval_code = epointData.approval_code || epointData.APPROVAL_CODE || epointData.approvalCode || "";
                        payload.epoint_result_code = epointData.result_code || epointData.RESULT_CODE || epointData.resultCode || "";
                        payload.epoint_3dsecure = epointData.secure || epointData['3dsecure'] || epointData['3DSECURE'] || "";
                        payload.epoint_bank_response = epointData.bank_response || epointData.bankResponse || "";
                        payload.epoint_transaction = epointData.transaction;
                        payload.epoint_rrn = epointData.rrn;
                    }
                }
            } catch (epointErr) {
                console.error("send-email.js-də Epoint API xətası:", epointErr);
            }

            if (!payload.note.includes('EPOINT VASİTƏSİLƏ ÖDƏNİLDİ')) {
                payload.note += ' | EPOINT VASİTƏSİLƏ ÖDƏNİLDİ. İmtahan giriş kuponu göndərildi.';
            }

            // Yeni sətir kimi əlavə edirik (RLS-i aşmaq üçün POST)
            await fetch(`${SUPABASE_URL}/rest/v1/registrations`, {
              method: 'POST',
              headers: {
                'apikey': SUPABASE_KEY,
                'Authorization': `Bearer ${SUPABASE_KEY}`,
                'Content-Type': 'application/json',
                'Prefer': 'return=representation'
              },
              body: JSON.stringify({ payload })
            });
        }
      }
    }
  } catch (err) {
    console.error("DB Update Error:", err);
  }

  // 2. Email Göndəririk
  const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: process.env.EMAIL_USER || 'yusifliqezenfer90@gmail.com',
      pass: process.env.EMAIL_PASS || 'nnzjppmkbpbhjvow'
    }
  });

  const verifyUrl = encodeURIComponent(`https://evrikaliseyi.edu.az/verify.html?id=${dbId}`);
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
            <p style="font-size: 16px; color: #333;">Hörmətli <b>${name || 'Namizəd'}</b>,</p>
            <p style="font-size: 15px; color: #555; line-height: 1.6;">
                Qeydiyyatınız və ödənişiniz uğurla təsdiqlənmişdir. İmtahanda iştirak etmək üçün bu QR kodu imtahan günü nəzarətçiyə təqdim etməyiniz xahiş olunur.
            </p>
            
            <div style="text-align: center; margin: 30px 0; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1;">
                <img src="${qrUrl}" alt="QR Code" style="width: 150px; height: 150px; display: block; margin: 0 auto;">
                <div style="margin-top: 15px; font-weight: bold; color: #0f172a; font-size: 14px; letter-spacing: 2px;">
                    KOD: EV-${String(dbId).padStart(4, '0')}
                </div>
            </div>

            <p style="font-size: 14px; color: #64748b; text-align: center;">
                Suallarınız yaranarsa, bizimlə əlaqə saxlamaqdan çəkinməyin. Uğurlar!
            </p>
        </div>
        <div style="background: #f1f5f9; padding: 15px; text-align: center; font-size: 12px; color: #94a3b8;">
            © 2026 Evrika Təhsil Ekosistemi. Bütün hüquqlar qorunur.
        </div>
      </div>
    `
  };

  try {
    await transporter.sendMail(mailOptions);
    return res.status(200).json({ message: 'Success' });
  } catch (error) {
    console.error('Error sending email:', error);
    return res.status(500).json({ message: 'Error sending email', error: error.message });
  }
}
