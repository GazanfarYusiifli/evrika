import re

def fix_syntax_error():
    paths = [
        '/Users/gazanfaryusifli/Downloads/EvrikaProje/schools.html',
        '/Users/gazanfaryusifli/Downloads/EvrikaProje/live_vercel_code/schools.html'
    ]
    
    for path in paths:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                html = f.read()

            # Remove backslashes before single quotes in the onmousedown we injected
            html = html.replace(r"\'.lang-text\'", "'.lang-text'")
            html = html.replace(r"innerText=\'AZ\'", "innerText='AZ'")
            html = html.replace(r"innerText=\'EN\'", "innerText='EN'")
            html = html.replace(r"innerText=\'RU\'", "innerText='RU'")
            html = html.replace(r"display=\'none\'", "display='none'")
            html = html.replace(r"updateContent(\'az\')", "updateContent('az')")
            html = html.replace(r"updateContent(\'en\')", "updateContent('en')")
            html = html.replace(r"updateContent(\'ru\')", "updateContent('ru')")
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Fixed syntax error in {path}")
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    fix_syntax_error()
