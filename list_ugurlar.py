import requests

API_URL = 'https://gziuhrlvagflokivfgwt.supabase.co/rest/v1'
API_KEY = 'sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP'
HEADERS = { 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY, 'Content-Type': 'application/json' }

# Fetch all ugurlar
res = requests.get(f"{API_URL}/ugurlar", headers=HEADERS)
if res.status_code == 200:
    data = res.json()
    print(f"Total entries: {len(data)}")
    for row in data:
        payload = row.get('payload', {})
        name = payload.get('name', '')
        uni = payload.get('uni', '')
        print(f"ID: {row['id']} | Name: {name} | Uni: {uni}")
else:
    print(f"Failed to fetch data: {res.text}")
