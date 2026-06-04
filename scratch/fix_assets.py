import os
import re

def fix_html_files():
    root_dir = "/Users/gazanfaryusifli/Downloads/EvrikaProje"
    
    js_pattern = re.compile(r'(src=["\'])\.?/?assets/main-CAvis0qM\.js(["\'])')
    css_pattern = re.compile(r'(href=["\'])\.?/?assets/style-BoASLbo9\.css(["\'])')
    
    for dirpath, _, filenames in os.walk(root_dir):
        # Exclude node_modules and .git
        if "node_modules" in dirpath or ".git" in dirpath:
            continue
            
        for filename in filenames:
            if filename.endswith(".html"):
                filepath = os.path.join(dirpath, filename)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                
                new_content = js_pattern.sub(r'\1/src/main.js\2', content)
                new_content = css_pattern.sub(r'\1/src/style.css\2', new_content)
                
                if new_content != content:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Fixed paths in {filepath}")

if __name__ == "__main__":
    fix_html_files()
