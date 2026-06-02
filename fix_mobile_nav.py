import re
import os

with open('register-lisey2.html', 'r', encoding='utf-8') as f:
    master = f.read()

mobile_nav_match = re.search(r'(<!-- Mobile Navigation Overlay \(Neo-Glass\) -->.*?</div>\s*</div>)', master, re.DOTALL)
mobile_nav = mobile_nav_match.group(1) if mobile_nav_match else ""

targets = ['register-montessori.html', 'register-eduhome.html', 'register-zumrud.html']

for target in targets:
    if not os.path.exists(target): continue
    with open(target, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'id="mobile-nav"' not in content:
        # Insert after </header>
        content = content.replace('</header>', '</header>\n\n  ' + mobile_nav)

    with open(target, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed mobile nav")
