import requests
API_URL = 'https://miwvdhwrmxoetszkxlzy.supabase.co/rest/v1'
API_KEY = 'sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV'
HEADERS = { 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY }

# Try to list buckets
res = requests.get("https://miwvdhwrmxoetszkxlzy.supabase.co/storage/v1/bucket", headers=HEADERS)
print("Buckets:", res.status_code, res.text)
