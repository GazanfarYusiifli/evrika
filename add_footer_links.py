import glob

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if "privacy.html" not in content and "Məxfilik Siyasəti" in content:
        # replace the generic link
        content = content.replace(
            '<a href="#" style="color: rgba(255,255,255,0.3); text-decoration: none; font-size: 0.85rem; transition: 0.3s;">Məxfilik Siyasəti</a>',
            '<a href="privacy.html" style="color: rgba(255,255,255,0.3); text-decoration: none; font-size: 0.85rem; transition: 0.3s;">Məxfilik Siyasəti</a>\n                <a href="terms.html" style="color: rgba(255,255,255,0.3); text-decoration: none; font-size: 0.85rem; transition: 0.3s;">İstifadə Şərtləri</a>'
        )
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")

