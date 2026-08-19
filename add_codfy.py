import os
import glob

old_str = '<p style="color: rgba(255,255,255,0.4); font-size: 0.85rem;"><span data-i18n="footer-rights">© 2026 Evrika Təhsil Ekosistemi. Bütün hüquqlar qorunur.</span></p>'
new_str = '<p style="color: rgba(255,255,255,0.4); font-size: 0.85rem;"><span data-i18n="footer-rights">© 2026 Evrika Təhsil Ekosistemi. Bütün hüquqlar qorunur.</span> | Developed by <a href="https://www.codfy.tech" target="_blank" style="color: rgba(255,255,255,0.7); text-decoration: none; font-weight: bold; transition: 0.3s;" onmouseover="this.style.color=\'white\'" onmouseout="this.style.color=\'rgba(255,255,255,0.7)\'">Codfy</a></p>'

files_changed = 0
for filepath in glob.glob('**/*.html', recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_str in content:
        content = content.replace(old_str, new_str)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        files_changed += 1

print(f"Added Codfy to {files_changed} HTML files.")
