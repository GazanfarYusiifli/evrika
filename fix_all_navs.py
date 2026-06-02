import os
import re

files_to_check = [f for f in os.listdir('.') if f.endswith('.html')]

for file in files_to_check:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # We want to replace the whole mobile media query block for the navbar, OR just delete specific bad rules
    # It's safer to use regex to replace specific properties in .nav-actions and .mobile-menu-btn
    
    # 1. Update .nav-actions in @media(max-width:1024px)
    content = re.sub(
        r'(\.nav-actions\s*\{\s*display:\s*flex\s*!important;\s*align-items:\s*center\s*!important;\s*margin-left:\s*auto\s*!important;)\s*margin-right:\s*25px\s*!important;\s*\}',
        r'\1 margin-right: 0 !important; flex-shrink: 0 !important; }',
        content
    )
    
    # 2. Update .mobile-menu-btn { margin-left: 0 !important; }
    content = re.sub(
        r'\.mobile-menu-btn\s*\{\s*margin-left:\s*0\s*!important;\s*\}',
        r'.mobile-menu-btn { margin-left: 8px !important; margin-right: 10px !important; flex-shrink: 0 !important; position: relative !important; right: auto !important; top: auto !important; transform: none !important; }',
        content
    )
    
    # 3. Remove the position: absolute block for .mobile-menu-btn
    content = re.sub(
        r'\.mobile-menu-btn\s*\{\s*position:\s*absolute\s*!important;\s*right:\s*15px\s*!important;\s*top:\s*50%\s*!important;\s*transform:\s*translateY\(-50%\)\s*!important;\s*\}',
        r'',
        content
    )
    
    # 4. Make .nav-glass-container have flex-direction: row and width: 100%
    content = re.sub(
        r'(\.nav-glass-container,\s*\.modern-floating-nav\.scrolled \.nav-glass-container\s*\{[^\}]+?position:\s*relative\s*!important;)\s*\}',
        r'\1 display: flex !important; align-items: center !important; flex-direction: row !important; width: 100% !important; box-sizing: border-box !important; }',
        content
    )

    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")

