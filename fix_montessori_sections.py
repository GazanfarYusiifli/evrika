import re

with open('montessori.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Revert Erkən İnkişaf background to white
# We can just remove the `<style>` block and `green-bg-section` class.
# Or since the user wants "white", we can literally set it to white if the theme uses var(--navy) which might be #f9fbf7.
# Let's just remove the style block and green-bg-section.
style_block = """  <style>
    #about.green-bg-section { background-color: #9ba278; color: #fff; }
    #about.green-bg-section .sec-eyebrow { color: #fff; }
    #about.green-bg-section .sec-eyebrow::before { background: #fff; }
    #about.green-bg-section .sec-h2 { color: #fff !important; }
    #about.green-bg-section .sec-h2 em { color: rgba(255,255,255,0.9) !important; }
    #about.green-bg-section .sec-lead { color: #fff !important; }
    #about.green-bg-section p { color: rgba(255,255,255,0.9) !important; }
    #about.green-bg-section .pill { background: rgba(255,255,255,0.15); border-color: rgba(255,255,255,0.3); color: #fff; }
    #about.green-bg-section .pill i { color: #fff; }
  </style>"""

content = content.replace(style_block, '')
content = content.replace('<section id="about" class="section green-bg-section">', '<section id="about" class="section" style="background-color: #fff;">')
# Revert colors inside #about
content = content.replace('<div class="sec-eyebrow" style="color: #fff;">Erkən inkişaf</div>', '<div class="sec-eyebrow">Erkən inkişaf</div>')
content = content.replace('<h2 class="sec-h2" style="color: #fff;">Uşağın həyatının ilk 6 ili onun <em style="color: rgba(255,255,255,0.8);">gələcək inkişafının</em> əsasını təşkil edir.</h2>', '<h2 class="sec-h2" style="color: var(--text);">Uşağın həyatının ilk 6 ili onun <em style="color: var(--accent-light);">gələcək inkişafının</em> əsasını təşkil edir.</h2>')
content = content.replace('<p class="sec-lead" style="font-size: 1.1rem; color: #fff; margin-bottom: 10px;">Dil, düşüncə və sosial bacarıqlar bu dövrdə formalaşır.</p>', '<p class="sec-lead" style="font-size: 1.1rem; color: var(--text); margin-bottom: 10px;">Dil, düşüncə və sosial bacarıqlar bu dövrdə formalaşır.</p>')
content = content.replace('<p style="color: rgba(255,255,255,0.85); line-height:1.8; margin-bottom: 20px;">Evrika-da bu mərhələ şüurlu inkişaf kimi qurulur.</p>', '<p style="color: var(--text-muted); line-height:1.8; margin-bottom: 20px;">Evrika-da bu mərhələ şüurlu inkişaf kimi qurulur.</p>')


# 2. Change background of "Montessori Yanaşması" section
# <section class="section" style="background: var(--navy-mid);">
# Replace with #9ba278
content = content.replace('<section class="section" style="background: var(--navy-mid);">', '<section class="section" style="background: #9ba278;">')
content = content.replace('<h2 class="sec-h2" style="color:var(--text);">Montessori <em style="color: var(--accent-light); font-style: normal;">Yanaşması</em></h2>', '<h2 class="sec-h2" style="color:#fff;">Montessori <em style="color: #fff; font-style: normal; opacity: 0.9;">Yanaşması</em></h2>')
content = content.replace('<p class="sec-p reveal-right" style="color:var(--text-muted);">Müstəqil düşünmə, fokus, seçim etmə və sosial inkişaf Montessori metodunun əsasını təşkil edir. Uşaqlar kəşf edərək öyrənir.</p>', '<p class="sec-p reveal-right" style="color:rgba(255,255,255,0.9);">Müstəqil düşünmə, fokus, seçim etmə və sosial inkişaf Montessori metodunun əsasını təşkil edir. Uşaqlar kəşf edərək öyrənir.</p>')

# We must also make sure text inside bento cards is visible.
# Originally, it was dark text on light, wait, bento-overlay has its own styling.
# Usually bento cards are dark or use an overlay image. Let's see:
# bento card has .bento-title, .bento-desc.
# Let's add a style block to enforce white text for bento titles/desc in case they were altered.
# Actually, the user says "burani #9ba278 bu reng ele arxa fonu". If it breaks some text color, I should fix it.

# 3. Change background of "Yaş Qrupları" section
# <section class="section section-red">
content = content.replace('<section class="section section-red">', '<section class="section section-red" style="background: #9ba278;">')
content = content.replace('<h2 class="sec-h2" style="color:var(--text);">Yaş <em style="color: var(--accent-light); font-style: normal;">Qrupları</em></h2>', '<h2 class="sec-h2" style="color:#fff;">Yaş <em style="color: #fff; font-style: normal; opacity: 0.9;">Qrupları</em></h2>')
content = content.replace('.level-card h4 { font-size: 1.6rem; color: var(--text); margin-bottom: 8px; font-weight: 900; }', '.level-card h4 { font-size: 1.6rem; color: #fff; margin-bottom: 8px; font-weight: 900; }')
content = content.replace('.level-card:hover p { color: var(--text); }', '.level-card:hover p { color: #fff; }')

# In my previous script I replaced `color: #fff;` with `color:var(--text);`.
# Let's inject a quick style rule to fix the colors in these specific sections.
fix_style = """
<style>
  .section[style*="#9ba278"] .sec-h2,
  .section[style*="#9ba278"] .sec-p,
  .section[style*="#9ba278"] .bento-title,
  .section[style*="#9ba278"] .bento-desc,
  .section[style*="#9ba278"] .bento-badge,
  .section[style*="#9ba278"] .bento-icon,
  .section[style*="#9ba278"] .level-card h4,
  .section[style*="#9ba278"] .level-card p,
  .section[style*="#9ba278"] .level-icon,
  .section[style*="#9ba278"] .level-age {
    color: #fff !important;
  }
  .section[style*="#9ba278"] .level-card {
    background: rgba(255,255,255,0.1);
    border-color: rgba(255,255,255,0.2);
  }
</style>
"""
content = content.replace('<!-- ── MONTESSORI YANAŞMASI & BÖLMƏLƏR ── -->', '<!-- ── MONTESSORI YANAŞMASI & BÖLMƏLƏR ── -->' + fix_style)

with open('montessori.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated colors successfully")
