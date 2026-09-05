import requests
import json

url = "https://osicmnagzeqkhwticiqp.supabase.co/rest/v1/ugurlar"
headers = {
    "apikey": "sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE",
    "Authorization": "Bearer sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE",
    "Content-Type": "application/json"
}

images = ["ugur1.jpeg", "ugur2.jpeg", "ugur3.jpeg", "ugur4.jpeg", "ugur5.jpeg", "ugur6.jpeg", "ugur7.jpeg"]

for img in images:
    payload = {
        "payload": {
            "name": "Evrika Uğurları",
            "uni": "",
            "img": img
        }
    }
    res = requests.post(url, headers=headers, json=payload)
    print(f"Added {img}: {res.status_code}")

