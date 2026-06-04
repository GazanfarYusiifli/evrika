import re

def translate_not_found():
    paths = [
        '/Users/gazanfaryusifli/Downloads/EvrikaProje/vacancy.html',
        '/Users/gazanfaryusifli/Downloads/EvrikaProje/live_vercel_code/vacancy.html'
    ]
    for path in paths:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                html = f.read()
            html = html.replace(
                '<h3 style="font-size: 1.5rem; color: var(--navy); margin-bottom: 12px;">Uyğun Vakansiya Tapmadınız?</h3>',
                '<h3 style="font-size: 1.5rem; color: var(--navy); margin-bottom: 12px;" data-i18n="vac-not-found-title">Uyğun Vakansiya Tapmadınız?</h3>'
            )
            html = html.replace(
                '<p style="color: var(--text-muted); margin-bottom: 24px; max-width: 600px; margin-left: auto; margin-right: auto;">\n              CV-nizi bizə birbaşa göndərin. Gələcəkdə açıla biləcək vakansiyalar üçün namizəd bazamıza əlavə edək.\n            </p>',
                '<p style="color: var(--text-muted); margin-bottom: 24px; max-width: 600px; margin-left: auto; margin-right: auto;" data-i18n="vac-not-found-desc">\n              CV-nizi bizə birbaşa göndərin. Gələcəkdə açıla biləcək vakansiyalar üçün namizəd bazamıza əlavə edək.\n            </p>'
            )
            # Just in case the whitespace differs
            html = re.sub(
                r'(<p style="[^"]*margin-bottom: 24px;[^"]*">)\s*CV-nizi bizə birbaşa göndərin.*?bazamıza əlavə edək\.\s*</p>',
                r'\1<span data-i18n="vac-not-found-desc">CV-nizi bizə birbaşa göndərin. Gələcəkdə açıla biləcək vakansiyalar üçün namizəd bazamıza əlavə edək.</span></p>',
                html,
                flags=re.DOTALL
            )

            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Updated HTML in {path}")
        except FileNotFoundError:
            pass

    # 2. Update main.js
    main_js_path = '/Users/gazanfaryusifli/Downloads/EvrikaProje/src/main.js'
    with open(main_js_path, 'r', encoding='utf-8') as f:
        js = f.read()

    new_az = r""",
    "vac-not-found-title": "Uyğun Vakansiya Tapmadınız?",
    "vac-not-found-desc": "CV-nizi bizə birbaşa göndərin. Gələcəkdə açıla biləcək vakansiyalar üçün namizəd bazamıza əlavə edək."
"""
    new_en = r""",
    "vac-not-found-title": "Didn't Find a Suitable Vacancy?",
    "vac-not-found-desc": "Send your CV directly to us. We will add it to our candidate database for future vacancies."
"""
    new_ru = r""",
    "vac-not-found-title": "Не нашли подходящую вакансию?",
    "vac-not-found-desc": "Отправьте свое резюме напрямую нам. Мы добавим его в нашу базу кандидатов для будущих вакансий."
"""

    # We need to insert these before the closing bracket of each language.
    
    js = re.sub(r'("vac-desc": "Təhsildə innovasiyalar.*?çalışırıq."\s*)\}', r'\1' + new_az + r'}', js, count=1)
    js = re.sub(r'("vac-desc": "We work together.*?education."\s*)\}', r'\1' + new_en + r'}', js, count=1)
    js = re.sub(r'("vac-desc": "Мы работаем вместе.*?образования."\s*)\}', r'\1' + new_ru + r'}', js, count=1)

    with open(main_js_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print("Updated main.js with vac-not-found translations")

if __name__ == "__main__":
    translate_not_found()
