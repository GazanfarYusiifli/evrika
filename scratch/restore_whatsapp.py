
import os
import re

# Target Settings
WA_PHONE = "994555945300"
WA_MSG = "Salam necə müraciət edə bilərəm?"
API_URL = 'https://miwvdhwrmxoetszkxlzy.supabase.co/rest/v1'
API_KEY = 'sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV'

final_button_html = f"""
    <!-- Global WhatsApp Direct Tracker -->
    <script>
      async function triggerWa() {{
        const API_URL = '{API_URL}';
        const API_KEY = '{API_KEY}';
        const HEADERS = {{ 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY, 'Content-Type': 'application/json', 'Prefer': 'return=minimal' }};
        
        // Track the click as a lead
        try {{
          fetch(`${{API_URL}}/registrations`, {{
            method: 'POST',
            headers: HEADERS,
            body: JSON.stringify({{ payload: {{ name: "WhatsApp Müraciəti", source: "whatsapp", status: "Yeni", date: new Date().toISOString() }} }})
          }});
        }} catch(e) {{}}
        
        // Open WhatsApp directly
        window.open(`https://wa.me/{WA_PHONE}?text=${{encodeURIComponent('{WA_MSG}')}}`, '_blank');
      }}
    </script>
    <a href="javascript:void(0)" onclick="triggerWa()" style="position: fixed; bottom: 30px; right: 30px; width: 60px; height: 60px; background: #25d366; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 30px; box-shadow: 0 10px 25px rgba(37,211,102,0.3); z-index: 9999; text-decoration: none; transition: 0.3s;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
        <i class="fab fa-whatsapp"></i>
    </a>
"""

def restore_simple_button(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove the widget code blocks
        content = re.sub(r'<!-- Professional WhatsApp Chat Widget.*?/style>', '', content, flags=re.DOTALL)
        content = re.sub(r'<!-- Professional WhatsApp Chat Widget.*?/script>', '', content, flags=re.DOTALL)
        content = re.sub(r'<!-- Global WhatsApp Direct Tracker.*?</a>', '', content, flags=re.DOTALL)
        content = re.sub(r'<div id="wa-widget".*?</div>\s*<script>.*?</script>\s*<style>.*?</style>', '', content, flags=re.DOTALL)
        content = re.sub(r'<!-- WhatsApp Button Tracker -->.*?</a>', '', content, flags=re.DOTALL)

        # Inject the refined direct button before </body>
        if "</body>" in content:
            new_content = content.replace("</body>", final_button_html + "\n</body>")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Restored: {filepath}")
    except Exception as e:
        print(f"Error on {filepath}: {e}")

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html') and file != 'admin.html':
            restore_simple_button(os.path.join(root, file))
