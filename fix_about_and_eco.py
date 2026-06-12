import re

with open('victory.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace the About section text
about_old = r'<div class="about-text-side reveal-right">\s*<span class="sec-eyebrow">Haqqımızda</span>\s*<h2 class="sec-h2">Victory Colleges by Evrika <em>Hazırlıq Mərkəzi</em></h2><br>\s*<p>Victory Colleges by Evrika Təhsil Mərkəzi.*?<div class="pill"><i class="fas fa-sun"></i> Yay məktəbi proqramı</div>\s*</div>\s*</div>\s*</div>'

about_new = """<div class="about-text-side reveal-right">
        <span class="sec-eyebrow">Haqqımızda</span>
        <h2 class="sec-h2">Azərbaycanın ən tanınmış<br><em style="color: #3b82f6; font-style: normal;">xaricdə təhsil və hazırlıq mərkəzlərindən biri.</em></h2><br>
        <p>Victory Group 2018-ci ildən rəsmi fəaliyyət göstərən və Azərbaycanda xaricdə təhsil istiqamətində tanınan hazırlıq mərkəzlərindən biridir. Əsas məqsədimiz Azərbaycan gənclərinin xarici ölkələrin nüfuzlu universitetlərinə qəbul almasına dəstək olmaqdır.</p>
        <p>Komandamız SAT, IELTS, TOEFL, Duolingo, General English, GRE və GMAT kursları ilə yanaşı universitet və təqaüd müraciəti prosesində də tələbələrə yol göstərir. 2022-2025-ci illərdə 170+ fərqli təqaüd proqramı üzrə rekord nəticələr əldə edərək təhsil sahəsində lider mövqe formalaşdırmışıq.</p>
        
        <div style="margin-top: 30px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px;">
          <div style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 12px; text-align: center; border: 1px solid rgba(255,255,255,0.1);">
             <div style="font-size: 2rem; font-weight: 900; color: #fff;">8+</div>
             <div style="font-size: 0.85rem; color: #ccc; text-transform: uppercase; letter-spacing: 0.05em;">İl</div>
          </div>
          <div style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 12px; text-align: center; border: 1px solid rgba(255,255,255,0.1);">
             <div style="font-size: 2rem; font-weight: 900; color: #fff;">2000+</div>
             <div style="font-size: 0.85rem; color: #ccc; text-transform: uppercase; letter-spacing: 0.05em;">Məmnun tələbə</div>
          </div>
          <div style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 12px; text-align: center; border: 1px solid rgba(255,255,255,0.1);">
             <div style="font-size: 2rem; font-weight: 900; color: #fff;">170+</div>
             <div style="font-size: 0.85rem; color: #ccc; text-transform: uppercase; letter-spacing: 0.05em;">Təqaüd Proqramı</div>
          </div>
        </div>
      </div>"""

html = re.sub(about_old, about_new, html, flags=re.DOTALL)

# 2. Insert Ecosystem section right before <section class="section" id="registration"
ecosystem_section = """<section class="section" style="background: rgba(14,27,65, 0.3);">
  <div class="container">
    <div class="reveal" style="text-align: center; max-width: 900px; margin: 0 auto;">
      <span class="sec-eyebrow">Tam Təhsil Ekosistemi</span>
      <h2 class="sec-h2">Education <em style="color: #3b82f6; font-style: normal;">Ecosystem</em></h2>
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

html = html.replace('<section class="section" id="registration"', ecosystem_section + '<section class="section" id="registration"')

with open('victory.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updates applied")
