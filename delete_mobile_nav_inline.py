import os
import re

files_to_check = [f for f in os.listdir('.') if f.endswith('.html')]

for file in files_to_check:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # We want to remove the specific @media(max-width:1024px) block that contains .nav-links { display: none !important; }
    # Because there might be other @media(max-width:1024px) blocks, we use a regex that looks for the start and ends at the closing brace of the logo img rule.
    
    # Pattern: @media(max-width:1024px) { \s* .nav-links ... .logo img { ... } \s* }
    # Let's match from @media(max-width:1024px) { down to the closing brace after .logo img { ... }
    
    pattern = re.compile(
        r'@media\s*\(\s*max-width\s*:\s*1024px\s*\)\s*\{\s*\.nav-links\s*\{\s*display:\s*none\s*!important;\s*\}.*?\.logo img\s*\{.*?\}.*?\}',
        re.DOTALL
    )
    
    content = pattern.sub('', content)

    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Removed inline mobile nav CSS in {file}")

