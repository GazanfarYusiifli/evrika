import glob
import re

desktop_lang_btn = r"""        <div class="lang-dropdown-wrapper" style="position: relative; display: inline-flex; margin-right: 12px; height: 100%;">
            <button class="lang-toggle-btn" onclick="let menu = this.nextElementSibling; menu.style.display = menu.style.display === 'flex' ? 'none' : 'flex';" onblur="let menu = this.nextElementSibling; setTimeout(() => menu.style.display = 'none', 200);" style="background: #1e3a8a; border: none; color: white; padding: 12px 22px; border-radius: 100px; font-weight: 800; font-size: 0.95rem; cursor: pointer; transition: 0.3s; display: inline-flex; align-items: center; justify-content: center; min-width: 80px;" onmouseover="this.style.background='#284baf'" onmouseout="this.style.background='#1e3a8a'">
               <span class="lang-text">AZ</span> <i class="fas fa-chevron-down" style="margin-left: 10px; font-size: 0.8rem; opacity: 0.9;"></i>
            </button>
            <div class="lang-menu" style="position: absolute; top: 115%; left: 50%; transform: translateX(-50%); background: white; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); display: none; flex-direction: column; overflow: hidden; min-width: 80px; z-index: 100;">
                <a href="#" onmousedown="event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='AZ'); this.parentElement.style.display='none';" style="padding: 10px 20px; color: #333; text-decoration: none; font-weight: 700; font-size: 0.9rem; text-align: center; border-bottom: 1px solid #eee;" onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background='white'">AZ</a>
                <a href="#" onmousedown="event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='EN'); this.parentElement.style.display='none';" style="padding: 10px 20px; color: #333; text-decoration: none; font-weight: 700; font-size: 0.9rem; text-align: center; border-bottom: 1px solid #eee;" onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background='white'">EN</a>
                <a href="#" onmousedown="event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='RU'); this.parentElement.style.display='none';" style="padding: 10px 20px; color: #333; text-decoration: none; font-weight: 700; font-size: 0.9rem; text-align: center;" onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background='white'">RU</a>
            </div>
        </div>
        \1"""

# The user explicitly said:
# "mobile versiada ise hamburg menu da goster ancaq, hamburg menu acilmamis gosterme"
# "ve mobile versiada hamburg menu de yuxarida kuncde dursun"
# I will put it as `position: absolute; top: 25px; left: 25px;` inside the `.mobile-nav-overlay`
mobile_lang_btn = r"""    <div class="close-mobile" id="mobile-close"><i class="fas fa-times"></i></div>
    <div class="mobile-lang-wrapper" style="position: absolute; top: 25px; left: 25px; z-index: 10001;">
        <div class="lang-dropdown-wrapper" style="position: relative; display: inline-block;">
            <button class="lang-toggle-btn" onclick="let menu = this.nextElementSibling; menu.style.display = menu.style.display === 'flex' ? 'none' : 'flex';" onblur="let menu = this.nextElementSibling; setTimeout(() => menu.style.display = 'none', 200);" style="background: #1e3a8a; border: none; color: white; padding: 12px 20px; border-radius: 100px; font-weight: 800; font-size: 0.95rem; cursor: pointer; transition: 0.3s; display: inline-flex; align-items: center; justify-content: center; min-width: 70px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);" onmouseover="this.style.background='#284baf'" onmouseout="this.style.background='#1e3a8a'">
               <span class="lang-text">AZ</span> <i class="fas fa-chevron-down" style="margin-left: 8px; font-size: 0.75rem; opacity: 0.9;"></i>
            </button>
            <div class="lang-menu" style="position: absolute; top: 115%; left: 0; background: white; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.2); display: none; flex-direction: column; overflow: hidden; min-width: 90px; z-index: 100;">
                <a href="#" onmousedown="event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='AZ'); this.parentElement.style.display='none';" style="padding: 12px 20px; color: #333; text-decoration: none; font-weight: 700; font-size: 0.9rem; text-align: center; border-bottom: 1px solid #eee;" onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background='white'">AZ</a>
                <a href="#" onmousedown="event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='EN'); this.parentElement.style.display='none';" style="padding: 12px 20px; color: #333; text-decoration: none; font-weight: 700; font-size: 0.9rem; text-align: center; border-bottom: 1px solid #eee;" onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background='white'">EN</a>
                <a href="#" onmousedown="event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='RU'); this.parentElement.style.display='none';" style="padding: 12px 20px; color: #333; text-decoration: none; font-weight: 700; font-size: 0.9rem; text-align: center;" onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background='white'">RU</a>
            </div>
        </div>
    </div>
    <div class="mobile-nav-links">"""

for filepath in glob.glob('*.html'):
    if filepath in ['admin.html', 'verify.html']:
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove Desktop E-jurnal
    content = re.sub(r'<a href="https://app\.e-evrika\.com" class="btn"[^>]*>\s*E-jurnal\s*</a>', '', content)
    # Remove any extra <a href="https://evrika.mektebim.edu.az/" ... >
    content = re.sub(r'<a href="https://evrika\.mektebim\.edu\.az/"[^>]*>\s*E-jurnal\s*</a>', '', content)

    # 2. Inject Desktop Lang Button
    # Put it right before Qeydiyyat
    content = re.sub(r'(<a href="[^"]+" class="btn btn-primary nav-btn"[^>]*>Qeydiyyat</a>)', desktop_lang_btn, content)

    # 3. Remove Mobile E-jurnal block
    content = re.sub(r'<div style="padding: 20px; border-bottom: 1px solid rgba\(255,255,255,0\.1\); margin-bottom: 20px;">.*?</div>', '', content, flags=re.DOTALL)

    # 4. Inject Mobile Lang Button
    # Replace from close-mobile to mobile-nav-links
    content = re.sub(r'<div class="close-mobile" id="mobile-close">.*?<div class="mobile-nav-links">', mobile_lang_btn, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Language togglers fully integrated.")
