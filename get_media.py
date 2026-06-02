import re
import sys

def extract_media(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.search(r'@media\s*\(max-width:\s*1024px\)\s*\{', content)
    if match:
        print(f"{filepath}: FOUND at index {match.start()}")
    else:
        print(f"{filepath}: NOT FOUND")

extract_media("montessori.html")
extract_media("eduhome.html")
extract_media("zumrud.html")
extract_media("lisey2.html")
