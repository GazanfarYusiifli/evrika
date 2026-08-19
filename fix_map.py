import re

file = 'contact.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Using regex to capture the entire object for "Eduhome & Zümrüd Club"
pattern = r'\{\s*name:\s*"Eduhome & Zümrüd Club",\s*shortName:\s*"Eduhome / Zümrüd",\s*label:\s*"Təhsil və Sağlamlıq",\s*coords:\s*\[40\.398059,\s*49\.862709\],\s*icon:\s*"fa-star"\s*\}'

replacement = """{ 
              name: "Victory Colleges by Evrika", 
              shortName: "Victory Colleges",
              label: "Təhsil Mərkəzi",
              coords: [40.398059, 49.862709],
              icon: "fa-graduation-cap"
            },
            { 
              name: "Zümrüd Club", 
              shortName: "Zümrüd Club",
              label: "İdman və Sağlamlıq",
              coords: [40.398200, 49.862800],
              icon: "fa-heartbeat"
            }"""

if re.search(pattern, content):
    content = re.sub(pattern, replacement, content)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Map updated.")
else:
    print("Pattern not found!")

