import requests

API_URL = 'https://gziuhrlvagflokivfgwt.supabase.co/rest/v1'
API_KEY = 'sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP'
HEADERS = { 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY, 'Content-Type': 'application/json' }

res = requests.get(f"{API_URL}/ugurlar?limit=2", headers=HEADERS)
if res.status_code == 200:
    for row in res.json():
        print(row.get('payload', {}).get('img'))
else:
    print(f"Error: {res.text}")
