import re

def add_en_vac_translations():
    main_js_path = '/Users/gazanfaryusifli/Downloads/EvrikaProje/src/main.js'
    with open(main_js_path, 'r', encoding='utf-8') as f:
        js = f.read()

    new_en = r""",
    "vac-eyebrow": "JOIN OUR TEAM",
    "vac-title": "Careers and <span style=\"position: relative; color: var(--white); z-index: 1;\">Vacancies<span style=\"position: absolute; bottom: 8px; left: 0; width: 100%; height: 18px; background: var(--navy); z-index: -1; opacity: 0.3; border-radius: 4px;\"></span></span>",
    "vac-desc": "We work together with <span style=\"color: var(--white); font-weight: 800;\">talented and professional</span> experts to create innovations in education."
"""

    js = re.sub(r'("nav-ptim-desc": "PTDC"\s*)\}', r'\1' + new_en + r'}', js, count=1)

    with open(main_js_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print("Fixed EN vacancy translations")

if __name__ == "__main__":
    add_en_vac_translations()
