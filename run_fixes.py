import re
import glob

# Fix Victory HTML Color and Content
with open('victory.html', 'r', encoding='utf-8') as f:
    vic_html = f.read()

# Replace any old blue or yellow variables with the new specific blue
# The user wants "sari olan yerlerin yerine goy reng olsun r 14 g 27 b 65" -> rgb(14, 27, 65) -> #0e1b41
vic_html = vic_html.replace('--accent:#3B82F6', '--accent:#0e1b41')
vic_html = vic_html.replace('--accent-light:#93C5FD', '--accent-light:#1d3557')
vic_html = vic_html.replace('--accent-glow:rgba(59,130,246,0.25)', '--accent-glow:rgba(14,27,65,0.25)')
vic_html = vic_html.replace('#2563EB', '#0e1b41')
vic_html = vic_html.replace('rgba(59,130,246,', 'rgba(14,27,65,')
# Just in case yellow is still there:
vic_html = vic_html.replace('--accent:#eab308', '--accent:#0e1b41')
vic_html = vic_html.replace('--accent-light:#fef08a', '--accent-light:#1d3557')
vic_html = vic_html.replace('--accent-glow:rgba(250,204,21,0.25)', '--accent-glow:rgba(14,27,65,0.25)')
vic_html = vic_html.replace('#fbbf24', '#0e1b41')
vic_html = vic_html.replace('rgba(250,204,21,', 'rgba(14,27,65,')

# Fix footer phone in victory.html
vic_html = re.sub(r'\+994 \d{2} \d{3} \d{2} \d{2}', '+994 55 519 99 32', vic_html)

# We need to replace the content correctly. Let's find the story-content block using a more robust regex or just string splitting
parts = vic_html.split('<div class="story-content">')
if len(parts) > 1:
    before = parts[0]
    after = parts[1]
    # Find the end of this block, which is roughly after the paragraph.
    # We can just replace the first paragraph inside story-content
    end_of_p_index = after.find('</p>')
    if end_of_p_index != -1:
        new_text = """
          <p class="story-p" data-i18n="branch-eduhome-desc">
            <strong style="color:white; font-size: 1.2rem;">📌 Akademik Hazırlıq Proqramları</strong><br><br>
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
            <br><br>
            Məqsədimiz tələbələrə sadəcə imtahana hazırlaşmaq deyil, onları dünyanın ən yaxşı universitetlərinə qəbul olmaq üçün kompleks şəkildə hazırlamaqdır.
            <br><br>
            <strong style="color:white; font-size: 1.2rem;">📌 Foundation Proqramı</strong><br><br>
            Victory Colleges by Evrika tələbələrə beynəlxalq standartlara uyğun Foundation proqramı təqdim edir. Bu proqram vasitəsilə tələbələr xarici universitetlərə hazırlıq keçərək birbaşa bakalavr təhsilinə başlamaq imkanı əldə edirlər. Foundation proqramının əsas üstünlüyü ondan ibarətdir ki, tələbələr xaricdə yüksək məbləğdə vəsait xərcləmədən hazırlıq mərhələsini Azərbaycanda tamamlaya və daha sonra universitet təhsilinə davam edə bilirlər. Proqram beynəlxalq Level 3 kvalifikasiyası əsasında qurulur və tələbələrin akademik, dil və peşəkar bacarıqlarını inkişaf etdirməyə yönəlib.
            <br><br>
            <strong style="color:white; font-size: 1.2rem;">📌 Education Ecosystem – Tam Təhsil Ekosistemi</strong><br><br>
            Victory Colleges by Evrika sadəcə xaricdə təhsil xidməti təqdim edən bir mərkəz deyil. Məqsəd tələbələrin məktəb dövründən başlayaraq universitet qəbuluna və beynəlxalq təhsilə qədər bütün mərhələləri əhatə edən vahid təhsil ekosistemi yaratmaqdır. Bu ekosistem daxilində tələbələr lisey təhsili, attestat proqramı, SAT hazırlığı, karyera planlaması, xaricdə universitet yerləşdirməsi və Foundation proqramlarını bir mərkəzdə əldə edə bilirlər. Beləliklə, tələbə bütün akademik inkişaf yolunu sistemli və ardıcıl şəkildə planlaşdıra bilir.
"""
        vic_html = before + '<div class="story-content">\n' + new_text + after[end_of_p_index:]

# Also remove the whole Instagram block if it's there
vic_html = re.sub(r'<div.*?class="reveal".*?Sosial Media.*?</div>', '', vic_html, flags=re.DOTALL)
vic_html = re.sub(r'<h2 class="sec-h2" style="text-align:center;">Bizi İnstagramda <em>İzləyin</em>.*?</div>', '', vic_html, flags=re.DOTALL)

with open('victory.html', 'w', encoding='utf-8') as f:
    f.write(vic_html)
print("Updated victory.html")


# 4. Navbars replacement
# Let's replace 'Victory Colleges\n                <span class="dropdown-item-desc" data-i18n="nav-eduhome-desc">Xaricdə Təhsil və Hazırlıq</span>' 
# with 'Victory Colleges by Evrika\n                <span class="dropdown-item-desc" data-i18n="nav-eduhome-desc">Xaricdə Təhsil və Hazırlıq</span>'
html_files = glob.glob('*.html') + glob.glob('live_vercel_code/*.html')
for file in set(html_files):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple regex to replace the name in the navbar
    # Look for Victory Colleges or Eduhome Hazırlıq before the span
    content = re.sub(r'(Eduhome Hazırlıq|Victory Colleges)\s*</span', r'Victory Colleges by Evrika</span', content)
    content = re.sub(r'(Eduhome Hazırlıq|Victory Colleges)</span><span class="acc-desc"', r'Victory Colleges by Evrika</span><span class="acc-desc"', content)
    
    # 5. Fix schools.html specifically
    if 'schools.html' in file:
        content = content.replace('Eduhome', 'Victory Colleges by Evrika')
        content = content.replace('Victory Colleges', 'Victory Colleges by Evrika')
        # avoid duplicating "by Evrika by Evrika"
        content = content.replace('by Evrika by Evrika', 'by Evrika')

    # 6. Fix index.html card
    if 'index.html' in file:
        # replace the address/title
        content = content.replace('Evrika Eduhome Hazırlıq Mərkəzi', 'Victory Colleges by Evrika')
        content = content.replace('Victory Colleges Hazırlıq Mərkəzi', 'Victory Colleges by Evrika')
        content = content.replace('Victory Colleges Mərkəzi', 'Victory Colleges by Evrika')
        content = content.replace('Baləmi Dadaşov küçəsi, Zümrüd Residence Kompleksi', 'Baləmi Dadaşov küçəsi, Zümrüd Residence Kompleksi')
        # Fix the old phone number
        content = content.replace('+994 10 300 30 05', '+994 55 519 99 32')
        content = content.replace('Eduhome', 'Victory Colleges by Evrika')
        content = content.replace('Victory Colleges by Evrika.html', 'victory.html')
        content = content.replace('register-Victory Colleges by Evrika.html', 'register-victory.html')
        content = content.replace('Victory Colleges by Evrika by Evrika', 'Victory Colleges by Evrika')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated all other requirements")
