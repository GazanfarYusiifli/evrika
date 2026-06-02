import glob
import re

desktop_btn = r"""        <div class="lang-dropdown-wrapper" style="position: relative; display: inline-flex; margin-right: 12px; height: 100%;">
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

mobile_btn = r"""    <div class="close-mobile" id="mobile-close"><i class="fas fa-times"></i></div>
    <div class="mobile-nav-links">
      <div class="mobile-lang-wrapper" style="padding: 15px 30px; border-bottom: 1px solid rgba(0,0,0,0.05); display: flex; justify-content: flex-start;">
        <div class="lang-dropdown-wrapper" style="position: relative; display: inline-block;">
            <button class="lang-toggle-btn" onclick="let menu = this.nextElementSibling; menu.style.display = menu.style.display === 'flex' ? 'none' : 'flex';" onblur="let menu = this.nextElementSibling; setTimeout(() => menu.style.display = 'none', 200);" style="background: #1e3a8a; border: none; color: white; padding: 12px 28px; border-radius: 100px; font-weight: 800; font-size: 1.1rem; cursor: pointer; transition: 0.3s; display: inline-flex; align-items: center; justify-content: center; min-width: 90px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);" onmouseover="this.style.background='#284baf'" onmouseout="this.style.background='#1e3a8a'">
               <span class="lang-text">AZ</span> <i class="fas fa-chevron-down" style="margin-left: 10px; font-size: 0.9rem; opacity: 0.9;"></i>
            </button>
            <div class="lang-menu" style="position: absolute; top: 115%; left: 0; background: white; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.2); display: none; flex-direction: column; overflow: hidden; min-width: 90px; z-index: 100;">
                <a href="#" onmousedown="event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='AZ'); this.parentElement.style.display='none';" style="padding: 14px 20px; color: #333; text-decoration: none; font-weight: 800; font-size: 1rem; text-align: center; border-bottom: 1px solid #eee;" onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background='white'">AZ</a>
                <a href="#" onmousedown="event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='EN'); this.parentElement.style.display='none';" style="padding: 14px 20px; color: #333; text-decoration: none; font-weight: 800; font-size: 1rem; text-align: center; border-bottom: 1px solid #eee;" onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background='white'">EN</a>
                <a href="#" onmousedown="event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='RU'); this.parentElement.style.display='none';" style="padding: 14px 20px; color: #333; text-decoration: none; font-weight: 800; font-size: 1rem; text-align: center;" onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background='white'">RU</a>
            </div>
        </div>
      </div>"""

for filepath in glob.glob('*.html'):
    if filepath in ['admin.html', 'verify.html']:
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Clear old desktop
    content = re.sub(r'<div class="lang-dropdown-wrapper".*?</div>\s*</div>', '', content, flags=re.DOTALL)
    
    # Inject new desktop
    content = re.sub(r'(<a href="[^"]+" class="btn btn-primary nav-btn"[^>]*>Qeydiyyat</a>)', desktop_btn, content)

    # Clean old mobile block from previous steps completely
    content = re.sub(r'<div class="close-mobile" id="mobile-close">.*?<div class="mobile-nav-links">', '', content, flags=re.DOTALL)
    # Also clean up if there was a stray mobile-lang-wrapper
    content = re.sub(r'<div class="mobile-lang-wrapper".*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)

    # Now inject the clean mobile
    # Since we removed <div class="close-mobile" id="mobile-close">...<div class="mobile-nav-links"> we just need to place it after <div class="mobile-nav-overlay" id="mobile-nav">
    # Wait! If I removed `<div class="close-mobile" id="mobile-close">.*?<div class="mobile-nav-links">` completely, I need to inject it back!
    # Ah, let's inject it into `<div class="mobile-nav-overlay" id="mobile-nav">`
    content = re.sub(r'(<div class="mobile-nav-overlay" id="mobile-nav">\s*)', r'\1' + mobile_btn + '\n', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Solid blue and balanced height applied.")
