import os
import re
from bs4 import BeautifulSoup
import json

def is_valid_text(text):
    text = text.strip()
    if not text: return False
    if len(text) < 2: return False
    if re.match(r'^[\d\s\W]+$', text): return False
    return True

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

untranslated = {}
counter = 1

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    for tag in soup.find_all(string=True):
        parent = tag.parent
        if parent.name in ['script', 'style', 'title', 'meta', 'link']: continue
        
        # Check if any ancestor has data-i18n
        has_translation = False
        for ancestor in tag.parents:
            if ancestor is None: break
            if ancestor.has_attr('data-i18n'):
                has_translation = True
                break
        
        if has_translation: continue
        
        text = tag.strip()
        if is_valid_text(text):
            if text not in untranslated.values():
                key = f"auto-{counter}"
                untranslated[key] = text
                counter += 1

print(json.dumps(untranslated, ensure_ascii=False, indent=2))
