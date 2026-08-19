import requests

API_URL = 'https://gziuhrlvagflokivfgwt.supabase.co/rest/v1'
API_KEY = 'sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP'
HEADERS = { 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY, 'Content-Type': 'application/json' }

# Delete ID 1
delete_res = requests.delete(f"{API_URL}/ugurlar?id=eq.1", headers=HEADERS)
if delete_res.status_code == 204:
    print("Deleted ID 1 successfully.")
else:
    print(f"Failed to delete: {delete_res.text}")
