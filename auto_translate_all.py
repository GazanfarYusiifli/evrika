import os
import re
import json
import time
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

# 1. Parse existing main.js translations
with open('src/main.js', 'r', encoding='utf-8') as f:
    main_js = f.read()

az_block = re.search(r'az:\s*\{([\s\S]*?)\}', main_js)
en_block = re.search(r'en:\s*\{([\s\S]*?)\}', main_js)
ru_block = re.search(r'ru:\s*\{([\s\S]*?)\}', main_js)

def parse_dict(block_str):
    if not block_str: return {}
    lines = block_str.group(1).split('\n')
    d = {}
    for line in lines:
        match = re.match(r'^\s*"([^"]+)":\s*"(.*)",?\s*$', line)
        if match:
            # unescape quotes if necessary, but here we just take the raw string
            d[match.group(1)] = match.group(2)
    return d

existing_az = parse_dict(az_block)
existing_en = parse_dict(en_block)
existing_ru = parse_dict(ru_block)

print(f"Loaded existing translations: {len(existing_az)} keys")

public_pages = [
    'index.html', 'about.html', 'lisey.html', 'lisey2.html', 'montessori.html', 
    'eduhome.html', 'zumrud.html', 'vacancy.html', 'ptim.html', 'contact.html', 
    'news.html', 'news-detail.html', 'alumni.html', 'achievements.html', 'schools.html',
    'privacy.html', 'terms.html', 'cookies.html', 'register-eduhome.html', 
    'register-lisey1.html', 'register-lisey2.html', 'register-montessori.html', 'register-zumrud.html'
]

def is_valid_text(text):
    text = text.strip()
    if not text: return False
    if len(text) < 2: return False
    if re.match(r'^[\d\s\W_]+$', text): return False
    return True

translator_en = GoogleTranslator(source='az', target='en')
translator_ru = GoogleTranslator(source='az', target='ru')

# Map from raw text to translation key
text_to_key = {v: k for k, v in existing_az.items()}
new_translations = {}

counter = 1

for file in public_pages:
    if not os.path.exists(file): continue
    with open(file, 'r', encoding='utf-8') as f:
        html_content = f.read()
        
    soup = BeautifulSoup(html_content, 'html.parser')
    modified = False
    
    # Also find missing keys that are in HTML but not in JS
    for tag in soup.find_all(True):
        if tag.has_attr('data-i18n'):
            k = tag['data-i18n']
            if k not in existing_az and k not in new_translations:
                txt = tag.get_text(strip=True)
                if txt:
                    new_translations[k] = {'az': txt}
    
    # Process text nodes
    for tag in soup.find_all(string=True):
        parent = tag.parent
        if parent is None or parent.name in ['script', 'style', 'title', 'meta', 'link']: continue
        
        has_translation = False
        for ancestor in tag.parents:
            if ancestor is None: break
            if ancestor.has_attr('data-i18n'):
                has_translation = True
                break
        
        if has_translation: continue
        
        text = tag.strip()
        if is_valid_text(text):
            # Check if this text already has a key in existing_az
            key = None
            if text in text_to_key:
                key = text_to_key[text]
            else:
                # Need a new key
                slug = re.sub(r'[^a-zA-Z0-9]+', '-', text.lower())[:25].strip('-')
                if not slug: slug = f"auto-{counter}"
                key = f"t-{slug}-{counter}"
                counter += 1
                
                new_translations[key] = {'az': text}
                text_to_key[text] = key
            
            # Since we can't easily add attributes to string nodes in BS4,
            # we wrap the string in a span with the data-i18n attribute
            if parent.string and parent.string.strip() == text:
                # If the parent only contains this string, add it to parent
                parent['data-i18n'] = key
                modified = True
            else:
                # wrap in span
                new_span = soup.new_tag("span")
                new_span['data-i18n'] = key
                new_span.string = text
                tag.replace_with(new_span)
                modified = True
                
    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Updated HTML: {file}")

print(f"Found {len(new_translations)} new translations to process.")

# Translate in chunks to avoid API limits
keys_to_translate = list(new_translations.keys())
total = len(keys_to_translate)

for i, k in enumerate(keys_to_translate):
    az_text = new_translations[k]['az']
    try:
        en_text = translator_en.translate(az_text)
        ru_text = translator_ru.translate(az_text)
    except Exception as e:
        print(f"Translation failed for {k}: {e}")
        time.sleep(2)
        try:
            en_text = translator_en.translate(az_text)
            ru_text = translator_ru.translate(az_text)
        except:
            en_text = az_text
            ru_text = az_text
            
    new_translations[k]['en'] = en_text.replace('"', "'")
    new_translations[k]['ru'] = ru_text.replace('"', "'")
    existing_az[k] = az_text.replace('"', "'")
    existing_en[k] = new_translations[k]['en']
    existing_ru[k] = new_translations[k]['ru']
    
    if (i+1) % 50 == 0:
        print(f"Translated {i+1}/{total}...")
        time.sleep(1) # brief pause

# Save back to main.js
def dict_to_js_string(d):
    lines = []
    for k, v in d.items():
        v = str(v).replace('\n', '\\n').replace('\r', '')
        lines.append(f'    "{k}": "{v}"')
    return ',\n'.join(lines)

new_az_str = dict_to_js_string(existing_az)
new_en_str = dict_to_js_string(existing_en)
new_ru_str = dict_to_js_string(existing_ru)

new_translations_js = f"""const translations = {{
  az: {{
{new_az_str}
  }},
  en: {{
{new_en_str}
  }},
  ru: {{
{new_ru_str}
  }}
}};"""

new_main_js = re.sub(r'const translations = \{[\s\S]*?\n};\n?', new_translations_js + '\n', main_js)

with open('src/main.js', 'w', encoding='utf-8') as f:
    f.write(new_main_js)

print("Finished updating main.js and HTML files.")
