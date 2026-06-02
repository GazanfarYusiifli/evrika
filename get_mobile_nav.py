import re

def extract_mobile_nav(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract the nav-glass-container block inside @media (max-width: 1024px)
    match = re.search(r'@media\s*\(max-width:\s*1024px\)\s*\{(.+?)\s*\.mobile-nav-overlay', content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return "Not found"

with open("lisey2_nav.txt", "w") as f:
    f.write(extract_mobile_nav("lisey2.html"))

with open("montessori_nav.txt", "w") as f:
    f.write(extract_mobile_nav("montessori.html"))

