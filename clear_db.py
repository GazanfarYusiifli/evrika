import requests
API_URL = 'https://osicmnagzeqkhwticiqp.supabase.co/rest/v1'
API_KEY = 'sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE'
HEADERS = { 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY }

tables = ['registrations', 'ugurlar', 'vacancies']
for t in tables:
    res = requests.delete(f"{API_URL}/{t}?id=not.is.null", headers=HEADERS)
    print(f"Deleted {t}: {res.status_code} {res.text}")
