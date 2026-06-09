import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changed = False
    
    if 'Eduhome Hazırlıq' in content:
        content = content.replace('Eduhome Hazırlıq', 'Victory Colleges by Evrika')
        changed = True
        
    if 'Eduhome' in content and 'Victory Colleges' not in content:
        # Just blind replace Eduhome with Victory Colleges in nav blocks if missed
        pass
        
    # Let's do a regex to catch any remaining "Eduhome Hazırlıq" or "Eduhome" text in the menu
    menu_regex = r'<span class="mobile-item-title".*?>Eduhome(?: Hazırlıq)?</span>'
    if re.search(menu_regex, content):
        content = re.sub(menu_regex, r'<span class="mobile-item-title" data-i18n="nav-eduhome">Victory Colleges by Evrika</span>', content)
        changed = True
        
    if changed:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated nav in {file}")

print("Mobile navbar replacements done.")
