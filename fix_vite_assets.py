import re

with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the script and link tags for vite dev mode
html = re.sub(
    r'<script type="module" crossorigin src="./assets/main-[a-zA-Z0-9_-]+\.js"></script>',
    r'<script type="module" src="/src/main.js"></script>',
    html
)

html = re.sub(
    r'<link rel="stylesheet" crossorigin href="./assets/style-[a-zA-Z0-9_-]+\.css">',
    r'',
    html
)

html = html.replace('</link></link></meta>', '')

with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
