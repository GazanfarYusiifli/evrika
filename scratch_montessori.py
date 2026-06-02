import re

with open('lisey2.html', 'r', encoding='utf-8') as f:
    content = f.read()

montessori_html = """
<div class="montessori-details" style="margin-top: 40px; color: rgba(255,255,255,0.85); font-size: 1.1rem; line-height: 1.7;">
  <style>
    .mont-acc { margin-bottom: 15px; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; overflow: hidden; }
    .mont-acc-header { background: rgba(0,0,0,0.2); padding: 18px 25px; cursor: pointer; display: flex; justify-content: space-between; align-items: center; font-weight: 700; color: #fff; font-size: 1.1rem; transition: background 0.3s; }
    .mont-acc-header:hover { background: rgba(0,0,0,0.3); }
    .mont-acc-body { padding: 0 25px; max-height: 0; overflow: hidden; transition: all 0.4s ease; background: rgba(0,0,0,0.1); }
    .mont-acc.active .mont-acc-body { padding: 25px; max-height: 2000px; }
    .mont-acc.active .mont-acc-header .fa-chevron-down { transform: rotate(180deg); }
    .mont-acc-body h4 { color: #ff6b6b; margin: 20px 0 10px; font-size: 1.2rem; }
    .mont-acc-body h4:first-child { margin-top: 0; }
    .mont-acc-body ul { list-style: none; padding-left: 0; margin-bottom: 15px; }
    .mont-acc-body ul li { position: relative; padding-left: 20px; margin-bottom: 8px; }
    .mont-acc-body ul li::before { content: "•"; color: #ff6b6b; position: absolute; left: 0; font-size: 1.2rem; line-height: 1; }
    .mont-acc-body p { margin-bottom: 15px; }
  </style>

  <div class="mont-acc">
    <div class="mont-acc-header" onclick="this.parentElement.classList.toggle('active')">
      İBTİDAİ TƏHSİL (Lower & Upper Elementary) <i class="fas fa-chevron-down" style="transition:0.3s;"></i>
    </div>
    <div class="mont-acc-body">
      <h4>Lower Elementary (6–9 yaş)</h4>
      <p>İbtidai təhsil mərhələsi uşağın öyrənmə sevgisinin formalaşdığı, təməl akademik və sosial bacarıqların inkişaf etdiyi ən vacib dövrdür. Montessori yanaşması ilə uşaqlar fərdi sürətinə uyğun, stresssiz və maraq əsaslı şəkildə öyrənirlər.</p>
      
      <h4>📚 Tədris sistemi:</h4>
      <ul>
        <li>Montessori “Work Cycle” (fasiləsiz öyrənmə modeli)</li>
        <li>Riyaziyyat</li>
        <li>İngilis dili</li>
        <li>Rus dili (ehtiyaca görə)</li>
        <li>Cosmic Education (bütün elmlərin inteqrasiyası)</li>
      </ul>

      <h4>🌍 Cosmic Education daxilində:</h4>
      <p>Coğrafiya, tarix, biologiya, fizika, kimya, astronomiya, ekologiya və geologiya bir-biri ilə əlaqəli şəkildə öyrədilir.</p>

      <h4>📖 Tədris yanaşması:</h4>
      <ul>
        <li>Cambridge tədris materiallarından istifadə</li>
        <li>Beynəlxalq standartlara uyğun akademik baza</li>
        <li>Dil və kommunikasiya bacarıqlarının inkişafı</li>
      </ul>

      <h4>🌟 Əlavə fəaliyyətlər:</h4>
      <ul>
        <li>Üzgüçülük, futbol, gimnastika</li>
        <li>Şahmat və STEAM</li>
        <li>Rəsm, keramika, musiqi, piano</li>
        <li>Drama və sosial bacarıqlar</li>
        <li>Kompüter elmləri</li>
        <li>Native speaker dərsləri</li>
      </ul>
      <p><strong>✨ Məqsəd:</strong> Müstəqil, özünə güvənən və çoxşaxəli inkişaf etmiş uşaqlar yetişdirmək</p>

      <hr style="border:0; border-top:1px solid rgba(255,255,255,0.1); margin: 30px 0;">

      <h4>Upper Elementary (9–12 yaş)</h4>
      <p>Bu mərhələ uşağın daha analitik düşünməyə başladığı, akademik biliklərin dərinləşdiyi və məsuliyyət hissinin gücləndiyi dövrdür.</p>

      <h4>📚 Akademik istiqamət:</h4>
      <ul>
        <li>İngilis dili (Grammar, Writing, Reading, Speaking)</li>
        <li>Riyaziyyat və məntiq</li>
        <li>Elm fənləri (Physics, Biology, Chemistry)</li>
        <li>Social Studies və Azerbaijan tarixi</li>
        <li>Laboratoriya və STEAM dərsləri</li>
      </ul>

      <h4>🌍 Dil inkişafı:</h4>
      <ul>
        <li>İngilis dili intensiv proqram</li>
        <li>Rus dili</li>
        <li>German / French / Chinese tanışlıq səviyyəsi</li>
      </ul>

      <h4>📖 Beynəlxalq hazırlıq:</h4>
      <ul>
        <li>Cambridge Exam Preparation</li>
        <li>Akademik yazı və oxu bacarıqları</li>
        <li>Analitik düşünmə və problem həll etmə</li>
      </ul>

      <h4>🎨 İnkişaf fəaliyyətləri:</h4>
      <ul>
        <li>İdman və üzgüçülük</li>
        <li>Şahmat və logic</li>
        <li>Rəsm, keramika, drama</li>
        <li>Musiqi və piano</li>
        <li>Kompüter elmləri</li>
      </ul>
      <p><strong>✨ Məqsəd:</strong> Akademik olaraq güclü, yaradıcı və beynəlxalq düşüncəli şagirdlər yetişdirmək</p>
    </div>
  </div>

  <div class="mont-acc">
    <div class="mont-acc-header" onclick="this.parentElement.classList.toggle('active')">
      ORTA TƏHSİL (Lower & Upper Secondary, 12–15 yaş) <i class="fas fa-chevron-down" style="transition:0.3s;"></i>
    </div>
    <div class="mont-acc-body">
      <p>Bu mərhələ şagirdlərin akademik biliklərini dərinləşdirdiyi, universitet və karyera yoluna keçid etdiyi vacib inkişaf dövrüdür. Proqram Cambridge beynəlxalq kurikulumu və Montessori yanaşmasının inteqrasiyası ilə qurulmuşdur.</p>

      <h4>📚 Akademik fənlər</h4>
      <ul>
        <li>English Language & Literature</li>
        <li>Mathematics (Core & Advanced)</li>
        <li>Science (Biology, Chemistry, Physics)</li>
        <li>Global Perspectives</li>
        <li>ICT / Computer Science</li>
        <li>Social Studies</li>
      </ul>

      <h4>🌍 Bu proqram şagirdlərə qazandırır:</h4>
      <ul>
        <li>Analitik və tənqidi düşünmə</li>
        <li>Beynəlxalq akademik standart</li>
        <li>Güclü İngilis dili bazası</li>
        <li>Problem həll etmə bacarıqları</li>
      </ul>

      <h4>🔬 Proje əsaslı öyrənmə (Project-Based Learning)</h4>
      <p>Bu mərhələdə təhsil sistemi tamamilə proje əsaslı yanaşma ilə dəstəklənir.<br>Şagirdlər:</p>
      <ul>
        <li>Real problemlər üzərində çalışır</li>
        <li>Komanda işi ilə layihələr hazırlayır</li>
        <li>Araşdırma və təqdimat bacarıqları inkişaf etdirir</li>
        <li>Akademik bilikləri praktikaya tətbiq edir</li>
      </ul>
      <p><strong>✨ Məqsəd:</strong> öyrənməni real həyatla birləşdirmək</p>

      <h4>➕ Əlavə inkişaf proqramları</h4>
      <div style="display:grid; grid-template-columns: 1fr 1fr; gap:10px;">
        <div>
          <ul>
            <li>Üzgüçülük</li>
            <li>Futbol / Gym</li>
            <li>Şahmat və məntiq</li>
            <li>STEAM və laboratoriya dərsləri</li>
            <li>Rəsm və keramika</li>
          </ul>
        </div>
        <div>
          <ul>
            <li>Drama və rəqs</li>
            <li>Piano və musiqi</li>
            <li>Kompüter elmləri</li>
            <li>Native speaker dərsləri</li>
            <li>Azərbaycan dili, Rus dili</li>
            <li>German / French / Chinese (tanışlıq)</li>
          </ul>
        </div>
      </div>

      <h4>🏢 Staj və real təcrübə imkanı</h4>
      <p>Şagirdlər üçün yarım gün əsaslı praktik təcrübə (internship) imkanı yaradılır.</p>
      <ul>
        <li>Şagirdin ilgi sahəsinə uyğun müəssisələrdə təcrübə</li>
        <li>Real iş mühiti ilə tanışlıq</li>
        <li>Peşə yönümlü bacarıqların inkişafı</li>
        <li>Karyera istiqamətinin erkən formalaşdırılması</li>
      </ul>
    </div>
  </div>

  <div class="mont-acc">
    <div class="mont-acc-header" onclick="this.parentElement.classList.toggle('active')">
      🎓 9-CU SINIF VƏ SONRASI (Universitetə Hazırlıq) <i class="fas fa-chevron-down" style="transition:0.3s;"></i>
    </div>
    <div class="mont-acc-body">
      <p>Bu mərhələdə şagirdlər artıq gələcək universitet və karyera yoluna yönləndirilir. Hər bir şagird üçün fərdi təhsil planı və akademik mentor dəstəyi ilə sistemli inkişaf təmin edilir.</p>

      <h4>👩‍🏫 Sistem:</h4>
      <ul>
        <li>Hər şagird üçün fərdi karyera koçu (coach)</li>
        <li>Akademik mentorluq sistemi</li>
        <li>Kariyera mərkəzi dəstəyi</li>
        <li>Universitet istiqamətləndirmə proqramı</li>
      </ul>

      <h4>📚 Beynəlxalq imtahan hazırlığı:</h4>
      <ul>
        <li>IELTS, TOEFL, SAT, YÖS</li>
        <li>A Level proqramı</li>
      </ul>

      <h4>🎓 Əlavə imkanlar:</h4>
      <ul>
        <li>Cambridge və beynəlxalq akademik sertifikatlar</li>
        <li>Güclü akademik portfel hazırlanması</li>
        <li>Universitet qəbul strategiyası</li>
      </ul>

      <h4>📖 DİM imtahan hazırlığı və “Qızıl / Qırmızı Diplom” imkanı</h4>
      <p>Şagirdlər eyni zamanda milli təhsil sistemi üzrə də hazırlıq keçirlər:</p>
      <ul>
        <li>Dövlət İmtahan Mərkəzi (DİM) imtahanlarına hazırlıq</li>
        <li>Yüksək nəticə əldə edən şagirdlər üçün Qırmızı Diplom (fərqlənmə diplomu) imkanı</li>
        <li>Güclü akademik nəticə və universitetə yüksək balla qəbul strategiyası</li>
      </ul>

      <p><strong>🌍 Məqsəd:</strong> Şagirdlərin həm yerli, həm də beynəlxalq universitetlərə maksimum səviyyədə hazırlaşdırılması və uğurlu gələcək qurmasıdır.</p>
    </div>
  </div>

</div>
"""

target = """<p style="color:rgba(255,255,255,0.85); line-height:1.9; margin-top: 30px; font-size: 1.55rem; font-weight: 300;">Lisey daxilində I–XI siniflər üzrə Montessori sinifləri fəaliyyət göstərir.<br><br>Bu yanaşma Cambridge proqramı ilə inteqrasiya olunaraq müstəqil düşünmə və məsuliyyət bacarıqlarını inkişaf etdirir.</p>"""

if target in content:
    content = content.replace(target, target + "\n" + montessori_html)
    with open('lisey2.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated lisey2.html successfully.")
else:
    print("Could not find target string.")
