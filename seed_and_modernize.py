import urllib.request
import json
import re

# 1. Seed Supabase
url = 'https://gziuhrlvagflokivfgwt.supabase.co/rest/v1/popups'
headers = {
    'apikey': 'sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP',
    'Authorization': 'Bearer sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP',
    'Content-Type': 'application/json',
    'Prefer': 'return=representation'
}
payload_data = {
    "payload": {
        "title": "Gələcəyin uğuru burada başlayır..",
        "img": "./assets/admission_popup.jpg",
        "link": "schools.html",
        "status": "active"
    }
}
req = urllib.request.Request(url, headers=headers, data=json.dumps(payload_data).encode('utf-8'))
try:
    with urllib.request.urlopen(req) as response:
        print("Seeded popup in Supabase.")
except Exception as e:
    print("Error seeding:", e)

# 2. Modernize admin.html UI
file = 'admin.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the panel divs with modernized ones
modern_panel_start = '<div class="panel" style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); padding: 25px;">'
modern_panel_list_start = '<div class="panel" style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); padding: 0; overflow: hidden;">'

content = content.replace(
    '<div class="panel" style="padding: 25px;">',
    modern_panel_start
)
content = content.replace(
    '<div class="panel" style="padding: 0;">',
    modern_panel_list_start
)

# Upgrade inputs
form_group_old = 'class="form-control"'
form_group_new = 'class="form-control" style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; color: white; padding: 12px; transition: all 0.3s ease;" onfocus="this.style.borderColor=\'var(--accent)\'" onblur="this.style.borderColor=\'rgba(255,255,255,0.1)\'"'

content = content.replace('id="popup-title" class="form-control"', f'id="popup-title" {form_group_new}')
content = content.replace('id="popup-link" class="form-control"', f'id="popup-link" {form_group_new}')
content = content.replace('id="popup-img" class="form-control"', f'id="popup-img" {form_group_new}')

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("UI modernized.")
