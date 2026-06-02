import glob
import re

desktop_dropdown = """        <div class="nav-item-has-dropdown">
          <a href="about.html">Haqqımızda</a>
          <div class="nav-dropdown">
            <a href="about.html" class="dropdown-item">
              <div class="item-icon"><i class="fas fa-info-circle"></i></div>
              <div class="dropdown-item-text">
                <span class="dropdown-item-title">Haqqımızda</span>
                <span class="dropdown-item-desc">Tariximiz və Missiyamız</span>
              </div>
            </a>
            <a href="alumni.html" class="dropdown-item">
              <div class="item-icon"><i class="fas fa-user-graduate"></i></div>
              <div class="dropdown-item-text">
                <span class="dropdown-item-title">Məzunlar</span>
                <span class="dropdown-item-desc">Tələbə və məzunlarımız</span>
              </div>
            </a>
            <a href="achievements.html" class="dropdown-item">
              <div class="item-icon"><i class="fas fa-medal"></i></div>
              <div class="dropdown-item-text">
                <span class="dropdown-item-title">Uğurlar</span>
                <span class="dropdown-item-desc">Nailiyyətlərimiz</span>
              </div>
            </a>
          </div>
        </div>"""

mobile_accordion = """      <div class="mobile-accordion" id="mob-acc-about">
        <div class="mobile-accordion-trigger" onclick="toggleMobileAcc('mob-acc-about')">
          Haqqımızda
          <i class="fas fa-chevron-right acc-arrow"></i>
        </div>
        <div class="mobile-accordion-body">
          <a href="about.html">
            <div class="acc-icon"><i class="fas fa-info-circle"></i></div>
            <div class="acc-text"><span class="acc-title">Haqqımızda</span><span class="acc-desc">Tariximiz və Missiyamız</span></div>
          </a>
          <a href="alumni.html">
            <div class="acc-icon"><i class="fas fa-user-graduate"></i></div>
            <div class="acc-text"><span class="acc-title">Məzunlar</span><span class="acc-desc">Tələbə və məzunlarımız</span></div>
          </a>
          <a href="achievements.html">
            <div class="acc-icon"><i class="fas fa-medal"></i></div>
            <div class="acc-text"><span class="acc-title">Uğurlar</span><span class="acc-desc">Nailiyyətlərimiz</span></div>
          </a>
        </div>
      </div>"""

for filepath in glob.glob('*.html'):
    if filepath == 'admin.html' or filepath == 'verify.html':
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the nav block using a regex or simple text replace
    # We will look inside <nav class="nav-links">...</nav>
    # Since regex can be tricky with HTML, we can replace the specific links directly.

    # 1. Replace the standalone Haqqimizda in the desktop nav (usually right after <nav class="nav-links"> or near it)
    # Be careful not to replace footer links. 
    # Desktop nav typically doesn't have data-i18n, but mobile nav does.
    
    # We can split the file into header and rest to be safe
    if '<header' in content and '</header>' in content:
        header_split = content.split('</header>')
        header_content = header_split[0]
        
        # Replace desktop Haqqimizda
        header_content = re.sub(r'<a href="about\.html"[^>]*>Haqqımızda</a>', desktop_dropdown, header_content, count=1)
        # Remove standalone Alumni and Achievements
        header_content = re.sub(r'\s*<a href="alumni\.html"[^>]*>Məzunlar</a>', '', header_content)
        header_content = re.sub(r'\s*<a href="achievements\.html"[^>]*>Uğurlar</a>', '', header_content)
        
        content = header_content + '</header>' + header_split[1]

    # Mobile nav is usually inside <div class="mobile-nav-links">
    if '<div class="mobile-nav-links">' in content and '</div>' in content:
        # Actually it's easier to just replace it within the whole document but restricted to the first match AFTER <div class="mobile-nav-links">
        parts = content.split('<div class="mobile-nav-links">')
        if len(parts) > 1:
            mobile_nav_content = parts[1]
            # Replace mobile Haqqimizda
            mobile_nav_content = re.sub(r'<a href="about\.html"[^>]*>Haqqımızda</a>', mobile_accordion, mobile_nav_content, count=1)
            # Remove standalone Alumni and Achievements
            mobile_nav_content = re.sub(r'\s*<a href="alumni\.html"[^>]*>Məzunlar</a>', '', mobile_nav_content)
            mobile_nav_content = re.sub(r'\s*<a href="achievements\.html"[^>]*>Uğurlar</a>', '', mobile_nav_content)
            
            content = parts[0] + '<div class="mobile-nav-links">' + mobile_nav_content

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Navbar updated in all HTML files.")
