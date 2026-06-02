import re

with open('lisey2.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<div class="montessori-bento-grid"'
end_marker = '</div>\n          </div>\n<div class="about-img-side'

start_idx = content.find(start_marker)
end_idx = content.find('</div>\n          </div>\n<div class="about-img-side')

if start_idx != -1:
    end_of_grid = content.find('<!-- 3. Ultra-Modern Horizontal Scroll', start_idx)
    # Actually the grid is placed right before the "<!-- 3. Ultra-Modern Horizontal Scroll" section
    # Let's find the closing of the grid container.
    
    # We will just replace the whole `<div class="montessori-bento-grid" ...` until `<section class="section" style="position: relative; z-index: 20; background: #fff; text-align: center; padding: 120px 0; overflow: hidden;">`
    # wait, the grid is between:
    # <!-- Full Width Bento Grid -->
    # <div class="montessori-bento-grid"
    # ...
    # </div>
    #       </div>
    #     </section>
    #   </div>
    #
    #   <!-- 3. Ultra-Modern Horizontal Scroll Clubs Section -->
    
    grid_start_tag = '<!-- Full Width Bento Grid -->'
    grid_start_idx = content.find(grid_start_tag)
    end_tag = '<!-- 3. Ultra-Modern Horizontal Scroll Clubs Section -->'
    grid_end_idx = content.find(end_tag)

    if grid_start_idx != -1 and grid_end_idx != -1:
        # Extract the trailing tags that need to be kept
        trailing = '\n      </div>\n    </section>\n  </div>\n\n  '
        
        # We replace the grid with an elegant accordion layout that looks exactly like the bento but expands.
        new_html = """
<!-- Full Width Bento Accordion -->
<div class="montessori-accordion-container" style="margin-top: 50px;">
  
  <style>
    .m-acc-item {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 20px;
      margin-bottom: 20px;
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      overflow: hidden;
      transition: all 0.3s ease;
    }
    .m-acc-header {
      padding: 25px 30px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 20px;
      transition: background 0.3s ease;
    }
    .m-acc-header:hover {
      background: rgba(255, 255, 255, 0.06);
    }
    .m-acc-icon {
      width: 50px;
      height: 50px;
      border-radius: 12px;
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.5rem;
      flex-shrink: 0;
    }
    .m-acc-title-group {
      flex: 1;
    }
    .m-acc-title {
      font-size: 1.5rem;
      font-weight: 900;
      color: #fff;
      margin: 0;
      letter-spacing: -0.02em;
    }
    .m-acc-subtitle {
      font-size: 0.95rem;
      color: rgba(255,255,255,0.5);
      margin: 5px 0 0;
      font-weight: 500;
    }
    .m-acc-toggle {
      color: white;
      font-size: 1.2rem;
      transition: transform 0.3s ease;
    }
    .m-acc-body {
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.5s cubic-bezier(0.4, 0, 0.2, 1), padding 0.5s ease;
      padding: 0 30px;
    }
    .m-acc-item.active .m-acc-body {
      max-height: 3000px;
      padding: 10px 30px 30px;
      border-top: 1px solid rgba(255,255,255,0.05);
    }
    .m-acc-item.active .m-acc-toggle {
      transform: rotate(180deg);
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
      align-items: flex-start;
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
    .divider-sub {
      height: 1px;
      background: rgba(255,255,255,0.05);
      margin: 30px 0;
    }
    .sub-section-title {
      font-size: 1.3rem;
      font-weight: 800;
      color: #fff;
      margin-bottom: 15px;
      background: linear-gradient(135deg, #fff, #aaa);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
  </style>

  <!-- ACCORDION 1: İBTİDAİ TƏHSİL -->
  <div class="m-acc-item active" onclick="this.classList.toggle('active')">
    <div class="m-acc-header">
      <div class="m-acc-icon" style="background: linear-gradient(135deg, #ff6b6b, #c92a2a); box-shadow: 0 10px 20px rgba(201, 42, 42, 0.3);"><i class="fas fa-shapes"></i></div>
      <div class="m-acc-title-group">
        <h3 class="m-acc-title">İBTİDAİ TƏHSİL</h3>
        <p class="m-acc-subtitle">Lower & Upper Elementary</p>
      </div>
      <div class="m-acc-toggle"><i class="fas fa-chevron-down"></i></div>
    </div>
    <div class="m-acc-body m-bento-content" onclick="event.stopPropagation()">
      <div class="sub-section-title">Lower Elementary (6–9 yaş)</div>
      <p>İbtidai təhsil mərhələsi uşağın öyrənmə sevgisinin formalaşdığı, təməl akademik və sosial bacarıqların inkişaf etdiyi ən vacib dövrdür. Montessori yanaşması ilə uşaqlar fərdi sürətinə uyğun, stresssiz və maraq əsaslı şəkildə öyrənirlər.</p>
      
      <h4>📚 Tədris sistemi:</h4>
      <ul class="m-bento-list">
        <li><i class="fas fa-check"></i> Montessori “Work Cycle” (fasiləsiz öyrənmə modeli)</li>
        <li><i class="fas fa-check"></i> Riyaziyyat</li>
        <li><i class="fas fa-check"></i> İngilis dili</li>
        <li><i class="fas fa-check"></i> Rus dili (ehtiyaca görə)</li>
        <li><i class="fas fa-check"></i> Cosmic Education (bütün elmlərin inteqrasiyası)</li>
      </ul>

      <h4>🌍 Cosmic Education daxilində:</h4>
      <p>Coğrafiya, tarix, biologiya, fizika, kimya, astronomiya, ekologiya və geologiya bir-biri ilə əlaqəli şəkildə öyrədilir.</p>

      <h4>📖 Tədris yanaşması:</h4>
      <ul class="m-bento-list">
        <li><i class="fas fa-check"></i> Cambridge tədris materiallarından istifadə</li>
        <li><i class="fas fa-check"></i> Beynəlxalq standartlara uyğun akademik baza</li>
        <li><i class="fas fa-check"></i> Dil və kommunikasiya bacarıqlarının inkişafı</li>
      </ul>

      <h4>🌟 Əlavə fəaliyyətlər:</h4>
      <ul class="m-bento-list">
        <li><i class="fas fa-star"></i> Üzgüçülük, futbol, gimnastika</li>
        <li><i class="fas fa-star"></i> Şahmat və STEAM</li>
        <li><i class="fas fa-star"></i> Rəsm, keramika, musiqi, piano</li>
        <li><i class="fas fa-star"></i> Drama və sosial bacarıqlar</li>
        <li><i class="fas fa-star"></i> Kompüter elmləri</li>
        <li><i class="fas fa-star"></i> Native speaker dərsləri</li>
      </ul>

      <div class="m-bento-highlight">
        <p>✨ Məqsəd: Müstəqil, özünə güvənən və çoxşaxəli inkişaf etmiş uşaqlar yetişdirmək</p>
      </div>

      <div class="divider-sub"></div>

      <div class="sub-section-title">Upper Elementary (9–12 yaş)</div>
      <p>Bu mərhələ uşağın daha analitik düşünməyə başladığı, akademik biliklərin dərinləşdiyi və məsuliyyət hissinin gücləndiyi dövrdür.</p>

      <h4>📚 Akademik istiqamət:</h4>
      <ul class="m-bento-list">
        <li><i class="fas fa-check"></i> İngilis dili (Grammar, Writing, Reading, Speaking)</li>
        <li><i class="fas fa-check"></i> Riyaziyyat və məntiq</li>
        <li><i class="fas fa-check"></i> Elm fənləri (Physics, Biology, Chemistry)</li>
        <li><i class="fas fa-check"></i> Social Studies və Azerbaijan tarixi</li>
        <li><i class="fas fa-check"></i> Laboratoriya və STEAM dərsləri</li>
      </ul>

      <h4>🌍 Dil inkişafı:</h4>
      <ul class="m-bento-list">
        <li><i class="fas fa-check"></i> İngilis dili intensiv proqram</li>
        <li><i class="fas fa-check"></i> Rus dili</li>
        <li><i class="fas fa-check"></i> German / French / Chinese tanışlıq səviyyəsi</li>
      </ul>

      <h4>📖 Beynəlxalq hazırlıq:</h4>
      <ul class="m-bento-list">
        <li><i class="fas fa-check"></i> Cambridge Exam Preparation</li>
        <li><i class="fas fa-check"></i> Akademik yazı və oxu bacarıqları</li>
        <li><i class="fas fa-check"></i> Analitik düşünmə və problem həll etmə</li>
      </ul>

      <h4>🎨 İnkişaf fəaliyyətləri:</h4>
      <ul class="m-bento-list">
        <li><i class="fas fa-star"></i> İdman və üzgüçülük</li>
        <li><i class="fas fa-star"></i> Şahmat və logic</li>
        <li><i class="fas fa-star"></i> Rəsm, keramika, drama</li>
        <li><i class="fas fa-star"></i> Musiqi və piano</li>
        <li><i class="fas fa-star"></i> Kompüter elmləri</li>
      </ul>

      <div class="m-bento-highlight">
        <p>✨ Məqsəd: Akademik olaraq güclü, yaradıcı və beynəlxalq düşüncəli şagirdlər yetişdirmək</p>
      </div>
    </div>
  </div>

  <!-- ACCORDION 2: ORTA TƏHSİL -->
  <div class="m-acc-item" onclick="this.classList.toggle('active')">
    <div class="m-acc-header">
      <div class="m-acc-icon" style="background: linear-gradient(135deg, #4dabf7, #1971c2); box-shadow: 0 10px 20px rgba(25, 113, 194, 0.3);"><i class="fas fa-microscope"></i></div>
      <div class="m-acc-title-group">
        <h3 class="m-acc-title">ORTA TƏHSİL</h3>
        <p class="m-acc-subtitle">Lower & Upper Secondary (12–15 yaş)</p>
      </div>
      <div class="m-acc-toggle"><i class="fas fa-chevron-down"></i></div>
    </div>
    <div class="m-acc-body m-bento-content" onclick="event.stopPropagation()">
      <p>Bu mərhələ şagirdlərin akademik biliklərini dərinləşdirdiyi, universitet və karyera yoluna keçid etdiyi vacib inkişaf dövrüdür. Proqram Cambridge beynəlxalq kurikulumu və Montessori yanaşmasının inteqrasiyası ilə qurulmuşdur.</p>

      <h4>📚 Akademik fənlər</h4>
      <ul class="m-bento-list">
        <li><i class="fas fa-chevron-right" style="color:#4dabf7"></i> English Language & Literature</li>
        <li><i class="fas fa-chevron-right" style="color:#4dabf7"></i> Mathematics (Core & Advanced)</li>
        <li><i class="fas fa-chevron-right" style="color:#4dabf7"></i> Science (Biology, Chemistry, Physics)</li>
        <li><i class="fas fa-chevron-right" style="color:#4dabf7"></i> Global Perspectives</li>
        <li><i class="fas fa-chevron-right" style="color:#4dabf7"></i> ICT / Computer Science</li>
        <li><i class="fas fa-chevron-right" style="color:#4dabf7"></i> Social Studies</li>
      </ul>

      <h4>🌍 Bu proqram şagirdlərə qazandırır:</h4>
      <ul class="m-bento-list">
        <li><i class="fas fa-check" style="color:#4dabf7"></i> Analitik və tənqidi düşünmə</li>
        <li><i class="fas fa-check" style="color:#4dabf7"></i> Beynəlxalq akademik standart</li>
        <li><i class="fas fa-check" style="color:#4dabf7"></i> Güclü İngilis dili bazası</li>
        <li><i class="fas fa-check" style="color:#4dabf7"></i> Problem həll etmə bacarıqları</li>
      </ul>

      <h4>🔬 Proje əsaslı öyrənmə (Project-Based Learning)</h4>
      <p>Bu mərhələdə təhsil sistemi tamamilə proje əsaslı yanaşma ilə dəstəklənir. Şagirdlər:</p>
      <ul class="m-bento-list">
        <li><i class="fas fa-check" style="color:#4dabf7"></i> Real problemlər üzərində çalışır</li>
        <li><i class="fas fa-check" style="color:#4dabf7"></i> Komanda işi ilə layihələr hazırlayır</li>
        <li><i class="fas fa-check" style="color:#4dabf7"></i> Araşdırma və təqdimat bacarıqları inkişaf etdirir</li>
        <li><i class="fas fa-check" style="color:#4dabf7"></i> Akademik bilikləri praktikaya tətbiq edir</li>
      </ul>
      <div class="m-bento-highlight" style="background: rgba(77, 171, 247, 0.1); border-left-color: #4dabf7;">
        <p>✨ Məqsəd: öyrənməni real həyatla birləşdirmək</p>
      </div>

      <h4>➕ Əlavə inkişaf proqramları</h4>
      <ul class="m-bento-list">
        <li><i class="fas fa-star" style="color:#4dabf7"></i> Üzgüçülük</li>
        <li><i class="fas fa-star" style="color:#4dabf7"></i> Futbol / Gym</li>
        <li><i class="fas fa-star" style="color:#4dabf7"></i> Şahmat və məntiq</li>
        <li><i class="fas fa-star" style="color:#4dabf7"></i> STEAM və laboratoriya dərsləri</li>
        <li><i class="fas fa-star" style="color:#4dabf7"></i> Rəsm və keramika</li>
        <li><i class="fas fa-star" style="color:#4dabf7"></i> Drama və rəqs</li>
        <li><i class="fas fa-star" style="color:#4dabf7"></i> Piano və musiqi</li>
        <li><i class="fas fa-star" style="color:#4dabf7"></i> Kompüter elmləri</li>
        <li><i class="fas fa-star" style="color:#4dabf7"></i> Native speaker dərsləri</li>
        <li><i class="fas fa-star" style="color:#4dabf7"></i> Azərbaycan dili</li>
        <li><i class="fas fa-star" style="color:#4dabf7"></i> Rus dili</li>
        <li><i class="fas fa-star" style="color:#4dabf7"></i> German / French / Chinese (tanışlıq səviyyəsi)</li>
      </ul>

      <h4>🏢 Staj və real təcrübə imkanı</h4>
      <p>Şagirdlər üçün yarım gün əsaslı praktik təcrübə (internship) imkanı yaradılır. İmkanlar:</p>
      <ul class="m-bento-list">
        <li><i class="fas fa-check" style="color:#4dabf7"></i> Şagirdin ilgi sahəsinə uyğun müəssisələrdə təcrübə</li>
        <li><i class="fas fa-check" style="color:#4dabf7"></i> Real iş mühiti ilə tanışlıq</li>
        <li><i class="fas fa-check" style="color:#4dabf7"></i> Peşə yönümlü bacarıqların inkişafı</li>
        <li><i class="fas fa-check" style="color:#4dabf7"></i> Karyera istiqamətinin erkən formalaşdırılması</li>
      </ul>
    </div>
  </div>

  <!-- ACCORDION 3: 9-CU SINIF VƏ SONRASI -->
  <div class="m-acc-item" onclick="this.classList.toggle('active')">
    <div class="m-acc-header">
      <div class="m-acc-icon" style="background: linear-gradient(135deg, #fcc419, #e67700); box-shadow: 0 10px 20px rgba(230, 119, 0, 0.3);"><i class="fas fa-graduation-cap"></i></div>
      <div class="m-acc-title-group">
        <h3 class="m-acc-title">9-CU SINIF VƏ SONRASI</h3>
        <p class="m-acc-subtitle">Universitetə Hazırlıq Proqramı</p>
      </div>
      <div class="m-acc-toggle"><i class="fas fa-chevron-down"></i></div>
    </div>
    <div class="m-acc-body m-bento-content" onclick="event.stopPropagation()">
      <p>Bu mərhələdə şagirdlər artıq gələcək universitet və karyera yoluna yönləndirilir. Hər bir şagird üçün fərdi təhsil planı və akademik mentor dəstəyi ilə sistemli inkişaf təmin edilir.</p>

      <h4>👩‍🏫 Sistem:</h4>
      <ul class="m-bento-list">
        <li><i class="fas fa-check" style="color:#fcc419"></i> Hər şagird üçün fərdi karyera koçu (coach)</li>
        <li><i class="fas fa-check" style="color:#fcc419"></i> Akademik mentorluq sistemi</li>
        <li><i class="fas fa-check" style="color:#fcc419"></i> Kariyera mərkəzi dəstəyi</li>
        <li><i class="fas fa-check" style="color:#fcc419"></i> Universitet istiqamətləndirmə proqramı</li>
      </ul>

      <h4>📚 Beynəlxalq imtahan hazırlığı:</h4>
      <ul class="m-bento-list">
        <li><i class="fas fa-certificate" style="color:#fcc419"></i> IELTS</li>
        <li><i class="fas fa-certificate" style="color:#fcc419"></i> TOEFL</li>
        <li><i class="fas fa-certificate" style="color:#fcc419"></i> SAT</li>
        <li><i class="fas fa-certificate" style="color:#fcc419"></i> YÖS</li>
        <li><i class="fas fa-certificate" style="color:#fcc419"></i> A Level proqramı</li>
      </ul>

      <h4>🎓 Əlavə imkanlar:</h4>
      <ul class="m-bento-list">
        <li><i class="fas fa-star" style="color:#fcc419"></i> Cambridge və beynəlxalq akademik sertifikatlar</li>
        <li><i class="fas fa-star" style="color:#fcc419"></i> Güclü akademik portfel hazırlanması</li>
        <li><i class="fas fa-star" style="color:#fcc419"></i> Universitet qəbul strategiyası</li>
      </ul>

      <h4>📖 DİM imtahan hazırlığı və “Qızıl / Qırmızı Diplom” imkanı</h4>
      <p>Şagirdlər eyni zamanda milli təhsil sistemi üzrə də hazırlıq keçirlər:</p>
      <ul class="m-bento-list">
        <li><i class="fas fa-check" style="color:#fcc419"></i> Dövlət İmtahan Mərkəzi (DİM) imtahanlarına hazırlıq</li>
        <li><i class="fas fa-check" style="color:#fcc419"></i> Yüksək nəticə əldə edən şagirdlər üçün Qırmızı Diplom (fərqlənmə diplomu) imkanı</li>
        <li><i class="fas fa-check" style="color:#fcc419"></i> Güclü akademik nəticə və universitetə yüksək balla qəbul strategiyası</li>
      </ul>

      <div class="m-bento-highlight" style="background: rgba(252, 196, 25, 0.1); border-left-color: #fcc419;">
        <p>🌍 Məqsəd: Şagirdlərin həm yerli, həm də beynəlxalq universitetlərə maksimum səviyyədə hazırlaşdırılması və uğurlu gələcək qurmasıdır.</p>
      </div>
    </div>
  </div>

</div>
""" + trailing

        final_html = content[:grid_start_idx] + new_html + content[grid_end_idx:]
        with open('lisey2.html', 'w', encoding='utf-8') as f:
            f.write(final_html)
        print("Successfully updated the accordion.")
    else:
        print("Could not find grid start or end.")
else:
    print("Failed finding start marker.")
