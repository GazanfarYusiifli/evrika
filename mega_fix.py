import re

with open('victory.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove subtitle text
html = html.replace('<br><br>Tələbələr aşağıdakı istiqamətlər üzrə hazırlıq keçə bilərlər:', '')

# 2. Update icons in xidmetler
# The grid has 8 items, each with <i class="fas fa-check-circle"></i>
icons = [
    'fa-book-open',    # SAT
    'fa-award',        # SAT + Attestat
    'fa-language',     # IELTS
    'fa-comment-dots', # TOEFL
    'fa-university',   # Foundation
    'fa-chalkboard-teacher', # Academic English
    'fa-passport',     # Pearson/A-Level
    'fa-globe-asia'    # CSCA
]
for icon in icons:
    html = html.replace('<i class="fas fa-check-circle"></i>', f'<i class="fas {icon}"></i>', 1)

# 3. Clean up story-content (Remove the Foundation and Ecosystem boxes)
# Let's find the specific divs to remove using regex
foundation_div_regex = r'<div style="background: rgba\(255, 255, 255, 0\.03\); border: 1px solid rgba\(255, 255, 255, 0\.08\); border-radius: 20px; padding: 40px; margin-bottom: 30px; position: relative; overflow: hidden;">\s*<div style="position: absolute; top: -50px; right: -50px; width: 150px; height: 150px; background: var\(--accent\); filter: blur\(50px\); opacity: 0\.2; pointer-events: none;"></div>\s*<h3 style="color: white; font-size: 1\.6rem; font-weight: 800; margin-bottom: 20px; display: flex; align-items: center; gap: 10px;">.*?Foundation Proqramı.*?</div>'

ecosystem_div_regex = r'<div style="background: rgba\(255, 255, 255, 0\.03\); border: 1px solid rgba\(255, 255, 255, 0\.08\); border-radius: 20px; padding: 40px; position: relative; overflow: hidden;">\s*<div style="position: absolute; bottom: -50px; left: -50px; width: 150px; height: 150px; background: var\(--accent-light\); filter: blur\(50px\); opacity: 0\.15; pointer-events: none;"></div>\s*<h3 style="color: white; font-size: 1\.6rem; font-weight: 800; margin-bottom: 20px; display: flex; align-items: center; gap: 10px;">.*?Education Ecosystem.*?</div>'

html = re.sub(foundation_div_regex, '', html, flags=re.DOTALL)
html = re.sub(ecosystem_div_regex, '', html, flags=re.DOTALL)

# 4. Replace Abituriyent with Foundation
# Regex to match the about-text-side containing Abituriyent
abituriyent_regex = r'<div class="about-text-side reveal-left">.*?<span class="sec-eyebrow">Abituriyent Məktəbi</span>.*?<ul style="list-style: none; display: grid; gap: 12px;">.*?</ul>\s*</div>\s*</div>'

foundation_text = """<div class="about-text-side reveal-left">
        <span class="sec-eyebrow">Beynəlxalq Standartlar</span>
        <h2 class="sec-h2">Foundation <em>Proqramı</em></h2><br>
        <p>Victory Colleges by Evrika tələbələrə beynəlxalq standartlara uyğun Foundation proqramı təqdim edir. Bu proqram vasitəsilə tələbələr xarici universitetlərə hazırlıq keçərək birbaşa bakalavr təhsilinə başlamaq imkanı əldə edirlər.</p>
        <p>Foundation proqramının əsas üstünlüyü ondan ibarətdir ki, tələbələr xaricdə yüksək məbləğdə vəsait xərcləmədən hazırlıq mərhələsini Azərbaycanda tamamlaya və daha sonra universitet təhsilinə davam edə bilirlər.</p>
        <p>Proqram beynəlxalq Level 3 kvalifikasiyası əsasında qurulur və tələbələrin akademik, dil və peşəkar bacarıqlarını inkişaf etdirməyə yönəlib.</p>
      </div>"""

html = re.sub(abituriyent_regex, foundation_text, html, flags=re.DOTALL)
html = html.replace('<span class="num" style="color: var(--accent, #0e1b41);">Dövlət</span><span class="lbl">Attestatı</span>', '<span class="num" style="color: var(--accent, #0e1b41);">Level 3</span><span class="lbl">Kvalifikasiyası</span>')


# 5. Insert Ecosystem above Gələcəyi hədəfləyən section
ecosystem_section = """<section class="section" style="background: rgba(14,27,65, 0.3);">
  <div class="container">
    <div class="reveal" style="text-align: center; max-width: 900px; margin: 0 auto;">
      <span class="sec-eyebrow">Tam Təhsil Ekosistemi</span>
      <h2 class="sec-h2">Education <em>Ecosystem</em></h2>
      <p style="font-size: 1.15rem; color: rgba(255,255,255,0.85); line-height: 1.8; margin-top: 20px;">
        Victory Colleges by Evrika sadəcə xaricdə təhsil xidməti təqdim edən bir mərkəz deyil. Məqsəd tələbələrin məktəb dövründən başlayaraq universitet qəbuluna və beynəlxalq təhsilə qədər bütün mərhələləri əhatə edən vahid təhsil ekosistemi yaratmaqdır.
      </p>
      <p style="font-size: 1.15rem; color: rgba(255,255,255,0.85); line-height: 1.8; margin-top: 15px;">
        Bu ekosistem daxilində tələbələr lisey təhsili, attestat proqramı, SAT hazırlığı, karyera planlaması, xaricdə universitet yerləşdirməsi və Foundation proqramlarını bir mərkəzdə əldə edə bilirlər. Beləliklə, tələbə bütün akademik inkişaf yolunu sistemli və ardıcıl şəkildə planlaşdıra bilir.
      </p>
    </div>
  </div>
</section>

"""

# Insert right before the section containing Gələcəyi hədəfləyən
# Find <section class="section"> right before <h2 ...>Gələcəyi hədəfləyən...
call_to_action_regex = r'(<section class="section">\s*<div class="container">\s*<div class="reveal" style="background: linear-gradient.*?Gələcəyi hədəfləyən)'
html = re.sub(call_to_action_regex, ecosystem_section + r'\1', html)

# 6. Footer fixes
html = html.replace('(+994) 12 525 10 10', '+994 55 519 99 32')
html = html.replace('color: var(--accent, #8B1A2B);', 'color: #fff !important;')
# There might be some explicit colors in the footer, let's fix them:
html = html.replace('<h4 style="text-transform: uppercase; letter-spacing: 0.15em; margin-bottom: 30px; font-size: 0.9rem; font-weight: 800; color: #fff !important;" data-i18n="footer-nav">NAVİQASİYA</h4>', '<h4 style="text-transform: uppercase; letter-spacing: 0.15em; margin-bottom: 30px; font-size: 0.9rem; font-weight: 800; color: white !important;" data-i18n="footer-nav">NAVİQASİYA</h4>')

# Let's just blindly force all h4s in the footer to white
html = re.sub(r'<h4 style="([^"]*?)color:\s*var\(--accent(?:,\s*#[A-Fa-f0-9]+)?\);?([^"]*?)"', r'<h4 style="\1color: white !important;\2"', html)

with open('victory.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updates applied")
