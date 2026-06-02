import os
import glob

# HTML chunks to replace
old_haqqimizda = '<a href="about.html">Haqqımızda</a>'
new_haqqimizda = """<div class="nav-item-has-dropdown">
          <a href="about.html">Haqqımızda</a>
          <div class="nav-dropdown">
            <a href="about.html" class="dropdown-item">
              <div class="item-icon"><i class="fas fa-info-circle"></i></div>
              <div class="dropdown-item-text">
                <span class="dropdown-item-title">Haqqımızda</span>
                <span class="dropdown-item-desc">Bizim hekayəmiz</span>
              </div>
            </a>
            <a href="alumni.html" class="dropdown-item">
              <div class="item-icon"><i class="fas fa-user-graduate"></i></div>
              <div class="dropdown-item-text">
                <span class="dropdown-item-title">Məzunlar</span>
                <span class="dropdown-item-desc">Fəxrlərimiz</span>
              </div>
            </a>
            <a href="achievements.html" class="dropdown-item">
              <div class="item-icon"><i class="fas fa-trophy"></i></div>
              <div class="dropdown-item-text">
                <span class="dropdown-item-title">Uğurlar</span>
                <span class="dropdown-item-desc">Nailiyyətlərimiz</span>
              </div>
            </a>
          </div>
        </div>"""

# Jurnal in Vakansiya block:
old_jurnal = """            <a href="jurnal.html" class="dropdown-item">
              <div class="item-icon"><i class="fas fa-book-open"></i></div>
              <div class="dropdown-item-text">
                <span class="dropdown-item-title">Evrika Məktəbli Jurnalı</span>
                <span class="dropdown-item-desc">Aylıq Nəşr</span>
              </div>
            </a>"""

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # 1. Update Haqqimizda
    if old_haqqimizda in content and 'class="nav-item-has-dropdown"' not in content.split(old_haqqimizda)[0][-50:]:
        content = content.replace(old_haqqimizda, new_haqqimizda)
        
    # 2. Remove standalone Mezunlar and Ugurlar
    content = content.replace('<a href="alumni.html">Məzunlar</a>', '')
    content = content.replace('<a href="achievements.html">Uğurlar</a>', '')
    
    # 3. Remove Jurnal from Vakansiya
    content = content.replace(old_jurnal, '')
    
    # 4. Add Jurnal directly before Elaqe if not there
    if '<a href="jurnal.html">Evrika Jurnalı</a>' not in content:
        content = content.replace('<a href="contact.html">Əlaqə</a>', '<a href="jurnal.html">Evrika Jurnalı</a>\n        <a href="contact.html">Əlaqə</a>')

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

if __name__ == "__main__":
    html_files = glob.glob('*.html')
    for file in html_files:
        if file not in ['admin.html', 'verify.html']:
            process_file(file)
