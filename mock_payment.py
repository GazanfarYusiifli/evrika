import requests
import json
import datetime

SUPABASE_URL = "https://miwvdhwrmxoetszkxlzy.supabase.co"
SUPABASE_KEY = "sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV"

payload = {
    "name": "TEST ŞAGİRD (Epoint Simulyasiya)",
    "phone": "+994501234567",
    "source": "Qeydiyyat - Lisey 1",
    "status": "Yeni",
    "payment_status": "Ödənilib",
    "amount": "0.01 AZN",
    "note": "Filial: EVRİKA Beynəlxalq | Bölmə: Azərbaycan | Sinif: 1-ci sinif | Ödəniş Məbləği: 0.01 AZN",
    "date": datetime.datetime.now().isoformat() + "Z",
    "epoint_amount": 0.01,
    "epoint_currency": "AZN",
    "epoint_card_number": "416973******0717",
    "epoint_card_type": "VISA",
    "epoint_bank": "Kapital Bank",
    "epoint_transaction": "TEST-TX-999888777",
    "epoint_rrn": "RRN-123456789",
    "epoint_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

url = f"{SUPABASE_URL}/rest/v1/registrations"
headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}

response = requests.post(url, headers=headers, json={"payload": payload})

if response.status_code in [200, 201]:
    print("Success! Simulated payment injected.")
    print(response.json())
else:
    print("Failed:")
    print(response.text)
