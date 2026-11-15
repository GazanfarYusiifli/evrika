import nodemailer from 'nodemailer';

const CF_BASE_URL = "https://evrika-api.yusifliqezenfer90.workers.dev";

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Only POST requests allowed' });
  }

  const { email, name, dbId, force } = req.body || {};
  const cleanDbId = dbId ? parseInt(String(dbId).replace(/\D/g, ''), 10) : null;

  if (!cleanDbId || isNaN(cleanDbId)) {
    return res.status(400).json({ message: 'Missing valid dbId' });
  }

  let regRow = null;
  let isConfirmedPaid = false;

  try {
    const [regRes, statusRes] = await Promise.all([
      fetch(`${CF_BASE_URL}/api/registrations?id=${cleanDbId}`).catch(() => null),
      fetch(`${CF_BASE_URL}/api/payment-status?id=${cleanDbId}`).catch(() => null)
    ]);

    if (regRes && regRes.ok) {
      const records = await regRes.json().catch(() => []);
      regRow = Array.isArray(records) && records.length > 0 ? records[0] : null;
    }

    const statusJson = statusRes && statusRes.ok ? await statusRes.json().catch(() => null) : null;
    isConfirmedPaid =
      regRow?.payment_status === 'Ödənilib' ||
      statusJson?.data?.isPaid === true ||
      statusJson?.data?.status === 'PAID';
  } catch (err) {
    console.error("D1 lookup error in send-email:", err);
  }

  if (!isConfirmedPaid) {
    return res.status(409).json({ message: 'Payment is not confirmed yet' });
  }

  if (regRow?.coupon_email_sent && !force) {
    return res.status(200).json({ message: 'Coupon email already sent', skipped: true });
  }

  const targetEmail = (email || regRow?.email || regRow?.payload?.email || '').trim();
  const targetName = (name || regRow?.name || regRow?.payload?.name || 'Namizəd').trim();

  if (!targetEmail || !targetEmail.includes('@')) {
    return res.status(400).json({ message: 'Missing valid email address' });
  }

  // 2. Email Göndəririk
  const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: process.env.EMAIL_USER || 'yusifliqezenfer90@gmail.com',
      pass: process.env.EMAIL_PASS || 'rpgxzocjbyrefdlj'
    }
  });

  const couponCode = regRow?.coupon_code || `EV-${String(cleanDbId).padStart(4, '0')}`;
  const verifyUrl = encodeURIComponent(`https://evrikaliseyi.edu.az/verify.html?id=${cleanDbId}`);
  const qrUrl = `https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=${verifyUrl}`;

  const mailOptions = {
    from: '"Evrika Portal" <' + (process.env.EMAIL_USER || 'yusifliqezenfer90@gmail.com') + '>',
    to: targetEmail,
    subject: 'İmtahana Giriş Kuponu - Evrika Təhsil Ekosistemi',
    html: `
      <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #e2e8f0; border-radius: 12px; overflow: hidden;">
        <div style="background: #8B1A2B; padding: 30px; text-align: center; color: white;">
            <h1 style="margin: 0; font-size: 24px;">İmtahana Giriş Kuponu</h1>
            <p style="margin: 10px 0 0; opacity: 0.8;">Evrika Beynəlxalq Elm və Texnologiya Liseyi</p>
        </div>
        <div style="padding: 30px; background: #ffffff;">
            <p style="font-size: 16px; color: #333;">Hörmətli <b>${targetName}</b>,</p>
            <p style="font-size: 15px; color: #555; line-height: 1.6;">
                Qeydiyyatınız və ödənişiniz uğurla təsdiqlənmişdir. İmtahanda iştirak etmək üçün bu QR kodu imtahan günü nəzarətçiyə təqdim etməyiniz xahiş olunur.
            </p>
            
            <div style="text-align: center; margin: 30px 0; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1;">
                <img src="${qrUrl}" alt="QR Code" style="width: 150px; height: 150px; display: block; margin: 0 auto;">
                <div style="margin-top: 15px; font-weight: bold; color: #0f172a; font-size: 14px; letter-spacing: 2px;">
                    KOD: ${couponCode}
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

    try {
      const existingNote = String(regRow?.note || '');
      const updatedNote = existingNote.includes('İmtahan giriş kuponu göndərildi')
        ? existingNote
        : (existingNote ? `${existingNote} | ` : '') + 'EPOINT VASİTƏSİLƏ ÖDƏNİLDİ. İmtahan giriş kuponu göndərildi.';

      await fetch(`${CF_BASE_URL}/api/registrations?id=${cleanDbId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          coupon_email_sent: true,
          coupon_email_sent_at: new Date().toISOString(),
          note: updatedNote
        })
      });
    } catch (noteErr) {
      console.warn("Could not record coupon_email_sent flag:", noteErr);
    }

    return res.status(200).json({ message: 'Success' });
  } catch (error) {
    console.error('Error sending email:', error);
    return res.status(500).json({ message: 'Error sending email', error: error.message });
  }
}
