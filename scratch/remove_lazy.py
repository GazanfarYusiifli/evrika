with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace('loading="lazy" decoding="async"', '')
content = content.replace('loading="lazy"', '')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
