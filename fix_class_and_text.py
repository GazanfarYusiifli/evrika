import re

with open('admin.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix className logic 1
old_c1 = "const className = p.class_name || p['Neçənci sinif üçün imtahan verəcək?'] || 'Qeyd edilməyib';"
new_c1 = "const className = p.Sinif || p['Sinif'] || p.class_name || p['Neçənci sinif üçün imtahan verəcək?'] || (p.note && p.note.match(/Sinif:\s*([^|]+)/) ? p.note.match(/Sinif:\s*([^|]+)/)[1].trim() : 'Qeyd edilməyib');"
content = content.replace(old_c1, new_c1)

# Fix className logic 2
old_c2 = "const className = item.class_name || item['Neçənci sinif üçün imtahan verəcək?'] || 'Qeyd edilməyib';"
new_c2 = "const className = item.Sinif || item['Sinif'] || item.class_name || item['Neçənci sinif üçün imtahan verəcək?'] || (item.note && item.note.match(/Sinif:\s*([^|]+)/) ? item.note.match(/Sinif:\s*([^|]+)/)[1].trim() : 'Qeyd edilməyib');"
content = content.replace(old_c2, new_c2)

# Remove the text
old_text = '<p style="font-size:16px; line-height:1.6; margin-bottom:40px;">Ətraflı məlumat üçün təqdim olunan fərdi hesabatla tanış ola bilərsiniz.</p>'
content = content.replace(old_text, "")

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Class name logic fixed and text removed.")
