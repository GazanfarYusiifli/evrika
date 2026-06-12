with open('victory.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<div class="story-content">'
end_marker = '</section>'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    new_content = """<div class="story-content" style="max-width: 900px; margin: 0 auto;">
          <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 20px; padding: 40px; margin-bottom: 30px;">
            <h3 style="color: white; font-size: 1.8rem; font-weight: 800; margin-bottom: 20px; display: flex; align-items: center; gap: 10px;">
              <span style="background: var(--accent); color: white; width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem;"><i class="fas fa-graduation-cap"></i></span>
              Akademik Hazırlıq Proqramları
            </h3>
            <p class="story-p" data-i18n="branch-eduhome-desc" style="color: rgba(255, 255, 255, 0.85); font-size: 1.05rem; line-height: 1.8; margin-bottom: 25px;">
              Victory Colleges by Evrika tələbələrə beynəlxalq universitetlərə qəbul olmaq üçün müxtəlif akademik hazırlıq proqramları təqdim edir. Tədris proqramlarımız dünyanın aparıcı universitetlərinin qəbul tələblərinə uyğun şəkildə hazırlanıb.
            </p>
            <p style="color: white; font-weight: 700; margin-bottom: 15px; font-size: 1.1rem;">Tələbələr aşağıdakı istiqamətlər üzrə hazırlıq keçə bilərlər:</p>
            <ul style="color: var(--text-muted); line-height: 2; margin-left: 0; margin-bottom: 30px; list-style: none; display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 12px;">
                <li style="background: rgba(14,27,65, 0.2); padding: 12px 20px; border-radius: 10px; border: 1px solid rgba(14,27,65, 0.4); display: flex; align-items: center; gap: 10px;"><i class="fas fa-check-circle" style="color: var(--accent-light);"></i> SAT Hazırlığı</li>
                <li style="background: rgba(14,27,65, 0.2); padding: 12px 20px; border-radius: 10px; border: 1px solid rgba(14,27,65, 0.4); display: flex; align-items: center; gap: 10px;"><i class="fas fa-check-circle" style="color: var(--accent-light);"></i> SAT + Attestat Proqramı</li>
                <li style="background: rgba(14,27,65, 0.2); padding: 12px 20px; border-radius: 10px; border: 1px solid rgba(14,27,65, 0.4); display: flex; align-items: center; gap: 10px;"><i class="fas fa-check-circle" style="color: var(--accent-light);"></i> IELTS Hazırlığı</li>
                <li style="background: rgba(14,27,65, 0.2); padding: 12px 20px; border-radius: 10px; border: 1px solid rgba(14,27,65, 0.4); display: flex; align-items: center; gap: 10px;"><i class="fas fa-check-circle" style="color: var(--accent-light);"></i> TOEFL Hazırlığı</li>
                <li style="background: rgba(14,27,65, 0.2); padding: 12px 20px; border-radius: 10px; border: 1px solid rgba(14,27,65, 0.4); display: flex; align-items: center; gap: 10px;"><i class="fas fa-check-circle" style="color: var(--accent-light);"></i> Foundation Proqramları</li>
                <li style="background: rgba(14,27,65, 0.2); padding: 12px 20px; border-radius: 10px; border: 1px solid rgba(14,27,65, 0.4); display: flex; align-items: center; gap: 10px;"><i class="fas fa-check-circle" style="color: var(--accent-light);"></i> Beynəlxalq universitetlərə qəbul üçün akademik ingilis dili hazırlığı</li>
                <li style="background: rgba(14,27,65, 0.2); padding: 12px 20px; border-radius: 10px; border: 1px solid rgba(14,27,65, 0.4); display: flex; align-items: center; gap: 10px;"><i class="fas fa-check-circle" style="color: var(--accent-light);"></i> Pearson və A-Level istiqamətləri üzrə hazırlıq proqramları</li>
                <li style="background: rgba(14,27,65, 0.2); padding: 12px 20px; border-radius: 10px; border: 1px solid rgba(14,27,65, 0.4); display: flex; align-items: center; gap: 10px;"><i class="fas fa-check-circle" style="color: var(--accent-light);"></i> Çin universitetlərinə qəbul üçün beynəlxalq CSCA hazırlıq proqramları</li>
            </ul>
            <p style="color: rgba(255, 255, 255, 0.85); font-size: 1.05rem; line-height: 1.8; margin-bottom: 20px; padding: 20px; border-left: 4px solid var(--accent); background: rgba(14,27,65,0.1); border-radius: 0 10px 10px 0;">
              Bundan əlavə, tələbələr xaricdə təhsil üzrə peşəkar konsultasiya, universitet seçimi, sənəd hazırlığı, təqaüd müraciətləri və universitet yerləşdirmə xidmətlərindən də faydalana bilirlər.
            </p>
            <p style="color: white; font-size: 1.1rem; line-height: 1.8; font-weight: 600;">
              Məqsədimiz tələbələrə sadəcə imtahana hazırlaşmaq deyil, onları dünyanın ən yaxşı universitetlərinə qəbul olmaq üçün kompleks şəkildə hazırlamaqdır.
            </p>
          </div>

          <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 20px; padding: 40px; margin-bottom: 30px; position: relative; overflow: hidden;">
            <div style="position: absolute; top: -50px; right: -50px; width: 150px; height: 150px; background: var(--accent); filter: blur(50px); opacity: 0.2; pointer-events: none;"></div>
            <h3 style="color: white; font-size: 1.6rem; font-weight: 800; margin-bottom: 20px; display: flex; align-items: center; gap: 10px;">
              <span style="color: var(--accent-light); font-size: 1.5rem;"><i class="fas fa-university"></i></span>
              Foundation Proqramı
            </h3>
            <p style="color: rgba(255, 255, 255, 0.85); font-size: 1.05rem; line-height: 1.8;">
              Victory Colleges by Evrika tələbələrə beynəlxalq standartlara uyğun Foundation proqramı təqdim edir. Bu proqram vasitəsilə tələbələr xarici universitetlərə hazırlıq keçərək birbaşa bakalavr təhsilinə başlamaq imkanı əldə edirlər. Foundation proqramının əsas üstünlüyü ondan ibarətdir ki, tələbələr xaricdə yüksək məbləğdə vəsait xərcləmədən hazırlıq mərhələsini Azərbaycanda tamamlaya və daha sonra universitet təhsilinə davam edə bilirlər. Proqram beynəlxalq Level 3 kvalifikasiyası əsasında qurulur və tələbələrin akademik, dil və peşəkar bacarıqlarını inkişaf etdirməyə yönəlib.
            </p>
          </div>

          <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 20px; padding: 40px; position: relative; overflow: hidden;">
            <div style="position: absolute; bottom: -50px; left: -50px; width: 150px; height: 150px; background: var(--accent-light); filter: blur(50px); opacity: 0.15; pointer-events: none;"></div>
            <h3 style="color: white; font-size: 1.6rem; font-weight: 800; margin-bottom: 20px; display: flex; align-items: center; gap: 10px;">
              <span style="color: var(--accent-light); font-size: 1.5rem;"><i class="fas fa-globe-americas"></i></span>
              Education Ecosystem – Tam Təhsil Ekosistemi
            </h3>
            <p style="color: rgba(255, 255, 255, 0.85); font-size: 1.05rem; line-height: 1.8;">
              Victory Colleges by Evrika sadəcə xaricdə təhsil xidməti təqdim edən bir mərkəz deyil. Məqsəd tələbələrin məktəb dövründən başlayaraq universitet qəbuluna və beynəlxalq təhsilə qədər bütün mərhələləri əhatə edən vahid təhsil ekosistemi yaratmaqdır. Bu ekosistem daxilində tələbələr lisey təhsili, attestat proqramı, SAT hazırlığı, karyera planlaması, xaricdə universitet yerləşdirməsi və Foundation proqramlarını bir mərkəzdə əldə edə bilirlər. Beləliklə, tələbə bütün akademik inkişaf yolunu sistemli və ardıcıl şəkildə planlaşdıra bilir.
            </p>
          </div>
        </div>
      </div>
"""
    html = html[:start_idx] + new_content + html[end_idx:]
    with open('victory.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Replaced!")
else:
    print("Not found.")
