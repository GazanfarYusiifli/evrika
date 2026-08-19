import re

file = 'admin.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure AMOUNT is translated to ÖDƏNİŞ MƏBLƏĞİ
search_trans = "if (upperKey === 'EPOINT_AMOUNT') cleanKey = 'Ödəniş Məbləği';"
replace_trans = "if (upperKey === 'EPOINT_AMOUNT' || upperKey === 'AMOUNT') cleanKey = 'Ödəniş Məbləği';"
content = content.replace(search_trans, replace_trans, 1)

# Ensure "AD SOYAD" translation if not already
if "if (upperKey === 'AD SOYAD') cleanKey = 'Ad Soyad';" not in content:
    insert_after = "if (upperKey === 'PHONE') cleanKey = 'Telefon';"
    content = content.replace(insert_after, f"{insert_after}\n        if (upperKey === 'AD SOYAD') cleanKey = 'Ad Soyad';", 1)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Translations added")
