import urllib.request
import json

url = 'https://osicmnagzeqkhwticiqp.supabase.co/rest/v1/parent_testimonials'
headers = {
    'apikey': 'sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE',
    'Authorization': 'Bearer sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE',
    'Content-Type': 'application/json',
    'Prefer': 'return=representation'
}

# 1. Delete existing
try:
    del_req = urllib.request.Request(url + '?id=gt.0', headers=headers, method='DELETE')
    urllib.request.urlopen(del_req)
except Exception as e:
    print("Delete error:", e)

# 2. Insert new
data = [
    {
        "payload": {
            "name": "Zaur İsmayılov",
            "status": "2019",
            "text": "Evrika Liseyini seçdiyimiz üçün çox məmnunuq. Burada uşaqlara həm savadlı təhsil verilir, həm də onların fərdi inkişafına xüsusi diqqət yetirilir. Müəllimlər çox qayğıkeş və peşəkardırlar. Övladım dərslərə marağı artıb, özünü daha rahat və inamlı hiss edir. Məktəbdə yaradılan təhlükəsiz və nizamlı mühit də valideyn olaraq bizi rahat edir.",
            "type": "text",
            "avatar": "assets/parents/zauraliyev.png"
        }
    },
    {
        "payload": {
            "name": "Şahbaz Xuduoğlu",
            "status": "Evrika Liseyi valideyni",
            "text": "Övladımızın təhsil və inkişafı üçün Evrika Liseyini seçdiyimiz üçün çox məmnunuq. Burada uşaqlara yalnız yüksək səviyyədə təhsil deyil, həm də onların fərdi inkişafına xüsusi diqqət göstərilir. Müəllimlərin peşəkarlığı və uşaqlara yanaşması bizi xüsusilə qane edir. Övladımızın dərslərə marağının artdığını və özünəinamının daha da gücləndiyini görürük. Evrika Liseyində yaradılan təhlükəsiz və sağlam mühit valideyn olaraq bizə böyük rahatlıq verir.",
            "type": "text",
            "avatar": "assets/parents/shahbaz.png"
        }
    }
]

req = urllib.request.Request(url, headers=headers, method='POST', data=json.dumps(data).encode('utf-8'))
try:
    with urllib.request.urlopen(req) as response:
        print("Inserted new parents.")
except Exception as e:
    print("Insert error:", e)
