import re

def fix_founder_title():
    # 1. Update about.html
    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/about.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Wrap the texts in span to avoid destroying the DOM
    # Original:
    # <h2 class="titan-header" style="..." data-i18n="about-founder-title-1">TƏSİSÇİNİN <br>
    #   <span class="gradient-text-burgundy" style="position: relative; z-index: 1;" data-i18n="about-founder-title-2">MESAJI
    #     <span style="..."></span>
    #   </span>
    # </h2>

    html = re.sub(
        r'<h2 class="titan-header"(.*?)data-i18n="about-founder-title-1">TƏSİSÇİNİN \s*<br>\s*<span class="gradient-text-burgundy"(.*?)data-i18n="about-founder-title-2">MESAJI',
        r'<h2 class="titan-header"\1><span data-i18n="about-founder-title-1">TƏSİSÇİNİN</span> <br>\n              <span class="gradient-text-burgundy"\2><span data-i18n="about-founder-title-2">MESAJI</span>',
        html,
        flags=re.DOTALL
    )

    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/about.html', 'w', encoding='utf-8') as f:
        f.write(html)

    # 2. Update main.js
    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/src/main.js', 'r', encoding='utf-8') as f:
        js = f.read()

    # AZ
    js = js.replace('"about-founder-title-1": "TƏSİSÇİNİN <br>",', '"about-founder-title-1": "TƏSİSÇİNİN MESAJI",')
    js = js.replace('"about-founder-title-2": "MESAJI <span",', '"about-founder-title-2": "",')

    # EN
    js = js.replace('"about-founder-title-1": "FOUNDER\\\'S <br>",', '"about-founder-title-1": "FOUNDER\\\'S MESSAGE",')
    js = js.replace('"about-founder-title-2": "MESSAGE <span",', '"about-founder-title-2": "",')

    # RU
    js = js.replace('"about-founder-title-1": "ПОСЛАНИЕ <br>",', '"about-founder-title-1": "ПОСЛАНИЕ УЧРЕДИТЕЛЯ",')
    js = js.replace('"about-founder-title-2": "УЧРЕДИТЕЛЯ <span",', '"about-founder-title-2": "",')

    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/src/main.js', 'w', encoding='utf-8') as f:
        f.write(js)

if __name__ == "__main__":
    fix_founder_title()
    print("Fixed founder title DOM structure and translations.")
