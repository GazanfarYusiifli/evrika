import os
import re

files = [
    'register-lisey1.html',
    'register-lisey2.html',
    'register-montessori.html',
    'register-eduhome.html',
    'register-zumrud.html',
    'generate_forms.cjs'
]

for file in files:
    if not os.path.exists(file):
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Force the Qeydiyyat h1 to be burgundy by overriding the webkit fill
    content = re.sub(
        r'<h1 class="titan-header"(.*?)color: var\(--burgundy\);(.*?)>Qeydiyyat</h1>',
        r'<h1 class="titan-header"\g<1>color: var(--burgundy) !important; -webkit-text-fill-color: var(--burgundy) !important;\g<2>>Qeydiyyat</h1>',
        content
    )
    
    # Also handle if it still has color: #fff; or something in generate_forms
    content = re.sub(
        r'<h1 class="titan-header"(.*?)color: var\(--text-primary\);(.*?)>Qeydiyyat</h1>',
        r'<h1 class="titan-header"\g<1>color: var(--burgundy) !important; -webkit-text-fill-color: var(--burgundy) !important;\g<2>>Qeydiyyat</h1>',
        content
    )
    content = re.sub(
        r'<h1 class="titan-header"(.*?)color: #fff;(.*?)>Qeydiyyat</h1>',
        r'<h1 class="titan-header"\g<1>color: var(--burgundy) !important; -webkit-text-fill-color: var(--burgundy) !important;\g<2>>Qeydiyyat</h1>',
        content
    )

    # 2. Make form container background visibly reddish
    # It might be #fdf0f2 now or rgba(255, 255, 255, 0.85)
    content = re.sub(
        r'\.form-container \{([\s\S]*?)background: #[a-fA-F0-9]{6};',
        r'.form-container {\g<1>background: #fcf0f3;',
        content
    )
    content = re.sub(
        r'\.form-container \{([\s\S]*?)background: rgba\(255, 255, 255, 0\.85\);',
        r'.form-container {\g<1>background: #fce8ec;',
        content
    )
    # If I just want to replace any background in .form-container:
    # Actually, let's use a stronger regex
    content = re.sub(
        r'(\.form-container\s*\{[^}]*?background:\s*)[^;]+(;)',
        r'\g<1>#fdebf0\g<2>',
        content,
        count=1
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed Qeydiyyat color and form container background.")
