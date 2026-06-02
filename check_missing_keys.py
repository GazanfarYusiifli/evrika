import os
import re
from bs4 import BeautifulSoup

# Read main.js to get the keys
with open('src/main.js', 'r', encoding='utf-8') as f:
    main_js = f.read()

# Find the translations dictionary for 'az'
az_block = re.search(r'az:\s*\{([\s\S]*?)\}', main_js)
if az_block:
    # extract all keys
    keys_in_js = re.findall(r'"([^"]+)":', az_block.group(1))
    keys_in_js = set(keys_in_js)
else:
    keys_in_js = set()
    print("Could not find 'az' translations in main.js")

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

missing_keys = set()
found_keys = {}

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    for tag in soup.find_all(True):
        if tag.has_attr('data-i18n'):
            key = tag['data-i18n']
            if key not in keys_in_js:
                missing_keys.add(key)
                # Save the text to translate
                found_keys[key] = tag.get_text(strip=True)

import json
print(json.dumps(found_keys, ensure_ascii=False, indent=2))
