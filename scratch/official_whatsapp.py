
import os
import re

# Professional Configuration
WA_PHONE = "994555945300"
WA_MSG = "Salam, mən Evrika Təhsil Ekosistemi ilə maraqlanıram. Qəbul və qeydiyyat şərtləri barədə ətraflı məlumat almaq üçün müraciət edirəm."
API_URL = 'https://miwvdhwrmxoetszkxlzy.supabase.co/rest/v1'
API_KEY = 'sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV'

precise_tracker_html = f"""
    <!-- Precise WhatsApp Lead Tracker (Counts on Send, not Click) -->
    <div id="wa-precise-widget" style="position: fixed; bottom: 30px; right: 30px; z-index: 10000; font-family: 'Inter', sans-serif;">
        <div id="wa-bubble" style="display: none; background: white; padding: 20px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.15); margin-bottom: 20px; width: 280px; animation: waFadeUp 0.3s ease;">
            <div style="font-size: 0.9rem; color: #333; font-weight: 600; margin-bottom: 12px; line-height: 1.4;">
                WhatsApp vasitəsilə rəsmi müraciət etmək üçün aşağıdakı düyməni sıxın:
            </div>
            <div style="background: #f0f2f5; padding: 12px; border-radius: 10px; font-size: 0.75rem; color: #555; margin-bottom: 15px; font-style: italic;">
                "{WA_MSG}"
            </div>
            <button onclick="commitAndOpenWa()" id="wa-send-btn" style="width: 100%; background: #25d366; color: white; border: none; border-radius: 12px; padding: 12px; font-weight: 800; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 10px; transition: 0.3s;">
                Müraciəti Göndər <i class="fab fa-whatsapp"></i>
            </button>
        </div>
        <button onclick="toggleWaBubble()" id="wa-floating-btn" style="width: 60px; height: 60px; background: #25d366; border: none; border-radius: 50%; color: white; font-size: 30px; cursor: pointer; box-shadow: 0 10px 25px rgba(37,211,102,0.3); display: flex; align-items: center; justify-content: center; transition: 0.3s; padding:0;">
            <i class="fab fa-whatsapp" id="wa-main-icon"></i>
        </button>
    </div>

    <script>
      function toggleWaBubble() {{
        const b = document.getElementById('wa-bubble');
        b.style.display = b.style.display === 'none' ? 'block' : 'none';
      }}

      async function commitAndOpenWa() {{
        const btn = document.getElementById('wa-send-btn');
        btn.disabled = true;
        btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Göndərilir...';
        
        try {{
          await fetch('{API_URL}/registrations', {{
            method: 'POST',
            headers: {{ 'apikey': '{API_KEY}', 'Authorization': 'Bearer {API_KEY}', 'Content-Type': 'application/json' }},
            body: JSON.stringify({{ payload: {{ name: "Rəsmi WhatsApp", source: "whatsapp", status: "Yeni", note: "{WA_MSG}", date: new Date().toISOString() }} }})
          }});
        }} catch(e) {{}}
        
        window.open(`https://wa.me/{WA_PHONE}?text=${{encodeURIComponent('{WA_MSG}')}}`, '_blank');
        toggleWaBubble();
        btn.disabled = false;
        btn.innerHTML = 'Müraciəti Göndər <i class="fab fa-whatsapp"></i>';
      }}
    </script>
    <style>@keyframes waFadeUp {{ from {{ opacity: 0; transform: translateY(20px); }} to {{ opacity: 1; transform: translateY(0); }} }}</style>
"""

def update_wa_msg(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the entire widget block with the new official version
        pattern = r'<!-- Precise WhatsApp Lead Tracker.*?/style>'
        new_content = re.sub(pattern, precise_tracker_html, content, flags=re.DOTALL)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Professionalized: {filepath}")
    except Exception as e:
        print(f"Error on {filepath}: {e}")

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html') and file != 'admin.html':
            update_wa_msg(os.path.join(root, file))
