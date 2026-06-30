import re

with open('admin.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update name logic
old_name_logic = "p['[2.Şagird] Adı'] ? (p['[2.Şagird] Adı'] + ' ' + (p['[2.Şagird] Soyadı']||'')) : (p.fullName || p.name || 'Adsız Şagird')"
new_name_logic = "p['[2.Şagird] Adı'] ? (p['[2.Şagird] Adı'] + ' ' + (p['[2.Şagird] Soyadı']||'')) : (p['Ad Soyad'] || p.fullName || p.name || p.firstName || 'Adsız Şagird')"
content = content.replace(old_name_logic, new_name_logic)

old_item_name_logic = "item['[2.Şagird] Adı'] ? (item['[2.Şagird] Adı'] + ' ' + (item['[2.Şagird] Soyadı']||'')) : (item.fullName || item.name || 'Adsız Şagird')"
new_item_name_logic = "item['[2.Şagird] Adı'] ? (item['[2.Şagird] Adı'] + ' ' + (item['[2.Şagird] Soyadı']||'')) : (item['Ad Soyad'] || item.fullName || item.name || item.firstName || 'Adsız Şagird')"
content = content.replace(old_item_name_logic, new_item_name_logic)

# Update logo
old_logo = '<img src="assets/loqoYeni.PNG"'
new_logo = '<img src="https://evrikaliseyi.edu.az/assets/loqoYeni.PNG"'
content = content.replace(old_logo, new_logo)

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Names and logo updated.")
