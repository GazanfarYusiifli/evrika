import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Pattern to remove the jurnal block from mobile accordion body
jurnal_mobile_pattern = re.compile(
    r'<a href="jurnal\.html">\s*<div class="acc-icon"><i class="fas fa-book-open"></i></div>\s*<div class="acc-text"><span class="acc-title">Evrika Məktəbli Jurnalı</span><span class="acc-desc">Aylıq Nəşr</span></div>\s*</a>',
    re.DOTALL
)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Remove the jurnal block from the mobile accordion
    content = jurnal_mobile_pattern.sub('', content)

    # 2. Insert simple <a href="jurnal.html">Evrika Məktəbli Jurnalı</a> right before <a href="contact.html"
    # Note: We need to make sure we only do this in the mobile menu.
    # The contact.html link in mobile menu usually looks like: <a href="contact.html" data-i18n="nav-contact">Əlaqə</a>
    # Let's target that exact string.
    
    # We only want to replace the one in the mobile nav.
    # The mobile nav has:
    # <div class="mobile-nav-links">
    # ...
    # <a href="contact.html" data-i18n="nav-contact">Əlaqə</a>
    
    # To be safe, let's use a regex that looks for the contact link within mobile-nav-links
    
    mobile_contact_pattern = re.compile(r'(<a href="contact\.html" data-i18n="nav-contact">Əlaqə</a>)')
    
    # Check if the simple link already exists
    if '<a href="jurnal.html">Evrika Məktəbli Jurnalı</a>' not in content:
        # We will replace the first occurrence of the contact link that comes AFTER the vacancy accordion, or just the contact link inside mobile-nav-links.
        # Actually, in most files, the mobile contact link has data-i18n="nav-contact". The desktop one usually just has href="contact.html".
        
        # Let's just do a simple replace on the string: '<a href="contact.html" data-i18n="nav-contact">Əlaqə</a>'
        # Wait, what if the desktop link also has data-i18n="nav-contact"? In index.html it doesn't: <a href="contact.html">Əlaqə</a>
        
        content = content.replace(
            '<a href="contact.html" data-i18n="nav-contact">Əlaqə</a>',
            '<a href="jurnal.html">Evrika Məktəbli Jurnalı</a>\n      <a href="contact.html" data-i18n="nav-contact">Əlaqə</a>'
        )

    if content != original_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")

