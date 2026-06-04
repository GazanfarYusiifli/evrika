import re

def fix_ru_translation():
    main_js_path = '/Users/gazanfaryusifli/Downloads/EvrikaProje/src/main.js'
    with open(main_js_path, 'r', encoding='utf-8') as f:
        js = f.read()

    # The EN one is the first remaining "Kids Academy", and RU is the second.
    # We can replace the last occurrence of Kids Academy with Детская Академия
    
    parts = js.rsplit('"school-mont": "Evrika Montessori<br>Kids Academy"', 1)
    if len(parts) == 2:
        js = parts[0] + '"school-mont": "Детская Академия<br>Evrika Montessori"' + parts[1]

    with open(main_js_path, 'w', encoding='utf-8') as f:
        f.write(js)

if __name__ == "__main__":
    fix_ru_translation()
