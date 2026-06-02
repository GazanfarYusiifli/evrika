import glob
import re

for filepath in glob.glob('*.html'):
    if filepath in ['admin.html', 'verify.html']:
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to remove lines like:
    # <a href="alumni.html" data-i18n="nav-alumni">Məzunlar</a>
    # <a href="achievements.html" data-i18n="nav-achievements">Uğurlar</a>
    # Also without data-i18n:
    # <a href="alumni.html">Məzunlar</a>
    
    # But preserve:
    # <a href="alumni.html" class="dropdown-item">...
    
    # We will use regex to find <a href="alumni.html"...>Məzunlar</a> that do NOT contain class="dropdown-item"
    
    content = re.sub(r'<a href="alumni\.html"(?!.*class="dropdown-item")[^>]*>\s*Məzunlar\s*</a>', '', content)
    content = re.sub(r'<a href="achievements\.html"(?!.*class="dropdown-item")[^>]*>\s*Uğurlar\s*</a>', '', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Standalone alumni and achievements links removed.")
