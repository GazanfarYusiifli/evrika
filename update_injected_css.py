import os
import re

files_to_check = [f for f in os.listdir('.') if f.endswith('.html')]

for file in files_to_check:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if 'style.css' not in content and 'main.js' not in content:
        # We need to add background: #ffffff !important; to .nav-glass-container and .modern-floating-nav
        content = re.sub(
            r'(\.nav-glass-container\s*\{\s*display:\s*flex\s*!important;)',
            r'\1\n    background: #ffffff !important;\n    backdrop-filter: none !important;\n    -webkit-backdrop-filter: none !important;\n    border: none !important;\n    box-shadow: none !important;',
            content
        )
        content = re.sub(
            r'(\.modern-floating-nav\s*\{\s*position:\s*fixed\s*!important;)',
            r'\1\n    background: #ffffff !important;',
            content
        )
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated background in {file}")

