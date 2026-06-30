with open('admin.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# We want to change the condition in viewDetails
# Currently it is:
#           if (!isFinance && (upperKey.includes('EPOINT') || ['RRN', 'APPROVAL_CODE', 'CARD_NUMBER', 'CARDNAME', 'RESULT_CODE', '3DSECURE', 'RESULT_PS', 'RESULT'].includes(upperKey))) {
#              if (upperKey === 'EPOINT_AMOUNT' || upperKey === 'PAYMENT_STATUS' || upperKey === 'EPOINT_CARD_NUMBER' || upperKey === 'EPOINT_CARD_TYPE') {
#                 groups['ÖDƏNİŞ DETALLARI'].push(dataPair);
#              }
#           } else {
#              groups['ÖDƏNİŞ DETALLARI'].push(dataPair);
#           }

# Let's replace it with logic that completely hides it if isExam is true.
# Wait, let's first inject `const isExam = document.getElementById('exam-panel').style.display === 'block';`

old_isFinance = "const isFinance = document.getElementById('finance-panel').style.display === 'block';"
new_isFinance = "const isFinance = document.getElementById('finance-panel').style.display === 'block';\n        const isExam = document.getElementById('exam-panel').style.display === 'block';"
content = content.replace(old_isFinance, new_isFinance)

# Now find the block pushing to ÖDƏNİŞ DETALLARI
old_block = """          if (!isFinance && (upperKey.includes('EPOINT') || ['RRN', 'APPROVAL_CODE', 'CARD_NUMBER', 'CARDNAME', 'RESULT_CODE', '3DSECURE', 'RESULT_PS', 'RESULT'].includes(upperKey))) {
             if (upperKey === 'EPOINT_AMOUNT' || upperKey === 'PAYMENT_STATUS' || upperKey === 'EPOINT_CARD_NUMBER' || upperKey === 'EPOINT_CARD_TYPE') {
                groups['ÖDƏNİŞ DETALLARI'].push(dataPair);
             }
          } else {
             groups['ÖDƏNİŞ DETALLARI'].push(dataPair);
          }"""

new_block = """          if (isExam) {
             // Imtahan panelinde ödəniş detallarını ümumiyyətlə gizlədirik
          } else if (!isFinance && (upperKey.includes('EPOINT') || ['RRN', 'APPROVAL_CODE', 'CARD_NUMBER', 'CARDNAME', 'RESULT_CODE', '3DSECURE', 'RESULT_PS', 'RESULT'].includes(upperKey))) {
             if (upperKey === 'EPOINT_AMOUNT' || upperKey === 'PAYMENT_STATUS' || upperKey === 'EPOINT_CARD_NUMBER' || upperKey === 'EPOINT_CARD_TYPE') {
                groups['ÖDƏNİŞ DETALLARI'].push(dataPair);
             }
          } else {
             groups['ÖDƏNİŞ DETALLARI'].push(dataPair);
          }"""

content = content.replace(old_block, new_block)

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(content)
