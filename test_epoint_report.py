import requests, json, base64, hashlib
pub = "i000201608"
pvt = "HNIbtyFLu3PbxXlVykJEwOR1"

endpoints = [
    "https://epoint.az/api/1/get-transactions",
    "https://epoint.az/api/1/report",
    "https://epoint.az/api/1/transactions"
]

data_obj = {"public_key": pub, "date_from": "2026-06-01", "date_to": "2026-06-11"}
data_json = json.dumps(data_obj)
data_b64 = base64.b64encode(data_json.encode('utf-8')).decode('utf-8')
sign_string = pvt + data_b64 + pvt
signature = base64.b64encode(hashlib.sha1(sign_string.encode('utf-8')).digest()).decode('utf-8')

for ep in endpoints:
    res = requests.post(ep, data={"data": data_b64, "signature": signature})
    print(f"{ep}: {res.status_code}")
    print(res.text[:200])
