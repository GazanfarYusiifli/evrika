import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# The CSS we want to insert right after .nav-links { display: none !important; }
new_css = """
  /* Mobile Nav Actions - consistent spacing */
  .nav-actions { display: flex !important; align-items: center !important; margin-left: auto !important; margin-right: 25px !important; }
  .nav-actions > a:not(.nav-btn) { display: none !important; }
  .nav-actions > a.nav-btn { padding: 8px 18px !important; font-size: 0.85rem !important; margin: 0 !important; border-radius: 10px !important; }
  .mobile-menu-btn { margin-left: 0 !important; }
"""

for f_name in html_files:
    with open(f_name, "r", encoding="utf-8") as f:
        content = f.read()
        
    # We want to replace the old .nav-actions inline block in index.html and others
    # First, let's clean up any existing .nav-actions lines inside media queries to avoid duplicates.
    content = re.sub(r'\s*\.nav-actions\s*\{\s*display:\s*flex[^}]+\}', '', content)
    content = re.sub(r'\s*\.nav-actions\s*>\s*a:first-child\s*\{\s*display:\s*none[^}]+\}', '', content)
    content = re.sub(r'\s*\.nav-actions\s*>\s*a\.nav-btn\s*\{[^}]+\}', '', content)
    content = re.sub(r'\s*\.nav-actions\s*>\s*a:not\(\.nav-btn\)\s*\{[^}]+\}', '', content)
    
    # Now, insert the new block right after ".nav-links { display: none !important; }"
    if ".nav-links { display: none !important; }" in content:
        content = content.replace(".nav-links { display: none !important; }", 
                                  ".nav-links { display: none !important; }" + new_css)
        with open(f_name, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {f_name}")

