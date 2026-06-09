import re
import glob

html_files = glob.glob('*.html') + glob.glob('live_vercel_code/*.html')

for file in set(html_files):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Navbar text
    content = content.replace('Victory Colleges \n', 'Victory Colleges by Evrika \n')
    content = content.replace('Victory Colleges</span', 'Victory Colleges by Evrika</span')
    # Prevent duplication
    content = content.replace('Victory Colleges by Evrika by Evrika', 'Victory Colleges by Evrika')
    content = content.replace('Evrika Victory Colleges by Evrika', 'Victory Colleges by Evrika')
    content = content.replace('Evrika Victory Colleges', 'Victory Colleges by Evrika')
    content = content.replace('Victory Colleges by Evrika by Evrika', 'Victory Colleges by Evrika')
    
    # 2. In index.html specific things
    if 'index.html' in file:
        content = content.replace('EVRIKA EDUHOME', 'VICTORY COLLEGES')
        content = content.replace('Eduhome', 'Victory Colleges by Evrika')
        content = content.replace('+994 10 300 30 05', '+994 55 519 99 32')
        content = content.replace('Baləmi Dadaşov küçəsi, Zümrüd Residence Kompleksi', 'Baləmi Dadaşov küçəsi, Zümrüd Residence Kompleksi')

    # 3. In schools.html
    if 'schools.html' in file:
        content = content.replace('eduhome', 'Victory Colleges by Evrika')
        content = content.replace('Eduhome', 'Victory Colleges by Evrika')

    # Write changes
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# 4. Victory HTML content rewrite
with open('victory.html', 'r', encoding='utf-8') as f:
    vic = f.read()

# Exact text
vic_exact_text = """<div class="story-content">
          <p class="story-p" data-i18n="branch-eduhome-desc">
            <strong style="color:white; font-size: 1.2rem;">📌 Akademik Hazırlıq Proqramları</strong><br><br>
            Victory Colleges by Evrika tələbələrə beynəlxalq universitetlərə qəbul olmaq üçün müxtəlif akademik hazırlıq proqramları təqdim edir. Tədris proqramlarımız dünyanın aparıcı universitetlərinin qəbul tələblərinə uyğun şəkildə hazırlanıb.
            <br><br>
            Tələbələr aşağıdakı istiqamətlər üzrə hazırlıq keçə bilərlər:<br><br>
            <ul style="color: var(--text-muted); line-height: 1.8; margin-left: 20px; margin-bottom: 20px;">
                <li>SAT Hazırlığı</li>
                <li>SAT + Attestat Proqramı</li>
                <li>IELTS Hazırlığı</li>
                <li>TOEFL Hazırlığı</li>
                <li>Foundation Proqramları</li>
                <li>Beynəlxalq universitetlərə qəbul üçün akademik ingilis dili hazırlığı</li>
                <li>Pearson və A-Level istiqamətləri üzrə hazırlıq proqramları</li>
                <li>Çin universitetlərinə qəbul üçün beynəlxalq CSCA hazırlıq proqramları</li>
            </ul>
            Bundan əlavə, tələbələr xaricdə təhsil üzrə peşəkar konsultasiya, universitet seçimi, sənəd hazırlığı, təqaüd müraciətləri və universitet yerləşdirmə xidmətlərindən də faydalana bilirlər.
            <br><br>
            Məqsədimiz tələbələrə sadəcə imtahana hazırlaşmaq deyil, onları dünyanın ən yaxşı universitetlərinə qəbul olmaq üçün kompleks şəkildə hazırlamaqdır.
            <br><br>
            <strong style="color:white; font-size: 1.2rem;">📌 Foundation Proqramı</strong><br><br>
            Victory Colleges by Evrika tələbələrə beynəlxalq standartlara uyğun Foundation proqramı təqdim edir. Bu proqram vasitəsilə tələbələr xarici universitetlərə hazırlıq keçərək birbaşa bakalavr təhsilinə başlamaq imkanı əldə edirlər. Foundation proqramının əsas üstünlüyü ondan ibarətdir ki, tələbələr xaricdə yüksək məbləğdə vəsait xərcləmədən hazırlıq mərhələsini Azərbaycanda tamamlaya və daha sonra universitet təhsilinə davam edə bilirlər. Proqram beynəlxalq Level 3 kvalifikasiyası əsasında qurulur və tələbələrin akademik, dil və peşəkar bacarıqlarını inkişaf etdirməyə yönəlib.
            <br><br>
            <strong style="color:white; font-size: 1.2rem;">📌 Education Ecosystem – Tam Təhsil Ekosistemi</strong><br><br>
            Victory Colleges by Evrika sadəcə xaricdə təhsil xidməti təqdim edən bir mərkəz deyil. Məqsəd tələbələrin məktəb dövründən başlayaraq universitet qəbuluna və beynəlxalq təhsilə qədər bütün mərhələləri əhatə edən vahid təhsil ekosistemi yaratmaqdır. Bu ekosistem daxilində tələbələr lisey təhsili, attestat proqramı, SAT hazırlığı, karyera planlaması, xaricdə universitet yerləşdirməsi və Foundation proqramlarını bir mərkəzdə əldə edə bilirlər. Beləliklə, tələbə bütün akademik inkişaf yolunu sistemli və ardıcıl şəkildə planlaşdıra bilir.
          </p>
        </div>"""

vic = re.sub(r'<div class="story-content">.*?</div>\s*</div>\s*</section>', vic_exact_text + '\n      </div>\n    </section>', vic, flags=re.DOTALL)

# 5. Fix Color to rgb(14, 27, 65)
# Ensure --accent is #0e1b41 and rgba(14,27,65)
vic = vic.replace('--accent:#eab308', '--accent:#0e1b41')
vic = vic.replace('--accent:#3B82F6', '--accent:#0e1b41')
vic = vic.replace('rgba(250,204,21,', 'rgba(14,27,65,')
vic = vic.replace('rgba(59,130,246,', 'rgba(14,27,65,')
vic = vic.replace('#fbbf24', '#0e1b41')
vic = vic.replace('#2563EB', '#0e1b41')

# 6. Ensure footer phone
vic = re.sub(r'\+994 \d{2} \d{3} \d{2} \d{2}', '+994 55 519 99 32', vic)

with open('victory.html', 'w', encoding='utf-8') as f:
    f.write(vic)

print("Quick fixes applied!")
