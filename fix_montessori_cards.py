import re

with open('montessori.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace .prog-card-modern background
old_card = """.prog-card-modern {
      background: rgba(255,255,255,0.03);"""
new_card = """.prog-card-modern {
      background: #9ba278;"""
content = content.replace(old_card, new_card)

# Replace .prog-h-modern color
old_h = ".prog-h-modern { font-size: 1.1rem; font-weight: 800; color:var(--text); margin: 0; line-height: 1.3; }"
new_h = ".prog-h-modern { font-size: 1.1rem; font-weight: 800; color:#fff; margin: 0; line-height: 1.3; }"
content = content.replace(old_h, new_h)

with open('montessori.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated cards")
