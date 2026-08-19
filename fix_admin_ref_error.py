import re

file = 'admin.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the broken lines
search_err = """        if(key.startsWith('_') || upperKey === 'PAYMENT_STATUS') continue;
        const val = item[key];
        const upperKey = key.toLocaleUpperCase('az-AZ');"""
replace_err = """        if(key.startsWith('_')) continue;
        const val = item[key];
        const upperKey = key.toLocaleUpperCase('az-AZ');
        if(upperKey === 'PAYMENT_STATUS' || upperKey === 'DAXILI ÖDƏNIŞ STATUSU') continue;"""

content = content.replace(search_err, replace_err, 1)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("ReferenceError fixed")
