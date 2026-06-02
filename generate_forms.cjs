const fs = require('fs');

const formCss = `
<style>
  :root {
    --burgundy: #8B1A2B;
    --navy: #070d1f;
    --accent: #e11d48;
    --accent-glow: rgba(225, 29, 72, 0.6);
    --text-primary: #f8fafc;
    --text-muted: #94a3b8;
  }
  body {
    background: linear-gradient(135deg, var(--burgundy) 0%, var(--navy) 100%);
    background-attachment: fixed;
    margin: 0; font-family: 'Inter', sans-serif; color: var(--text-primary);
    overflow-x: hidden;
  }
  .mesh-bg {
    position: fixed; inset: 0; z-index: 0; pointer-events: none;
    background: url('data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%22100%25%22 height=%22100%25%22 viewBox=%220 0 100 100%22><path d=%22M-20 50 Q 50 10, 120 50 T 250 50%22 stroke=%22rgba(255,255,255,0.03)%22 fill=%22none%22 stroke-width=%220.5%22/></svg>');
    background-size: cover; opacity: 0.8;
  }
  .centered-layout { display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; position: relative; z-index: 1; padding: 140px 20px 60px; }
  
  .form-container { width: 100%; max-width: 650px; background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(255,255,255,0.1); padding: 50px; border-radius: 32px; backdrop-filter: blur(40px); -webkit-backdrop-filter: blur(40px); box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5); transition: transform 0.4s ease, box-shadow 0.4s ease; margin-top: 20px; }
  .form-container:hover { transform: translateY(-8px); box-shadow: 0 40px 80px -15px rgba(0,0,0,0.7); border-color: rgba(255,255,255,0.15); }
  
  .form-header { text-align: center; margin-bottom: 40px; }
  .form-header h2 { font-size: 1.8rem; font-weight: 800; margin: 0 0 10px 0; color: #e11d48; }
  .form-header p { margin: 0; color: var(--text-muted); font-size: 0.95rem; }

  .dyn-form-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
  @media (max-width: 640px) { .dyn-form-grid { grid-template-columns: 1fr; } }
  .full-width { grid-column: 1 / -1; }
  
  .dyn-input-group label { display: block; font-size: 0.8rem; font-weight: 600; color: rgba(255, 255, 255, 0.5); margin-bottom: 8px; transition: color 0.3s ease; }
  .dyn-input-group:focus-within label { color: rgba(255, 255, 255, 0.9); }
  .dyn-input-group input, .dyn-input-group select { width: 100%; padding: 14px 18px; background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 12px; font-family: inherit; font-size: 0.95rem; color: white; transition: all 0.3s ease; appearance: none; box-sizing: border-box; }
  .dyn-input-group input::placeholder { color: rgba(255, 255, 255, 0.2); }
  .dyn-input-group select option { background: var(--navy); color: white; }
  .dyn-input-group input:hover, .dyn-input-group select:hover { background: rgba(255, 255, 255, 0.06); border-color: rgba(255, 255, 255, 0.15); }
  .dyn-input-group input:focus, .dyn-input-group select:focus { border-color: rgba(255, 255, 255, 0.3); background: rgba(255, 255, 255, 0.05); box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.05); outline: none; }
  .select-arrow { position: absolute; right: 15px; top: 50%; transform: translateY(-50%); color: rgba(255,255,255,0.3); pointer-events: none; transition: color 0.3s ease; font-size: 0.8rem; }
  .dyn-input-group select:focus + .select-arrow { color: rgba(255,255,255,0.8); }
  
  .submit-btn { width: 100%; margin-top: 30px; padding: 20px; background: #fff; color: #000; border: none; border-radius: 16px; font-size: 1.05rem; font-weight: 800; letter-spacing: 0.02em; cursor: pointer; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); display: flex; align-items: center; justify-content: center; gap: 12px; }
  .submit-btn:hover { transform: translateY(-3px); box-shadow: 0 20px 40px rgba(255, 255, 255, 0.15); }
  
  #payment-gateway-simulation { position: fixed; inset: 0; background: rgba(3, 7, 18, 0.9); backdrop-filter: blur(20px); z-index: 10000; display: none; align-items: center; justify-content: center; animation: fadeIn 0.3s ease; }
  .pay-card { background: #0f172a; border: 1px solid rgba(255,255,255,0.08); padding: 40px; border-radius: 32px; box-shadow: 0 40px 100px rgba(0,0,0,0.8); width: 100%; max-width: 440px; color: white; position: relative; overflow: hidden; }
  .pay-card::before { content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 5px; background: linear-gradient(90deg, #3b82f6, #8b5cf6, #e11d48); }
  .pay-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 35px; }
  .pay-amount-box { background: rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.05); padding: 20px; border-radius: 20px; text-align: center; margin-bottom: 30px; }
  .pay-amount-box p { margin: 0 0 5px 0; font-size: 0.8rem; color: var(--text-muted); text-transform: uppercase; font-weight: 700; letter-spacing: 1px; }
  .pay-amount-box h2 { margin: 0; font-size: 2.2rem; font-weight: 900; color: #fff; letter-spacing: -1px; }
  
  .pay-input-group { margin-bottom: 20px; }
  .pay-input-group label { display: block; font-size: 0.75rem; font-weight: 700; color: var(--text-muted); margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px; }
  .pay-input { width: 100%; padding: 16px; background: rgba(0,0,0,0.2); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; color: white; font-family: 'Inter', monospace; font-size: 1rem; transition: all 0.3s; box-sizing: border-box; }
  .pay-input:focus { border-color: #3b82f6; background: rgba(0,0,0,0.4); outline: none; }
  .pay-btn { width: 100%; padding: 20px; background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%); color: white; border: none; border-radius: 16px; font-weight: 800; font-size: 1.1rem; cursor: pointer; transition: all 0.3s; margin-top: 10px; box-shadow: 0 10px 20px rgba(37, 99, 235, 0.3); }
  .pay-btn:hover { transform: translateY(-2px); box-shadow: 0 15px 30px rgba(37, 99, 235, 0.4); }
  @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

  .payment-info-alert {
    background: rgba(59, 130, 246, 0.1); border: 1px solid rgba(59, 130, 246, 0.2); border-radius: 16px; padding: 18px 20px; margin-top: 30px; display: flex; gap: 15px; align-items: flex-start; margin-bottom: -15px;
  }
  .alert-icon { color: #3b82f6; font-size: 1.3rem; margin-top: 2px; }
  .alert-text { font-size: 0.85rem; color: #cbd5e1; line-height: 1.5; }
  .alert-text strong { color: white; }
</style>
`;

function getHtml(branchTitle, sectors, sourceName, hasPayment) {
    let sectorOptions = sectors.map(s => `<option value="${s}">${s}</option>`).join('');
    let isKids = sourceName.includes('Montessori') || sourceName.includes('Eduhome') || sourceName.includes('Zumrud');
    
    let classOptions = isKids ? `
        <option value="" disabled selected></option>
        <option value="1-3 yaş">1-3 yaş qrupu</option>
        <option value="3-6 yaş">3-6 yaş qrupu</option>
    ` : `
        <option value="" disabled selected></option>
        <option value="Məktəbəqədər">Məktəbəqədər</option>
        <option value="1-ci sinif">1-ci sinif</option>
        <option value="2-ci sinif">2-ci sinif</option>
        <option value="3-cü sinif">3-cü sinif</option>
        <option value="4-cü sinif">4-cü sinif</option>
        <option value="5-ci sinif">5-ci sinif</option>
        <option value="6-cı sinif">6-cı sinif</option>
        <option value="7-ci sinif">7-ci sinif</option>
        <option value="8-ci sinif">8-ci sinif</option>
        <option value="9-cu sinif">9-cu sinif</option>
        <option value="10-cu sinif">10-cu sinif</option>
        <option value="11-ci sinif">11-ci sinif</option>
    `;
    let classLabel = isKids ? "Yaş Qrupu" : "Sinif";
    let btnText = hasPayment ? "DAVAM ET" : "MÜRACİƏTİ TAMAMLA";

    let jsLogic = `
      <script>
        window.currentRegistrationId = null;
        window.currentPayloadData = null;

        (function() {
          var mainForm = document.getElementById('branchContactForm');
          if (mainForm) {
            mainForm.addEventListener('submit', async function(event) {
              event.preventDefault();
              var btn = event.target.querySelector('button[type="submit"]');
              var originalBtnContent = btn.innerHTML;
              btn.disabled = true;
              btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> GÖNDƏRİLİR...';

              var firstName = document.getElementById('mf_firstName').value;
              var lastName = document.getElementById('mf_lastName').value;
              var sectorText = document.getElementById('mf_sector').value;
              var grade = document.getElementById('mf_class').value;
              var phoneNum = document.getElementById('mf_phoneNum').value;
              var email = document.getElementById('mf_email').value;

              var note = "Filial: ${branchTitle} | Bölmə: " + sectorText + " | Sinif: " + grade + " | E-mail: " + email;

              var payloadData = {
                name: firstName + " " + lastName,
                phone: "+994" + phoneNum,
                source: "Qeydiyyat - ${sourceName}",
                status: "Yeni",
                note: note,
                date: new Date().toISOString()
              };

              try {
                const res = await fetch('https://miwvdhwrmxoetszkxlzy.supabase.co/rest/v1/registrations', {
                  method: 'POST',
                  headers: {
                    'apikey': 'sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV',
                    'Authorization': 'Bearer sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV',
                    'Content-Type': 'application/json',
                    'Prefer': 'return=representation'
                  },
                  body: JSON.stringify({ payload: payloadData })
                });
                
                const data = await res.json();
                if(data && data.length > 0) {
                    window.currentRegistrationId = data[0].id;
                    window.currentPayloadData = payloadData;
                }
                
                ${hasPayment ? `
                   window.location.href = 'payment.html?id=' + data[0].id + '&name=' + encodeURIComponent(firstName + ' ' + lastName);
                ` : `
                   alert('Təbrik edirik! Müraciətiniz uğurla qeydə alındı.');
                   event.target.reset();
                   window.location.href = 'index.html';
                `}
              } catch(e) {
                alert('Sistem xətası baş verdi. Yenidən cəhd edin.');
              } finally {
                ${hasPayment ? '' : `btn.disabled = false; btn.innerHTML = originalBtnContent;`}
              }
            });
          }
        })();
      </script>
    `;

    return `<!DOCTYPE html>
<html lang="az">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>${branchTitle.replace(/<br>/g, ' ')} | Evrika Qeydiyyat</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link rel="stylesheet" href="src/style.css">
    ${formCss}
  </head>
  <body>
  
  <header class="navbar modern-floating-nav">
    <div class="nav-glass-container">
      <a href="index.html" class="logo" style="display:flex;align-items:center;padding:0;background:none;"><img src="loqoYeni.PNG" alt="Evrika" style="height:125px;width:125px;object-fit:contain;display:block;"></a>
      <nav class="nav-links">
        <a href="index.html">Ana Səhifə</a>
        <a href="about.html">Haqqımızda</a>
        <a href="schools.html">Akademik İstiqamətlər</a>
        <a href="alumni.html">Məzunlar</a>
        <a href="achievements.html">Uğurlar</a>
        <a href="contact.html">Əlaqə</a>
      </nav>
      <div class="nav-actions">
        <a href="schools.html" class="btn btn-primary nav-btn">Qeydiyyat</a>
      </div>
      <div class="mobile-menu-btn" id="mobile-toggle"><i class="fas fa-bars"></i></div>
    </div>
  </header>

  <div class="mesh-bg"></div>

  <div class="centered-layout">
    <div style="text-align: center; margin-bottom: 50px; padding: 0 20px; position: relative; z-index: 10;">
      <div class="brand-eyebrow modern-glow" style="margin-bottom: 24px; color: rgba(255,255,255,0.7); opacity: 1; letter-spacing: 0.6em; text-transform: uppercase; font-weight: 800; font-size: 0.8rem;">
        EVRİKA TƏHSİL EKOSİSTEMİ
      </div>
      <h1 class="titan-header" style="font-size: clamp(3rem, 6vw, 5.5rem); color: #fff; margin-bottom: 30px; line-height: 1.1; font-weight: 900; letter-spacing: -0.02em;">
        Qeydiyyat
      </h1>
      <div style="width: 100px; height: 2px; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent); margin: 0 auto 30px;"></div>
      <p class="subtitle-pro" style="max-width: 850px; margin: 0 auto; font-size: 1.6rem; color: #fff; line-height: 1.6; font-weight: 700; opacity: 1;">
        ${branchTitle.replace(/<br>/g, ' ')}
      </p>
      <p style="max-width: 700px; margin: 15px auto 0; font-size: 1.1rem; color: rgba(255,255,255,0.7); line-height: 1.6;">
        Məlumatlarınızı daxil edərək onlayn müraciətinizi tamamlayın.
      </p>
    </div>

    <div class="form-container">
      <div class="form-header">
        <h2>Müraciət Forması</h2>
      </div>
      <form id="branchContactForm">
          <div class="dyn-form-grid">
            <div class="dyn-input-group">
              <label>Şagirdin Adı</label>
              <input type="text" id="mf_firstName" placeholder="Məs: Əli" required>
            </div>
            <div class="dyn-input-group">
              <label>Şagirdin Soyadı</label>
              <input type="text" id="mf_lastName" placeholder="Məs: Əliyev" required>
            </div>
            <div class="dyn-input-group full-width">
              <label>Bölmə (Sektor)</label>
              <div style="position: relative;">
                <select id="mf_sector" required>
                  <option value="" disabled selected>Bölmə seçin</option>
                  ${sectorOptions}
                </select>
                <i class="fas fa-chevron-down select-arrow"></i>
              </div>
            </div>
            <div class="dyn-input-group">
              <label>${classLabel}</label>
              <div style="position: relative;">
                <select id="mf_class" required>
                  ${classOptions}
                </select>
                <i class="fas fa-chevron-down select-arrow"></i>
              </div>
            </div>
            <div class="dyn-input-group">
              <label>Nömrə (55 123 45 67)</label>
              <input type="tel" id="mf_phoneNum" placeholder="Məs: 551234567" required>
            </div>
            <div class="dyn-input-group full-width">
              <label>E-mail ünvanı</label>
              <input type="email" id="mf_email" placeholder="Məs: info@evrika.az" required>
            </div>
          </div>
          ${hasPayment ? `
          <div class="payment-info-alert">
            <div class="alert-icon"><i class="fas fa-info-circle"></i></div>
            <div class="alert-text">
              <strong>Diqqət:</strong> Qəbul imtahanında iştirak etmək və buraxılış kuponunu əldə etmək üçün <strong>20 AZN</strong> onlayn ödəniş tələb olunur.
            </div>
          </div>
          ` : ''}
          <button type="submit" class="submit-btn" style="${hasPayment ? 'margin-top: 35px;' : ''}">
            ${btnText} <i class="fas fa-arrow-right"></i>
          </button>
        </form>
      </div>
    </div>
  </div>

  <script type="module" src="src/main.js"></script>
  ${jsLogic}
  </body>
</html>`;
}

fs.writeFileSync('/Users/gazanfaryusifli/Downloads/Evrika/register-lisey1.html', getHtml('EVRİKA Beynəlxalq<br>Elm və Texnologiya Liseyi<br>(Nərimanov filialı)', ['Azərbaycan bölməsi', 'Rus bölməsi', 'İngilis bölməsi'], 'Lisey 1', true));
fs.writeFileSync('/Users/gazanfaryusifli/Downloads/Evrika/register-lisey2.html', getHtml('EVRİKA Beynəlxalq<br>Elm və Texnologiya Liseyi<br>(Gənclik filialı)', ['Azərbaycan bölməsi', 'Türk bölməsi', 'Rus bölməsi', 'İngilis bölməsi', 'Montessori'], 'Lisey 2', true));
fs.writeFileSync('/Users/gazanfaryusifli/Downloads/Evrika/register-montessori.html', getHtml('Montessori Kids', ['Azərbaycan bölməsi', 'Rus bölməsi', 'İngilis bölməsi', 'Türk bölməsi'], 'Montessori', false));
fs.writeFileSync('/Users/gazanfaryusifli/Downloads/Evrika/register-eduhome.html', getHtml('Eduhome Center', ['Azərbaycan bölməsi', 'Rus bölməsi'], 'Eduhome', false));
fs.writeFileSync('/Users/gazanfaryusifli/Downloads/Evrika/register-zumrud.html', getHtml('Zümrüd Bağçası', ['Azərbaycan bölməsi', 'Rus bölməsi', 'İngilis bölməsi'], 'Zumrud', false));
