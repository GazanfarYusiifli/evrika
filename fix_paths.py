import os
import re
import glob

html_files = glob.glob("*.html")

# Regular expression to match Vite hashed assets (e.g., something-HASH8.ext)
# Specifically looking for -[A-Za-z0-9_-]{8}\.
import re

def fix_content(content):
    # Fix main.js and style.css
    content = re.sub(r'\./assets/main-[a-zA-Z0-9_-]{8}\.js', '/src/main.js', content)
    content = re.sub(r'\./assets/style-[a-zA-Z0-9_-]{8}\.css', '/src/style.css', content)
    
    # Remove crossorigin attribute inserted by Vite
    content = content.replace('<script type="module" crossorigin src="/src/main.js"></script>', '<script type="module" src="/src/main.js"></script>')
    content = content.replace('<link rel="stylesheet" crossorigin href="/src/style.css">', '<link rel="stylesheet" href="/src/style.css">')
    
    # Fix images/videos/etc
    def replacer(match):
        base = match.group(1)
        ext = match.group(2)
        return f'./assets/{base}.{ext}'
    
    # Replace anything looking like ./assets/filename-hash8.ext
    content = re.sub(r'\./assets/([^/]+)-[a-zA-Z0-9_-]{8}\.([a-zA-Z0-9]+)', replacer, content)
    
    return content

count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = fix_content(content)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Fixed {file}")

print(f"Total fixed: {count}")
