import urllib.request
import os

base_url = "https://evrika-phi.vercel.app/"
pages = [
    "index.html", "about.html", "contact.html", "schools.html", "lisey.html", 
    "lisey2.html", "montessori.html", "victory.html", "zumrud.html", "news.html", 
    "news-detail.html", "alumni.html", "achievements.html", "vacancy.html", 
    "crm.html", "management.html", "mission.html", "privacy.html", "terms.html", 
    "cookies.html", "payment.html", "branches.html", "ptim.html", "pthim.html",
    "jurnal.html", "register-lisey1.html", "register-lisey2.html", 
    "register-montessori.html", "register-victory.html", "register-zumrud.html"
]

for page in pages:
    try:
        url = base_url + page
        print(f"Downloading {page}...")
        urllib.request.urlretrieve(url, f"live_vercel_code/{page}")
    except Exception as e:
        print(f"Failed to download {page}: {e}")

print("Bütün canlı səhifələr live_vercel_code qovluğuna yükləndi!")
