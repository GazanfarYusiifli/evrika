import glob
import re

html_files = glob.glob("/Users/gazanfaryusifli/Downloads/Evrika/*.html")

desktop_target = '''            <a href="ptim.html" class="dropdown-item">
              <div class="item-icon"><i class="fas fa-chalkboard-teacher"></i></div>
              <div class="dropdown-item-text">
                <span class="dropdown-item-title">Pedaqoji Təcrübə və İnkişaf Mərkəzi</span>
                <span class="dropdown-item-desc">PTİM</span>
              </div>
            </a>'''

desktop_insert = '''            <a href="ptim.html" class="dropdown-item">
              <div class="item-icon"><i class="fas fa-chalkboard-teacher"></i></div>
              <div class="dropdown-item-text">
                <span class="dropdown-item-title">Pedaqoji Təcrübə və İnkişaf Mərkəzi</span>
                <span class="dropdown-item-desc">PTİM</span>
              </div>
            </a>
            <a href="jurnal.html" class="dropdown-item">
              <div class="item-icon"><i class="fas fa-book-open"></i></div>
              <div class="dropdown-item-text">
                <span class="dropdown-item-title">Evrika Məktəbli Jurnalı</span>
                <span class="dropdown-item-desc">Aylıq Nəşr</span>
              </div>
            </a>'''

mobile_target = '''          <a href="ptim.html">
            <div class="acc-icon"><i class="fas fa-chalkboard-teacher"></i></div>
            <div class="acc-text"><span class="acc-title">Pedaqoji Təcrübə və İnkişaf Mərkəzi</span><span class="acc-desc">PTİM</span></div>
          </a>'''

mobile_insert = '''          <a href="ptim.html">
            <div class="acc-icon"><i class="fas fa-chalkboard-teacher"></i></div>
            <div class="acc-text"><span class="acc-title">Pedaqoji Təcrübə və İnkişaf Mərkəzi</span><span class="acc-desc">PTİM</span></div>
          </a>
          <a href="jurnal.html">
            <div class="acc-icon"><i class="fas fa-book-open"></i></div>
            <div class="acc-text"><span class="acc-title">Evrika Məktəbli Jurnalı</span><span class="acc-desc">Aylıq Nəşr</span></div>
          </a>'''

for path in html_files:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if desktop_target in content:
        content = content.replace(desktop_target, desktop_insert)
    
    if mobile_target in content:
        content = content.replace(mobile_target, mobile_insert)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Added Jurnal to dropdowns in all files.")
