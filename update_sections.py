import re
import os

footer_template = """<footer class="site-footer" style="background: #070d1f; color: white; padding: 80px 0 40px; border-top: 1px solid rgba(255,255,255,0.05);">
    <div class="container" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 60px;">
        <div class="footer-brand">
            <a href="index.html" class="logo" style="color: var(--accent); font-size: 1.8rem; font-weight: 900; text-decoration: none; display: block; margin-bottom: 25px;">EVRIKA</a>
            <p style="color: rgba(255,255,255,0.6); line-height: 1.7; margin-bottom: 30px; font-size: 0.95rem; max-width: 320px;">
                {desc}
            </p>
            <div class="social-icons" style="display: flex; gap: 15px;">
                <a href="#" style="width: 45px; height: 45px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; display: flex; align-items: center; justify-content: center; color: white; transition: 0.3s;"><i class="fab fa-facebook-f"></i></a>
                <a href="#" style="width: 45px; height: 45px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; display: flex; align-items: center; justify-content: center; color: white; transition: 0.3s;"><i class="fab fa-instagram"></i></a>
            </div>
        </div>

        <div class="footer-links">
            <h4 style="text-transform: uppercase; letter-spacing: 0.15em; margin-bottom: 30px; font-size: 0.9rem; font-weight: 800; color: var(--accent);">Naviqasiya</h4>
            <div style="display: flex; flex-direction: column; gap: 15px;">
                <a href="index.html" style="color: rgba(255,255,255,0.6); text-decoration: none; font-size: 0.95rem; transition: 0.3s;">Ana Səhifə</a>
                <a href="about.html" style="color: rgba(255,255,255,0.6); text-decoration: none; font-size: 0.95rem; transition: 0.3s;">Haqqımızda</a>
                <a href="schools.html" style="color: rgba(255,255,255,0.6); text-decoration: none; font-size: 0.95rem; transition: 0.3s;">Akademik Kampuslar</a>
                <a href="contact.html" style="color: rgba(255,255,255,0.6); text-decoration: none; font-size: 0.95rem; transition: 0.3s;">Əlaqə</a>
            </div>
        </div>

        <div class="footer-contact">
            <h4 style="text-transform: uppercase; letter-spacing: 0.15em; margin-bottom: 30px; font-size: 0.9rem; font-weight: 800; color: var(--accent);">Əlaqə</h4>
            <div style="display: flex; flex-direction: column; gap: 20px;">
                <div style="display: flex; gap: 15px; align-items: center;"><i class="fas fa-map-marker-alt" style="color: var(--accent);"></i><span style="color: rgba(255,255,255,0.7);">Baku, Azerbaijan</span></div>
                <div style="display: flex; gap: 15px; align-items: center;"><i class="fas fa-phone-alt" style="color: var(--accent);"></i><span style="color: rgba(255,255,255,0.7);">+994-12 525 10 10</span></div>{extra}
            </div>
        </div>
    </div>

    <div class="footer-bottom" style="margin-top: 80px; padding-top: 40px; border-top: 1px solid rgba(255,255,255,0.05);">
        <div class="container" style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px;">
            <p style="color: rgba(255,255,255,0.4); font-size: 0.85rem;">&copy; 2026 Evrika Təhsil Ekosistemi. Bütün hüquqlar qorunur.</p>
            <div style="display: flex; gap: 30px;">
                <a href="#" style="color: rgba(255,255,255,0.3); text-decoration: none; font-size: 0.85rem; transition: 0.3s;">Məxfilik Siyasəti</a>
            </div>
        </div>
    </div>
</footer>"""

files_data = {
    "montessori.html": {
        "desc": "Montessori Kids Academy — Erkən yaşdan müstəqillik və kəşf sevinci.",
        "extra": ""
    },
    "zumrud.html": {
        "desc": "Zümrüd İdman Mərkəzi — Gələcəyin çempionları burada yetişir.",
         "extra": '\n                <div style="display: flex; gap: 15px; align-items: center;"><i class="fas fa-envelope" style="color: var(--accent);"></i><span style="color: rgba(255,255,255,0.7);">info@evrikaliseyi.edu.az</span></div>'
    },
    "victory.html": {
        "desc": "Eduhome Təhsil Mərkəzi — Qlobal təhsilə açılan qapı.",
         "extra": '\n                <div style="display: flex; gap: 15px; align-items: center;"><i class="fas fa-envelope" style="color: var(--accent);"></i><span style="color: rgba(255,255,255,0.7);">info@evrikaliseyi.edu.az</span></div>'
    }
}

for fname, data in files_data.items():
    if not os.path.exists(fname): continue
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_footer = footer_template.format(desc=data["desc"], extra=data["extra"])
    new_content = re.sub(r'<footer class="site-footer".*?</footer>', new_footer, content, flags=re.DOTALL)
    
    # Check if a::after is present in CSS
    if '.nav-links a::after' not in new_content:
        css_inject = """
.nav-links a::after {
  content: '';
  position: absolute;
  bottom: 0px;
  left: 50%;
  width: 0;
  height: 2px;
  background: var(--accent);
  transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  transform: translateX(-50%);
  border-radius: 2px;
}
.nav-links a:hover::after,
.nav-links a.active::after {
  width: 100%;
}
"""
        new_content = re.sub(r'(\.nav-links a:hover\s*\{[^}]+\})', r'\1' + css_inject, new_content)
        
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Done standardizing sections")
