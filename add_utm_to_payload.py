import glob
import re

html_files = glob.glob('register-*.html')

# We look for `var payloadData = {` or `const payloadData = {`
# and we add the UTM fields inside it.

utm_fields = """
                utm_source: sessionStorage.getItem('utm_source') || "",
                utm_medium: sessionStorage.getItem('utm_medium') || "",
                utm_campaign: sessionStorage.getItem('utm_campaign') || "",
                utm_term: sessionStorage.getItem('utm_term') || "",
                utm_content: sessionStorage.getItem('utm_content') || "","""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    if "sessionStorage.getItem('utm_source')" in content:
        continue

    # Using regex to insert fields after the opening brace of payloadData
    pattern = r'(payloadData\s*=\s*\{)'
    
    if re.search(pattern, content):
        content = re.sub(pattern, r'\1' + utm_fields, content)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added UTM fields to {file}")
    else:
        print(f"Could not find payloadData in {file}")

