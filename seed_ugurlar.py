import urllib.request
import json

ugurlar = [
    { "payload": { "name": "Evrika Uğurları", "uni": "", "img": "./assets/ugur1.jpeg" } },
    { "payload": { "name": "Evrika Uğurları", "uni": "", "img": "https://osicmnagzeqkhwticiqp.supabase.co/storage/v1/object/public/ems-documents/uploads/1783333509288_0_WhatsApp_Image_2026-07-06_at_12.56.19.jpeg" } },
    { "payload": { "name": "Evrika Uğurları", "uni": "", "img": "https://osicmnagzeqkhwticiqp.supabase.co/storage/v1/object/public/ems-documents/uploads/1783333448814_0_WhatsApp_Image_2026-07-06_at_12.56.20.jpeg" } },
    { "payload": { "name": "Evrika Uğurları", "uni": "", "img": "./assets/ugur2.jpeg" } },
    { "payload": { "name": "Evrika Uğurları", "uni": "", "img": "./assets/ugur3.jpeg" } },
    { "payload": { "name": "Evrika Uğurları", "uni": "", "img": "./assets/ugur4.jpeg" } },
    { "payload": { "name": "Evrika Uğurları", "uni": "", "img": "./assets/ugur5.jpeg" } },
    { "payload": { "name": "Evrika Uğurları", "uni": "", "img": "./assets/ugur6.jpeg" } },
    { "payload": { "name": "Evrika Uğurları", "uni": "", "img": "./assets/ugur7.jpeg" } }
]

url = 'https://osicmnagzeqkhwticiqp.supabase.co/rest/v1/ugurlar'
headers = {
    'apikey': 'sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE',
    'Authorization': 'Bearer sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE',
    'Content-Type': 'application/json',
    'Prefer': 'return=representation'
}

req = urllib.request.Request(url, headers=headers, data=json.dumps(ugurlar).encode('utf-8'))
try:
    with urllib.request.urlopen(req) as response:
        print("Seeded ugurlar in Supabase.")
except Exception as e:
    print("Error seeding:", e)
    if hasattr(e, 'read'):
        print(e.read().decode())
