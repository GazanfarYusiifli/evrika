import requests
API_URL = 'https://osicmnagzeqkhwticiqp.supabase.co/rest/v1'
API_KEY = 'sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE'
HEADERS = { 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY }

# Try to list buckets
res = requests.get("https://osicmnagzeqkhwticiqp.supabase.co/storage/v1/bucket", headers=HEADERS)
print("Buckets:", res.status_code, res.text)
