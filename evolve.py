import re

with open('lisey2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the start and end of the block we want to replace
start_marker = '<div class="montessori-details"'
end_marker = '</div>\n</div>\n\n</div>\n          </div>\n          <div class="about-img-side'

# Find the start
start_idx = content.find(start_marker)
# Find the exact end of the montessori-details div
# Actually, the block ends just before `<div class="about-img-side reveal-left">`
end_idx = content.find('<div class="about-img-side reveal-left">')

if start_idx != -1 and end_idx != -1:
    new_html = """
<div class="montessori-bento-grid" style="margin-top: 50px; display: grid; grid-template-columns: 1fr; gap: 30px;">
  
  <style>
    .m-bento-card {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 24px;
      padding: 35px;
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      transition: all 0.5s cubic-bezier(0.2, 0.8, 0.2, 1);
      position: relative;
      overflow: hidden;
    }
    .m-bento-card:hover {
      background: rgba(255, 255, 255, 0.06);
      transform: translateY(-5px);
      border-color: rgba(255, 107, 107, 0.3);
      box-shadow: 0 20px 40px rgba(0,0,0,0.3);
    }
    .m-bento-header {
      display: flex;
      align-items: center;
      gap: 15px;
      margin-bottom: 20px;
      border-bottom: 1px solid rgba(255,255,255,0.05);
      padding-bottom: 20px;
    }
    .m-bento-icon {
      width: 50px;
      height: 50px;
      border-radius: 12px;
      background: linear-gradient(135deg, #ff6b6b, #c92a2a);
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.5rem;
      box-shadow: 0 10px 20px rgba(201, 42, 42, 0.3);
    }
    .m-bento-title {
      font-size: 1.6rem;
      font-weight: 900;
      color: #fff;
      margin: 0;
      letter-spacing: -0.02em;
    }
    .m-bento-subtitle {
      font-size: 0.95rem;
      color: rgba(255,255,255,0.5);
      margin: 5px 0 0;
      font-weight: 500;
    }
    .m-bento-content h4 {
      color: #ff6b6b;
      font-size: 1.1rem;
      margin: 25px 0 10px;
      font-weight: 700;
      letter-spacing: 0.02em;
    }
    .m-bento-content h4:first-child { margin-top: 0; }
    .m-bento-content p {
      color: rgba(255,255,255,0.7);
      font-size: 1rem;
      line-height: 1.8;
      margin-bottom: 15px;
    }
    .m-bento-list {
      list-style: none;
      padding: 0;
      margin: 0 0 20px 0;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 10px 20px;
    }
    .m-bento-list li {
      position: relative;
      padding-left: 24px;
      color: rgba(255,255,255,0.8);
      font-size: 0.95rem;
      line-height: 1.5;
      display: flex;
      align-items: center;
    }
    .m-bento-list li i {
      position: absolute;
      left: 0;
      color: #ff6b6b;
      font-size: 0.8rem;
      top: 5px;
    }
    .m-bento-highlight {
      background: rgba(255, 107, 107, 0.1);
      padding: 15px 20px;
      border-radius: 12px;
      border-left: 4px solid #ff6b6b;
      margin-top: 20px;
    }
    .m-bento-highlight p { margin: 0; color: #fff; font-weight: 600; }
    
    @media(min-width: 992px) {
      .montessori-bento-grid {
        grid-template-columns: 1fr;
      }
    }
  </style>

  <!-- CARD 1: İBTİDAİ TƏHSİL -->
  <div class="m-bento-card">
    <div class="m-bento-header">
      <div class="m-bento-icon"><i class="fas fa-shapes"></i></div>
      <div>
        <h3 class="m-bento-title">İBTİDAİ TƏHSİL</h3>
        <p class="m-bento-subtitle">Lower & Upper Elementary (6–12 yaş)</p>
      </div>
    </div>
    <div class="m-bento-content">
      <p>İbtidai təhsil mərhələsi uşağın öyrənmə sevgisinin formalaşdığı, təməl akademik və sosial bacarıqların inkişaf etdiyi ən vacib dövrdür. Montessori "Work Cycle" və Cosmic Education vasitəsilə elmlər bir-biri ilə inteqrasiya olunmuş şəkildə öyrədilir.</p>
      
      <h4><i class="fas fa-book-open" style="margin-right:8px;"></i> Akademik Yanaşma</h4>
      <ul class="m-bento-list">
        <li><i class="fas fa-check"></i> Cambridge materialları</li>
        <li><i class="fas fa-check"></i> İntensiv İngilis və Rus dili</li>
        <li><i class="fas fa-check"></i> Riyaziyyat və məntiq</li>
        <li><i class="fas fa-check"></i> Laboratoriya və STEAM</li>
      </ul>

      <h4><i class="fas fa-palette" style="margin-right:8px;"></i> İnkişaf Fəaliyyətləri</h4>
      <ul class="m-bento-list">
        <li><i class="fas fa-star"></i> Üzgüçülük, futbol, gimnastika</li>
        <li><i class="fas fa-star"></i> Şahmat və STEAM</li>
        <li><i class="fas fa-star"></i> Rəsm, keramika, musiqi, piano</li>
        <li><i class="fas fa-star"></i> Kompüter elmləri</li>
      </ul>

      <div class="m-bento-highlight">
        <p>✨ Məqsəd: Müstəqil, özünə güvənən, analitik düşüncəli və çoxşaxəli inkişaf etmiş uşaqlar yetişdirmək.</p>
      </div>
    </div>
  </div>

  <!-- CARD 2: ORTA TƏHSİL -->
  <div class="m-bento-card">
    <div class="m-bento-header">
      <div class="m-bento-icon" style="background: linear-gradient(135deg, #4dabf7, #1971c2);"><i class="fas fa-microscope"></i></div>
      <div>
        <h3 class="m-bento-title">ORTA TƏHSİL</h3>
        <p class="m-bento-subtitle">Lower & Upper Secondary (12–15 yaş)</p>
      </div>
    </div>
    <div class="m-bento-content">
      <p>Cambridge beynəlxalq kurikulumu və Montessori yanaşmasının inteqrasiyası. Bu mərhələdə təhsil tamamilə <strong>Proje Əsaslı Öyrənmə (Project-Based Learning)</strong> üzərində qurulur.</p>

      <h4><i class="fas fa-atom" style="margin-right:8px;"></i> Akademik Fənlər</h4>
      <ul class="m-bento-list">
        <li><i class="fas fa-chevron-right"></i> English Language & Literature</li>
        <li><i class="fas fa-chevron-right"></i> Mathematics (Core & Advanced)</li>
        <li><i class="fas fa-chevron-right"></i> Science (Bio, Chem, Physics)</li>
        <li><i class="fas fa-chevron-right"></i> Global Perspectives & ICT</li>
      </ul>

      <h4><i class="fas fa-briefcase" style="margin-right:8px;"></i> Staj və Təcrübə (Internship)</h4>
      <p>Şagirdlər üçün yarım gün əsaslı praktik təcrübə imkanı yaradılır. Real iş mühiti ilə tanışlıq və peşəyönümlü bacarıqların erkən inkişafı təmin edilir.</p>

      <div class="m-bento-highlight" style="background: rgba(77, 171, 247, 0.1); border-left-color: #4dabf7;">
        <p>✨ Məqsəd: Öyrənməni real həyatla birləşdirmək və beynəlxalq akademik standartlara yiyələnmək.</p>
      </div>
    </div>
  </div>

  <!-- CARD 3: 9-CU SINIF VƏ SONRASI -->
  <div class="m-bento-card">
    <div class="m-bento-header">
      <div class="m-bento-icon" style="background: linear-gradient(135deg, #fcc419, #e67700);"><i class="fas fa-graduation-cap"></i></div>
      <div>
        <h3 class="m-bento-title">Universitetə Hazırlıq</h3>
        <p class="m-bento-subtitle">9-cu Sinif və Sonrası</p>
      </div>
    </div>
    <div class="m-bento-content">
      <p>Şagirdlər gələcək universitet və karyera yoluna yönləndirilir. Fərdi təhsil planı və akademik mentor dəstəyi ilə sistemli inkişaf təmin edilir.</p>

      <h4><i class="fas fa-globe-americas" style="margin-right:8px;"></i> Beynəlxalq İmtahanlara Hazırlıq</h4>
      <ul class="m-bento-list">
        <li><i class="fas fa-certificate"></i> IELTS & TOEFL</li>
        <li><i class="fas fa-certificate"></i> SAT & YÖS</li>
        <li><i class="fas fa-certificate"></i> A Level Proqramı</li>
        <li><i class="fas fa-certificate"></i> Cambridge Sertifikatları</li>
      </ul>

      <h4><i class="fas fa-award" style="margin-right:8px;"></i> DİM Hazırlığı və Fərqlənmə</h4>
      <p>Milli təhsil sistemi üzrə DİM imtahanlarına hazırlıq, yüksək nəticə əldə edən şagirdlər üçün <strong>Qırmızı Diplom</strong> imkanı.</p>

      <div class="m-bento-highlight" style="background: rgba(252, 196, 25, 0.1); border-left-color: #fcc419;">
        <p>✨ Məqsəd: Şagirdlərin həm yerli, həm də beynəlxalq universitetlərə maksimum səviyyədə hazırlaşdırılması.</p>
      </div>
    </div>
  </div>

</div>
          </div>
          """
    # Build the complete new content
    final_html = content[:start_idx] + new_html + content[end_idx:]
    with open('lisey2.html', 'w', encoding='utf-8') as f:
        f.write(final_html)
    print("Replaced with Bento UI successfully.")
else:
    print("Could not find boundaries.")
