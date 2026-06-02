import re

files = ["about.html", "alumni.html", "achievements.html", "contact.html", "vacancy.html", "ptim.html", "schools.html"]

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Find the first img tag after <main> or just the first img tag after nav
    match = re.search(r'<main>.*?(<img[^>]+>)', content, re.DOTALL | re.IGNORECASE)
    if match:
        print(f"{f}: {match.group(1)}")
    else:
        print(f"{f}: No image found after <main>")

