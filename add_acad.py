import re

def add_school_acad():
    paths = [
        '/Users/gazanfaryusifli/Downloads/EvrikaProje/schools.html',
        '/Users/gazanfaryusifli/Downloads/EvrikaProje/live_vercel_code/schools.html'
    ]
    
    for path in paths:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                html = f.read()

            # Find the h1 with class titan-header
            pattern = re.compile(r'(<h1 class="titan-header"[^>]*>)\s*Akademik\s*<span style="position: relative; color: var\(--white\); z-index: 1;">istiqamətlərimiz\s*<span\s*style="position: absolute; bottom: 8px; left: 0; width: 100%; height: 18px; background: var\(--navy\); z-index: -1; opacity: 0\.3; border-radius: 4px;"></span>\s*</span>\s*</h1>', re.DOTALL)
            
            replacement = r'\1\n          <span data-i18n="school-acad">Akademik <span style="position: relative; color: var(--white); z-index: 1;">istiqamətlərimiz<span style="position: absolute; bottom: 8px; left: 0; width: 100%; height: 18px; background: var(--navy); z-index: -1; opacity: 0.3; border-radius: 4px;"></span></span></span>\n        </h1>'
            
            html = re.sub(pattern, replacement, html)

            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Added school-acad tag in {path}")
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    add_school_acad()
