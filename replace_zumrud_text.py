import re

with open('zumrud.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '<span class="num">🏆</span><span class="lbl">Çempionlar Ocağı</span>',
    '<span class="num">❤️</span><span class="lbl">Ana və uşaq sağlamlığı</span>'
)

with open('zumrud.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Replaced Çempionlar Ocağı in zumrud.html")
