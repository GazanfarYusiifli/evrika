import re
import os

targets = [
    ('zumrud.html', 'register-zumrud.html'),
    ('eduhome.html', 'register-eduhome.html'),
    ('montessori.html', 'register-montessori.html'),
    ('lisey.html', 'register-lisey1.html')
]

for fname, reg_link in targets:
    if not os.path.exists(fname):
        continue
    
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update the nav-btn in the header
    content = re.sub(
        r'(<a\s+href=\")[^\"]*(\"\s+class=\"btn\s+btn-primary\s+nav-btn\"[^>]*data-i18n=\"nav-register\">)',
        r'\1' + reg_link + r'\2',
        content
    )
    
    # 2. Update the mobile nav link
    # Typically looks like: <a href="schools.html" style="color: var(--accent);" data-i18n="nav-register">Qeydiyyat</a>
    # or similar in the mobile nav overlay
    content = re.sub(
        r'(<a\s+href=\")[^\"]*(\"\s+style=\"[^\"]*color:\s*var\(--accent\)[^\"]*\"\s+data-i18n=\"nav-register\">)',
        r'\1' + reg_link + r'\2',
        content
    )
    
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed register links for {fname}")

