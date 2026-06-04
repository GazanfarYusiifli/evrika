import re

def modify_schools():
    paths = [
        '/Users/gazanfaryusifli/Downloads/EvrikaProje/schools.html',
        '/Users/gazanfaryusifli/Downloads/EvrikaProje/live_vercel_code/schools.html'
    ]
    
    for path in paths:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                html = f.read()

            # Remove the hub-eyebrow lines
            # Example: <div class="hub-eyebrow" style="color: rgb(30, 58, 138);"><span style="background: rgb(30, 58, 138);"></span> <span data-i18n="school-early">Erkən İnkişaf</span></div>
            # Or <div class="hub-eyebrow" style="color: rgb(30, 58, 138);"><span style="background: rgb(30, 58, 138);"></span> Peşəkar İdman</div>
            
            html = re.sub(r'<div class="hub-eyebrow"[^>]*>.*?</div>\s*', '', html, flags=re.DOTALL | re.IGNORECASE)

            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Removed hub-eyebrow from {path}")
        except FileNotFoundError:
            pass

    # Now update main.js
    main_js_path = '/Users/gazanfaryusifli/Downloads/EvrikaProje/src/main.js'
    with open(main_js_path, 'r', encoding='utf-8') as f:
        js = f.read()

    # AZ
    js = re.sub(
        r'"school-mont": "Evrika Montessori<br>Kids Academy"',
        r'"school-mont": "Evrika Montessori<br>Uşaq Akademiyası"',
        js,
        count=1
    )

    # Note: EN is already "Evrika Montessori<br>Kids Academy", so we can just match the second one (RU) 
    # Or just replace the RU one directly.
    # Let's find all occurrences:
    parts = js.split('"school-mont": "Evrika Montessori<br>Kids Academy"')
    if len(parts) == 4: # It matched 3 times
        # parts[0] ... AZ ... parts[1] ... EN ... parts[2] ... RU ... parts[3]
        new_js = parts[0] + '"school-mont": "Evrika Montessori<br>Uşaq Akademiyası"' + parts[1] + '"school-mont": "Evrika Montessori<br>Kids Academy"' + parts[2] + '"school-mont": "Evrika Montessori<br>Детская Академия"' + parts[3]
        js = new_js

    with open(main_js_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print("Updated translations for school-mont in main.js")

if __name__ == "__main__":
    modify_schools()
