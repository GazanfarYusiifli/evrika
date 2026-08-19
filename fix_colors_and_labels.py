import os
import re

files = [
    'register-lisey1.html',
    'register-lisey2.html',
    'register-montessori.html',
    'register-eduhome.html',
    'register-zumrud.html'
]

for file in files:
    if not os.path.exists(file):
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Make Qeydiyyat title red
    content = re.sub(
        r'<h1 class="titan-header"(.*?)color: var\(--text-primary\);(.*?)>Qeydiyyat</h1>',
        r'<h1 class="titan-header"\g<1>color: var(--burgundy);\g<2>>Qeydiyyat</h1>',
        content
    )

    # 2. Make form container slightly reddish
    content = re.sub(
        r'\.form-container \{([\s\S]*?)background: rgba\(255, 255, 255, 0\.85\);',
        r'.form-container {\g<1>background: #fdf0f2;',
        content
    )

    # 3. Fix the specific labels to match the requested case
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

print("Updated colors and labels in all files.")
