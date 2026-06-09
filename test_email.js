import nodemailer from 'nodemailer';

async function testEmail() {
  const transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
          user: 'yusifliqezenfer90@gmail.com',
          pass: 'nnzjppmkbpbhjvow'
      }
  });

  const mailOptions = {
      from: '"Evrika Portal" <yusifliqezenfer90@gmail.com>',
      to: 'yusifliqezenfer90@gmail.com',
      subject: 'Test Email',
      text: 'This is a test email'
  };

  try {
      const info = await transporter.sendMail(mailOptions);
      console.log('Email sent: ' + info.response);
  } catch (error) {
      console.error('Error sending email:', error);
  }
}
testEmail();
