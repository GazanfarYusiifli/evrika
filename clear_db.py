import requests
API_URL = 'https://gziuhrlvagflokivfgwt.supabase.co/rest/v1'
API_KEY = 'sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP'
HEADERS = { 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY }

tables = ['registrations', 'ugurlar', 'vacancies']
for t in tables:
    res = requests.delete(f"{API_URL}/{t}?id=not.is.null", headers=HEADERS)
    print(f"Deleted {t}: {res.status_code} {res.text}")
