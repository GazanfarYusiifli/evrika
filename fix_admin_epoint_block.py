import re

file = 'admin.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the complicated EPOINT block that hides things
search_block = r"""        } else if \(upperKey.includes\('EPOINT'\) \|\| upperKey.includes\('EPOİNT'\) \|\| upperKey === 'AMOUNT' \|\| upperKey.includes\('PAYMENT'\) \|\| \['RRN', 'APPROVAL_CODE', 'CARD_NUMBER', 'CARDNAME', 'RESULT_CODE', '3DSECURE', 'RESULT_PS', 'RESULT'\].includes\(upperKey\)\) \{
          // Eğer isFinance false ise, bəzi spesifik bank detallarını CRM-də gizəlidirik
          if \(isExam\) \{
             // Imtahan panelinde ödəniş detallarını ümumiyyətlə gizəlidirik
          \} else if \(!isFinance && \(upperKey.includes\('EPOINT'\) \|\| \['RRN', 'APPROVAL_CODE', 'CARD_NUMBER', 'CARDNAME', 'RESULT_CODE', '3DSECURE', 'RESULT_PS', 'RESULT'\].includes\(upperKey\)\)\) \{
             if \(upperKey === 'EPOINT_AMOUNT' \|\| upperKey === 'PAYMENT_STATUS' \|\| upperKey === 'EPOINT_CARD_NUMBER' \|\| upperKey === 'EPOINT_CARD_TYPE'\) \{
                groups\['ÖDƏNİŞ DETALLARI'\].push\(dataPair\);
             \}
          \} else \{
             groups\['ÖDƏNİŞ DETALLARI'\].push\(dataPair\);
          \}"""

replace_block = """        } else if (upperKey.includes('EPOINT') || upperKey.includes('EPOİNT') || upperKey === 'AMOUNT' || upperKey.includes('PAYMENT') || ['RRN', 'APPROVAL_CODE', 'CARD_NUMBER', 'CARDNAME', 'RESULT_CODE', '3DSECURE', 'RESULT_PS', 'RESULT'].includes(upperKey) || upperKey === 'DATE' || upperKey === 'TARIX' || upperKey === 'CREATED_AT' || upperKey === 'MƏNBƏ' || upperKey === 'STATUS' || upperKey === 'ORDER_ID') {
          groups['ÖDƏNİŞ DETALLARI'].push(dataPair);"""

content = re.sub(search_block, replace_block, content, count=1)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("EPOINT block replaced")
