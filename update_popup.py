import re

def update_popup():
    # 1. Update index.html
    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace modal title
    html = re.sub(
        r'<h2 class="welcome-modal-title" data-i18n="modal-title">.*?</h2\s*>',
        r'<h2 class="welcome-modal-title" data-i18n="modal-title">Gələcəyin uğuru burada başlayır..</h2>',
        html,
        flags=re.DOTALL
    )

    # Replace modal description
    html = re.sub(
        r'<p class="welcome-modal-desc" data-i18n="modal-desc">.*?</p\s*>',
        r'<p class="welcome-modal-desc" data-i18n="modal-desc">\n          2026/27-ci tədris ili üzrə şagird qəbulu davam edir.\n        </p>',
        html,
        flags=re.DOTALL
    )

    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/index.html', 'w', encoding='utf-8') as f:
        f.write(html)

    # 2. Update src/main.js
    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/src/main.js', 'r', encoding='utf-8') as f:
        js = f.read()

    az_add = '"modal-title": "Gələcəyin uğuru burada başlayır..",\n    "modal-desc": "2026/27-ci tədris ili üzrə şagird qəbulu davam edir.",\n    "modal-btn": "Qeydiyyatdan keç",'
    en_add = '"modal-title": "The success of the future starts here..",\n    "modal-desc": "Student admission for the 2026/27 academic year is ongoing.",\n    "modal-btn": "Register now",'
    ru_add = '"modal-title": "Успех будущего начинается здесь..",\n    "modal-desc": "Продолжается прием учащихся на 2026/27 учебный год.",\n    "modal-btn": "Зарегистрироваться",'

    js = re.sub(r'("nav-home": "Ana Səhifə",)', r'\1\n    ' + az_add, js)
    js = re.sub(r'("nav-home": "Home",)', r'\1\n    ' + en_add, js)
    js = re.sub(r'("nav-home": "Главная",)', r'\1\n    ' + ru_add, js)

    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/src/main.js', 'w', encoding='utf-8') as f:
        f.write(js)

if __name__ == "__main__":
    update_popup()
    print("Done")
