import urllib.request
import json

url = 'https://gziuhrlvagflokivfgwt.supabase.co/rest/v1/partners?select=*'
headers = {
    'apikey': 'sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP',
    'Authorization': 'Bearer sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP'
}

req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        print(f"Partners Table Rows: {len(data)}")
        if len(data) > 0:
            print(data[0])
except Exception as e:
    print("Error:", e)
