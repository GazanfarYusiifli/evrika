import re

def fix_lang_switcher():
    paths = [
        '/Users/gazanfaryusifli/Downloads/EvrikaProje/schools.html',
        '/Users/gazanfaryusifli/Downloads/EvrikaProje/live_vercel_code/schools.html'
    ]
    
    for path in paths:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                html = f.read()

            # Fix AZ button
            html = re.sub(
                r'onmousedown="event\.preventDefault\(\);\s*document\.querySelectorAll\(\'\.lang-text\'\)\.forEach\(e=>e\.innerText=\'AZ\'\);\s*this\.parentElement\.style\.display=\'none\';"',
                r'onmousedown="event.preventDefault(); document.querySelectorAll(\'.lang-text\').forEach(e=>e.innerText=\'AZ\'); this.parentElement.style.display=\'none\'; if(window.updateContent) window.updateContent(\'az\');"',
                html
            )
            
            # Fix EN button
            html = re.sub(
                r'onmousedown="event\.preventDefault\(\);\s*document\.querySelectorAll\(\'\.lang-text\'\)\.forEach\(e=>e\.innerText=\'EN\'\);\s*this\.parentElement\.style\.display=\'none\';"',
                r'onmousedown="event.preventDefault(); document.querySelectorAll(\'.lang-text\').forEach(e=>e.innerText=\'EN\'); this.parentElement.style.display=\'none\'; if(window.updateContent) window.updateContent(\'en\');"',
                html
            )
            
            # Fix RU button
            html = re.sub(
                r'onmousedown="event\.preventDefault\(\);\s*document\.querySelectorAll\(\'\.lang-text\'\)\.forEach\(e=>e\.innerText=\'RU\'\);\s*this\.parentElement\.style\.display=\'none\';"',
                r'onmousedown="event.preventDefault(); document.querySelectorAll(\'.lang-text\').forEach(e=>e.innerText=\'RU\'); this.parentElement.style.display=\'none\'; if(window.updateContent) window.updateContent(\'ru\');"',
                html
            )
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Fixed lang switcher in {path}")
        except FileNotFoundError:
            print(f"File not found: {path}")

if __name__ == "__main__":
    fix_lang_switcher()
