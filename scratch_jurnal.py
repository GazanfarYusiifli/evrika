import os
import glob
import re

base_dir = "/Users/gazanfaryusifli/Downloads/Evrika"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

desktop_insert = """            <a href="jurnal.html" class="dropdown-item">
              <div class="item-icon"><i class="fas fa-book-open"></i></div>
              <div class="dropdown-item-text">
                <span class="dropdown-item-title">Evrika Məktəbli Jurnalı</span>
                <span class="dropdown-item-desc">Məktəb nəşri</span>
              </div>
            </a>"""

mobile_insert = """      <a href="achievements.html" data-i18n="nav-achievements">Uğurlar</a>
      <a href="jurnal.html">Evrika Məktəbli Jurnalı</a>"""

for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Mobile replace
    content = re.sub(r'<a href="achievements\.html"( data-i18n="nav-achievements")?>Uğurlar</a>', mobile_insert, content)

    # Desktop replace
    # we find ptim.html in the vacancy dropdown and insert jurnal.html after it.
    # The dropdown closes with </div> right after.
    ptim_block = r'(<a href="ptim\.html" class="dropdown-item">.*?</a>)'
    # We use re.DOTALL to match across newlines
    content = re.sub(ptim_block, r'\1\n' + desktop_insert, content, flags=re.DOTALL)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Updated navbars in all files")
