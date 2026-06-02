import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

old_style = """.nav-links, .nav-actions { display: none !important; }
      .mobile-menu-btn { display: flex !important; }"""

new_style = """.nav-links { display: none !important; }
      .nav-actions { display: flex !important; align-items: center; margin-left: auto; margin-right: 15px; }
      .nav-actions > a:first-child { display: none !important; }
      .nav-actions > a.nav-btn { padding: 8px 18px !important; font-size: 0.85rem !important; margin: 0 !important; }
      .mobile-menu-btn { display: flex !important; }"""

for f_name in html_files:
    with open(f_name, "r", encoding="utf-8") as f:
        content = f.read()
    
    if old_style in content:
        content = content.replace(old_style, new_style)
        with open(f_name, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {f_name}")

