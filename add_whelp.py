import os
import glob

widget_code = """
<!-- Whelp Widget Code -->
<script src="https://widget.whelp.co/app.js"></script>
<script type="text/javascript">
	Whelp("init", {
		app_id: "6880c82727fd01e5dc2bdcc4f78237cb"
	});
</script>
<!-- Whelp Widget Code -->
"""

# Find all HTML files in the directory
files = glob.glob('*.html')

exclude = ['admin.html', 'admin-passwords.html', 'crm.html', 'error.html', 'payment.html']

for file in files:
    if file in exclude:
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Avoid duplicating the widget
    if 'widget.whelp.co' in content:
        print(f"Skipping {file} - already has widget")
        continue

    # Insert right before </body>
    if '</body>' in content:
        content = content.replace('</body>', f"{widget_code}\n</body>")
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added to {file}")

print("Done.")
