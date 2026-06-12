import requests, json
API_URL = 'https://miwvdhwrmxoetszkxlzy.supabase.co/rest/v1'
API_KEY = 'sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV'
HEADERS = { 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY, 'Content-Type': 'application/json' }

# Just checking count to see how many we have
res = requests.get(f"{API_URL}/registrations?select=id", headers=HEADERS)
print("Total rows:", len(res.json()))
