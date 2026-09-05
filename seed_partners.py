import urllib.request
import json

partners = [
    { "payload": { "name": 'TEDx', "logo_url": 'assets/partners/tedx.jpg', "description": '', "sort_order": 1 } },
    { "payload": { "name": 'Cambridge', "logo_url": 'assets/partners/cambridge.png', "description": '', "sort_order": 2 } },
    { "payload": { "name": 'AP', "logo_url": 'assets/partners/ap.jpg', "description": '', "sort_order": 3 } },
    { "payload": { "name": 'EC IS', "logo_url": 'assets/partners/ecis.png', "description": '', "sort_order": 4 } },
    { "payload": { "name": 'APEIA', "logo_url": 'assets/partners/aotmalogo.png', "description": '', "sort_order": 5 } },
    { "payload": { "name": 'Elm və Təhsil Nazirliyi', "logo_url": 'assets/partners/tehsilnazirliyi.png', "description": '', "sort_order": 6 } }
]

url = 'https://osicmnagzeqkhwticiqp.supabase.co/rest/v1/partners'
headers = {
    'apikey': 'sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE',
    'Authorization': 'Bearer sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE',
    'Content-Type': 'application/json',
    'Prefer': 'return=representation'
}

req = urllib.request.Request(url, headers=headers, data=json.dumps(partners).encode('utf-8'))
try:
    with urllib.request.urlopen(req) as response:
        print("Seeded partners in Supabase.")
except Exception as e:
    print("Error seeding:", e)
