import os
import requests
import json
import re

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('([0-9]+)', s)]

url = "https://miwvdhwrmxoetszkxlzy.supabase.co/rest/v1/mezunlar"
headers = {
    "apikey": "sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV",
    "Authorization": "Bearer sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV",
    "Content-Type": "application/json"
}

# The images are in assets/mezunlar/
# Path should be relative for the web page: 'assets/mezunlar/filename'
dir_path = "/Users/gazanfaryusifli/Downloads/EvrikaProje/assets/mezunlar"
images = [f for f in os.listdir(dir_path) if f.startswith("mezun_")]
images.sort(key=natural_sort_key, reverse=True) # Reverse so mezun_1 gets inserted last, and thus gets highest ID (if ordered desc)

for img in images:
    # Use relative path in the db
    img_path = f"assets/mezunlar/{img}"
    payload = {
        "payload": {
            "name": "Evrika Məzunu",
            "uni": "",
            "img": img_path
        }
    }
    res = requests.post(url, headers=headers, json=payload)
    print(f"Added {img}: {res.status_code}")
