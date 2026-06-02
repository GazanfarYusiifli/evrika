import os
import glob

html_files = glob.glob("/Users/gazanfaryusifli/Downloads/Evrika/*.html")

for path in html_files:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove the navbar link "Evrika Məktəbli Jurnalı"
    # Often it looks like: <a href="jurnal.html">Evrika Məktəbli Jurnalı</a>
    # Or in mobile nav: <a href="jurnal.html" data-i18n="nav-jurnal">Evrika Məktəbli Jurnalı</a>
    
    import re
    
    # 1. Desktop dropdown item
    content = re.sub(
        r'<a href="jurnal\.html" class="dropdown-item">[\s\S]*?<span class="dropdown-item-title">Evrika Məktəbli Jurnalı</span>[\s\S]*?</a>',
        '',
        content
    )
    
    # 2. Direct link (desktop or mobile)
    content = re.sub(
        r'<a href="jurnal\.html"[^>]*>Evrika Məktəbli Jurnalı</a>',
        '',
        content
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
print("Removed Məktəbli Jurnalı")
