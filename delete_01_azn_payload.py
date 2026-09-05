import requests

API_URL = 'https://osicmnagzeqkhwticiqp.supabase.co/rest/v1'
API_KEY = 'sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE'
HEADERS = { 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY, 'Content-Type': 'application/json' }

# Fetch all registrations
res = requests.get(f"{API_URL}/registrations", headers=HEADERS)
if res.status_code == 200:
    data = res.json()
    to_delete = []
    for row in data:
        payload = row.get('payload', {})
        amount = str(payload.get('amount', ''))
        
        if '0.01' in amount:
            to_delete.append(row['id'])
            print(f"Queueing ID {row['id']} for deletion. Amount: {amount}")
    
    print(f"Found {len(to_delete)} entries to delete.")
    
    for rid in to_delete:
        delete_res = requests.delete(f"{API_URL}/registrations?id=eq.{rid}", headers=HEADERS)
        if delete_res.status_code == 204:
            print(f"Deleted {rid}")
        else:
            print(f"Failed to delete {rid}: {delete_res.text}")
else:
    print(f"Failed to fetch data: {res.text}")
