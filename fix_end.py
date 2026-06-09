import os

wa_snippet = """    <script>
        document.addEventListener('DOMContentLoaded', () => {
            if (typeof updateContent === 'function') {
                updateContent(localStorage.getItem('evrika-lang') || 'az');
            }
        });
    </script>
    
    <!-- Precise WhatsApp Lead Tracker -->
    <div id="wa-precise-widget" style="position: fixed; bottom: 30px; right: 30px; z-index: 10000; font-family: 'Inter', sans-serif;">
        <div id="wa-bubble" style="display: none; background: white; padding: 20px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.15); margin-bottom: 20px; width: 280px; animation: waFadeUp 0.3s ease;">
            <div style="font-size: 0.9rem; color: #333; font-weight: 600; margin-bottom: 12px; line-height: 1.4;">
                WhatsApp vasitəsilə rəsmi müraciət etmək üçün aşağıdakı düyməni sıxın:
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
      function toggleWaBubble() {
        const b = document.getElementById('wa-bubble');
        b.style.display = b.style.display === 'none' ? 'block' : 'none';
      }

      async function commitAndOpenWa() {
        const btn = document.getElementById('wa-send-btn');
        btn.disabled = true;
        btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Göndərilir...';
        
        try {
          await fetch('https://miwvdhwrmxoetszkxlzy.supabase.co/rest/v1/registrations', {
            method: 'POST',
            headers: { 'apikey': 'sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV', 'Authorization': 'Bearer sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV', 'Content-Type': 'application/json' },
            body: JSON.stringify({ payload: { name: "Rəsmi WhatsApp", source: "whatsapp", status: "Yeni", note: "Salam, mən Evrika Təhsil Ekosistemi ilə maraqlanıram. Qəbul və qeydiyyat şərtləri barədə ətraflı məlumat almaq üçün müraciət edirəm.", date: new Date().toISOString() } })
          });
        } catch(e) {}
        
        window.open(`https://wa.me/994555945300?text=${encodeURIComponent('Salam, mən Evrika Təhsil Ekosistemi ilə maraqlanıram. Qəbul və qeydiyyat şərtləri barədə ətraflı məlumat almaq üçün müraciət edirəm.')}`, '_blank');
        toggleWaBubble();
        btn.disabled = false;
        btn.innerHTML = 'Müraciəti Göndər <i class="fab fa-whatsapp"></i>';
      }
    </script>
</body>"""

targets = ['register-montessori.html', 'register-victory.html', 'register-zumrud.html']

for target in targets:
    if not os.path.exists(target): continue
    with open(target, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'wa-precise-widget' not in content:
        content = content.replace('</body>', wa_snippet)
        with open(target, 'w', encoding='utf-8') as f:
            f.write(content)

print("Widgets attached")
