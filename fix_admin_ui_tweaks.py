import re

file = 'admin.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Skip payment_status entirely
# find: if(key.startsWith('_')) continue;
search_skip = "if(key.startsWith('_')) continue;"
replace_skip = "if(key.startsWith('_') || key === 'payment_status') continue;"
content = content.replace(search_skip, replace_skip, 1)

# 2. Fix the grouping so EPOINT CARD NAME doesn't go to ŞƏXSİ MƏLUMATLAR
# Currently, EPOINT keys are checked first:
# } else if (upperKey.includes('EPOINT') || upperKey === 'AMOUNT' || upperKey.includes('PAYMENT') || ['RRN', 'APPROVAL_CODE', 'CARD_NUMBER', 'CARDNAME', 'RESULT_CODE', '3DSECURE', 'RESULT_PS', 'RESULT'].includes(upperKey)) {
# Actually, wait, let's see why it's not going there.
# Let's check the actual code logic in admin.html by finding the group push order.
