import re

with open('montessori.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove badges
content = re.sub(r'<div class="bento-badge">Akademik</div>', '', content)
content = re.sub(r'<div class="bento-badge">Kurikulum</div>', '', content)
content = re.sub(r'<div class="bento-badge">Sağlamlıq</div>', '', content)

# 2. Fix bento overlay & img
old_img = ".bento-item img { width: 100%; height: 100%; object-fit: cover; opacity: 0.85; filter: brightness(0.9); transition: all 0.8s ease; }"
new_img = ".bento-item img { width: 100%; height: 100%; object-fit: cover; opacity: 1; transition: all 0.8s ease; }"
content = content.replace(old_img, new_img)

old_hover = ".bento-item:hover img { opacity: 1; filter: brightness(1.1); transform: scale(1.1); }"
new_hover = ".bento-item:hover img { transform: scale(1.1); filter: brightness(1.05); }"
content = content.replace(old_hover, new_hover)

old_overlay = "background: linear-gradient(to top, rgba(7, 13, 31, 0.9) 0%, rgba(7, 13, 31, 0.4) 50%, transparent 100%);"
new_overlay = "background: linear-gradient(to top, rgba(0, 0, 0, 0.4) 0%, transparent 50%);"
content = content.replace(old_overlay, new_overlay)

with open('montessori.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated bento grid")
