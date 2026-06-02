import os
import re

files_to_check = [f for f in os.listdir('.') if f.endswith('.html')]

for file in files_to_check:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # Strip any positioning from .mobile-menu-btn in the media query
    # Find .mobile-menu-btn { ... } and remove position, right, top, transform
    content = re.sub(
        r'(\.mobile-menu-btn\s*\{[^}]*?)position:\s*absolute\s*!important;\s*right:\s*[^;]+;\s*top:\s*[^;]+;\s*transform:\s*translateY\(-50%\)\s*!important;',
        r'\1 position: relative !important; right: auto !important; top: auto !important; transform: none !important;',
        content
    )
    
    # Let's just be aggressive and replace ANY position: absolute inside .mobile-menu-btn block
    content = re.sub(
        r'(\.mobile-menu-btn\s*\{[^}]*?)position:\s*absolute\s*!important;',
        r'\1 position: relative !important;',
        content
    )

    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")

