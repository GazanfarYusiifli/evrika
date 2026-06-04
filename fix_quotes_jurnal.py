import re

def fix_quotes():
    paths = [
        '/Users/gazanfaryusifli/Downloads/EvrikaProje/jurnal.html',
        '/Users/gazanfaryusifli/Downloads/EvrikaProje/live_vercel_code/jurnal.html'
    ]
    
    for path in paths:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                html = f.read()

            # Fix the escaped quotes
            html = html.replace(r'onmousedown=\"', 'onmousedown="')
            html = html.replace(r"('az');\"", "('az');\"")
            html = html.replace(r"('en');\"", "('en');\"")
            html = html.replace(r"('ru');\"", "('ru');\"")
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Fixed quotes in {path}")
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    fix_quotes()
