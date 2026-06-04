import nodemailer from 'nodemailer';

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Only POST requests allowed' });
  }

  const { email, name, dbId } = req.body;

  if (!email || !dbId) {
    return res.status(400).json({ message: 'Missing required fields' });
  }

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
    if (!process.env.EMAIL_PASS && !'nnzjppmkbpbhjvow') {
        console.warn('No EMAIL_PASS provided. Simulating success.');
        return res.status(200).json({ message: 'Simulated email success. Set EMAIL_PASS to send real email.' });
    }
    
    await transporter.sendMail(mailOptions);
    return res.status(200).json({ message: 'Email sent successfully' });
  } catch (error) {
    console.error('Error sending email:', error);
    return res.status(500).json({ message: 'Error sending email', error: error.message });
  }
}
