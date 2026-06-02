import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for f_name in html_files:
    with open(f_name, "r", encoding="utf-8") as f:
        content = f.read()

    # We want to change things like:
    # .nav-links, .nav-actions { display: none !important; }
    # to .nav-links { display: none !important; }
    
    content = content.replace(".nav-links, .nav-actions { display: none !important; }", ".nav-links { display: none !important; }")
    content = content.replace(".nav-links, .nav-actions .lang-toggle-btn { display: none !important; }", ".nav-links { display: none !important; }")
    
    with open(f_name, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Updated {f_name}")

