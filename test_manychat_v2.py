import requests

def test_token(token):
    headers = {
        "Authorization": f"Bearer {token}",
        "accept": "application/json"
    }
    url = "https://api.manychat.com/fb/page/getInfo"
    response = requests.get(url, headers=headers)
    print(f"Token `{token}` üçün status: {response.status_code}")
    if response.status_code == 200:
        print("UĞURLU!")
        return True
    return False

if __name__ == "__main__":
    t1 = "9577574:c37988dafb8b2b24da662caa5452a397"
    t2 = "c37988dafb8b2b24da662caa5452a397"
    
    if not test_token(t1):
        test_token(t2)
