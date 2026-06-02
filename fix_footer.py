import os
import re

def update_footer(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove address line
    address_pattern = r'<div style="display:\s*flex;\s*gap:\s*15px;\s*align-items:\s*center;"><i class="fas fa-map-marker-alt".*?Baku, Azerbaijan</span></div>'
    content = re.sub(address_pattern, '', content, flags=re.DOTALL)

    # 2. Update phone to short number
    phone_pattern = r'<div style="display:\s*flex;\s*gap:\s*15px;\s*align-items:\s*center;"><i class="fas fa-phone-alt".*?\+994-12 525 10 10</span></div>'
    new_phone = '<div style="display: flex; gap: 15px; align-items: center;"><i class="fas fa-phone-alt" style="color: var(--accent, #8B1A2B);"></i><span style="color: rgba(255,255,255,0.7); font-weight: 800; font-size: 1.2rem; letter-spacing: 0.1em;">*3005</span></div>'
    content = re.sub(phone_pattern, new_phone, content, flags=re.DOTALL)

    # 3. Standardize "Akademik Kampuslar" to "Akademik İstiqamətlər"
    content = content.replace('Akademik Kampuslar', 'Akademik İstiqamətlər')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for html_file in html_files:
    print(f"Updating {html_file}...")
    update_footer(html_file)

print("Done!")
