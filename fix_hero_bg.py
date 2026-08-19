import re

file = 'lisey2.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("url('./assets/genclik-bg.jpg')", "url('./assets/genclik342.jpeg')")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Background replaced.")
