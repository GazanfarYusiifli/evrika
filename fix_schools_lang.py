import glob
import re

desktop_lang_btn = r"""        <div class="lang-dropdown-wrapper desktop-lang-wrapper" style="position: relative; display: inline-flex; margin-right: 12px; height: 100%;">
            <button class="lang-toggle-btn" onclick="let menu = this.nextElementSibling; menu.style.display = menu.style.display === 'flex' ? 'none' : 'flex';" onblur="let menu = this.nextElementSibling; setTimeout(() => menu.style.display = 'none', 200);" style="background: #1e3a8a; border: none; color: white; padding: 12px 22px; border-radius: 100px; font-weight: 800; font-size: 0.95rem; cursor: pointer; transition: 0.3s; display: inline-flex; align-items: center; justify-content: center; min-width: 80px;" onmouseover="this.style.background='#284baf'" onmouseout="this.style.background='#1e3a8a'">
               <span class="lang-text">AZ</span> <i class="fas fa-chevron-down" style="margin-left: 10px; font-size: 0.8rem; opacity: 0.9;"></i>
            </button>
            <div class="lang-menu" style="position: absolute; top: 115%; left: 50%; transform: translateX(-50%); background: white; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); display: none; flex-direction: column; overflow: hidden; min-width: 80px; z-index: 100;">
                <a href="#" onmousedown="event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='AZ'); this.parentElement.style.display='none';" style="padding: 10px 20px; color: #333; text-decoration: none; font-weight: 700; font-size: 0.9rem; text-align: center; border-bottom: 1px solid #eee;" onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background='white'">AZ</a>
                <a href="#" onmousedown="event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='EN'); this.parentElement.style.display='none';" style="padding: 10px 20px; color: #333; text-decoration: none; font-weight: 700; font-size: 0.9rem; text-align: center; border-bottom: 1px solid #eee;" onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background='white'">EN</a>
                <a href="#" onmousedown="event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='RU'); this.parentElement.style.display='none';" style="padding: 10px 20px; color: #333; text-decoration: none; font-weight: 700; font-size: 0.9rem; text-align: center;" onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background='white'">RU</a>
            </div>
        </div>"""

for filepath in ['schools.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<div class="lang-dropdown-wrapper' not in content.split('<div class="nav-actions">')[1].split('</div>')[0]:
        content = re.sub(r'<div class="nav-actions">\s*</div>', f'<div class="nav-actions">\n{desktop_lang_btn}\n      </div>', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Language dropdown added to schools.html")
