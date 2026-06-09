import re

with open('victory.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. CSS modifications for all yellow sections to use dark blue
html = html.replace('#facc15', '#0e1b41')
html = html.replace('#eab308', '#0e1b41')
html = html.replace('#about { background-color: #0e1b41 !important; color: #000 !important; }', '#about { background-color: #0e1b41 !important; color: #fff !important; }')
html = html.replace('#about .sec-eyebrow { color: #000 !important;', '#about .sec-eyebrow { color: #fff !important;')
html = html.replace('#about .sec-h2, #about .sec-h2 em { color: #000 !important; }', '#about .sec-h2, #about .sec-h2 em { color: #fff !important; }')
html = html.replace('#about p { color: #333 !important; }', '#about p { color: #fff !important; }')
html = html.replace('#about h4 { color: #000 !important; }', '#about h4 { color: #fff !important; }')
html = html.replace('#about .pills .pill i { color: #000 !important; }', '#about .pills .pill i { color: #fff !important; }')
html = html.replace('#about .pill { background: #fff !important; color: #000 !important; border: none !important; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }', '#about .pill { background: rgba(255,255,255,0.1) !important; color: #fff !important; border: 1px solid rgba(255,255,255,0.2) !important; }')

# Ustunlukler styling
html = html.replace('#ustunlukler { background-color: #0e1b41 !important; }', '#ustunlukler { background-color: #0e1b41 !important; color: #fff !important; }')
html = html.replace('#ustunlukler .sec-eyebrow { color: #000 !important;', '#ustunlukler .sec-eyebrow { color: #fff !important;')
html = html.replace('#ustunlukler .sec-h2, #ustunlukler .sec-h2 em { color: #000 !important; }', '#ustunlukler .sec-h2, #ustunlukler .sec-h2 em { color: #fff !important; }')
html = html.replace('#ustunlukler .prog-title { color: #000 !important; }', '#ustunlukler .prog-title { color: #0e1b41 !important; }') # The boxes are white
html = html.replace('#ustunlukler .prog-desc { color: #333 !important; }', '#ustunlukler .prog-desc { color: #333 !important; }')
html = html.replace('#ustunlukler .prog-ico { background: #0e1b41 !important; color: #000 !important;', '#ustunlukler .prog-ico { background: #0e1b41 !important; color: #fff !important;')

# Sosial Media styling
html = html.replace('#sosial-media { background: #0e1b41 !important; }', '#sosial-media { background: #0e1b41 !important; color: #fff !important; }')
html = html.replace('#sosial-media .sec-eyebrow { color: #000 !important;', '#sosial-media .sec-eyebrow { color: #fff !important;')
html = html.replace('#sosial-media .sec-h2, #sosial-media .sec-h2 em { color: #000 !important; }', '#sosial-media .sec-h2, #sosial-media .sec-h2 em { color: #fff !important; }')
html = html.replace('#sosial-media a { color: #333 !important; }', '#sosial-media a { color: #fff !important; }')
html = html.replace('#sosial-media .btn-primary { background: #000 !important; color: #fff !important; }', '#sosial-media .btn-primary { background: #1d3557 !important; color: #fff !important; border-color: #1d3557 !important; }')

# xidmetler icon text color
html = html.replace('#xidmetler .prog-ico { background: #0e1b41 !important; color: #000 !important; border: none !important; }', '#xidmetler .prog-ico { background: #0e1b41 !important; color: #fff !important; border: none !important; }')

# 2. Replacing the grid
old_grid = r'<section class="section prog-bg" id="xidmetler">.*?<div class="prog-grid">.*?</div>\s*</div>\s*</section>'

new_grid = """<section class="section prog-bg" id="xidmetler">
  <div class="container">
    <div style="text-align:center" class="reveal">
      <span class="sec-eyebrow">Xidmətlərimiz</span>
      <h2 class="sec-h2" style="text-align:center">Akademik <em>Hazırlıq Proqramları</em></h2>
    </div>
    <div class="prog-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; background: transparent; padding-top: 20px;">
      <div class="prog-item reveal" style="border-radius: 20px;">
        <div class="prog-ico"><i class="fas fa-check-circle"></i></div>
        <div class="prog-n">01 · HAZIRLIQ</div>
        <div class="prog-title">SAT Hazırlığı</div>
      </div>
      <div class="prog-item reveal" style="border-radius: 20px;">
        <div class="prog-ico"><i class="fas fa-check-circle"></i></div>
        <div class="prog-n">02 · HAZIRLIQ</div>
        <div class="prog-title">SAT + Attestat Proqramı</div>
      </div>
      <div class="prog-item reveal" style="border-radius: 20px;">
        <div class="prog-ico"><i class="fas fa-check-circle"></i></div>
        <div class="prog-n">03 · DİL HAZIRLIĞI</div>
        <div class="prog-title">IELTS Hazırlığı</div>
      </div>
      <div class="prog-item reveal" style="border-radius: 20px;">
        <div class="prog-ico"><i class="fas fa-check-circle"></i></div>
        <div class="prog-n">04 · DİL HAZIRLIĞI</div>
        <div class="prog-title">TOEFL Hazırlığı</div>
      </div>
      <div class="prog-item reveal" style="border-radius: 20px;">
        <div class="prog-ico"><i class="fas fa-check-circle"></i></div>
        <div class="prog-n">05 · PROQRAM</div>
        <div class="prog-title">Foundation Proqramları</div>
      </div>
      <div class="prog-item reveal" style="border-radius: 20px;">
        <div class="prog-ico"><i class="fas fa-check-circle"></i></div>
        <div class="prog-n">06 · PROQRAM</div>
        <div class="prog-title">Beynəlxalq universitetlərə qəbul üçün akademik ingilis dili hazırlığı</div>
      </div>
      <div class="prog-item reveal" style="border-radius: 20px;">
        <div class="prog-ico"><i class="fas fa-check-circle"></i></div>
        <div class="prog-n">07 · PROQRAM</div>
        <div class="prog-title">Pearson və A-Level istiqamətləri üzrə hazırlıq proqramları</div>
      </div>
      <div class="prog-item reveal" style="border-radius: 20px;">
        <div class="prog-ico"><i class="fas fa-check-circle"></i></div>
        <div class="prog-n">08 · PROQRAM</div>
        <div class="prog-title">Çin universitetlərinə qəbul üçün beynəlxalq CSCA hazırlıq proqramları</div>
      </div>
    </div>
  </div>
</section>"""

html = re.sub(old_grid, new_grid, html, flags=re.DOTALL)

with open('victory.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Grid replaced!")
