import os
import re

dir_path = "/Users/gazanfaryusifli/Downloads/Evrika"
files = [f for f in os.listdir(dir_path) if f.endswith(".html")]

for file in files:
    file_path = os.path.join(dir_path, file)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Pattern for Precise WhatsApp
    pattern1 = r'<!-- Precise WhatsApp Lead Tracker.*?</style>'
    # Pattern for Professional WhatsApp Chat Widget v2
    pattern2 = r'<!-- Professional WhatsApp Chat Widget v2.*?</style>'
    
    # Just in case there are missing comments, also try targeting by ID directly
    pattern3 = r'<div id="wa-precise-widget".*?</style>'
    pattern4 = r'<div id="wa-widget".*?</style>'

    new_content = re.sub(pattern1, '', content, flags=re.DOTALL)
    new_content = re.sub(pattern2, '', new_content, flags=re.DOTALL)
    new_content = re.sub(pattern3, '', new_content, flags=re.DOTALL)
    new_content = re.sub(pattern4, '', new_content, flags=re.DOTALL)

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Removed WA from {file}")

