import os
import glob

# Find all HTML files
html_files = glob.glob('*.html')

old_whelp = """	Whelp("init", {
		app_id: "6880c82727fd01e5dc2bdcc4f78237cb"
	});"""

new_whelp = """	Whelp("init", {
		app_id: "6880c82727fd01e5dc2bdcc4f78237cb"
	});
	// Mobil ekranda avtomatik açılmanın qarşısını almaq üçün (JS üsulu)
	if (window.innerWidth < 768) {
		let wCount = 0;
		let wTimer = setInterval(() => {
			if (typeof Whelp === 'function') { Whelp('close'); }
			if (++wCount > 10) clearInterval(wTimer);
		}, 500);
	}"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_whelp in content:
        content = content.replace(old_whelp, new_whelp)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")

