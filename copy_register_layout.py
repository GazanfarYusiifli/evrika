import re
import os

with open('register-lisey2.html', 'r', encoding='utf-8') as f:
    master = f.read()

header_match = re.search(r'(<header class="navbar modern-floating-nav">.*?</header>)', master, re.DOTALL)
header = header_match.group(1) if header_match else ""

mobile_nav_match = re.search(r'(<!-- Mobile Navigation Overlay \(Neo-Glass\) -->.*?</div>\s*</div>)', master, re.DOTALL)
mobile_nav = mobile_nav_match.group(1) if mobile_nav_match else ""

footer_match = re.search(r'(<footer class="site-footer".*?</footer>)', master, re.DOTALL)
footer = footer_match.group(1) if footer_match else ""

wa_match = re.search(r'(<!-- Precise WhatsApp Lead Tracker.*?</body>)', master, re.DOTALL)
wa = wa_match.group(1) if wa_match else "    </body>"

# Fix active states in register headers based on page name if needed? 
# Actually, wait, no active color is forced.

targets = ['register-lisey1.html', 'register-montessori.html', 'register-victory.html', 'register-zumrud.html']

for target in targets:
    if not os.path.exists(target): continue
    with open(target, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace Header
    content = re.sub(r'<header class="navbar.*?</header>', header, content, flags=re.DOTALL)

    # Replace Mobile Nav (if exists) or insert after header
    if 'id="mobile-nav"' in content:
        content = re.sub(r'<!-- Mobile Navigation Overlay \(Neo-Glass\) -->.*?</div>(?=\s*<main)', mobile_nav, content, flags=re.DOTALL)
    elif 'class="mobile-nav-overlay"' in content:
        content = re.sub(r'<div class="mobile-nav-overlay".*?</div>(?=\s*<main)', mobile_nav, content, flags=re.DOTALL)

    # Replace Footer
    content = re.sub(r'<footer class="site-footer".*?</footer>', footer, content, flags=re.DOTALL)

    # Add WA widget if missing, or replace it
    if 'wa-precise-widget' in content:
        content = re.sub(r'<!-- Precise WhatsApp Lead Tracker.*?</body>', wa, content, flags=re.DOTALL)
    elif 'wa-floating-btn' in content:
        content = re.sub(r'<!-- WhatsApp.*?</body>', wa, content, flags=re.DOTALL)

    with open(target, 'w', encoding='utf-8') as f:
        f.write(content)

print("Registration pages standardized!")
