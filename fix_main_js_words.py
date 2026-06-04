import re

def fix_founder_title():
    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/src/main.js', 'r', encoding='utf-8') as f:
        js = f.read()

    # Fix AZ
    js = js.replace('"about-founder-title-1": "TƏSİSÇİNİN MESAJI",', '"about-founder-title-1": "TƏSİSÇİNİN",')
    js = js.replace('"about-founder-title-2": "",', '"about-founder-title-2": "MESAJI",', 1)  # replace only first occurrence if AZ is first

    # Actually using regex for precise replacement
    js = re.sub(r'("about-founder-title-1":\s*)"TƏSİSÇİNİN MESAJI"', r'\1"TƏSİSÇİNİN"', js)
    js = re.sub(r'("about-founder-title-2":\s*)""(.*? Evrika Təhsil)', r'\1"MESAJI"\2', js, flags=re.DOTALL)
    
    # Fix EN
    js = re.sub(r'("about-founder-title-1":\s*)"FOUNDER\'S MESSAGE"', r'\1"FOUNDER\'S"', js)
    js = re.sub(r'("about-founder-title-2":\s*)""(.*? Evrika Education)', r'\1"MESSAGE"\2', js, flags=re.DOTALL)

    # Fix RU
    js = re.sub(r'("about-founder-title-1":\s*)"ПОСЛАНИЕ УЧРЕДИТЕЛЯ"', r'\1"ПОСЛАНИЕ"', js)
    js = re.sub(r'("about-founder-title-2":\s*)""(.*? Образовательная Экосистема)', r'\1"УЧРЕДИТЕЛЯ"\2', js, flags=re.DOTALL)

    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/src/main.js', 'w', encoding='utf-8') as f:
        f.write(js)

if __name__ == "__main__":
    fix_founder_title()
    print("Fixed founder title words in main.js.")
