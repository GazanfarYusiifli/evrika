import os
import re
from bs4 import BeautifulSoup
import json

def is_valid_text(text):
    text = text.strip()
    if not text: return False
    # Ignore pure numbers or symbols
    if re.match(r'^[\d\s\W]+$', text): return False
    return True

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

untranslated = {}
counter = 1

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # We want elements that contain direct text
    for tag in soup.find_all(string=False):
        if tag.name in ['script', 'style', 'meta', 'link', 'title', 'br', 'hr']:
            continue
            
        if tag.has_attr('data-i18n'):
            continue
            
        # Get direct text, not text from children
        direct_texts = [text.strip() for text in tag.find_all(string=True, recursive=False) if is_valid_text(text.strip())]
        
        if direct_texts:
            text = " ".join(direct_texts).strip()
            if text and is_valid_text(text):
                # Add to dict
                if text not in untranslated.values():
                    key = f"auto-{counter}"
                    untranslated[key] = text
                    counter += 1

with open('untranslated.json', 'w', encoding='utf-8') as f:
    json.dump(untranslated, f, ensure_ascii=False, indent=2)

print(f"Found {len(untranslated)} untranslated unique strings.")
