import requests
import json
import time

OLD_URL = 'https://osicmnagzeqkhwticiqp.supabase.co/rest/v1'
OLD_KEY = 'sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE'

NEW_URL = 'https://osicmnagzeqkhwticiqp.supabase.co/rest/v1'
NEW_KEY = 'sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE'

TABLES = ['registrations', 'news', 'ugurlar', 'partners', 'vacancies']

def migrate():
    for table in TABLES:
        print(f"Fetching {table}...")
        headers_old = {
            'apikey': OLD_KEY,
            'Authorization': f'Bearer {OLD_KEY}'
        }
        res = requests.get(f"{OLD_URL}/{table}?select=*", headers=headers_old, timeout=10)
        if not res.ok:
            print(f"Failed to fetch {table}: {res.status_code}")
            continue
        
        data = res.json()
        print(f"Found {len(data)} rows in {table}.")
        if not data:
            continue
        
        print(f"Inserting {len(data)} rows into new {table}...")
        headers_new = {
            'apikey': NEW_KEY,
            'Authorization': f'Bearer {NEW_KEY}',
            'Content-Type': 'application/json',
            'Prefer': 'return=minimal'
        }
        
        # Batch insert
        for i in range(0, len(data), 50):
            batch = data[i:i+50]
            r = requests.post(f"{NEW_URL}/{table}", json=batch, headers=headers_new)
            if not r.ok:
                print(f"Warning inserting {table}: {r.status_code} {r.text}")
            else:
                print(f"Inserted batch {i//50 + 1} for {table}")

if __name__ == '__main__':
    migrate()
