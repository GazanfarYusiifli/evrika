import urllib.request
import json

url = "https://gziuhrlvagflokivfgwt.supabase.co/rest/v1/management?select=*"
req = urllib.request.Request(url, headers={
    'apikey': 'sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP',
    'Authorization': 'Bearer sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP'
})

with urllib.request.urlopen(req) as response:
    data = json.loads(response.read())

for item in data:
    role = item.get('payload', {}).get('role', '')
    print(f"'{role}' (length: {len(role)})")
