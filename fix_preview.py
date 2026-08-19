import re

file = 'admin.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Add preview logic to the file reader
old_reader = "reader.onload = function(evt) { document.getElementById('popup-img').value = evt.target.result; };"
new_reader = """reader.onload = function(evt) { 
                    document.getElementById('popup-img').value = evt.target.result; 
                    const pv = document.getElementById('popup-img-preview');
                    if(pv) { pv.src = evt.target.result; pv.style.display = 'block'; }
                };"""

if old_reader in content:
    content = content.replace(old_reader, new_reader)

# Add preview update in editPopup
old_edit = "document.getElementById('popup-img').value = p.img || '';"
new_edit = "document.getElementById('popup-img').value = p.img || '';\n        const pv = document.getElementById('popup-img-preview'); if(pv && p.img) { pv.src = p.img; pv.style.display = 'block'; } else if(pv) { pv.style.display = 'none'; }"

if old_edit in content:
    content = content.replace(old_edit, new_edit)

# Add preview clear in resetPopupForm
old_reset = "document.getElementById('popup-img').value = '';"
new_reset = "document.getElementById('popup-img').value = '';\n        const pv = document.getElementById('popup-img-preview'); if(pv) { pv.style.display = 'none'; pv.src = ''; }"

if old_reset in content:
    content = content.replace(old_reset, new_reset)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

