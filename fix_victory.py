import os
import re

file = 'register-victory.html'

if os.path.exists(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # The new CSS for the light theme
    new_css = """<style>
  :root {
    --burgundy: #8B1A2B;
    --burgundy-light: #FDF4F6;
    --navy: #070d1f;
    --accent: #e11d48;
    --text-primary: #1e293b;
    --text-muted: #64748b;
    --surface: #ffffff;
    --bg-color: #f8fafc;
  }
  body {
    background: linear-gradient(135deg, var(--bg-color) 0%, var(--burgundy-light) 100%);
    background-attachment: fixed;
    margin: 0; font-family: 'Inter', sans-serif; color: var(--text-primary);
    overflow-x: hidden;
  }
  .mesh-bg {
    position: fixed; inset: 0; z-index: 0; pointer-events: none;
    background: url('data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%22100%25%22 height=%22100%25%22 viewBox=%220 0 100 100%22><path d=%22M-20 50 Q 50 10, 120 50 T 250 50%22 stroke=%22rgba(139,26,43,0.05)%22 fill=%22none%22 stroke-width=%220.5%22/></svg>');
    background-size: cover; opacity: 0.8;
  }
  .centered-layout { display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; position: relative; z-index: 1; padding: 140px 20px 60px; }
  
  .form-container { 
    width: 100%; max-width: 650px; 
    background: #fdebf0; 
    border: 1px solid rgba(139, 26, 43, 0.1); 
    padding: 50px; border-radius: 32px; 
    backdrop-filter: blur(40px); -webkit-backdrop-filter: blur(40px); 
    box-shadow: 0 25px 50px -12px rgba(139, 26, 43, 0.15); 
    transition: transform 0.4s ease, box-shadow 0.4s ease; 
    margin-top: 20px; 
  }
  .form-container:hover { 
    transform: translateY(-8px); 
    box-shadow: 0 40px 80px -15px rgba(139, 26, 43, 0.2); 
    border-color: rgba(139, 26, 43, 0.2); 
  }
  
  .form-header { text-align: center; margin-bottom: 40px; }
  .form-header h2 { font-size: 1.8rem; font-weight: 800; margin: 0 0 10px 0; color: var(--burgundy); }
  .form-header p { margin: 0; color: var(--text-muted); font-size: 0.95rem; }

  .dyn-form-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
  @media (max-width: 640px) { .dyn-form-grid { grid-template-columns: 1fr; } }
  .full-width { grid-column: 1 / -1; }
  
  .dyn-input-group label { display: block; font-size: 0.8rem; font-weight: 700; color: var(--burgundy); margin-bottom: 8px; transition: color 0.3s ease; letter-spacing: 0.05em; }
  .dyn-input-group:focus-within label { color: var(--accent); }
  
  .dyn-input-group input, .dyn-input-group select { 
    width: 100%; padding: 14px 18px; 
    background: rgba(255, 255, 255, 0.9); 
    border: 1px solid rgba(139, 26, 43, 0.15); 
    border-radius: 12px; font-family: inherit; font-size: 0.95rem; 
    color: var(--text-primary); transition: all 0.3s ease; appearance: none; box-sizing: border-box; 
  }
  .dyn-input-group input::placeholder { color: #94a3b8; }
  .dyn-input-group select option { background: var(--surface); color: var(--text-primary); }
  .dyn-input-group input:hover, .dyn-input-group select:hover { background: #ffffff; border-color: rgba(139, 26, 43, 0.3); }
  .dyn-input-group input:focus, .dyn-input-group select:focus { 
    border-color: var(--burgundy); 
    background: #ffffff; 
    box-shadow: 0 0 0 3px rgba(139, 26, 43, 0.1); 
    outline: none; 
  }
  .select-arrow { position: absolute; right: 15px; top: 50%; transform: translateY(-50%); color: rgba(139,26,43,0.4); pointer-events: none; transition: color 0.3s ease; font-size: 0.8rem; }
  .dyn-input-group select:focus + .select-arrow { color: var(--burgundy); }
  
  .submit-btn { 
    width: 100%; margin-top: 30px; padding: 20px; 
    background: var(--burgundy); color: #ffffff; 
    border: none; border-radius: 16px; font-size: 1.05rem; font-weight: 800; 
    letter-spacing: 0.02em; cursor: pointer; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); 
    display: flex; align-items: center; justify-content: center; gap: 12px; 
  }
  .submit-btn:hover { transform: translateY(-3px); box-shadow: 0 20px 40px rgba(139, 26, 43, 0.3); background: #6b1220; }
  
  .payment-info-alert {
    background: rgba(139, 26, 43, 0.05); border: 1px solid rgba(139, 26, 43, 0.15); 
    border-radius: 16px; padding: 18px 20px; margin-top: 30px; display: flex; gap: 15px; align-items: flex-start; margin-bottom: -15px;
  }
  .alert-icon { color: var(--burgundy); font-size: 1.3rem; margin-top: 2px; }
  .alert-text { font-size: 0.85rem; color: var(--text-primary); line-height: 1.5; }
  .alert-text strong { color: var(--burgundy); }
</style>"""

    # 1. Apply light theme CSS block
    content = re.sub(r'<style>[\s\S]*?</style>', new_css, content, count=1)

    # 2. Update inline styles for light theme
    content = re.sub(r'color: rgba\(255,255,255,0.7\);', r'color: var(--burgundy);', content)
    content = re.sub(r'color: #fff;', r'color: var(--text-primary);', content)
    content = re.sub(r'rgba\(255,255,255,0.3\)', r'rgba(139,26,43,0.3)', content)

    # 3. Force the Qeydiyyat h1 to be burgundy by overriding the webkit fill
    content = re.sub(
        r'<h1 class="titan-header"(.*?)color: var\(--text-primary\);(.*?)>Qeydiyyat</h1>',
        r'<h1 class="titan-header"\g<1>color: var(--burgundy) !important; -webkit-text-fill-color: var(--burgundy) !important;\g<2>>Qeydiyyat</h1>',
        content
    )

    # 4. Fix labels
    content = re.sub(
        r'<label>HAZIRDA TƏHSİL ALDIĞI TƏHSİL MÜƏSSİSƏSİ \( BAĞÇA VƏ MƏKTƏB\)</label>',
        r'<label>Hazırda təhsil aldığı təhsil müəssisəsi ( bağça və məktəb)</label>',
        content
    )
    content = re.sub(
        r'<label data-i18n="reg-prev-school">HAZIRDA TƏHSİL ALDIĞI TƏHSİL MÜƏSSİSƏSİ \( BAĞÇA VƏ MƏKTƏB\)</label>',
        r'<label data-i18n="reg-prev-school">Hazırda təhsil aldığı təhsil müəssisəsi ( bağça və məktəb)</label>',
        content
    )
    
    content = re.sub(
        r'<label>MÜRACİƏT ETDİYİ SİNİF</label>',
        r'<label>Müraciət etdiyi sinif</label>',
        content
    )
    content = re.sub(
        r'<label data-i18n="reg-class">MÜRACİƏT ETDİYİ SİNİF</label>',
        r'<label data-i18n="reg-class">Müraciət etdiyi sinif</label>',
        content
    )
    
    content = re.sub(
        r'<label>MÜRACİƏT ETDİYİ BÖLMƏ</label>',
        r'<label>Müraciət etdiyi bölmə</label>',
        content
    )
    content = re.sub(
        r'<label data-i18n="reg-sector">MÜRACİƏT ETDİYİ BÖLMƏ</label>',
        r'<label data-i18n="reg-sector">Müraciət etdiyi bölmə</label>',
        content
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("register-victory.html updated successfully!")
