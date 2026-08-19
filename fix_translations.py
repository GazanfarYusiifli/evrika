import re

file = 'src/main.js'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    r'"reg-student-name":.*?,': '"reg-student-name": "ŞAGİRDİN ADI",',
    r'"reg-student-surname":.*?,': '"reg-student-surname": "ŞAGİRDİN SOYADI",',
    r'"reg-prev-school":.*?,': '"reg-prev-school": "Hazırda təhsil aldığı təhsil müəssisəsi ( bağça və məktəb)",',
    r'"reg-class":.*?,': '"reg-class": "Müraciət etdiyi sinif",',
    r'"reg-sector":.*?,': '"reg-sector": "Müraciət etdiyi bölmə",',
    r'"reg-parent-phone":.*?,': '"reg-parent-phone": "VALİDEYNİN ƏLAQƏ NÖMRƏSİ",',
    r'"reg-email":.*?,': '"reg-email": "MAİL ÜNVANI",'
}

for pattern, replacement in replacements.items():
    content = re.sub(pattern, replacement, content)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
    
file2 = 'index_i18n_dictionary.json'
with open(file2, 'r', encoding='utf-8') as f:
    content2 = f.read()

for pattern, replacement in replacements.items():
    content2 = re.sub(pattern, replacement, content2)

with open(file2, 'w', encoding='utf-8') as f:
    f.write(content2)

print("Translations updated")
