
import os
import re

# Supabase details
API_URL = 'https://miwvdhwrmxoetszkxlzy.supabase.co/rest/v1'
API_KEY = 'sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV'

tracking_script = f"""
    <!-- WhatsApp Button Tracker -->
    <script>
      async function trackWhatsAppClick() {{
        const API_URL = '{API_URL}';
        const API_KEY = '{API_KEY}';
        const HEADERS = {{ 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY, 'Content-Type': 'application/json', 'Prefer': 'return=minimal' }};
        try {{
          fetch(`${{API_URL}}/registrations`, {{
            method: 'POST',
            headers: HEADERS,
            body: JSON.stringify({{ payload: {{ name: "WhatsApp Müraciəti", source: "WhatsApp", status: "Yeni", date: new Date().toISOString() }} }})
          }});
        }} catch (e) {{}}
      }}
    </script>
    <a href="https://wa.me/994707770404" target="_blank" onclick="trackWhatsAppClick()" style="position: fixed; bottom: 30px; right: 30px; width: 60px; height: 60px; background: #25d366; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 30px; box-shadow: 0 10px 25px rgba(37,211,102,0.3); z-index: 9999; text-decoration: none; transition: 0.3s;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
        <i class="fab fa-whatsapp"></i>
    </a>
"""

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to find the WhatsApp button block (even if duplicated)
    # We look for the first WhatsApp link and replace the surrounding comments/links
    pattern = r'<!-- WhatsApp Button -->\s*<a href="https://wa\.me/994707770404".*?</a>(\s*<!-- WhatsApp Button -->\s*<a href="https://wa\.me/994707770404".*?</a>)*'
    
    # If no comments, just look for the link
    if "<!-- WhatsApp Button -->" not in content:
        pattern = r'<a href="https://wa\.me/994707770404".*?</a>'

    new_content = re.sub(pattern, tracking_script, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed: {filepath}")

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            fix_file(os.path.join(root, file))
