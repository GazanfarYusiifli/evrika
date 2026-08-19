import re

file = 'admin.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace: const upperKey = key.toUpperCase();
# With: const upperKey = key.toLocaleUpperCase('az-AZ');
content = content.replace("const upperKey = key.toUpperCase();", "const upperKey = key.toLocaleUpperCase('az-AZ');")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated toLocaleUpperCase in admin.html")
