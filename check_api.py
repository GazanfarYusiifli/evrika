import urllib.request
import json

url = "https://miwvdhwrmxoetszkxlzy.supabase.co/rest/v1/management?select=*"
req = urllib.request.Request(url, headers={
    'apikey': 'sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV',
    'Authorization': 'Bearer sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV'
})

with urllib.request.urlopen(req) as response:
    data = json.loads(response.read())

for item in data:
    role = item.get('payload', {}).get('role', '')
    print(f"'{role}' (length: {len(role)})")
