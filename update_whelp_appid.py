import glob
import re

html_files = glob.glob('*.html')

# We'll completely replace the old Whelp block with the new one.
# Since the old block might have the mobile hack, we'll use regex to remove everything between <!-- Whelp Widget Code --> and the end of the script, then inject the new one.

new_whelp_block = """<!-- Whelp Widget Code -->
<script src="https://widget.whelp.co/app.js"></script>
<script type="text/javascript">
	Whelp("init", {
		app_id: "fdbc088cd36f5d0531bd6672933d00b2"
	});
	
	// Ensure Whelp doesn't auto open on mobile by intercepting its state
	if (window.innerWidth <= 768) {
	    // Poll and force close if it opens automatically without user interaction
	    let userClicked = false;
	    window.addEventListener('touchstart', (e) => { userClicked = true; }, {once: true});
	    let wTimer = setInterval(() => {
	        if (!userClicked && typeof Whelp === 'function') {
	            try { Whelp('close'); } catch(e) {}
	        } else if (userClicked) {
	            clearInterval(wTimer);
	        }
	    }, 300);
	    setTimeout(() => clearInterval(wTimer), 8000);
	}
</script>"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex to find the Whelp block and replace it
    pattern = r'<!-- Whelp Widget Code -->.*?</script>\s*</script>' 
    # Actually the previous block looks like:
    # <!-- Whelp Widget Code -->
    # <script src="https://widget.whelp.co/app.js"></script>
    # <script type="text/javascript">
    # 	Whelp("init", { ... }); ...
    # </script>
    
    pattern = r'<!-- Whelp Widget Code -->\s*<script src="https://widget\.whelp\.co/app\.js"></script>\s*<script type="text/javascript">.*?</script>'
    
    if re.search(pattern, content, flags=re.DOTALL):
        content = re.sub(pattern, new_whelp_block, content, flags=re.DOTALL)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
    else:
        print(f"Could not find Whelp block in {file}")

