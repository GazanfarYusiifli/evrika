import re

with open('victory.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('Evrika <em>Abituriyent?</em>', 'Victory <em>Colleges?</em>')
html = html.replace('Abituriyent proqramına', 'Akademik proqrama')
html = html.replace('Evrika Abituriyent', 'Victory Colleges')
html = html.replace('alt="Evrika Abituriyent"', 'alt="Victory Colleges"')

with open('victory.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Abituriyent traces removed")
