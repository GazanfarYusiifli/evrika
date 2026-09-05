import urllib.request
import json
import re

# 1. Update index.html to render desc if present
file_index = 'index.html'
with open(file_index, 'r', encoding='utf-8') as f:
    content_idx = f.read()

old_popup_html = """<h2 class="welcome-modal-title">${p.title}</h2>
                      ${linkHTML}"""
new_popup_html = """<h2 class="welcome-modal-title">${p.title}</h2>
                      ${p.desc ? `<p class="welcome-modal-desc">${p.desc}</p>` : ''}
                      ${linkHTML}"""
if old_popup_html in content_idx:
    content_idx = content_idx.replace(old_popup_html, new_popup_html)
    with open(file_index, 'w', encoding='utf-8') as f:
        f.write(content_idx)

# 2. Update admin.html form and js
file_admin = 'admin.html'
with open(file_admin, 'r', encoding='utf-8') as f:
    content_adm = f.read()

old_form_input = '<input type="text" id="popup-title" placeholder="Başlıq (Məs: Qəbul Kampaniyası 2026)" required class="admin-input">'
new_form_input = '<input type="text" id="popup-title" placeholder="Başlıq (Məs: Qəbul Kampaniyası 2026)" required class="admin-input">\n              <input type="text" id="popup-desc" placeholder="Alt Yazı (Məs: 2026/27-ci tədris ili...)" class="admin-input">'

if old_form_input in content_adm:
    content_adm = content_adm.replace(old_form_input, new_form_input)

# JS edits
content_adm = content_adm.replace(
    "document.getElementById('popup-title').value = p.title || '';", 
    "document.getElementById('popup-title').value = p.title || '';\n        document.getElementById('popup-desc').value = p.desc || '';"
)

content_adm = content_adm.replace(
    "title: document.getElementById('popup-title').value,",
    "title: document.getElementById('popup-title').value,\n            desc: document.getElementById('popup-desc').value,"
)

with open(file_admin, 'w', encoding='utf-8') as f:
    f.write(content_adm)

# 3. Update Supabase data to include description for the current popup
# Find the active popup and patch it
url = 'https://osicmnagzeqkhwticiqp.supabase.co/rest/v1/popups?select=*'
headers = {
    'apikey': 'sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE',
    'Authorization': 'Bearer sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE',
    'Content-Type': 'application/json'
}
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        if len(data) > 0:
            popup_id = data[0]['id']
            payload = data[0]['payload']
            payload['desc'] = "2026/27-ci tədris ili üzrə şagird qəbulu davam edir."
            
            patch_url = f"https://osicmnagzeqkhwticiqp.supabase.co/rest/v1/popups?id=eq.{popup_id}"
            patch_data = {"payload": payload}
            patch_req = urllib.request.Request(patch_url, data=json.dumps(patch_data).encode('utf-8'), headers=headers, method='PATCH')
            urllib.request.urlopen(patch_req)
            print("Database patched with desc.")
except Exception as e:
    print("DB error:", e)

