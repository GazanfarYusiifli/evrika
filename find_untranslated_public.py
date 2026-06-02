import os
import re
from bs4 import BeautifulSoup
import json

def is_valid_text(text):
    text = text.strip()
    if not text: return False
    if len(text) < 2: return False
    if re.match(r'^[\d\s\W_]+$', text): return False
    return True

public_pages = [
    'index.html', 'about.html', 'lisey.html', 'lisey2.html', 'montessori.html', 
    'eduhome.html', 'zumrud.html', 'vacancy.html', 'ptim.html', 'contact.html', 
    'news.html', 'news-detail.html', 'alumni.html', 'achievements.html', 'schools.html',
    'privacy.html', 'terms.html', 'cookies.html', 'register-eduhome.html', 
    'register-lisey1.html', 'register-lisey2.html', 'register-montessori.html', 'register-zumrud.html'
]

untranslated = {}
counter = 1

for file in public_pages:
    if not os.path.exists(file): continue
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
                # create a clean slug key
                slug = re.sub(r'[^a-zA-Z0-9]+', '-', text.lower())[:30].strip('-')
                if not slug: slug = f"auto-{counter}"
                key = f"t-{slug}-{counter}"
                untranslated[key] = text
                counter += 1

print(json.dumps(untranslated, ensure_ascii=False, indent=2))
