import os
import glob

# Search in HTML, JS, PY, JSON
patterns = ['*.html', '*.js', '*.py', '*.json', 'live_vercel_code/*.html']
files = []
for p in patterns:
    files.extend(glob.glob(p))
files = list(set(files))

for file in files:
    if os.path.isfile(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replacements
        new_content = content.replace('victory.html', 'victory.html')
        new_content = new_content.replace('register-victory.html', 'register-victory.html')
        
        # Only rewrite if changes were made
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file}")

print("Done replacing filenames.")
