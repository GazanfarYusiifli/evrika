import re

with open('zumrud.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove ❤️
content = content.replace('<span class="num">❤️</span><span class="lbl">Ana və uşaq sağlamlığı</span>', '<span class="num"></span><span class="lbl">Ana və uşaq sağlamlığı</span>')

# 2. Change open pool image to closed pool image
old_img = 'https://images.unsplash.com/photo-1576013551627-0cc20b96c2a7?auto=format&fit=crop&q=80&w=1200'
new_img = 'https://images.unsplash.com/photo-1582653291997-079a1c04e5d1?auto=format&fit=crop&q=80&w=1200'
content = content.replace(old_img, new_img)

# 3. Remove "Gələcəyin Çempionu Buradan Başlayır"
h2_pattern = re.compile(r'<h2[^>]*>\s*Gələcəyin Çempionu<br>\s*<em[^>]*>Buradan Başlayır</em>\s*</h2>', re.IGNORECASE)
content = h2_pattern.sub('', content)

with open('zumrud.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("zumrud.html updated successfully.")
