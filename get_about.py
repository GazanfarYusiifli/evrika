import re
with open('victory.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's extract the about section to see it
about_match = re.search(r'<div class="about-text-side reveal-right">.*?Hazırlıq Proqramlarımız:.*?</ul>\s*</div>', html, re.DOTALL)
if about_match:
    print("Found about section")
else:
    print("About section not found")
