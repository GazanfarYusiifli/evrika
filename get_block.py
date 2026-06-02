import re

def get_media_block(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.search(r'@media\s*\(max-width:\s*1024px\)\s*\{([^}]*)\.nav-glass-container.*?\}', content, re.DOTALL)
    if match:
        print(f"Found in {filepath}")
    else:
        print(f"Not found in {filepath}")

get_media_block("lisey2.html")
