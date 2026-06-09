import os
import glob

patterns = ['*.html', '*.json', 'live_vercel_code/*.html']
files = []
for p in patterns:
    files.extend(glob.glob(p))
files = list(set(files))

# We only want to replace visible text, so we'll be careful.
# 'Eduhome Hazırlıq' -> 'Victory Colleges'
# 'Eduhome' -> 'Victory Colleges'

for file in files:
    if os.path.isfile(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Don't touch admin.html or victory.html or register-victory.html since we already tailored them
        if file in ['admin.html', 'victory.html', 'register-victory.html']:
            continue

        new_content = content.replace('Eduhome Hazırlıq Mərkəzi', 'Victory Colleges by Evrika')
        new_content = new_content.replace('Eduhome Hazırlıq', 'Victory Colleges')
        new_content = new_content.replace('>Eduhome<', '>Victory Colleges<')
        new_content = new_content.replace('"Eduhome"', '"Victory Colleges"')
        
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated texts in {file}")

print("Done replacing texts.")
