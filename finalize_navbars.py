import re
import os

with open('lisey.html', 'r', encoding='utf-8') as f:
    master_html = f.read()

# Extract Navbar and Mobile Nav from lisey.html
navbar_match = re.search(r'(<header class=\"navbar modern-floating-nav\"\>.*?</header>)', master_html, re.DOTALL)
mobilenav_match = re.search(r'(<!-- Mobile Navigation Overlay \(Neo-Glass\) -->.*?</div>\s*</div>)', master_html, re.DOTALL)

master_navbar = navbar_match.group(1)
master_mobilenav = mobilenav_match.group(1)

targets = [
    ('zumrud.html', 'register-zumrud.html'),
    ('victory.html', 'register-victory.html')
]

for fname, reg_link in targets:
    if not os.path.exists(fname):
        continue
    
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Kill any existing header or mobile nav or messy bits
    content = re.sub(r'<header class=\"navbar.*?(\s*<div[^>]*nav-glass-container.*?</header>)?', '', content, flags=re.DOTALL)
    content = re.sub(r'<!-- Mobile Navigation Overlay.*?</div>\s*</div>', '', content, flags=re.DOTALL)
    # Also kill the rogue text I saw
    content = content.replace('    <!-- Ultra-Moder  <header class="navbar modern-floating-nav">', '')
    content = content.replace('iv>\n    </div>\n    </div>\n    </div>\n    </div>\n  </header>', '')
    
    # 2. Put Navbar right after body
    # Find <body> or <body ...>
    body_pattern = re.compile(r'(<body[^>]*>)', re.IGNORECASE)
    content = body_pattern.sub(r'\1\n\n  ' + master_navbar + '\n\n  ' + master_mobilenav, content)
    
    # 3. Specific replacements
    content = content.replace('register-lisey1.html', reg_link)
    content = content.replace('schools.html" class="btn btn-primary nav-btn"', reg_link + '" class="btn btn-primary nav-btn"')
    
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Finalized {fname}")

