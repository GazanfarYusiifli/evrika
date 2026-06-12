import re

# 1. victory.html - Level 3 z-index
with open('victory.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Change z-index of .about-float
html = html.replace('.about-float{position:absolute;bottom:-20px;right:-20px;', 
                    '.about-float{position:absolute;bottom:-20px;right:-20px;z-index:10;')

# In case it has a different format:
html = re.sub(r'(\.about-float\s*\{[^}]*?)(\})', r'\1z-index: 10;\2', html)

with open('victory.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. schools.html
with open('schools.html', 'r', encoding='utf-8') as f:
    s_html = f.read()

# hub-card-4 uses 1000720061.jpg
s_html = re.sub(r'(<!-- Item 4: Victory Colleges.*?<img src=")\./assets/1000720061\.jpg(")', r'\g<1>./assets/sekill3.jpeg\g<2>', s_html, flags=re.DOTALL)
with open('schools.html', 'w', encoding='utf-8') as f:
    f.write(s_html)

# 3. index.html
with open('index.html', 'r', encoding='utf-8') as f:
    i_html = f.read()

# Slide 5 uses 1000720067.jpg
i_html = re.sub(r'(<!-- Slide 5: Victory Colleges by Evrika -->.*?<img.*?src=")\./assets/1000720067\.jpg(")', r'\g<1>./assets/sekill3.jpeg\g<2>', i_html, flags=re.DOTALL)

# exp-card 4 uses 1000720061.jpg
i_html = re.sub(r'(<!-- Entity 4: Victory Colleges by Evrika -->.*?background-image:\s*url\(\')\./assets/1000720061\.jpg(\'\))', r'\g<1>./assets/sekill3.jpeg\g<2>', i_html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(i_html)

print("Updates applied to victory.html, schools.html, index.html.")
