import re

file = 'admin.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Current logic:
# } else if (upperKey.includes('FİLİAL') || upperKey.includes('BÖLMƏ') || upperKey.includes('SİNİF') || upperKey.includes('SEKTOR') || upperKey.includes('TƏHSİL')) {
#   groups['TƏHSİL VƏ İSTİQAMƏT'].push(dataPair);

search_str = "} else if (upperKey.includes('FİLİAL') || upperKey.includes('BÖLMƏ') || upperKey.includes('SİNİF') || upperKey.includes('SEKTOR') || upperKey.includes('TƏHSİL')) {"
replace_str = "} else if (upperKey.includes('FİLİAL') || upperKey.includes('BÖLMƏ') || upperKey.includes('SİNİF') || upperKey.includes('SEKTOR') || upperKey.includes('TƏHSİL') || upperKey.includes('MÜƏSSİSƏ') || upperKey.includes('MƏKTƏB') || upperKey.includes('BAĞÇA') || upperKey.includes('HAZIRDA OXUDUĞU') || upperKey.includes('MƏRKƏZ')) {"

if search_str in content:
    content = content.replace(search_str, replace_str, 1)
    
# Wait, also rename the key in the UI
# if (upperKey === 'ƏVVƏLKİ MÜƏSSİSƏ') cleanKey = 'Hazırda təhsil aldığı təhsil müəssisəsi';
add_rename = "if (upperKey === 'ƏVVƏLKİ MÜƏSSİSƏ' || upperKey.includes('ƏVVƏL OXUDUĞU') || upperKey.includes('GƏLDİYİNİZ TƏHSİL')) cleanKey = 'Hazırda Təhsil Aldığı Müəssisə';"
# insert this below let displayVal = val;
insert_target = "let displayVal = val;"
if insert_target in content:
    content = content.replace(insert_target, f"{insert_target}\n        {add_rename}", 1)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated groups in admin.html")
