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

mobile_btn = r"""    <div class="close-mobile" id="mobile-close"><i class="fas fa-times"></i></div>
    <div class="mobile-lang-wrapper" style="padding: 15px 20px; border-bottom: 1px solid rgba(255,255,255,0.1); margin-bottom: 15px; display: flex; justify-content: center;">
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
    <div class="mobile-nav-links">"""

for filepath in glob.glob('*.html'):
    if filepath in ['admin.html', 'verify.html']:
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Carefully strip desktop solid blue wrapper
    content = re.sub(r'<div class="lang-dropdown-wrapper".*?</div>\s*</div>', '', content, flags=re.DOTALL)
    
    # Strip the mobile solid blue wrapper inside .mobile-nav-links
    # Note: it looks like: <div class="mobile-nav-links">\s*<div class="mobile-lang-wrapper"...>...</div>\s*</div>
    # Actually let's just strip `<div class="mobile-lang-wrapper" ...> ... </div>\s*</div>\s*</div>` maybe.
    # A safer way is to just target the close-mobile to mobile-nav-links again!
    # Because my `refine_lang.py` put it inside `.mobile-nav-links`.
    # Wait, `refine_lang.py` did: 
    # `content = re.sub(r'(<div class="mobile-nav-overlay" id="mobile-nav">\s*)', r'\1' + mobile_btn + '\n', content)`
    # where mobile_btn contained `close-mobile` and `mobile-nav-links` inside it!
    # Let's replace from `<div class="mobile-nav-overlay" id="mobile-nav">` to the `<a href="index.html" data-i18n="nav-home">Ana Səhifə</a>`
    
    content = re.sub(
        r'<div class="mobile-nav-overlay" id="mobile-nav">.*?<a href="index\.html" data-i18n="nav-home">Ana Səhifə</a>',
        '<div class="mobile-nav-overlay" id="mobile-nav">\n' + mobile_btn + '\n      <a href="index.html" data-i18n="nav-home">Ana Səhifə</a>',
        content,
        flags=re.DOTALL
    )

    # Inject desktop transparent button
    content = re.sub(r'(<a href="[^"]+" class="btn btn-primary nav-btn"[^>]*>Qeydiyyat</a>)', desktop_btn, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Reverted to transparent dropdown.")
