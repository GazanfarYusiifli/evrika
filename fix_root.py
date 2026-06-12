import re

with open('victory.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace root variables to eliminate all yellowish tints
html = html.replace('--accent-light:#fef08a', '--accent-light:#3b82f6')
html = html.replace('--navy:#0a0a05', '--navy:#020617')
html = html.replace('--navy-mid:#141200', '--navy-mid:#0f172a')

# Also fix the background for Foundation Program
html = html.replace('<em style="color: var(--accent-light);">Proqramı</em>', '<em>Proqramı</em>')
html = html.replace('<h2 class="sec-h2">Foundation <em>Proqramı</em></h2>', '<h2 class="sec-h2">Foundation <em style="color: #3b82f6; font-style: normal;">Proqramı</em></h2>')

with open('victory.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Root variables fixed")
