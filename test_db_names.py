import requests

API_URL = 'https://osicmnagzeqkhwticiqp.supabase.co/rest/v1'
API_KEY = 'sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE'
HEADERS = { 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY, 'Content-Type': 'application/json' }

res = requests.get(f"{API_URL}/ugurlar", headers=HEADERS)
if res.status_code == 200:
    for row in res.json():
        print(f"ID: {row['id']} | name: {row.get('payload', {}).get('name')}")
else:
    print(f"Error: {res.text}")
