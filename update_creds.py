import os
import glob

OLD_URL = 'gziuhrlvagflokivfgwt'
NEW_URL = 'gziuhrlvagflokivfgwt'

OLD_KEY = 'sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE'
NEW_KEY = 'sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE'

def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        return # Skip binary files

    if OLD_URL in content or OLD_KEY in content:
        content = content.replace(OLD_URL, NEW_URL)
        content = content.replace(OLD_KEY, NEW_KEY)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

for root, dirs, files in os.walk('.'):
    if '.git' in dirs:
        dirs.remove('.git')
    if 'node_modules' in dirs:
        dirs.remove('node_modules')
    if '.next' in dirs:
        dirs.remove('.next')
    if 'dist' in dirs:
        dirs.remove('dist')
    
    for file in files:
        if file.endswith(('.js', '.cjs', '.html', '.py', '.txt', '.json')):
            filepath = os.path.join(root, file)
            replace_in_file(filepath)

print("Done replacing credentials.")
