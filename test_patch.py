import requests, json
API_URL = 'https://miwvdhwrmxoetszkxlzy.supabase.co/rest/v1'
API_KEY = 'sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV'
HEADERS = { 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY, 'Content-Type': 'application/json' }

# get id 10
res = requests.get(f"{API_URL}/registrations?id=eq.10", headers=HEADERS)
row = res.json()[0]
print("Before:", row['payload']['status'])

# update status to 'Baxılıb'
payload = row['payload']
payload['status'] = 'Baxılıb'
res2 = requests.patch(f"{API_URL}/registrations?id=eq.10", headers=HEADERS, json={"payload": payload})
print("Patch status:", res2.status_code, res2.text)

res3 = requests.get(f"{API_URL}/registrations?id=eq.10", headers=HEADERS)
row3 = res3.json()[0]
print("After:", row3['payload']['status'])
