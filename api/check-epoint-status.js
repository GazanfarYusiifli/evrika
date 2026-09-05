import crypto from 'crypto';
import nodemailer from 'nodemailer';

export default async function handler(req, res) {
  const PUBLIC_KEY = "i000201608";
  const PRIVATE_KEY = process.env.EPOINT_PRIVATE_KEY || "HNIbtyFLu3PbxXlVykJEwOR1";
  const SUPABASE_URL = "https://osicmnagzeqkhwticiqp.supabase.co";
  const SUPABASE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY || process.env.SUPABASE_ANON_KEY || "sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE";

  const regId = req.query.regId || req.body?.regId;
  const orderIdParam = req.query.order_id || req.body?.order_id;

  if (!regId && !orderIdParam) {
    return res.status(400).json({ message: 'regId və ya order_id tələb olunur' });
  }

  const dbId = regId ? parseInt(String(regId).replace(/\D/g, ''), 10) : parseInt(String(orderIdParam).replace(/\D/g, ''), 10);
  const targetOrderId = orderIdParam || (dbId ? ("EV-" + String(dbId).padStart(4, '0')) : "");

  try {
    // 1. Epoint-dən statusu yoxlayırıq
    const dataObj = { public_key: PUBLIC_KEY, order_id: targetOrderId };
    const dataJson = JSON.stringify(dataObj);
    const dataB64 = Buffer.from(dataJson).toString('base64');
    
    const shasum = crypto.createHash('sha1');
    shasum.update(PRIVATE_KEY + dataB64 + PRIVATE_KEY);
    const signatureStr = shasum.digest('base64');

    const epointRes = await fetch("https://epoint.az/api/1/get-status", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams({ data: dataB64, signature: signatureStr }).toString()
    });

    if (!epointRes.ok) {
      return res.status(500).json({ message: 'Epoint server xətası' });
    }

    const epointData = await epointRes.json();
    console.log(`Check status for ${targetOrderId}:`, epointData);

    // 2. Supabase-də həmin qeydi tapırıq
    let targetRow = null;
    if (dbId) {
      const getRes = await fetch(`${SUPABASE_URL}/rest/v1/registrations?id=eq.${dbId}&select=id,payload`, {
        headers: {
          'apikey': SUPABASE_KEY,
          'Authorization': `Bearer ${SUPABASE_KEY}`
        }
      });
      if (getRes.ok) {
        const records = await getRes.json();
        if (records && records.length > 0) targetRow = records[0];
      }
    }

    if (!targetRow && targetOrderId) {
      const searchRes = await fetch(`${SUPABASE_URL}/rest/v1/registrations?payload->>order_id=eq.${targetOrderId}&select=id,payload`, {
        headers: {
          'apikey': SUPABASE_KEY,
          'Authorization': `Bearer ${SUPABASE_KEY}`
        }
      });
      if (searchRes.ok) {
        const records = await searchRes.json();
        if (records && records.length > 0) targetRow = records[0];
      }
    }

    if (!targetRow) {
      return res.status(200).json({
        status: epointData.status,
        epointData,
        isPaid: epointData.status === 'success'
      });
    }

    let payload = targetRow.payload || {};
    const rowId = targetRow.id;
    let updated = false;

    if (epointData.status === 'success') {
      if (payload.payment_status !== 'Ödənilib') {
        payload.status = 'Yeni';
        payload.payment_status = 'Ödənilib';
        payload.order_id = "EV-" + String(rowId).padStart(4, '0');
        payload.epoint_amount = epointData.amount;
        payload.epoint_currency = epointData.currency || 'AZN';
        payload.epoint_card_number = epointData.card_mask || epointData.card_number || epointData.CARD_NUMBER || "";
        payload.epoint_card_name = epointData.card_name || epointData.cardname || epointData.CARDNAME || "Bilinmir";
        payload.epoint_approval_code = epointData.approval_code || epointData.APPROVAL_CODE || "";
        payload.epoint_result_code = epointData.code || epointData.result_code || epointData.RESULT_CODE || "000";
        payload.epoint_3dsecure = epointData.secure || epointData['3dsecure'] || "AUTHENTICATED";
        payload.epoint_bank_response = epointData.bank_response || epointData.bankResponse || "RESULT: OK";
        payload.epoint_transaction = epointData.transaction;
        payload.epoint_rrn = epointData.rrn;
        payload.epoint_date = epointData.date || new Date().toISOString();

        if (!payload.note || !payload.note.includes('EPOINT VASİTƏSİLƏ ÖDƏNİLDİ')) {
          payload.note = (payload.note ? payload.note + ' | ' : '') + 'EPOINT VASİTƏSİLƏ ÖDƏNİLDİ. İmtahan giriş kuponu göndərildi.';
        }

        updated = true;

        // Email göndərilməsi
        try {
          const email = payload.email || payload['E-mail'] || (payload.note && payload.note.match(/E-mail:\s*([^ |]+)/)?.[1]);
          const name = payload.fullName || payload['Ad Soyad'] || payload['[1.Əlaqə] Valideyn Adı'] || 'Şagird';

          if (email) {
            const transporter = nodemailer.createTransport({
              service: 'gmail',
              auth: {
                user: process.env.EMAIL_USER || 'yusifliqezenfer90@gmail.com',
                pass: process.env.EMAIL_PASS || 'nnzjppmkbpbhjvow'
              }
            });

            const verifyUrl = encodeURIComponent(`https://evrikaliseyi.edu.az/verify.html?id=EV-${String(rowId).padStart(4, '0')}`);
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
                              KOD: EV-${String(rowId).padStart(4, '0')}
                          </div>
                      </div>
                  </div>
              </div>`
            };
            await transporter.sendMail(mailOptions);
          }
        } catch (mErr) {
          console.error("Mail error in check-status:", mErr);
        }
      }
    } else {
      if (payload.payment_status !== 'Ödənilib') {
        payload.epoint_bank_response = epointData.bank_response || epointData.bankResponse || epointData.message || `Status: ${epointData.status}`;
        payload.epoint_result_code = epointData.code || epointData.result_code || epointData.RESULT_CODE || "";
        updated = true;
      }
    }

    if (updated) {
      await fetch(`${SUPABASE_URL}/rest/v1/registrations?id=eq.${rowId}`, {
        method: 'PATCH',
        headers: {
          'apikey': SUPABASE_KEY,
          'Authorization': `Bearer ${SUPABASE_KEY}`,
          'Content-Type': 'application/json',
          'Prefer': 'return=representation'
        },
        body: JSON.stringify({ payload })
      });
    }

    return res.status(200).json({
      status: epointData.status,
      epointData,
      isPaid: payload.payment_status === 'Ödənilib'
    });

  } catch (error) {
    console.error("Check status error:", error);
    return res.status(500).json({ error: error.message });
  }
}
