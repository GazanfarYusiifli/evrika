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
        print("UĞURLU! Səhifə:", response.json().get('data', {}).get('name'))
        return True
    return False

if __name__ == "__main__":
    t_new = "9577574:de10e18a60b17e63ac46d92f5236b37e"
    t_part = "de10e18a60b17e63ac46d92f5236b37e"
    
    if not test_token(t_new):
        test_token(t_part)
