import requests

API_URL = 'https://miwvdhwrmxoetszkxlzy.supabase.co/rest/v1'
API_KEY = 'sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV'
HEADERS = {
    'apikey': API_KEY,
    'Authorization': 'Bearer ' + API_KEY,
    'Content-Type': 'application/json'
}

res = requests.get(f"{API_URL}/registrations?limit=1", headers=HEADERS)
data = res.json()
if data:
    id = data[0]['id']
    payload = data[0]['payload']
    
    # Try updating status just like admin.html does
    payload['status'] = 'Baxılıb'
    
    patch_res = requests.patch(
        f"{API_URL}/registrations?id=eq.{id}",
        headers=HEADERS,
        json={"payload": payload}
    )
    print("PATCH Status:", patch_res.status_code)
    print("PATCH Text:", patch_res.text)
    
    get_res = requests.get(f"{API_URL}/registrations?id=eq.{id}", headers=HEADERS)
    print("GET after PATCH:", get_res.json())

