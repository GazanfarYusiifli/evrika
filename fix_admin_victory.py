import re

with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace CRM keys
html = html.replace("else if (allText.includes('eduhome')) s = 'eduhome';", "else if (allText.includes('victory') || allText.includes('eduhome')) s = 'victory';")
html = html.replace("'eduhome':'Eduhome',", "'victory':'Victory',")
html = html.replace("'Eduhome', 'Zümrüd'", "'Victory', 'Zümrüd'")
html = html.replace("'eduhome': 'Eduhome Hazırlıq (Qeydiyyat)'", "'victory': 'Victory Colleges (Qeydiyyat)'")
html = html.replace("'eduhome', 'zumrud'", "'victory', 'zumrud'")

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated admin.html")
