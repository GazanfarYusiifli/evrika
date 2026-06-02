import glob
import re

desktop_lang_btn = """        <div class="lang-switcher" style="display: flex; gap: 6px; font-weight: 700; font-size: 0.75rem; align-items: center; background: rgba(255,255,255,0.08); padding: 8px 14px; border-radius: 50px; border: 1px solid rgba(255,255,255,0.15); margin-right: 8px;">
           <a href="#" style="color: white; text-decoration: none; cursor: pointer;">AZ</a>
           <span style="color: rgba(255,255,255,0.3);">|</span>
           <a href="#" style="color: rgba(255,255,255,0.6); text-decoration: none; transition: 0.3s; cursor: pointer;" onmouseover="this.style.color='white'" onmouseout="this.style.color='rgba(255,255,255,0.6)'">EN</a>
           <span style="color: rgba(255,255,255,0.3);">|</span>
           <a href="#" style="color: rgba(255,255,255,0.6); text-decoration: none; transition: 0.3s; cursor: pointer;" onmouseover="this.style.color='white'" onmouseout="this.style.color='rgba(255,255,255,0.6)'">RU</a>
        </div>
        <a href="schools.html" class="btn btn-primary nav-btn">Qeydiyyat</a>"""

# Since different pages might have different registration links (e.g. register-montessori.html), 
# I will use a regex to capture the original Qeydiyyat link and just prepend the switcher to it!

desktop_replacement = r"""        <div class="lang-switcher" style="display: flex; gap: 6px; font-weight: 700; font-size: 0.75rem; align-items: center; background: rgba(255,255,255,0.08); padding: 8px 14px; border-radius: 50px; border: 1px solid rgba(255,255,255,0.15); margin-right: 8px;">
           <a href="#" style="color: white; text-decoration: none; cursor: pointer;">AZ</a>
           <span style="color: rgba(255,255,255,0.3);">|</span>
           <a href="#" style="color: rgba(255,255,255,0.6); text-decoration: none; transition: 0.3s; cursor: pointer;" onmouseover="this.style.color='white'" onmouseout="this.style.color='rgba(255,255,255,0.6)'">EN</a>
           <span style="color: rgba(255,255,255,0.3);">|</span>
           <a href="#" style="color: rgba(255,255,255,0.6); text-decoration: none; transition: 0.3s; cursor: pointer;" onmouseover="this.style.color='white'" onmouseout="this.style.color='rgba(255,255,255,0.6)'">RU</a>
        </div>
        \1"""


mobile_lang_btn = r"""    <div style="padding: 15px 20px; border-bottom: 1px solid rgba(255,255,255,0.1); margin-bottom: 15px; display: flex; justify-content: center;">
        <div class="lang-switcher" style="display: flex; gap: 15px; font-weight: 700; font-size: 0.9rem; align-items: center; background: rgba(255,255,255,0.08); padding: 10px 24px; border-radius: 50px; border: 1px solid rgba(255,255,255,0.15);">
           <a href="#" style="color: white; text-decoration: none;">AZ</a>
           <span style="color: rgba(255,255,255,0.3);">|</span>
           <a href="#" style="color: rgba(255,255,255,0.6); text-decoration: none;">EN</a>
           <span style="color: rgba(255,255,255,0.3);">|</span>
           <a href="#" style="color: rgba(255,255,255,0.6); text-decoration: none;">RU</a>
        </div>
    </div>
    \1"""


for filepath in glob.glob('*.html'):
    if filepath in ['admin.html', 'verify.html']:
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Avoid adding multiple times
    if 'class="lang-switcher"' in content:
        # Just in case we ran it before and want to avoid duplication
        # First we remove the existing ones so we can cleanly add them back
        content = re.sub(r'<div class="lang-switcher".*?</div>', '', content, flags=re.DOTALL)
        content = re.sub(r'<div style="padding: 15px 20px; border-bottom: 1px solid rgba\(255,255,255,0\.1\); margin-bottom: 15px; display: flex; justify-content: center;">\s*</div>', '', content)

    # In desktop nav, replace the <a href="..." class="btn btn-primary nav-btn">...</a> 
    # with the switcher followed by the captured link.
    # We must only match inside `<div class="nav-actions">`
    content = re.sub(r'(<a href="[^"]+" class="btn btn-primary nav-btn"[^>]*>Qeydiyyat</a>)', desktop_replacement, content)

    # In mobile nav, replace `<div class="mobile-nav-links">` with the switcher followed by `<div class="mobile-nav-links">`
    content = re.sub(r'(<div class="mobile-nav-links">)', mobile_lang_btn, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Language switchers added to all HTML files.")
