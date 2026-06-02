
import os
import re

# Precise Tracking Settings
WA_PHONE = "994555945300"
WA_MSG = "Salam necə müraciət edə bilərəm?"
API_URL = 'https://miwvdhwrmxoetszkxlzy.supabase.co/rest/v1'
API_KEY = 'sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV'

precise_tracker_html = f"""
    <!-- Precise WhatsApp Lead Tracker (Counts on Send, not Click) -->
    <div id="wa-precise-widget" style="position: fixed; bottom: 30px; right: 30px; z-index: 10000; font-family: 'Inter', sans-serif;">
        <!-- Small Bubble (Initially Hidden) -->
        <div id="wa-bubble" style="display: none; background: white; padding: 20px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.15); margin-bottom: 20px; width: 280px; animation: waFadeUp 0.3s ease;">
            <div style="font-size: 0.9rem; color: #333; font-weight: 600; margin-bottom: 12px; line-height: 1.4;">
                WhatsApp ilə müraciət etmək üçün aşağıdakı düyməni sıxın:
            </div>
            <div style="background: #f0f2f5; padding: 10px; border-radius: 10px; font-size: 0.8rem; color: #666; margin-bottom: 15px;">
                "{WA_MSG}"
            </div>
            <button onclick="commitAndOpenWa()" id="wa-send-btn" style="width: 100%; background: #25d366; color: white; border: none; border-radius: 12px; padding: 12px; font-weight: 800; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 10px; transition: 0.3s;">
                Müraciəti Göndər <i class="fab fa-whatsapp"></i>
            </button>
        </div>
        
        <!-- Main Floating Button -->
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
        
        const API_URL = '{API_URL}';
        const API_KEY = '{API_KEY}';
        const HEADERS = {{ 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY, 'Content-Type': 'application/json', 'Prefer': 'return=minimal' }};
        
        // Track ONLY when the user clicks "Müraciəti Göndər"
        try {{
          await fetch(`${{API_URL}}/registrations`, {{
            method: 'POST',
            headers: HEADERS,
            body: JSON.stringify({{ payload: {{ name: "WhatsApp Müraciəti", source: "whatsapp", status: "Yeni", note: "{WA_MSG}", date: new Date().toISOString() }} }})
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

def apply_precise_tracker(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Strip all previous incarnations
        content = re.sub(r'<!-- Global WhatsApp Direct Tracker.*?</a>', '', content, flags=re.DOTALL)
        content = re.sub(r'<!-- Professional WhatsApp Chat Widget.*?/script>', '', content, flags=re.DOTALL)
        content = re.sub(r'<!-- Precise WhatsApp Lead Tracker.*?/style>', '', content, flags=re.DOTALL)
        content = re.sub(r'<!-- WhatsApp Button Tracker -->.*?</a>', '', content, flags=re.DOTALL)
        content = re.sub(r'<a href="javascript:void\(0\)" onclick="triggerWa\(\)".*?</a>', '', content, flags=re.DOTALL)
        content = re.sub(r'<div id="wa-precise-widget".*?</div>\s*<script>.*?</script>\s*<style>.*?</style>', '', content, flags=re.DOTALL)

        # Inject the refined tracker
        if "</body>" in content:
            new_content = content.replace("</body>", precise_tracker_html + "\n</body>")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Applied Precise Tracking: {filepath}")
    except Exception as e:
        print(f"Error on {filepath}: {e}")

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html') and file != 'admin.html':
            apply_precise_tracker(os.path.join(root, file))
