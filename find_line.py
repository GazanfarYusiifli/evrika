import re

with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if re.search(r'mobil', line, re.IGNORECASE):
        print(f"Line {i+1}: {line.strip()[:100]}")
