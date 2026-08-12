import requests
API_URL = 'https://gziuhrlvagflokivfgwt.supabase.co/rest/v1'
API_KEY = 'sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP'
HEADERS = { 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY }

# Try to list buckets
res = requests.get("https://gziuhrlvagflokivfgwt.supabase.co/storage/v1/bucket", headers=HEADERS)
print("Buckets:", res.status_code, res.text)
