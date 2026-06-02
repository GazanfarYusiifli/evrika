import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

target_string = 'span style="color: rgba(255,255,255,0.7); font-weight: 800; font-size: 1.2rem; letter-spacing: 0.1em;">&nbsp;</span>'
replacement_string = 'span style="color: rgba(255,255,255,0.7); font-weight: 800; font-size: 1.2rem; letter-spacing: 0.1em;">(+994) 12 525 10 10</span>'

for f_name in html_files:
    with open(f_name, "r", encoding="utf-8") as f:
        content = f.read()
    
    if target_string in content:
        content = content.replace(target_string, replacement_string)
        with open(f_name, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {f_name}")

