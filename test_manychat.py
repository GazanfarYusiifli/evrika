import requests

MANYCHAT_API_KEY = "9577574:c37988dafb8b2b24da662caa5452a397"
HEADERS = {
    "Authorization": f"Bearer {MANYCHAT_API_KEY}",
    "accept": "application/json"
}

def check_manychat_connection():
    url = "https://api.manychat.com/fb/page/getInfo"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        print("ManyChat Bağlantısı Uğurludur!")
        print("Səhifə Məlumatı:", response.json().get('data', {}).get('name'))
    else:
        print("Xəta:", response.status_code, response.text)

if __name__ == "__main__":
    check_manychat_connection()
