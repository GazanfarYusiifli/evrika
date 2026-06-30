with open('admin.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_logic = "p['[2.Şagird] Adı'] ? (p['[2.Şagird] Adı'] + ' ' + (p['[2.Şagird] Soyadı']||'')) : (p['Ad Soyad'] || p.fullName || p.name || p.firstName || 'Adsız Şagird')"
new_logic = "p['[2.Şagird] Adı'] ? (p['[2.Şagird] Adı'] + ' ' + (p['[2.Şagird] Soyadı']||'')) : (p['Ad Soyad'] || p.fullName || p.name || p.firstName || p['[1.Əlaqə] Valideyn Adı'] || p['Valideyn'] || 'Adsız Şagird')"
content = content.replace(old_logic, new_logic)

old_logic_item = "item['[2.Şagird] Adı'] ? (item['[2.Şagird] Adı'] + ' ' + (item['[2.Şagird] Soyadı']||'')) : (item['Ad Soyad'] || item.fullName || item.name || item.firstName || 'Adsız Şagird')"
new_logic_item = "item['[2.Şagird] Adı'] ? (item['[2.Şagird] Adı'] + ' ' + (item['[2.Şagird] Soyadı']||'')) : (item['Ad Soyad'] || item.fullName || item.name || item.firstName || item['[1.Əlaqə] Valideyn Adı'] || item['Valideyn'] || 'Adsız Şagird')"
content = content.replace(old_logic_item, new_logic_item)

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(content)
