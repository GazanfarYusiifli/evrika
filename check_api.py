import urllib.request
import json

url = "https://osicmnagzeqkhwticiqp.supabase.co/rest/v1/management?select=*"
req = urllib.request.Request(url, headers={
    'apikey': 'sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE',
    'Authorization': 'Bearer sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE'
})

with urllib.request.urlopen(req) as response:
    data = json.loads(response.read())

for item in data:
    role = item.get('payload', {}).get('role', '')
    print(f"'{role}' (length: {len(role)})")
