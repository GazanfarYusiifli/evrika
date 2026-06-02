import glob
import re

desktop_btn_pattern = re.compile(
    r'\s*<a href="https://app\.e-evrika\.com" class="btn" style="background: linear-gradient[^>]+>\s*E-jurnal\s*</a>',
    re.MULTILINE
)

mobile_btn_pattern = re.compile(
    r'\s*<div style="padding: 20px; border-bottom: 1px solid rgba\(255,255,255,0\.1\); margin-bottom: 20px;">\s*<a href="https://app\.e-evrika\.com" class="btn" style="width: 100%; background: linear-gradient[^>]+>\s*E-jurnal\s*</a>\s*</div>',
    re.MULTILINE
)

# Also a fallback if it has slightly different spacing
fallback_desktop_pattern = re.compile(
    r'\s*<a href="https://app\.e-evrika\.com"[^>]*>\s*E-jurnal\s*</a>',
    re.MULTILINE | re.IGNORECASE
)

for filepath in glob.glob('*.html'):
    if filepath in ['admin.html', 'verify.html']:
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove Mobile block
    content = mobile_btn_pattern.sub('', content)
    
    # 2. Remove Desktop block
    content = desktop_btn_pattern.sub('', content)

    # 3. If any E-jurnal link is still left with that URL, remove it
    if 'https://app.e-evrika.com' in content and 'E-jurnal' in content:
        content = fallback_desktop_pattern.sub('', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("E-jurnal links removed from all HTML files.")
