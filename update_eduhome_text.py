import os

directory = '.'

for root, _, files in os.walk(directory):
    for filename in files:
        if filename.endswith('.html') or filename.endswith('.js'):
            filepath = os.path.join(root, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Simple replace
            if 'Eduhome Təhsil' in content:
                content = content.replace('Eduhome Təhsil', 'Eduhome Hazırlıq')
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated {filepath}")
