import re

def fix_footer():
    # 1. Update main.js
    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/src/main.js', 'r', encoding='utf-8') as f:
        js = f.read()

    az_add = '''
    "footer-ejournal": "E- JURNAL",
    "footer-copyright": "&copy; 2026 Evrika Təhsil Ekosistemi. Bütün hüquqlar qorunur.",
    "footer-privacy": "Məxfilik Siyasəti",
    "footer-terms": "İstifadə Şərtləri",'''

    en_add = '''
    "footer-ejournal": "E-JOURNAL",
    "footer-copyright": "&copy; 2026 Evrika Education Ecosystem. All rights reserved.",
    "footer-privacy": "Privacy Policy",
    "footer-terms": "Terms of Use",'''

    ru_add = '''
    "footer-ejournal": "Э-ЖУРНАЛ",
    "footer-copyright": "&copy; 2026 Образовательная Экосистема Эврика. Все права защищены.",
    "footer-privacy": "Политика конфиденциальности",
    "footer-terms": "Условия использования",'''

    js = js.replace('"footer-nav": "NAVİQASİYA",', '"footer-nav": "NAVİQASİYA",' + az_add)
    js = js.replace('"footer-nav": "NAVIGATION",', '"footer-nav": "NAVIGATION",' + en_add)
    js = js.replace('"footer-nav": "НАВИГАЦИЯ",', '"footer-nav": "НАВИГАЦИЯ",' + ru_add)

    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/src/main.js', 'w', encoding='utf-8') as f:
        f.write(js)

    # 2. Update about.html
    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/about.html', 'r', encoding='utf-8') as f:
        html = f.read()

    html = html.replace('<h4>E- JURNAL</h4>', '<h4 data-i18n="footer-ejournal">E- JURNAL</h4>')
    html = html.replace('color: var(--accent, #8B1A2B);">E- JURNAL</h4>', 'color: var(--accent, #8B1A2B);" data-i18n="footer-ejournal">E- JURNAL</h4>')
    html = html.replace('<p style="color: rgba(255,255,255,0.4); font-size: 0.85rem;">&copy; 2026 Evrika Təhsil Ekosistemi. Bütün hüquqlar qorunur.</p>', '<p style="color: rgba(255,255,255,0.4); font-size: 0.85rem;" data-i18n="footer-copyright">&copy; 2026 Evrika Təhsil Ekosistemi. Bütün hüquqlar qorunur.</p>')
    html = html.replace('href="privacy.html" style="color: rgba(255,255,255,0.3); text-decoration: none; font-size: 0.85rem; transition: 0.3s;">Məxfilik Siyasəti</a>', 'href="privacy.html" style="color: rgba(255,255,255,0.3); text-decoration: none; font-size: 0.85rem; transition: 0.3s;" data-i18n="footer-privacy">Məxfilik Siyasəti</a>')
    html = html.replace('href="terms.html" style="color: rgba(255,255,255,0.3); text-decoration: none; font-size: 0.85rem; transition: 0.3s;">İstifadə Şərtləri</a>', 'href="terms.html" style="color: rgba(255,255,255,0.3); text-decoration: none; font-size: 0.85rem; transition: 0.3s;" data-i18n="footer-terms">İstifadə Şərtləri</a>')

    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/about.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    fix_footer()
    print("Fixed footer!")
