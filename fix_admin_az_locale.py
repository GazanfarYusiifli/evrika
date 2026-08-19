import re

file = 'admin.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hide PAYMENT_STATUS
search_skip = "if(key.startsWith('_')) continue;"
replace_skip = "if(key.startsWith('_') || upperKey === 'PAYMENT_STATUS') continue;"
content = content.replace(search_skip, replace_skip, 1)

# 2. Fix EPOINT block matcher
# from: } else if (upperKey.includes('EPOINT') || upperKey === 'AMOUNT' || upperKey.includes('PAYMENT') || ...
# to:   } else if (upperKey.includes('EPOINT') || upperKey.includes('EPOİNT') || upperKey === 'AMOUNT' || upperKey.includes('PAYMENT') || ...
search_epoint = "} else if (upperKey.includes('EPOINT') || upperKey === 'AMOUNT'"
replace_epoint = "} else if (upperKey.includes('EPOINT') || upperKey.includes('EPOİNT') || upperKey === 'AMOUNT'"
content = content.replace(search_epoint, replace_epoint, 1)

# 3. Fix PHONE/MAIL block matcher
# from: } else if (upperKey.includes('PHONE') || upperKey.includes('TEL') || upperKey.includes('MAIL') || upperKey === 'ƏLAQƏ') {
# to:   } else if (upperKey.includes('PHONE') || upperKey.includes('TEL') || upperKey.includes('MAIL') || upperKey.includes('MAİL') || upperKey === 'ƏLAQƏ') {
search_mail = "} else if (upperKey.includes('PHONE') || upperKey.includes('TEL') || upperKey.includes('MAIL') || upperKey === 'ƏLAQƏ') {"
replace_mail = "} else if (upperKey.includes('PHONE') || upperKey.includes('TEL') || upperKey.includes('MAIL') || upperKey.includes('MAİL') || upperKey === 'ƏLAQƏ') {"
content = content.replace(search_mail, replace_mail, 1)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Locale regex fixed")
