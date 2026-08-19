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
    
    # 1. Update Labels to uppercase as requested
    content = re.sub(r'<label data-i18n="reg-prev-school">.*?</label>', r'<label data-i18n="reg-prev-school">HAZIRDA TƏHSİL ALDIĞI TƏHSİL MÜƏSSİSƏSİ ( BAĞÇA VƏ MƏKTƏB)</label>', content)
    content = re.sub(r'<label data-i18n="reg-class">.*?</label>', r'<label data-i18n="reg-class">MÜRACİƏT ETDİYİ SİNİF</label>', content)
    content = re.sub(r'<label data-i18n="reg-sector">.*?</label>', r'<label data-i18n="reg-sector">MÜRACİƏT ETDİYİ BÖLMƏ</label>', content)
    content = re.sub(r'<label data-i18n="reg-parent-phone">.*?</label>', r'<label data-i18n="reg-parent-phone">VALİDEYNİN ƏLAQƏ NÖMRƏSİ</label>', content)
    content = re.sub(r'<label data-i18n="reg-email">.*?</label>', r'<label data-i18n="reg-email">MAİL ÜNVANI</label>', content)

    # 2. Add the two new inputs BEFORE the Müraciət etdiyi sinif
    if 'id="mf_currentClass"' not in content:
        insert_html = r"""            <div class="dyn-input-group">
              <label>HAZIRDA TƏHSİL ALDIĞI TƏHSİL SİNİF</label>
              <input type="text" id="mf_currentClass" placeholder="Məs: 9-cu sinif" required>
            </div>
            <div class="dyn-input-group">
              <label>HAZIRDA TƏHSİL ALDIĞI TƏHSİL BÖLMƏ</label>
              <input type="text" id="mf_currentSector" placeholder="Məs: Azərbaycan bölməsi" required>
            </div>
            <div class="dyn-input-group">
              <label data-i18n="reg-class">"""
        
        content = re.sub(r'            <div class="dyn-input-group">\s*<label data-i18n="reg-class">', insert_html, content)

    # 3. Update JS variables
    if 'var currentClass =' not in content:
        js_insert = r"""              var email = document.getElementById('mf_email').value;
              var currentClass = document.getElementById('mf_currentClass') ? document.getElementById('mf_currentClass').value : '';
              var currentSector = document.getElementById('mf_currentSector') ? document.getElementById('mf_currentSector').value : '';"""
        content = re.sub(r'              var email = document.getElementById\(\'mf_email\'\).value;', js_insert, content)
        
    # 4. Update the note string concatenation
    if 'Hazırda oxuduğu sinif' not in content:
        content = re.sub(
            r'" \| Əvvəlki müəssisə: " \+ previousSchool \+',
            r'" | Əvvəlki müəssisə: " + previousSchool + " | Hazırda oxuduğu sinif: " + currentClass + " | Hazırda oxuduğu bölmə: " + currentSector +',
            content
        )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated all register forms successfully.")
