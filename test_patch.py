import requests

SUPABASE_URL = "https://miwvdhwrmxoetszkxlzy.supabase.co"
SUPABASE_KEY = "sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV"
url = f"{SUPABASE_URL}/rest/v1/registrations?id=eq.259"
headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

res = requests.patch(url, headers=headers, json={"payload": {"status": "Yeni"}})
print(res.status_code)
print(res.text)
