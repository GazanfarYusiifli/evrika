import urllib.request
import re
import json

req = urllib.request.Request("https://www.evrikaliseyi.edu.az/", headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        
    members = []
    # Try to find all team member divs
    matches = re.finditer(r'url\((https://files.cdn-files-a.com[^)]+)\).*?aria-label="([^"]+)"', html, re.IGNORECASE | re.DOTALL)
    for m in matches:
        members.append({"name": m.group(2).strip(), "image": m.group(1).strip()})
        
    # Also check if img tags are used
    img_matches = re.finditer(r'<img[^>]*src="([^"]+)"[^>]*alt="([^"]+)"', html, re.IGNORECASE | re.DOTALL)
    for m in img_matches:
        members.append({"name": m.group(2).strip(), "image": m.group(1).strip()})
        
    print(json.dumps(members, indent=2, ensure_ascii=False))
except Exception as e:
    print(e)
