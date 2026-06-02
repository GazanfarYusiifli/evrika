import re
from bs4 import BeautifulSoup

def find_untranslated(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    untranslated = []
    for text in soup.find_all(text=True):
        if text.parent.name in ['script', 'style', 'title']:
            continue
        s = text.strip()
        if not s:
            continue
        # Check if parent or any ancestor has data-i18n
        has_i18n = False
        p = text.parent
        while p and p.name != '[document]':
            if p.has_attr('data-i18n'):
                has_i18n = True
                break
            p = p.parent
        if not has_i18n and len(s) > 2 and re.search('[a-zA-ZəöğüşıçƏÖĞÜŞIÇ]', s):
            untranslated.append((s, text.parent.name))
    
    return untranslated

files = ['index.html']
for f in files:
    res = find_untranslated(f)
    print(f"--- {f} ---")
    for t in set(res):
        print(t)
