import requests, json
API_URL = 'https://miwvdhwrmxoetszkxlzy.supabase.co/rest/v1'
API_KEY = 'sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV'
HEADERS = { 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY, 'Content-Type': 'application/json' }

res = requests.get(f"{API_URL}/registrations?select=payload&limit=50", headers=HEADERS)
data = res.json()
epoint_keys = set()
for r in data:
    payload = r['payload']
    if isinstance(payload, str):
        try: payload = json.loads(payload)
        except: continue
    if isinstance(payload, dict):
        for k in payload.keys():
            if 'epoint' in k.lower() or 'card' in k.lower() or 'order' in k.lower() or 'amount' in k.lower() or 'tx' in k.lower():
                epoint_keys.add(k)
print("Keys:", epoint_keys)
