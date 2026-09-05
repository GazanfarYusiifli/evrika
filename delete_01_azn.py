import requests

API_URL = 'https://osicmnagzeqkhwticiqp.supabase.co/rest/v1'
API_KEY = 'sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE'
HEADERS = { 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY, 'Content-Type': 'application/json' }

# Fetch all registrations
res = requests.get(f"{API_URL}/registrations", headers=HEADERS)
if res.status_code == 200:
    data = res.json()
    to_delete = []
    print(f"Total entries: {len(data)}")
    for row in data:
        amount = row.get('amount')
        order_id = row.get('order_id', '')
        # Delete if amount is 0.01, OR if order_id is among the ones listed (EV-0020 down to EV-0001)
        if str(amount) == "0.01" or order_id in [f"EV-{str(i).zfill(4)}" for i in range(1, 21)]:
            to_delete.append(row['id'])
    
    print(f"Found {len(to_delete)} entries to delete.")
    
    for rid in to_delete:
        delete_res = requests.delete(f"{API_URL}/registrations?id=eq.{rid}", headers=HEADERS)
        if delete_res.status_code == 204:
            print(f"Deleted {rid}")
        else:
            print(f"Failed to delete {rid}: {delete_res.text}")
else:
    print(f"Failed to fetch data: {res.text}")
