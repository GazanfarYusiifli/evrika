import re

with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the renderFinance Javascript function variables and display
old_table_header = "<th>RRN / Tarix</th>"
new_table_header = "<th>Tranzaksiya ID / Tarix</th>"
html = html.replace(old_table_header, new_table_header)

old_table_header2 = "<th>RRN / Tarix</th>" # in case it's in the other table
html = html.replace(old_table_header2, new_table_header)

# Fix the Javascript mappings
# I will just replace the specific strings in window.renderFinance
html = html.replace("const rrn = p.epoint_transaction || '---';", "const txId = p.epoint_transaction || p.epoint_rrn || '---';")
html = html.replace("RRN: ${rrn}", "ID: ${txId}")

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(html)
