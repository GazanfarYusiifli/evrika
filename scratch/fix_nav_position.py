import re

files = [
    '/Users/gazanfaryusifli/Downloads/Evrika/eduhome.html',
    '/Users/gazanfaryusifli/Downloads/Evrika/zumrud.html',
    '/Users/gazanfaryusifli/Downloads/Evrika/montessori.html',
]

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    # Add position: relative to .nav-glass-container
    content = content.replace(
        '.nav-glass-container {\n  pointer-events: auto;\n  display: flex;\n  align-items: center;\n  justify-content: space-between;',
        '.nav-glass-container {\n  pointer-events: auto;\n  display: flex;\n  align-items: center;\n  justify-content: space-between;\n  position: relative;'
    )

    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Updated: {fpath.split('/')[-1]}")
    else:
        print(f"✗ No change: {fpath.split('/')[-1]}")
