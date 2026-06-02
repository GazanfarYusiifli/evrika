import re

with open('montessori.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Change Qrupları to black
content = content.replace('<em style="color: #fff; font-style: normal; opacity: 0.9;">Qrupları</em>', '<em style="color: #070d1f !important; font-style: normal; opacity: 0.9;">Qrupları</em>')

# 2. Remove "Aktiv" badges
content = content.replace('<div class="level-badge">Aktiv</div>', '')

# 3. Change Toddler and Primary to black
content = content.replace('<h4>Toddler</h4>', '<h4 style="color: #070d1f !important;">Toddler</h4>')
content = content.replace('<h4>Primary</h4>', '<h4 style="color: #070d1f !important;">Primary</h4>')

with open('montessori.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated yas qruplari")
