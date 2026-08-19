import re

file = 'admin.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Make the onchange cleaner
old_input = '<input type="file" hidden accept="image/jpeg,image/png,image/webp" id="popup-img-file" onchange="uploadImage(this, \'popup-img\'); const p = this.parentElement.nextElementSibling; if(p){ p.style.display=\'block\'; setTimeout(()=>p.src=document.getElementById(\'popup-img\').value, 2000); }">'

new_input = '<input type="file" hidden accept="image/jpeg,image/png,image/webp" id="popup-img-file" onchange="uploadImage(this, \'popup-img\'); let i=0; let int=setInterval(()=>{let v=document.getElementById(\'popup-img\').value; if(v && v.startsWith(\'http\')){ let p=document.getElementById(\'popup-img-preview\'); p.src=v; p.style.display=\'block\'; clearInterval(int);} i++; if(i>30)clearInterval(int);}, 1000);">'

if old_input in content:
    content = content.replace(old_input, new_input)
else:
    print("Old input not found")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
