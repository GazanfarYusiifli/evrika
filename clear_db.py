import requests
API_URL = 'https://miwvdhwrmxoetszkxlzy.supabase.co/rest/v1'
API_KEY = 'sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV'
HEADERS = { 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY }

tables = ['registrations', 'ugurlar', 'vacancies']
for t in tables:
    res = requests.delete(f"{API_URL}/{t}?id=not.is.null", headers=HEADERS)
    print(f"Deleted {t}: {res.status_code} {res.text}")
