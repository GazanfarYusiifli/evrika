import glob
import re

desktop_nav_actions = r"""      <div class="nav-actions">
        <div class="lang-dropdown-wrapper" style="position: relative; display: inline-block; margin-right: 8px;">
            <button class="lang-toggle-btn" onclick="let menu = this.nextElementSibling; menu.style.display = menu.style.display === 'flex' ? 'none' : 'flex';" onblur="let menu = this.nextElementSibling; setTimeout(() => menu.style.display = 'none', 200);" style="background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); color: white; padding: 12px 20px; border-radius: 100px; font-weight: 700; font-size: 0.85rem; cursor: pointer; transition: 0.3s; display: inline-flex; align-items: center; justify-content: center; min-width: 70px;" onmouseover="this.style.background='rgba(255,255,255,0.2)'" onmouseout="this.style.background='rgba(255,255,255,0.08)'">
               <span class="lang-text">AZ</span> <i class="fas fa-chevron-down" style="margin-left: 8px; font-size: 0.7rem; opacity: 0.8;"></i>
            </button>
            <div class="lang-menu" style="position: absolute; top: 115%; left: 50%; transform: translateX(-50%); background: white; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); display: none; flex-direction: column; overflow: hidden; min-width: 80px; z-index: 100;">
                <a href="#" onmousedown="event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='AZ'); this.parentElement.style.display='none';" style="padding: 10px 20px; color: #333; text-decoration: none; font-weight: 600; font-size: 0.85rem; text-align: center; border-bottom: 1px solid #eee;" onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background='white'">AZ</a>
                <a href="#" onmousedown="event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='EN'); this.parentElement.style.display='none';" style="padding: 10px 20px; color: #333; text-decoration: none; font-weight: 600; font-size: 0.85rem; text-align: center; border-bottom: 1px solid #eee;" onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background='white'">EN</a>
                <a href="#" onmousedown="event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='RU'); this.parentElement.style.display='none';" style="padding: 10px 20px; color: #333; text-decoration: none; font-weight: 600; font-size: 0.85rem; text-align: center;" onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background='white'">RU</a>
            </div>
        </div>
        <a href="schools.html" class="btn btn-primary nav-btn">Qeydiyyat</a>
      </div>"""

for filepath in glob.glob('*.html'):
    if filepath in ['admin.html', 'verify.html']:
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # If the file has a specific register link (e.g. register-montessori.html), we should preserve it.
    # So we'll extract the Qeydiyyat link.
    q_match = re.search(r'<a href="([^"]+)" class="btn btn-primary nav-btn"[^>]*>Qeydiyyat</a>', content)
    q_link = q_match.group(1) if q_match else "schools.html"

    desktop_nav_actions_dynamic = desktop_nav_actions.replace('href="schools.html"', f'href="{q_link}"')

    content = re.sub(r'<div class="nav-actions">.*?<div class="mobile-menu-btn"', desktop_nav_actions_dynamic + '\n      <div class="mobile-menu-btn"', content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Desktop nav perfectly reverted.")
