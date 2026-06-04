import re

def fix_vacancy_text():
    # 1. Update HTML
    paths = [
        '/Users/gazanfaryusifli/Downloads/EvrikaProje/vacancy.html',
        '/Users/gazanfaryusifli/Downloads/EvrikaProje/live_vercel_code/vacancy.html'
    ]
    for path in paths:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                html = f.read()
            html = html.replace(
                '<a href="schools.html" class="btn btn-primary nav-btn">Qeydiyyat</a>',
                '<a href="schools.html" class="btn btn-primary nav-btn" data-i18n="nav-register">Qeydiyyat</a>'
            )
            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Updated Qeydiyyat in {path}")
        except FileNotFoundError:
            pass

    # 2. Update main.js
    main_js_path = '/Users/gazanfaryusifli/Downloads/EvrikaProje/src/main.js'
    with open(main_js_path, 'r', encoding='utf-8') as f:
        js = f.read()

    new_az = r""",
    "vac-eyebrow": "BİZİM KOMANDAMIZA QOŞUL",
    "vac-title": "Karyera və <span style=\"position: relative; color: var(--white); z-index: 1;\">Vakansiyalar<span style=\"position: absolute; bottom: 8px; left: 0; width: 100%; height: 18px; background: var(--navy); z-index: -1; opacity: 0.3; border-radius: 4px;\"></span></span>",
    "vac-desc": "Təhsildə innovasiyalar yaratmaq üçün <span style=\"color: var(--white); font-weight: 800;\">istedadlı və peşəkar</span> mütəxəssislərlə birlikdə çalışırıq."
"""
    new_en = r""",
    "vac-eyebrow": "JOIN OUR TEAM",
    "vac-title": "Careers and <span style=\"position: relative; color: var(--white); z-index: 1;\">Vacancies<span style=\"position: absolute; bottom: 8px; left: 0; width: 100%; height: 18px; background: var(--navy); z-index: -1; opacity: 0.3; border-radius: 4px;\"></span></span>",
    "vac-desc": "We work together with <span style=\"color: var(--white); font-weight: 800;\">talented and professional</span> experts to create innovations in education."
"""
    new_ru = r""",
    "vac-eyebrow": "ПРИСОЕДИНЯЙТЕСЬ К НАШЕЙ КОМАНДЕ",
    "vac-title": "Карьера и <span style=\"position: relative; color: var(--white); z-index: 1;\">Вакансии<span style=\"position: absolute; bottom: 8px; left: 0; width: 100%; height: 18px; background: var(--navy); z-index: -1; opacity: 0.3; border-radius: 4px;\"></span></span>",
    "vac-desc": "Мы работаем вместе с <span style=\"color: var(--white); font-weight: 800;\">талантливыми и профессиональными</span> специалистами для создания инноваций в сфере образования."
"""

    # We need to insert these before the closing bracket of each language.
    # The structure is:
    # "nav-ptim-desc": "PTİM"
    # },
    # for az, en, ru.

    # Find the end of 'az' dictionary
    js = re.sub(r'("nav-ptim-desc": "PTİM"\s*)\}', r'\1' + new_az + r'}', js, count=1)
    
    # After doing az, the NEXT one is EN
    js = re.sub(r'("nav-ptim-desc": "PTİM"\s*)\}', r'\1' + new_en + r'}', js, count=1)
    
    # After EN, the NEXT one is RU
    # But wait, RU has "nav-ptim-desc": "ЦППР"
    js = re.sub(r'("nav-ptim-desc": "ЦППР"\s*)\}', r'\1' + new_ru + r'}', js, count=1)

    with open(main_js_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print("Updated main.js with vacancy translations")

if __name__ == "__main__":
    fix_vacancy_text()
