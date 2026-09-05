import urllib.request
import json

url = 'https://osicmnagzeqkhwticiqp.supabase.co/rest/v1/popups?select=*&order=id.desc'
headers = {
    'apikey': 'sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE',
    'Authorization': 'Bearer sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE'
}

req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        print(f"Rows: {len(data)}")
        if len(data) > 0:
            print(data[0])
except Exception as e:
    print("Error:", e)
