import re

files = [
    '/Users/gazanfaryusifli/Downloads/Evrika/lisey.html',
    '/Users/gazanfaryusifli/Downloads/Evrika/lisey2.html',
]

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    # 1) Remove E-jurnal button from nav-actions (desktop only)
    content = re.sub(
        r'<div class="nav-actions"[^>]*>\s*<a href="https://app\.e-evrika\.com".*?E-jurnal\s*</a>\s*',
        '<div class="nav-actions" style="display:flex; align-items:center; gap:15px;">\n        ',
        content,
        flags=re.DOTALL
    )

    # 2) Center nav-links with absolute positioning
    content = content.replace(
        '<nav class="nav-links">',
        '<nav class="nav-links" style="position:absolute; left:50%; transform:translateX(-50%);">'
    )

    # 3) Add position:relative to nav-glass-container (inline style in <style> tag)
    # The CSS for nav-glass-container is inline in these files
    content = re.sub(
        r'(\.nav-glass-container\s*\{[^}]*?)(display:\s*flex;)',
        r'\1position: relative;\n    display: flex;',
        content,
        flags=re.DOTALL
    )

    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Updated: {fpath.split('/')[-1]}")
    else:
        print(f"✗ No change: {fpath.split('/')[-1]}")
