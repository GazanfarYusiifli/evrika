import requests
import json

url = "https://miwvdhwrmxoetszkxlzy.supabase.co/rest/v1/mezunlar"
headers = {
    "apikey": "sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV",
    "Authorization": "Bearer sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV"
}

# Delete all IDs from 159 to 178
for i in range(159, 179):
    res = requests.delete(f"{url}?id=eq.{i}", headers=headers)
    print(f"Deleted ID {i}: {res.status_code}")
