import re
import json

def update_index():
    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Akademik istiqamətlərimiz
    html = re.sub(
        r'<span style="color: var\(--navy\);">Akademik</span> <span style="color: var\(--burgundy\);">istiqamətlərimiz</span>',
        r'<span data-i18n="eco-title2-part1" style="color: var(--navy);">Akademik</span> <span data-i18n="eco-title2-part2" style="color: var(--burgundy);">istiqamətlərimiz</span>',
        html
    )

    # 2. Dünyaya Açılan Uğur Yolumuz!
    html = re.sub(
        r'Dünyaya Açılan<br>',
        r'<span data-i18n="alumni-sec-title2-part1">Dünyaya Açılan</span><br>',
        html
    )
    html = re.sub(
        r'Uğur Yolumuz!',
        r'<span data-i18n="alumni-sec-title2-part2">Uğur Yolumuz!</span>',
        html
    )

    # 3. TƏSİSÇİNİN MESAJI
    html = re.sub(
        r'TƏSİSÇİNİN <br/>',
        r'<span data-i18n="founder-title-part1">TƏSİSÇİNİN</span> <br/>',
        html
    )
    html = re.sub(
        r'MESAJI\s*<span style="position: absolute; bottom: 8px;',
        r'<span data-i18n="founder-title-part2">MESAJI</span>\n                <span style="position: absolute; bottom: 8px;',
        html
    )

    # 4. Milli dəyərlərə sadiq...
    html = re.sub(
        r'Milli dəyərlərə sadiq, qlobal düşüncəyə malik, <strong style="color:white;font-weight:700;">yenilikçi şəxsiyyətlər</strong> yetişdirməkdir!',
        r'<span data-i18n="mission-desc-part1">Milli dəyərlərə sadiq, qlobal düşüncəyə malik, </span><strong data-i18n="mission-desc-part2" style="color:white;font-weight:700;">yenilikçi şəxsiyyətlər</strong><span data-i18n="mission-desc-part3"> yetişdirməkdir!</span>',
        html
    )

    # 5. Gələcəyin yalnız liderlərini deyil...
    html = re.sub(
        r'Gələcəyin yalnız liderlərini deyil, dünyanı dəyişdirə bilən, cəmiyyətə fayda verən <strong style="color:white;font-weight:700;">şəxsiyyətlər formalaşdırmaqdır!</strong>',
        r'<span data-i18n="vision-desc-part1">Gələcəyin yalnız liderlərini deyil, dünyanı dəyişdirə bilən, cəmiyyətə fayda verən </span><strong data-i18n="vision-desc-part2" style="color:white;font-weight:700;">şəxsiyyətlər formalaşdırmaqdır!</strong>',
        html
    )

    # 6. EVRİKA artıq sadəcə məktəb deyil.
    html = re.sub(
        r'EVRİKA artıq sadəcə məktəb deyil\. <br/>',
        r'<span data-i18n="v2026-desc1">EVRİKA artıq sadəcə məktəb deyil.</span> <br/>',
        html
    )

    # 7. Evrika Montessori Kids Academy
    # Replace plain text h3 without data-i18n if it doesn't have it
    html = re.sub(
        r'<h3>Evrika Montessori Kids Academy</h3>',
        r'<h3 data-i18n="home-sec1-tag">Evrika Montessori Kids Academy</h3>',
        html
    )
    # Also if it has style
    html = re.sub(
        r'<h3 style="color: white; font-size: 3\.2rem; font-weight: 900; margin-bottom: 16px; line-height: 1\.1;">\s*Evrika Montessori Kids Academy</h3>',
        r'<h3 data-i18n="home-sec1-tag" style="color: white; font-size: 3.2rem; font-weight: 900; margin-bottom: 16px; line-height: 1.1;">\n                Evrika Montessori Kids Academy</h3>',
        html
    )

    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/index.html', 'w', encoding='utf-8') as f:
        f.write(html)

def update_js():
    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/src/main.js', 'r', encoding='utf-8') as f:
        js_content = f.read()

    new_az = {
        "eco-title2-part1": "Akademik",
        "eco-title2-part2": "istiqamətlərimiz",
        "alumni-sec-title2-part1": "Dünyaya Açılan",
        "alumni-sec-title2-part2": "Uğur Yolumuz!",
        "founder-title-part1": "TƏSİSÇİNİN",
        "founder-title-part2": "MESAJI",
        "mission-desc-part1": "Milli dəyərlərə sadiq, qlobal düşüncəyə malik, ",
        "mission-desc-part2": "yenilikçi şəxsiyyətlər",
        "mission-desc-part3": " yetişdirməkdir!",
        "vision-desc-part1": "Gələcəyin yalnız liderlərini deyil, dünyanı dəyişdirə bilən, cəmiyyətə fayda verən ",
        "vision-desc-part2": "şəxsiyyətlər formalaşdırmaqdır!"
    }
    new_en = {
        "eco-title2-part1": "Academic",
        "eco-title2-part2": "Branches",
        "alumni-sec-title2-part1": "Our Path of Success",
        "alumni-sec-title2-part2": "Opening to the World!",
        "founder-title-part1": "FOUNDER'S",
        "founder-title-part2": "MESSAGE",
        "mission-desc-part1": "To raise ",
        "mission-desc-part2": "innovative individuals",
        "mission-desc-part3": " loyal to national values with a global mindset!",
        "vision-desc-part1": "To shape individuals who are not only future leaders but also ",
        "vision-desc-part2": "capable of changing the world and benefiting society!"
    }
    new_ru = {
        "eco-title2-part1": "Академические",
        "eco-title2-part2": "направления",
        "alumni-sec-title2-part1": "Наш путь успеха,",
        "alumni-sec-title2-part2": "открытый миру!",
        "founder-title-part1": "ПОСЛАНИЕ",
        "founder-title-part2": "УЧРЕДИТЕЛЯ",
        "mission-desc-part1": "Воспитывать ",
        "mission-desc-part2": "инновационных людей",
        "mission-desc-part3": ", верных национальным ценностям, с глобальным мышлением!",
        "vision-desc-part1": "Формировать личностей, способных изменить мир ",
        "vision-desc-part2": "и принести пользу обществу!"
    }

    # For az
    az_str = ',\\n    '.join([f'"{k}": "{v}"' for k,v in new_az.items()])
    js_content = re.sub(r'("eco-title2": "Akademik istiqamətlərimiz",)', r'\1\n    ' + az_str + ',', js_content)

    # For en
    en_str = ',\\n    '.join([f'"{k}": "{v}"' for k,v in new_en.items()])
    js_content = re.sub(r'("eco-title2": "Our Academic Branches",)', r'\1\n    ' + en_str + ',', js_content)

    # For ru
    ru_str = ',\\n    '.join([f'"{k}": "{v}"' for k,v in new_ru.items()])
    js_content = re.sub(r'("eco-title2": "Наши академические направления",)', r'\1\n    ' + ru_str + ',', js_content)

    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/src/main.js', 'w', encoding='utf-8') as f:
        f.write(js_content)

if __name__ == "__main__":
    update_index()
    update_js()
    print("Updates applied.")
