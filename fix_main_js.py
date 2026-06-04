import re

with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/src/main.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix newline in "about-founder-title-2"
content = re.sub(
    r'"about-founder-title-2": "(.*?)\n\s*<span",',
    r'"about-founder-title-2": "\1 <span",',
    content
)

# Fix unescaped quotes in "about-founder-quote"
content = re.sub(
    r'"about-founder-quote": ""(.*?)"',
    r'"about-founder-quote": "«\1"',
    content
)

# Also fix the AZ one which uses "Evrika..." 
content = re.sub(
    r'"about-founder-quote": ""Evrika(.*?)"',
    r'"about-founder-quote": "«Evrika\1"',
    content
)

with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/src/main.js', 'w', encoding='utf-8') as f:
    f.write(content)
