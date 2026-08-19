import re

file = 'admin.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# We want to format the value before creating the dataPair
# Find the line: let cleanKey = key.replace(/\[.*?\]\s*/g, '').replace(/_/g, ' ');
# Then add date formatting logic.

search_str = "let cleanKey = key.replace(/\\[.*?\\]\\s*/g, '').replace(/_/g, ' ');"
insert_str = """
        let cleanKey = key.replace(/\\[.*?\\]\\s*/g, '').replace(/_/g, ' ');
        
        let displayVal = val;
        if ((upperKey === 'DATE' || upperKey === 'TARIX' || upperKey === 'CREATED_AT') && typeof val === 'string') {
            try {
                let d = new Date(val);
                if (!isNaN(d.getTime())) {
                    displayVal = d.toLocaleString('az-AZ', { day:'2-digit', month:'2-digit', year:'numeric', hour:'2-digit', minute:'2-digit', second:'2-digit' }).replace(',', '');
                }
            } catch(e){}
        }
"""
if search_str in content:
    content = content.replace(search_str, insert_str, 1)

# Now find where dataPair is created and change value: val to value: displayVal
# const dataPair = { rawKey: key, label: cleanKey.toUpperCase(), value: val };
search_pair = "const dataPair = { rawKey: key, label: cleanKey.toUpperCase(), value: val };"
replace_pair = "const dataPair = { rawKey: key, label: cleanKey.toUpperCase(), value: displayVal };"
if search_pair in content:
    content = content.replace(search_pair, replace_pair, 1)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Date formatting added.")
