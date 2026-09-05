import requests
import json

API_URL = 'https://osicmnagzeqkhwticiqp.supabase.co/rest/v1'
API_KEY = 'sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE'
HEADERS = {
    'apikey': API_KEY,
    'Authorization': 'Bearer ' + API_KEY,
    'Content-Type': 'application/json',
    'Prefer': 'return=representation'
}

res = requests.get(f"{API_URL}/registrations?limit=1", headers=HEADERS)
data = res.json()
print("GET Data:", data)

if data:
    id = data[0]['id']
    payload = data[0]['payload']
    payload['qr_scanned'] = True
    
    print("Trying to update ID:", id)
    patch_res = requests.patch(
        f"{API_URL}/registrations?id=eq.{id}",
        headers=HEADERS,
        json={"payload": payload}
    )
    print("PATCH Status:", patch_res.status_code)
    print("PATCH Response:", patch_res.text)

