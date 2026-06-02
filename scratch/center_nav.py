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

    # 1) Remove the AZ lang-toggle button (desktop) - the old one that wasn't replaced
    # It may still be there with id="lang-toggle-btn"
    content = re.sub(
        r'\s*<button[^>]*lang-toggle-btn[^>]*id="lang-toggle-btn"[^>]*>.*?</button>',
        '',
        content,
        flags=re.DOTALL
    )
    # Also remove without id
    content = re.sub(
        r'\s*<button[^>]*lang-toggle-btn[^>]*>.*?<span id="lang-code">.*?</span>.*?</button>',
        '',
        content,
        flags=re.DOTALL
    )

    # 2) Remove E-jurnal button from nav-actions (desktop only; keep mobile)
    # Target: the <a href="https://app.e-evrika.com" ...> E-jurnal </a> inside nav-actions
    content = re.sub(
        r'<div class="nav-actions">\s*<a href="https://app\.e-evrika\.com".*?E-jurnal\s*</a>\s*',
        '<div class="nav-actions">\n        ',
        content,
        flags=re.DOTALL
    )

    # 3) Center nav-links by making nav-glass-container use space-between layout with centered nav
    # Change nav-glass-container to: logo on left, nav centered absolutely, actions on right
    # We'll add a style override inside the <style> tag or inline
    # Approach: wrap nav-links with a centered flex grow div
    content = content.replace(
        '<nav class="nav-links">',
        '<nav class="nav-links" style="position:absolute; left:50%; transform:translateX(-50%);">'
    )

    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Updated: {fpath.split('/')[-1]}")
    else:
        print(f"✗ No change: {fpath.split('/')[-1]}")
