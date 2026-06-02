import os
import re

files_to_check = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']

for file in files_to_check:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # We want to find width: 44px, height: 44px, border-radius: 50% and change it.
    content = re.sub(
        r'width:\s*44px\s*!important;\s*height:\s*44px\s*!important;(\s*)background:\s*#f8f9fa\s*!important;\s*border:\s*1px solid rgba\(0,0,0,0\.1\)\s*!important;\s*color:\s*#070d1f\s*!important;\s*border-radius:\s*50%\s*!important;',
        r'width: 38px !important; height: 38px !important;\1background: #f8f9fa !important; border: 1px solid rgba(0,0,0,0.1) !important; color: #070d1f !important; border-radius: 10px !important; box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important;',
        content
    )

    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")

