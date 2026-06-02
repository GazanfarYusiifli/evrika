import glob
import re

dropdown_block = """            <a href="jurnal.html" class="dropdown-item">
              <div class="item-icon"><i class="fas fa-book-open"></i></div>
              <div class="dropdown-item-text">
                <span class="dropdown-item-title">Evrika Məktəbli Jurnalı</span>
                <span class="dropdown-item-desc">Aylıq Nəşr</span>
              </div>
            </a>"""

for filepath in glob.glob('*.html'):
    if filepath == 'admin.html' or filepath == 'verify.html':
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove from dropdown (ignoring slight whitespace differences)
    # The safest way is regex that matches the a tag to its closing tag
    pattern_dropdown = re.compile(r'\s*<a href="jurnal\.html"[^>]*class="dropdown-item"[^>]*>.*?</a>', re.DOTALL)
    content = pattern_dropdown.sub('', content)

    # 2. Change existing text (like in mobile nav or footer)
    content = content.replace("Evrika Məktəbli Jurnalı", "Evrika Jurnalı")

    # 3. Add to desktop nav before contact
    # In desktop nav, it looks like: 
    #       </div>
    #     </div>
    #     <a href="contact.html">Əlaqə</a>
    #   </nav>
    # So we can search for `<nav class="nav-links">...<a href="contact.html"`
    
    # Let's split by `<nav class="nav-links">` and `</nav>` to only modify desktop nav
    if '<nav class="nav-links">' in content:
        parts = content.split('<nav class="nav-links">')
        nav_parts = parts[1].split('</nav>')
        desktop_nav = nav_parts[0]
        
        # Insert <a href="jurnal.html">Evrika Jurnalı</a> before contact.html
        desktop_nav = re.sub(r'(<a href="contact\.html"[^>]*>)', r'<a href="jurnal.html">Evrika Jurnalı</a>\n        \1', desktop_nav, count=1)
        
        content = parts[0] + '<nav class="nav-links">' + desktop_nav + '</nav>' + nav_parts[1]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Jurnal updated in all HTML files.")
