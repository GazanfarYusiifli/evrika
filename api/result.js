import crypto from 'crypto';
import nodemailer from 'nodemailer';

export default async function handler(req, res) {
  // Epoint callback handles POST requests (and GET for verification)
  if (req.method !== 'POST' && req.method !== 'GET') {
    return res.status(405).json({ message: 'Yalnız POST/GET sorğusuna icazə verilir' });
  }

  const PRIVATE_KEY = process.env.EPOINT_PRIVATE_KEY || "HNIbtyFLu3PbxXlVykJEwOR1"; 
  const SUPABASE_URL = "https://osicmnagzeqkhwticiqp.supabase.co";
  const SUPABASE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY || process.env.SUPABASE_ANON_KEY || "sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE";

  // Parse body / query safely for all content types
  let body = req.body;
  if (typeof body === 'string') {
    try {
      body = JSON.parse(body);
    } catch {
      body = Object.fromEntries(new URLSearchParams(body));
    }
  }

  const data = body?.data || req.query?.data;
  const signature = body?.signature || req.query?.signature;

  if (!data || !signature) {
    if (req.method === 'GET') {
      return res.status(200).json({
        status: 'active',
        service: 'Evrika Epoint Payment Callback Gateway',
        endpoint: '/result',
        timestamp: new Date().toISOString()
      });
    }
    return res.status(400).json({ message: 'Məlumat çatışmır (data və ya signature tapılmadı)' });
  }

  // Signature (İmza) yoxlanılması
  const shasum = crypto.createHash('sha1');
  shasum.update(PRIVATE_KEY + data + PRIVATE_KEY);
  const mySignature = shasum.digest('base64');

  if (mySignature !== signature) {
    console.error("Epoint callback signature uyğun deyil!", { mySignature, signature });
    return res.status(403).json({ message: 'İmza xətası' });
  }

  try {
    // Data dəyərini deşifrə edirik
    const resultString = Buffer.from(data, 'base64').toString('utf8');
    const result = JSON.parse(resultString);

    const { order_id, status } = result;
    console.log(`Epoint callback: Sifariş ${order_id}, Status: ${status}`, result);

    // order_id 'EV-0010' və ya 'EV-5027-1724...' kimi gələ bilər
    const match = String(order_id).match(/^EV-(\d+)/i) || String(order_id).match(/(\d+)/);
    const dbId = match ? parseInt(match[1], 10) : null;

    let targetRow = null;

    // 1. Mövcud datanı ID ilə axtarırıq
    if (dbId) {
      const getResponse = await fetch(`${SUPABASE_URL}/rest/v1/registrations?id=eq.${dbId}&select=id,payload`, {
        headers: {
          'apikey': SUPABASE_KEY,
          'Authorization': `Bearer ${SUPABASE_KEY}`
        }
      });
      const rows = await getResponse.json();
      if (rows && rows.length > 0) {
        targetRow = rows[0];
      }
    }

    // Əgər ID ilə tapılmadısa, payload->>order_id ilə axtarırıq
    if (!targetRow && order_id) {
      const searchRes = await fetch(`${SUPABASE_URL}/rest/v1/registrations?payload->>order_id=eq.${order_id}&select=id,payload`, {
        headers: {
          'apikey': SUPABASE_KEY,
          'Authorization': `Bearer ${SUPABASE_KEY}`
        }
      });
      const rows = await searchRes.json();
      if (rows && rows.length > 0) {
        targetRow = rows[0];
      }
    }

    if (targetRow) {
      let existingPayload = targetRow.payload || {};
      const rowId = targetRow.id;

      // Əgər ödəniş uğurludursa Supabase bazasında statusu yeniləyirik
      if (status === 'success') {
        existingPayload.status = 'Yeni';
        existingPayload.payment_status = 'Ödənilib';
        existingPayload.order_id = "EV-" + String(rowId).padStart(4, '0');
        existingPayload.epoint_amount = result.amount;
        existingPayload.epoint_currency = result.currency || 'AZN';
        existingPayload.epoint_card_number = result.card_mask || result.card_number || "";
        existingPayload.epoint_card_type = result.card_type || "BANK KARTI";
        existingPayload.epoint_bank = result.bank || "Epoint";
        existingPayload.epoint_transaction = result.transaction || "";
        existingPayload.epoint_rrn = result.rrn || "";
        existingPayload.epoint_date = result.date || new Date().toISOString();
        
        // Kart sahibinin adı və bank detalları
        existingPayload.epoint_card_name = result.card_name || result.cardname || result.name || "Bilinmir";
        existingPayload.epoint_approval_code = result.approval_code || result.approvalCode || "";
        existingPayload.epoint_result_code = result.code || result.result_code || "000";
        existingPayload.epoint_3dsecure = result.secure || result['3dsecure'] || "AUTHENTICATED";
        existingPayload.epoint_bank_response = result.bank_response || result.bankResponse || "RESULT: OK";

        if (!existingPayload.note || !existingPayload.note.includes('EPOINT VASİTƏSİLƏ ÖDƏNİLDİ')) {
          existingPayload.note = (existingPayload.note ? existingPayload.note + ' | ' : '') + 'EPOINT VASİTƏSİLƏ ÖDƏNİLDİ. İmtahan giriş kuponu göndərildi.';
        }

        // Update Supabase
        await fetch(`${SUPABASE_URL}/rest/v1/registrations?id=eq.${rowId}`, {
          method: 'PATCH',
          headers: {
            'apikey': SUPABASE_KEY,
            'Authorization': `Bearer ${SUPABASE_KEY}`,
            'Content-Type': 'application/json',
            'Prefer': 'return=representation'
          },
          body: JSON.stringify({ payload: existingPayload })
        });

        // Email göndərilməsini asinxron başladırıq
        const email = existingPayload.email || existingPayload['E-mail'] || (existingPayload.note && existingPayload.note.match(/E-mail:\s*([^ |]+)/)?.[1]);
        const name = existingPayload.fullName || existingPayload['Ad Soyad'] || existingPayload['[1.Əlaqə] Valideyn Adı'] || 'Şagird';

        if (email) {
          try {
            const transporter = nodemailer.createTransport({
              service: 'gmail',
              auth: {
                user: process.env.EMAIL_USER || 'yusifliqezenfer90@gmail.com',
                pass: process.env.EMAIL_PASS || 'nnzjppmkbpbhjvow'
              }
            });

            const verifyUrl = encodeURIComponent(`https://evrikaliseyi.edu.az/verify.html?id=EV-${String(rowId).padStart(4, '0')}`);
            const qrUrl = `https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=${verifyUrl}`;

            transporter.sendMail({
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
            }).catch(err => console.error("Async email error:", err));
          } catch (mErr) {
            console.error("Transporter creation error:", mErr);
          }
        }
      } else {
        // Ödəniş uğursuz olarsa
        if (existingPayload.payment_status !== 'Ödənilib') {
          existingPayload.epoint_bank_response = result.bank_response || result.bankResponse || result.message || `Status: ${status}`;
          existingPayload.epoint_result_code = result.code || result.result_code || "";
          
          await fetch(`${SUPABASE_URL}/rest/v1/registrations?id=eq.${rowId}`, {
            method: 'PATCH',
            headers: {
              'apikey': SUPABASE_KEY,
              'Authorization': `Bearer ${SUPABASE_KEY}`,
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({ payload: existingPayload })
          });
        }
      }
    }

    return res.status(200).json({ status: 'success', message: 'Callback uğurla işləndi' });

  } catch (error) {
    console.error("Callback xətası:", error);
    return res.status(500).json({ error: error.message });
  }
}
