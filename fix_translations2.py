import re

file = 'src/main.js'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    r'"reg-child-name":.*?,': '"reg-child-name": "ŞAGİRDİN ADI",',
    r'"reg-child-surname":.*?,': '"reg-child-surname": "ŞAGİRDİN SOYADI",',
    r'"reg-prev-school-kinder":.*?,': '"reg-prev-school-kinder": "Hazırda təhsil aldığı təhsil müəssisəsi ( bağça və məktəb)",',
    r'"form-child-name":.*?,': '"form-child-name": "ŞAGİRDİN ADI",',
    r'"form-child-surname":.*?,': '"form-child-surname": "ŞAGİRDİN SOYADI",'
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

print("Translations updated again")
