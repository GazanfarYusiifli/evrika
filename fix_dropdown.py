import glob
import re

desktop_btn = r"""        <div class="lang-dropdown-wrapper" style="position: relative; display: inline-block; margin-right: 8px;">
            <button class="lang-toggle-btn" onclick="let menu = this.nextElementSibling; menu.style.display = menu.style.display === 'flex' ? 'none' : 'flex';" onblur="let menu = this.nextElementSibling; setTimeout(() => menu.style.display = 'none', 200);" style="background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); color: white; padding: 12px 20px; border-radius: 100px; font-weight: 700; font-size: 0.85rem; cursor: pointer; transition: 0.3s; display: inline-flex; align-items: center; justify-content: center; min-width: 70px;" onmouseover="this.style.background='rgba(255,255,255,0.2)'" onmouseout="this.style.background='rgba(255,255,255,0.08)'">
               <span class="lang-text">AZ</span> <i class="fas fa-chevron-down" style="margin-left: 8px; font-size: 0.7rem; opacity: 0.8;"></i>
            </button>
            <div class="lang-menu" style="position: absolute; top: 115%; left: 50%; transform: translateX(-50%); background: white; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); display: none; flex-direction: column; overflow: hidden; min-width: 80px; z-index: 100;">
                <a href="#" onmousedown="event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='AZ'); this.parentElement.style.display='none';" style="padding: 10px 20px; color: #333; text-decoration: none; font-weight: 600; font-size: 0.85rem; text-align: center; border-bottom: 1px solid #eee;" onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background='white'">AZ</a>
                <a href="#" onmousedown="event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='EN'); this.parentElement.style.display='none';" style="padding: 10px 20px; color: #333; text-decoration: none; font-weight: 600; font-size: 0.85rem; text-align: center; border-bottom: 1px solid #eee;" onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background='white'">EN</a>
                <a href="#" onmousedown="event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='RU'); this.parentElement.style.display='none';" style="padding: 10px 20px; color: #333; text-decoration: none; font-weight: 600; font-size: 0.85rem; text-align: center;" onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background='white'">RU</a>
            </div>
        </div>
        \1"""

mobile_btn = r"""    <div class="mobile-lang-wrapper" style="padding: 15px 20px; border-bottom: 1px solid rgba(255,255,255,0.1); margin-bottom: 15px; display: flex; justify-content: center;">
        <div class="lang-dropdown-wrapper" style="position: relative; display: inline-block;">
            <button class="lang-toggle-btn" onclick="let menu = this.nextElementSibling; menu.style.display = menu.style.display === 'flex' ? 'none' : 'flex';" onblur="let menu = this.nextElementSibling; setTimeout(() => menu.style.display = 'none', 200);" style="background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); color: white; padding: 12px 24px; border-radius: 100px; font-weight: 700; font-size: 0.95rem; cursor: pointer; transition: 0.3s; display: inline-flex; align-items: center; justify-content: center; min-width: 90px;" onmouseover="this.style.background='rgba(255,255,255,0.2)'" onmouseout="this.style.background='rgba(255,255,255,0.08)'">
               <span class="lang-text">AZ</span> <i class="fas fa-chevron-down" style="margin-left: 8px; font-size: 0.75rem; opacity: 0.8;"></i>
            </button>
            <div class="lang-menu" style="position: absolute; top: 115%; left: 50%; transform: translateX(-50%); background: white; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.2); display: none; flex-direction: column; overflow: hidden; min-width: 90px; z-index: 100;">
                <a href="#" onmousedown="event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='AZ'); this.parentElement.style.display='none';" style="padding: 12px 20px; color: #333; text-decoration: none; font-weight: 700; font-size: 0.9rem; text-align: center; border-bottom: 1px solid #eee;" onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background='white'">AZ</a>
                <a href="#" onmousedown="event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='EN'); this.parentElement.style.display='none';" style="padding: 12px 20px; color: #333; text-decoration: none; font-weight: 700; font-size: 0.9rem; text-align: center; border-bottom: 1px solid #eee;" onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background='white'">EN</a>
                <a href="#" onmousedown="event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='RU'); this.parentElement.style.display='none';" style="padding: 12px 20px; color: #333; text-decoration: none; font-weight: 700; font-size: 0.9rem; text-align: center;" onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background='white'">RU</a>
            </div>
        </div>
    </div>
    \1"""

for filepath in glob.glob('*.html'):
    if filepath in ['admin.html', 'verify.html']:
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Step 1: Strip out all previous language elements completely.
    # Remove the desktop wrapper if it exists
    content = re.sub(r'<div class="lang-dropdown-wrapper".*?</div>\s*</div>', '', content, flags=re.DOTALL)
    # Remove any remaining toggle buttons
    content = re.sub(r'<button class="lang-toggle-btn".*?</button>', '', content, flags=re.DOTALL)
    # Remove the mobile wrapper container div
    content = re.sub(r'<div style="padding: 15px 20px; border-bottom: 1px solid rgba\(255,255,255,0\.1\); margin-bottom: 15px; display: flex; justify-content: center;">\s*</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="mobile-lang-wrapper".*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
    # And clean up any stray <div class="lang-switcher">
    content = re.sub(r'<div class="lang-switcher".*?</div>', '', content, flags=re.DOTALL)

    # Now the code is clean, let's inject them at the specific anchor points.
    
    # 1. Desktop: Before the Qeydiyyat button in nav-actions.
    content = re.sub(r'(<a href="[^"]+" class="btn btn-primary nav-btn"[^>]*>Qeydiyyat</a>)', desktop_btn, content)

    # 2. Mobile: Right after <div class="close-mobile" id="mobile-close"><i class="fas fa-times"></i></div>
    # Actually, we can inject it right before <div class="mobile-nav-links">
    content = re.sub(r'(<div class="mobile-nav-links">)', mobile_btn, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Final clean dropdown injection applied.")
