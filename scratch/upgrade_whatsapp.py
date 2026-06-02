
import os
import re

# New WhatsApp target
WA_PHONE = "994555945300"
API_URL = 'https://miwvdhwrmxoetszkxlzy.supabase.co/rest/v1'
API_KEY = 'sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV'

chat_widget_html = f"""
    <!-- Professional WhatsApp Chat Widget -->
    <div id="wa-chat-widget" style="position: fixed; bottom: 100px; right: 30px; width: 350px; background: white; border-radius: 20px; box-shadow: 0 20px 50px rgba(0,0,0,0.2); z-index: 10000; overflow: hidden; display: none; flex-direction: column; animation: waFadeUp 0.4s ease;">
        <div style="background: #075e54; padding: 20px; color: white; display: flex; align-items: center; gap: 15px;">
            <div style="width: 45px; height: 45px; background: rgba(255,255,255,0.2); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;"><i class="fab fa-whatsapp"></i></div>
            <div>
                <div style="font-weight: 800; font-size: 1rem;">Evrika Dəstək</div>
                <div style="font-size: 0.75rem; opacity: 0.8;">Onlayn | 24/7 Xidmət</div>
            </div>
            <button onclick="toggleWaChat()" style="margin-left: auto; background: none; border: none; color: white; cursor: pointer; font-size: 1.2rem;">&times;</button>
        </div>
        <div style="padding: 20px; background: #e5ddd5; flex: 1; min-height: 100px;">
            <div style="background: white; padding: 12px; border-radius: 10px; font-size: 0.9rem; max-width: 85%; box-shadow: 0 2px 5px rgba(0,0,0,0.05); position: relative;">
                Salam! Sizə necə kömək edə bilərik? Zəhmət olmasa adınızı qeyd edin.
            </div>
        </div>
        <div style="padding: 20px; background: white; border-top: 1px solid #eee;">
            <input type="text" id="wa-user-name" placeholder="Adınız və Soyadınız..." style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 10px; margin-bottom: 10px; outline: none;">
            <button onclick="sendWaLead()" style="width: 100%; padding: 12px; background: #25d366; color: white; border: none; border-radius: 10px; font-weight: 800; cursor: pointer; transition: 0.3s; display: flex; align-items: center; justify-content: center; gap: 10px;">
                WhatsApp-da Yaz <i class="fas fa-paper-plane"></i>
            </button>
        </div>
    </div>

    <!-- Floating Trigger -->
    <a href="javascript:void(0)" onclick="toggleWaChat()" id="wa-trigger" style="position: fixed; bottom: 30px; right: 30px; width: 60px; height: 60px; background: #25d366; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 30px; box-shadow: 0 10px 25px rgba(37,211,102,0.3); z-index: 9999; text-decoration: none; transition: 0.3s;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
        <i class="fab fa-whatsapp"></i>
    </a>

    <script>
      function toggleWaChat() {{
        const w = document.getElementById('wa-chat-widget');
        w.style.display = w.style.display === 'flex' ? 'none' : 'flex';
      }}

      async function sendWaLead() {{
        const name = document.getElementById('wa-user-name').value || "WhatsApp Müraciətçisi";
        const API_URL = '{API_URL}';
        const API_KEY = '{API_KEY}';
        const HEADERS = {{ 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY, 'Content-Type': 'application/json', 'Prefer': 'return=minimal' }};
        
        // Count only when they submit the form
        try {{
          await fetch(`${{API_URL}}/registrations`, {{
            method: 'POST',
            headers: HEADERS,
            body: JSON.stringify({{ payload: {{ name: name + " (WhatsApp)", source: "WhatsApp", status: "Yeni", date: new Date().toISOString() }} }})
          }});
        }} catch (e) {{}}

        // Redirect to new WhatsApp number
        window.open(`https://wa.me/{WA_PHONE}?text=Salam, mən ${{name}}. Müraciət üçün yazıram.`, '_blank');
        toggleWaChat();
      }}
    </script>
    <style>@keyframes waFadeUp {{ from {{ opacity:0; transform:translateY(20px); }} to {{ opacity:1; transform:translateY(0); }} }}</style>
"""

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Target the tracker script I added in previous step
    # Or common patterns
    pattern = r'<!-- WhatsApp Button Tracker -->.*?</a>'
    if "<!-- WhatsApp Button Tracker -->" not in content:
        # Fallback to general button patterns
        pattern = r'<!-- WhatsApp Button -->\s*<a href="https://wa\.me/.*?</a>(\s*<!-- WhatsApp Button -->\s*<a href="https://wa\.me/.*?</a>)*'
        if "<!-- WhatsApp Button -->" not in content:
            pattern = r'<a href="https://wa\.me/.*?</a>'

    new_content = re.sub(pattern, chat_widget_html, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Upgraded: {filepath}")

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html') and file != 'admin.html': # Don't touch admin
            fix_file(os.path.join(root, file))
