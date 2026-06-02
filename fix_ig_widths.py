import os

with open('montessori.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the max-width in the instagram embeds
# original: max-width:540px; min-width:326px;
# target: max-width:350px; min-width:300px;
content = content.replace('max-width:540px;', 'max-width:350px;')
content = content.replace('min-width:326px;', 'min-width:320px;')

# Also add the nice rounded corners and shadow that Zümrüd had
# original had: border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px;
# We want: border-radius:16px; box-shadow:0 20px 40px rgba(0,0,0,0.3); margin: 0;
content = content.replace('border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px;', 'border-radius:16px; box-shadow:0 20px 40px rgba(0,0,0,0.3); margin: 0;')

with open('montessori.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated instagram styles in montessori.html")
