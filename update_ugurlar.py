import re

file = 'admin.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Form changes
search_form = r"""              <input type="hidden" id="ug-id">
              <input type="text" id="ug-name" placeholder="Ad Soyad" required class="admin-input">
              <input type="text" id="ug-uni" placeholder="Nailiyyət \(Məs: Respublika Birincisi\)" required class="admin-input">"""
replace_form = """              <input type="hidden" id="ug-id">
              <input type="number" id="ug-seq" placeholder="Ardıcıllıq (Məs: 1)" required class="admin-input">"""
content = re.sub(search_form, replace_form, content, count=1)

# Table headers changes
search_th = r"""            <table><thead><tr><th>Şəkil</th><th>Ad Soyad</th><th>Nailiyyət</th><th>Əməliyyat</th></tr></thead><tbody id="ug-tbody"></tbody></table>"""
replace_th = """            <table><thead><tr><th>Sıra</th><th>Şəkil</th><th>Əməliyyat</th></tr></thead><tbody id="ug-tbody"></tbody></table>"""
content = re.sub(search_th, replace_th, content, count=1)

# Table row changes
search_tr = r"""const tb = document.getElementById\('ug-tbody'\); if\(tb\) tb.innerHTML = ugurlarData.map\(\(u, i\) => `<tr><td><img src="\$\{u.img\}" style="width:40px;height:40px;object-fit:cover;border-radius:8px;"></td><td>\$\{u.name\}</td><td>\$\{u.uni\}</td><td><div style="display:flex; gap:8px;"><button class="btn-view" style="padding:8px 12px; background:rgba\(255,255,255,0.05\);" onclick="editUgur\(\$\{i\}\)"><i class="fas fa-edit"></i></button><button class="btn-danger" style="padding:8px 12px;" onclick="deleteUgur\('\$\{u._db_id_\}'\)"><i class="fas fa-trash"></i></button></div></td></tr>`\).join\(''\);"""
replace_tr = """const tb = document.getElementById('ug-tbody'); if(tb) {
          ugurlarData.sort((a,b) => (parseInt(a.seq)||0) - (parseInt(b.seq)||0));
          tb.innerHTML = ugurlarData.map((u, i) => `<tr><td>${u.seq || 0}</td><td><img src="${u.img}" style="width:100px;height:auto;object-fit:cover;border-radius:8px;"></td><td><div style="display:flex; gap:8px;"><button class="btn-view" style="padding:8px 12px; background:rgba(255,255,255,0.05);" onclick="editUgur(${i})"><i class="fas fa-edit"></i></button><button class="btn-danger" style="padding:8px 12px;" onclick="deleteUgur('${u._db_id_}')"><i class="fas fa-trash"></i></button></div></td></tr>`).join('');
      }"""
content = re.sub(search_tr, replace_tr, content, count=1)

# JS handleUgurSubmit
search_submit = r"""        const payload = \{ 
            name: document.getElementById\('ug-name'\).value, 
            uni: document.getElementById\('ug-uni'\).value, 
            detail: "",
            img: document.getElementById\('ug-img'\).value 
        \};"""
replace_submit = """        const payload = { 
            seq: parseInt(document.getElementById('ug-seq').value) || 0,
            img: document.getElementById('ug-img').value 
        };"""
content = re.sub(search_submit, replace_submit, content, count=1)

# JS editUgur
search_edit = r"""        document.getElementById\('ug-id'\).value = u._db_id_;
        document.getElementById\('ug-name'\).value = u.name;
        document.getElementById\('ug-uni'\).value = u.uni || '';"""
replace_edit = """        document.getElementById('ug-id').value = u._db_id_;
        document.getElementById('ug-seq').value = u.seq || 0;"""
content = re.sub(search_edit, replace_edit, content, count=1)

# JS resetUgurForm
search_reset = r"""        document.getElementById\('ug-id'\).value = "";
        document.getElementById\('ug-uni'\).value = "";"""
replace_reset = """        document.getElementById('ug-id').value = "";
        document.getElementById('ug-seq').value = "";"""
content = re.sub(search_reset, replace_reset, content, count=1)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("admin.html updated successfully")
