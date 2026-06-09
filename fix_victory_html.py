import re

with open('victory.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Title & Meta
html = html.replace('<title>Eduhome Hazırlıq Mərkəzi | Evrika Təhsil Ekosistemi</title>', '<title>Victory Colleges by Evrika | Evrika Təhsil Ekosistemi</title>')
html = html.replace('Eduhome Hazırlıq Mərkəzi', 'Victory Colleges by Evrika')
html = html.replace('Eduhome Hazırlıq', 'Victory Colleges')
html = html.replace('Eduhome', 'Victory Colleges')

# 2. Update Theme Colors
old_root = ':root { --accent:#eab308; --accent-light:#fef08a; --accent-glow:rgba(250,204,21,0.25); --navy:#0a0a05; --navy-mid:#141200; --text:#e8eaf2; --text-muted:#a3a39e; --surface:rgba(255,255,255,0.03); --border:rgba(255,255,255,0.08); }'
new_root = ':root { --accent:#3B82F6; --accent-light:#93C5FD; --accent-glow:rgba(59,130,246,0.25); --navy:#020617; --navy-mid:#0f172a; --text:#f8fafc; --text-muted:#94a3b8; --surface:rgba(255,255,255,0.03); --border:rgba(255,255,255,0.08); }'
html = html.replace(old_root, new_root)

# Replace RGB values of yellow with blue in specific spots
html = html.replace('rgba(250,204,21,', 'rgba(59,130,246,')
html = html.replace('#fbbf24', '#2563EB')

# 3. Replace content
content_to_replace_regex = r'<div class="story-content">.*?</div>\s*</div>\s*</section>'
new_content = '''<div class="story-content">
          <p class="story-p" data-i18n="branch-eduhome-desc">
            Victory Colleges by Evrika tələbələrə beynəlxalq universitetlərə qəbul olmaq üçün müxtəlif akademik hazırlıq proqramları təqdim edir. Tədris proqramlarımız dünyanın aparıcı universitetlərinin qəbul tələblərinə uyğun şəkildə hazırlanıb.
            <br><br>
            Tələbələr aşağıdakı istiqamətlər üzrə hazırlıq keçə bilərlər:<br>
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
            Məqsədimiz tələbələrə sadəcə imtahana hazırlaşmaq deyil, onları dünyanın ən yaxşı universitetlərinə qəbul olmaq üçün kompleks şəkildə hazırlamaqdır.
            <br><br>
            <strong style="color:white; font-size: 1.2rem;">📌 Foundation Proqramı</strong><br>
            Victory Colleges by Evrika tələbələrə beynəlxalq standartlara uyğun Foundation proqramı təqdim edir. Bu proqram vasitəsilə tələbələr xarici universitetlərə hazırlıq keçərək birbaşa bakalavr təhsilinə başlamaq imkanı əldə edirlər. Foundation proqramının əsas üstünlüyü ondan ibarətdir ki, tələbələr xaricdə yüksək məbləğdə vəsait xərcləmədən hazırlıq mərhələsini Azərbaycanda tamamlaya və daha sonra universitet təhsilinə davam edə bilirlər. Proqram beynəlxalq Level 3 kvalifikasiyası əsasında qurulur və tələbələrin akademik, dil və peşəkar bacarıqlarını inkişaf etdirməyə yönəlib.
            <br><br>
            <strong style="color:white; font-size: 1.2rem;">📌 Education Ecosystem – Tam Təhsil Ekosistemi</strong><br>
            Victory Colleges by Evrika sadəcə xaricdə təhsil xidməti təqdim edən bir mərkəz deyil. Məqsəd tələbələrin məktəb dövründən başlayaraq universitet qəbuluna və beynəlxalq təhsilə qədər bütün mərhələləri əhatə edən vahid təhsil ekosistemi yaratmaqdır. Bu ekosistem daxilində tələbələr lisey təhsili, attestat proqramı, SAT hazırlığı, karyera planlaması, xaricdə universitet yerləşdirməsi və Foundation proqramlarını bir mərkəzdə əldə edə bilirlər. Beləliklə, tələbə bütün akademik inkişaf yolunu sistemli və ardıcıl şəkildə planlaşdıra bilir.
          </p>
        </div>
      </div>
    </section>'''

html = re.sub(content_to_replace_regex, new_content, html, flags=re.DOTALL)

# 4. Remove Instagram embeds completely
ig_regex = r'<!-- Instagram Post.*?</blockquote>\s*</div>\s*</div>'
html = re.sub(ig_regex, '', html, flags=re.DOTALL)

# Also remove any remaining blockquote class="instagram-media"
ig_blockquote_regex = r'<blockquote class="instagram-media".*?</blockquote>'
html = re.sub(ig_blockquote_regex, '', html, flags=re.DOTALL)

# Update phone number
html = html.replace('+994 50 254 53 53', '+994 55 519 99 32')
html = html.replace('+994 51 254 53 53', '+994 55 519 99 32')
html = html.replace('+994 50 354 53 53', '+994 55 519 99 32')
html = html.replace('+994 55 254 53 53', '+994 55 519 99 32')

with open('victory.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated victory.html")
