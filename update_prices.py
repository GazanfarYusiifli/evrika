import re

def update_prices(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update static HTML (just in case)
    content = content.replace('<strong>20 AZN</strong> onlayn ödəniş', '<strong>25 AZN</strong> onlayn ödəniş')
    content = content.replace('<strong>30 AZN</strong> onlayn ödəniş', '<strong>35 AZN</strong> onlayn ödəniş')

    # 2. Update JS dynamic text logic
    content = content.replace("var amountText = '30 AZN';", "var amountText = '35 AZN';")
    content = content.replace("amountText = '20 AZN';", "amountText = '25 AZN';")

    # 3. Update JS payment processing amount
    content = content.replace("var amountNum = (grade === 'Məktəbəqədər') ? '20' : '30';", 
                              "var amountNum = (grade === 'Məktəbəqədər') ? '25' : '35';")
                              
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated prices in {filepath}")

for fp in ['register-lisey1.html', 'register-lisey2.html']:
    update_prices(fp)

