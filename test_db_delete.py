import requests, json
API_URL = 'https://osicmnagzeqkhwticiqp.supabase.co/rest/v1'
API_KEY = 'sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE'
HEADERS = { 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY, 'Content-Type': 'application/json' }

# Just checking count to see how many we have
res = requests.get(f"{API_URL}/registrations?select=id", headers=HEADERS)
print("Total rows:", len(res.json()))
