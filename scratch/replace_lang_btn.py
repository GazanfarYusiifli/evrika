import os
import re

# Desktop: full lang-toggle button block (with chevron icon inside)
desktop_old = re.compile(
    r'<button class="lang-toggle-btn" onclick="toggleLang\(this\)">\s*'
    r'<span id="lang-code">[^<]*</span>\s*'
    r'<i class="fas fa-chevron-down"[^>]*></i>\s*'
    r'</button>',
    re.DOTALL
)
desktop_new = (
    '<a href="https://app.e-evrika.com" class="btn" '
    'style="background: #1565C0; color: white; border-radius: 100px; padding: 12px 28px; '
    'font-weight: 800; font-size: 0.95rem; text-decoration: none; '
    'transition: all 0.4s cubic-bezier(0.175,0.885,0.32,1.275);" '
    'onmouseover="this.style.background=\'#0d47a1\'; this.style.transform=\'scale(1.05) translateY(-2px)\'" '
    'onmouseout="this.style.background=\'#1565C0\'; this.style.transform=\'scale(1) translateY(0)\'">'
    '\n          E-jurnal\n        </a>'
)

# Mobile: lang-toggle button with extra inline styles
mobile_old = re.compile(
    r'<button class="lang-toggle-btn" onclick="toggleLang\(this\)"[^>]*>\s*'
    r'<span id="lang-code">[^<]*</span>\s*'
    r'<i class="fas fa-chevron-down"[^>]*></i>\s*'
    r'</button>',
    re.DOTALL
)
mobile_new = (
    '<a href="https://app.e-evrika.com" class="btn" '
    'style="width: 100%; background: #1565C0; color: white; border-radius: 100px; padding: 12px 28px; '
    'font-weight: 800; font-size: 0.95rem; text-decoration: none;">'
    '\n          E-jurnal\n        </a>'
)

# Files to process (exclude dist/ and index.html which is already done)
html_dir = '/Users/gazanfaryusifli/Downloads/Evrika'
skip_files = {'index.html'}
skip_dirs = {'dist'}

changed = []
for fname in os.listdir(html_dir):
    if not fname.endswith('.html'):
        continue
    if fname in skip_files:
        continue
    fpath = os.path.join(html_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    # First try mobile (more specific pattern with extra styles)
    content = mobile_old.sub(mobile_new, content)
    # Then desktop
    content = desktop_old.sub(desktop_new, content)
    
    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        changed.append(fname)

print(f"Changed {len(changed)} files:")
for f in sorted(changed):
    print(f"  ✓ {f}")
