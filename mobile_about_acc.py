import glob
import re

mobile_about_accordion = r"""      <div class="mobile-accordion" id="mob-acc-about">
        <div class="mobile-accordion-trigger" onclick="toggleMobileAcc('mob-acc-about')">
          Haqqımızda
          <i class="fas fa-chevron-right acc-arrow"></i>
        </div>
        <div class="mobile-accordion-body">
          <a href="about.html">
            <div class="acc-icon"><i class="fas fa-info-circle"></i></div>
            <div class="acc-text"><span class="acc-title">Haqqımızda</span><span class="acc-desc">Bizim hekayəmiz</span></div>
          </a>
          <a href="alumni.html">
            <div class="acc-icon"><i class="fas fa-user-graduate"></i></div>
            <div class="acc-text"><span class="acc-title">Məzunlar</span><span class="acc-desc">Fəxrlərimiz</span></div>
          </a>
          <a href="achievements.html">
            <div class="acc-icon"><i class="fas fa-trophy"></i></div>
            <div class="acc-text"><span class="acc-title">Uğurlar</span><span class="acc-desc">Nailiyyətlərimiz</span></div>
          </a>
        </div>
      </div>"""

for filepath in glob.glob('*.html'):
    if filepath in ['admin.html', 'verify.html']:
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the simple mobile link
    content = re.sub(r'<a href="about\.html" data-i18n="nav-about">Haqqımızda</a>', mobile_about_accordion, content)
    # Also if it's missing the data-i18n in mobile nav
    content = re.sub(r'<a href="about\.html">Haqqımızda</a>\s*<div class="mobile-accordion" id="mob-acc-academic">', mobile_about_accordion + '\n      <div class="mobile-accordion" id="mob-acc-academic">', content)


    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Mobile Haqqimizda converted to accordion.")
