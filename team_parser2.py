import urllib.request
import re
import json

req = urllib.request.Request("https://www.evrikaliseyi.edu.az/", headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        
    members = []
    # Correct regex: aria-label comes first, then style="background-image: url(IMAGE)"
    matches = re.finditer(r'aria-label="([^"]+)".*?url\((https://files.cdn-files-a.com[^)]+)\)', html, re.IGNORECASE | re.DOTALL)
    for m in matches:
        members.append({"name": m.group(1).strip(), "image": m.group(2).strip()})
        
    print(json.dumps(members, indent=2, ensure_ascii=False))
except Exception as e:
    print(e)
