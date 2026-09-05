import requests

OLD_URL = 'https://osicmnagzeqkhwticiqp.supabase.co/rest/v1'
OLD_KEY = 'sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE'

try:
    print("Fetching with 60s timeout...")
    res = requests.get(f"{OLD_URL}/registrations?select=*&limit=1", headers={'apikey': OLD_KEY, 'Authorization': f'Bearer {OLD_KEY}'}, timeout=60)
    print(res.status_code)
    print(res.text)
except Exception as e:
    print("Error:", e)
