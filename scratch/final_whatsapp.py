
import os
import re

# Final WhatsApp Configuration
WA_TARGET = "994555945300"
API_URL = 'https://miwvdhwrmxoetszkxlzy.supabase.co/rest/v1'
API_KEY = 'sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV'

# NEW DESIGN: More premium, centered layout, tracks on SEND only
WIDGET_HTML = f"""
    <!-- Professional WhatsApp Chat Widget v2 -->
    <div id="wa-widget" style="position: fixed; bottom: 30px; right: 30px; z-index: 10000; font-family: 'Inter', sans-serif;">
        <div id="wa-chat" style="display: none; width: 350px; background: white; border-radius: 25px; box-shadow: 0 20px 50px rgba(0,0,0,0.15); overflow: hidden; margin-bottom: 20px; animation: waFadeUp 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
            <div style="background: #075e54; padding: 25px; color: white; position: relative;">
                <div style="display: flex; align-items: center; gap: 15px;">
                    <div style="position: relative;">
                        <div style="width: 45px; height: 45px; background: rgba(255,255,255,0.2); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;"><i class="fab fa-whatsapp"></i></div>
                        <div style="position: absolute; bottom: 2px; right: 2px; width: 12px; height: 12px; background: #45c655; border: 2px solid #075e54; border-radius: 50%;"></div>
                    </div>
                    <div>
                        <h4 style="margin: 0; font-size: 1rem; font-weight: 700;">Evrika Dəstək</h4>
                        <p style="margin: 0; font-size: 0.75rem; opacity: 0.8;">Onlayn | 24/7 Xidmət</p>
                    </div>
                </div>
                <button onclick="toggleWaChat()" style="position: absolute; top: 20px; right: 20px; background: none; border: none; color: white; font-size: 1.2rem; cursor: pointer; opacity: 0.5;">&times;</button>
            </div>
            <div style="padding: 25px; background: #e5ddd5; min-height: 100px;">
                <div style="background: white; padding: 15px; border-radius: 0 15px 15px 15px; max-width: 85%; font-size: 0.9rem; color: #333; box-shadow: 0 2px 5px rgba(0,0,0,0.05);">
                    Salam! 👋 Sizə necə kömək edə bilərik? Sualınızı bura qeyd edin.
                </div>
            </div>
            <div style="padding: 15px; background: white;">
                <textarea id="wa-msg-field" placeholder="Mesajınızı yazın..." style="width: 100%; border: 1px solid #eee; border-radius: 12px; padding: 12px; font-size: 0.9rem; resize: none; height: 80px; outline: none; font-family: inherit;"></textarea>
                <button onclick="commitWaLead()" style="width: 100%; background: #25d366; color: white; border: none; border-radius: 12px; padding: 12px; font-weight: 700; margin-top: 10px; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 10px;">
                    Göndər <i class="fab fa-whatsapp"></i>
                </button>
            </div>
        </div>
        <button id="wa-trigger" onclick="toggleWaChat()" style="width: 60px; height: 60px; background: #25d366; border: none; border-radius: 50%; color: white; font-size: 30px; cursor: pointer; box-shadow: 0 10px 25px rgba(37,211,102,0.3); display: flex; align-items: center; justify-content: center; transition: 0.3s; padding:0;">
            <i class="fab fa-whatsapp"></i>
        </button>
    </div>

    <script>
      function toggleWaChat() {{
        const chat = document.getElementById('wa-chat');
        chat.style.display = chat.style.display === 'none' ? 'block' : 'none';
      }}

      async function commitWaLead() {{
        const msg = document.getElementById('wa-msg-field').value;
        if(!msg.trim()) return alert("Zəhmət olmasa sualınızı və ya adınızı qeyd edin.");
        
        try {{
          await fetch('{API_URL}/registrations', {{
            method: 'POST',
            headers: {{ 'apikey': '{API_KEY}', 'Authorization': 'Bearer {API_KEY}', 'Content-Type': 'application/json' }},
            body: JSON.stringify({{ payload: {{ name: "WhatsApp Müraciəti", source: "whatsapp", note: msg, date: new Date().toISOString() }} }})
          }});
        }} catch(e) {{}}
        
        window.open(`https://wa.me/{WA_TARGET}?text=${{encodeURIComponent(msg)}}`, '_blank');
        toggleWaChat();
      }}
    </script>
    <style>@keyframes waFadeUp {{ from {{ opacity: 0; transform: translateY(30px); }} to {{ opacity: 1; transform: translateY(0); }} }}</style>
"""

def fix_all(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove any existing WhatsApp buttons and scripts
        content = re.sub(r'<!-- WhatsApp Button Tracker -->.*?</a>', '', content, flags=re.DOTALL)
        content = re.sub(r'<!-- Professional WhatsApp Chat Widget.*?/script>', '', content, flags=re.DOTALL)
        content = re.sub(r'<!-- WhatsApp Button -->\s*<a href="https://wa\.me/.*?</a>', '', content, flags=re.DOTALL)
        content = re.sub(r'<a href="https://wa\.me/.*?</a>', '', content, flags=re.DOTALL)
        
        # Inject the new widget before </body>
        if "</body>" in content:
            new_content = content.replace("</body>", WIDGET_HTML + "\n</body>")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Finalized: {filepath}")
    except Exception as e:
        print(f"Error on {filepath}: {e}")

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html') and file != 'admin.html':
            fix_all(os.path.join(root, file))
