import os
import re

files_to_check = ['montessori.html', 'victory.html', 'zumrud.html']

for file in files_to_check:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # Reverse the change
    content = re.sub(
        r'width:\s*38px\s*!important;\s*height:\s*38px\s*!important;(\s*)background:\s*#f8f9fa\s*!important;\s*border:\s*1px solid rgba\(0,0,0,0\.1\)\s*!important;\s*color:\s*#070d1f\s*!important;\s*border-radius:\s*10px\s*!important;\s*box-shadow:\s*0 2px 8px rgba\(0,0,0,0\.05\)\s*!important;',
        r'width: 44px !important; height: 44px !important;\1background: #f8f9fa !important; border: 1px solid rgba(0,0,0,0.1) !important; color: #070d1f !important; border-radius: 50% !important;',
        content
    )

    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Reverted {file}")
    else:
        print(f"No changes found in {file}")

