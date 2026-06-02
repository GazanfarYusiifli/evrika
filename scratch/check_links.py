import os
from bs4 import BeautifulSoup

def check_links(file_path):
    print(f"Checking {file_path}...")
    with open(file_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if not href or href.startswith('http') or href.startswith('#') or href.startswith('tel:') or href.startswith('mailto:'):
            continue
        
        target = os.path.join(os.path.dirname(file_path), href)
        if not os.path.exists(target):
            print(f"  [BROKEN] {href} -> {target}")
        else:
            print(f"  [OK] {href}")

check_links('index.html')
check_links('about.html')
