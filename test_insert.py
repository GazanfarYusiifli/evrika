import requests
API_URL = 'https://miwvdhwrmxoetszkxlzy.supabase.co/rest/v1'
API_KEY = 'sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV'
HEADERS = {
    'apikey': API_KEY,
    'Authorization': 'Bearer ' + API_KEY,
    'Content-Type': 'application/json',
    'Prefer': 'return=representation'
}

# Try inserting
res = requests.post(
    f"{API_URL}/registrations",
    headers=HEADERS,
    json={"payload": {"is_scan_log": True, "scanned_id": 10}}
)
print("POST Status:", res.status_code)
print("POST Data:", res.text)

# Try fetching it
res_get = requests.get(
    f"{API_URL}/registrations?payload->>is_scan_log=eq.true&payload->>scanned_id=eq.10",
    headers=HEADERS
)
print("GET Data:", res_get.text)

