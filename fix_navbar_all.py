import re
import os

with open('lisey.html', 'r', encoding='utf-8') as f:
    master_html = f.read()

# Extract Navbar and Mobile Nav from lisey.html
navbar_match = re.search(r'(<header class=\"navbar modern-floating-nav\"\>.*?</header>)', master_html, re.DOTALL)
mobilenav_match = re.search(r'(<!-- Mobile Navigation Overlay \(Neo-Glass\) -->.*?</div>\s*</div>)', master_html, re.DOTALL)

if not navbar_match or not mobilenav_match:
    print("Could not find navbar in lisey.html")
    exit(1)

master_navbar = navbar_match.group(1)
master_mobilenav = mobilenav_match.group(1)

# List of files to update
targets = [
    ('zumrud.html', 'register-zumrud.html'),
    ('eduhome.html', 'register-eduhome.html'),
    ('montessori.html', 'register-montessori.html') # Just in case it was missed
]

for fname, register_link in targets:
    if not os.path.exists(fname):
        continue
    
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. First, find any broken structure like 'iv> \n </div>' and remove it
    content = re.sub(r'iv>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</header>', '</header>', content)
    
    # 2. Replace Header
    content = re.sub(r'<header class=\"navbar modern-floating-nav\"\>.*?</header>', master_navbar, content, flags=re.DOTALL)
    
    # 3. Replace Mobile Nav
    # If no mobile nav comment exists, find a place to put it (after header)
    if '<!-- Mobile Navigation Overlay' in content:
        content = re.sub(r'<!-- Mobile Navigation Overlay.*?</div>\s*</div>', master_mobilenav, content, flags=re.DOTALL)
    else:
        content = content.replace('</header>', '</header>\n\n  ' + master_mobilenav)
    
    # 4. Tailor the Register Links
    # In master_navbar, find the register button and replace the link
    # The register button in master is usually <a href="schools.html" ... data-i18n="nav-register">Qeydiyyat</a>
    # or similar. We should check what it is in master_navbar.
    
    # Simple replacement for common register links
    content = content.replace('register-lisey1.html', register_link)
    # If the master link is schools.html for some reason, replace it specifically inside the header
    # But lisey.html master should have it's own.
    
    # 5. Fix gaps in CSS if they exist in the file
    content = content.replace('gap: 24px;', 'gap: 8px;')
    
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {fname}")

