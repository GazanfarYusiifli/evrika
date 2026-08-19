import re

file = 'lisey2.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('./assets/montessori-approach.jpg', './assets/1222.jpeg')

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
