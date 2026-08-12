import requests
import json

url = "https://gziuhrlvagflokivfgwt.supabase.co/rest/v1/mezunlar"
headers = {
    "apikey": "sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP",
    "Authorization": "Bearer sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP"
}

# Delete all IDs from 159 to 178
for i in range(159, 179):
    res = requests.delete(f"{url}?id=eq.{i}", headers=headers)
    print(f"Deleted ID {i}: {res.status_code}")
