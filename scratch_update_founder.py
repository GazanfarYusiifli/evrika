import os
import glob
import re

files = glob.glob('*.html') + ['index_i18n_dictionary.json']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace "Evrika Təhsil Ekosisteminin Təsisçisi" with "EVRİKA TƏHSİL EKOSİSTEMİNİN TƏSİSÇİSİ"
    new_content = content.replace("Evrika Təhsil Ekosisteminin Təsisçisi", "EVRİKA TƏHSİL EKOSİSTEMİNİN TƏSİSÇİSİ")
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
