import re

file = 'admin.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add ug-uni to the form
search_html = r'<input type="text" id="ug-name" placeholder="Ad Soyad" required class="admin-input">'
replace_html = r'<input type="text" id="ug-name" placeholder="Ad Soyad" required class="admin-input">\n              <input type="text" id="ug-uni" placeholder="Nailiyyət (Məs: Respublika Birincisi)" required class="admin-input">'
content = re.sub(search_html, replace_html, content, count=1)

# 2. Update handleUgurSubmit
search_submit = r"""        const payload = \{ 
            name: document.getElementById\('ug-name'\).value, 
            uni: "", 
            detail: "",
            img: document.getElementById\('ug-img'\).value 
        \};"""
replace_submit = """        const payload = { 
            name: document.getElementById('ug-name').value, 
            uni: document.getElementById('ug-uni').value, 
            detail: "",
            img: document.getElementById('ug-img').value 
        };"""
content = re.sub(search_submit, replace_submit, content, count=1)

# 3. Update editUgur
search_edit = r"""        document.getElementById\('ug-name'\).value = u.name;"""
replace_edit = """        document.getElementById('ug-name').value = u.name;\n        document.getElementById('ug-uni').value = u.uni || '';"""
content = re.sub(search_edit, replace_edit, content, count=1)

# 4. Add image preview next to upload button in the form (for both ug and mz)
search_ug_upload = r"""<label class="btn-view" style="cursor:pointer; padding:18px;"><i class="fas fa-upload"></i><input type="file" hidden accept="image/jpeg,image/png,image/webp" onchange="uploadImage\(this, 'ug-img'\)"></label>"""
replace_ug_upload = """<label class="btn-view" style="cursor:pointer; padding:18px;"><i class="fas fa-upload"></i><input type="file" hidden accept="image/jpeg,image/png,image/webp" onchange="uploadImage(this, 'ug-img')"></label>\n                <img id="ug-img-preview" style="width:40px; height:40px; border-radius:8px; object-fit:cover; display:none;">"""
content = re.sub(search_ug_upload, replace_ug_upload, content, count=1)

search_mz_upload = r"""<label class="btn-view" style="cursor:pointer; padding:18px;"><i class="fas fa-upload"></i><input type="file" hidden accept="image/jpeg,image/png,image/webp" onchange="uploadImage\(this, 'mz-img'\)"></label>"""
replace_mz_upload = """<label class="btn-view" style="cursor:pointer; padding:18px;"><i class="fas fa-upload"></i><input type="file" hidden accept="image/jpeg,image/png,image/webp" onchange="uploadImage(this, 'mz-img')"></label>\n                <img id="mz-img-preview" style="width:40px; height:40px; border-radius:50%; object-fit:cover; display:none;">"""
content = re.sub(search_mz_upload, replace_mz_upload, content, count=1)

# Update editUgur to show preview
search_edit_img = r"""        document.getElementById\('ug-img'\).value = u.img;"""
replace_edit_img = """        document.getElementById('ug-img').value = u.img;\n        const pv = document.getElementById('ug-img-preview'); if(u.img) { pv.src = u.img; pv.style.display='block'; } else { pv.style.display='none'; }"""
content = re.sub(search_edit_img, replace_edit_img, content, count=1)

# Update resetUgurForm to clear preview and uni
search_reset = r"""        document.getElementById\('ug-id'\).value = "";"""
replace_reset = """        document.getElementById('ug-id').value = "";\n        document.getElementById('ug-uni').value = "";\n        document.getElementById('ug-img-preview').style.display='none';"""
content = re.sub(search_reset, replace_reset, content, count=1)

# Update editMezun to show preview
search_edit_mz = r"""        document.getElementById\('mz-img'\).value = m.img;"""
replace_edit_mz = """        document.getElementById('mz-img').value = m.img;\n        const pv = document.getElementById('mz-img-preview'); if(m.img) { pv.src = m.img; pv.style.display='block'; } else { pv.style.display='none'; }"""
content = re.sub(search_edit_mz, replace_edit_mz, content, count=1)

# Update resetMezunForm to clear preview
search_reset_mz = r"""        document.getElementById\('mz-id'\).value = "";"""
replace_reset_mz = """        document.getElementById('mz-id').value = "";\n        document.getElementById('mz-img-preview').style.display='none';"""
content = re.sub(search_reset_mz, replace_reset_mz, content, count=1)

# Update uploadImage function to update preview if it exists
search_uploadImage = r"""        document.getElementById\(targetId\).value = fileUrl;"""
replace_uploadImage = """        document.getElementById(targetId).value = fileUrl;\n        const pv = document.getElementById(targetId + '-preview');\n        if(pv) { pv.src = fileUrl; pv.style.display='block'; }"""
content = re.sub(search_uploadImage, replace_uploadImage, content, count=1)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Modifications applied successfully")
