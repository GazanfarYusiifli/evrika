import re

with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make the keys even more readable
html = html.replace("cleanKey = 'Kartın Son Rəqəmləri'", "cleanKey = 'Ödəyici Kartı (Maska)'")
html = html.replace("cleanKey = 'Kart Növü / Adı'", "cleanKey = 'Kartın Növü'")

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(html)
