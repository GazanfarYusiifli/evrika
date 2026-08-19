import re

file = 'admin.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the input type="file" in view-popup to use onchange="uploadImage(this, 'popup-img')"
old_input = '<input type="file" hidden accept="image/jpeg,image/png,image/webp" id="popup-img-file">'
new_input = '<input type="file" hidden accept="image/jpeg,image/png,image/webp" id="popup-img-file" onchange="uploadImage(this, \'popup-img\'); const p = this.parentElement.nextElementSibling; if(p){ p.style.display=\'block\'; setTimeout(()=>p.src=document.getElementById(\'popup-img\').value, 2000); }">'

content = content.replace(old_input, new_input)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated popup image file input to use uploadImage function.")
