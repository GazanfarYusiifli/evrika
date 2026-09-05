import requests

API_URL = 'https://osicmnagzeqkhwticiqp.supabase.co/rest/v1'
API_KEY = 'sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE'
HEADERS = { 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY, 'Content-Type': 'application/json' }

res = requests.get(f"{API_URL}/registrations", headers=HEADERS)
data = res.json()
for row in data:
    print(f"ID: {row.get('id')} - Order: {row.get('order_id')} - Amount: {row.get('amount')}")
