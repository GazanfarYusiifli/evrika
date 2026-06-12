import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the Eduhome Hazırlıq navbar item
    if 'Eduhome Hazırlıq' in content:
        content = content.replace('Eduhome Hazırlıq', 'Victory Colleges by Evrika')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")

print("Navbar replacements done.")
