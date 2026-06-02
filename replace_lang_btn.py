import glob
import re

desktop_btn = r"""        <button class="lang-toggle-btn" onclick="let langs=['AZ','EN','RU']; let spans=document.querySelectorAll('.lang-text'); let current=spans[0].innerText.trim(); let next=langs[(langs.indexOf(current)+1)%langs.length]; spans.forEach(span => span.innerText=next);" style="background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); color: white; padding: 12px 20px; border-radius: 100px; font-weight: 700; font-size: 0.85rem; cursor: pointer; transition: 0.3s; margin-right: 8px; display: inline-flex; align-items: center; justify-content: center; min-width: 80px;" onmouseover="this.style.background='rgba(255,255,255,0.2)'" onmouseout="this.style.background='rgba(255,255,255,0.08)'">
           <i class="fas fa-globe" style="margin-right: 6px; opacity: 0.7;"></i> <span class="lang-text">AZ</span>
        </button>"""

mobile_btn = r"""    <div style="padding: 15px 20px; border-bottom: 1px solid rgba(255,255,255,0.1); margin-bottom: 15px; display: flex; justify-content: center;">
        <button class="lang-toggle-btn" onclick="let langs=['AZ','EN','RU']; let spans=document.querySelectorAll('.lang-text'); let current=spans[0].innerText.trim(); let next=langs[(langs.indexOf(current)+1)%langs.length]; spans.forEach(span => span.innerText=next);" style="background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); color: white; padding: 12px 24px; border-radius: 100px; font-weight: 700; font-size: 0.95rem; cursor: pointer; transition: 0.3s; display: inline-flex; align-items: center; justify-content: center; min-width: 100px;" onmouseover="this.style.background='rgba(255,255,255,0.2)'" onmouseout="this.style.background='rgba(255,255,255,0.08)'">
           <i class="fas fa-globe" style="margin-right: 8px; opacity: 0.7;"></i> <span class="lang-text">AZ</span>
        </button>
    </div>"""

desktop_regex = re.compile(r'<div class="lang-switcher"[^>]*>.*?</div>', re.DOTALL)
mobile_regex = re.compile(r'<div style="padding: 15px 20px; border-bottom: 1px solid rgba\(255,255,255,0\.1\); margin-bottom: 15px; display: flex; justify-content: center;">\s*<div class="lang-switcher"[^>]*>.*?</div>\s*</div>', re.DOTALL)

for filepath in glob.glob('*.html'):
    if filepath in ['admin.html', 'verify.html']:
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We replace the mobile one first to avoid overlapping logic if any
    content = mobile_regex.sub(mobile_btn, content)
    
    # Then replace the desktop one
    content = desktop_regex.sub(desktop_btn, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Language switchers replaced with single-click buttons in all HTML files.")
