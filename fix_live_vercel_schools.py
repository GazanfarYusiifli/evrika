import re

def fix_live_vercel_schools_page():
    # Update live_vercel_code/schools.html
    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/live_vercel_code/schools.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Apply all previous navbar and footer fixes
    nav_replacements = [
        (r'<a href="index\.html">Ana Səhifə</a>', r'<a href="index.html" data-i18n="nav-home">Ana Səhifə</a>'),
        (r'<a href="about\.html">Haqqımızda</a>', r'<a href="about.html" data-i18n="nav-about">Haqqımızda</a>'),
        (r'<a href="schools\.html">Akademik İstiqamətlər</a>', r'<a href="schools.html" data-i18n="nav-academic">Akademik İstiqamətlər</a>'),
        (r'<a href="vacancy\.html">Vakansiya &amp; Təcrübə</a>', r'<a href="vacancy.html" data-i18n="nav-vacancy">Vakansiya &amp; Təcrübə</a>'),
        (r'<a href="jurnal\.html">Evrika Jurnalı</a>', r'<a href="jurnal.html" data-i18n="nav-journal">Evrika Jurnalı</a>'),
        (r'<a href="contact\.html">Əlaqə</a>', r'<a href="contact.html" data-i18n="nav-contact">Əlaqə</a>'),
        
        (r'(<div class="accordion-header"[^>]*>)\s*Haqqımızda\s*', r'\1<span data-i18n="nav-about">Haqqımızda</span>'),
        (r'(<div class="accordion-header"[^>]*>)\s*Akademik İstiqamətlər\s*', r'\1<span data-i18n="nav-academic">Akademik İstiqamətlər</span>'),
        (r'(<div class="accordion-header"[^>]*>)\s*Vakansiya &amp; Təcrübə\s*', r'\1<span data-i18n="nav-vacancy">Vakansiya &amp; Təcrübə</span>'),
        (r'<a href="jurnal\.html" class="mobile-link">\s*Evrika Jurnalı\s*</a>', r'<a href="jurnal.html" class="mobile-link" data-i18n="nav-journal">Evrika Jurnalı</a>'),
        (r'<a href="contact\.html" class="mobile-link">\s*Əlaqə\s*</a>', r'<a href="contact.html" class="mobile-link" data-i18n="nav-contact">Əlaqə</a>'),
        
        (r'<span class="acc-title">Haqqımızda</span>', r'<span class="acc-title" data-i18n="nav-about">Haqqımızda</span>'),
        (r'<span class="acc-desc">Bizim hekayəmiz</span>', r'<span class="acc-desc" data-i18n="nav-about-desc">Bizim hekayəmiz</span>'),
        (r'<span class="acc-title">Məzunlar</span>', r'<span class="acc-title" data-i18n="nav-alumni">Məzunlar</span>'),
        (r'<span class="acc-desc">Fəxrlərimiz</span>', r'<span class="acc-desc" data-i18n="nav-alumni-desc">Fəxrlərimiz</span>'),
        (r'<span class="acc-title">Uğurlar</span>', r'<span class="acc-title" data-i18n="nav-achievements">Uğurlar</span>'),
        (r'<span class="acc-desc">Nailiyyətlərimiz</span>', r'<span class="acc-desc" data-i18n="nav-achievements-desc">Nailiyyətlərimiz</span>'),
        (r'<span class="acc-title">Xəbərlər</span>', r'<span class="acc-title" data-i18n="nav-news">Xəbərlər</span>'),
        (r'<span class="acc-desc">Ən son yeniliklər</span>', r'<span class="acc-desc" data-i18n="nav-news-desc">Ən son yeniliklər</span>'),
        (r'<span class="dropdown-item-title">Haqqımızda</span>', r'<span class="dropdown-item-title" data-i18n="nav-about">Haqqımızda</span>'),
        (r'<span class="dropdown-item-desc">Bizim hekayəmiz</span>', r'<span class="dropdown-item-desc" data-i18n="nav-about-desc">Bizim hekayəmiz</span>'),
        (r'<span class="dropdown-item-title">Məzunlar</span>', r'<span class="dropdown-item-title" data-i18n="nav-alumni">Məzunlar</span>'),
        (r'<span class="dropdown-item-desc">Fəxrlərimiz</span>', r'<span class="dropdown-item-desc" data-i18n="nav-alumni-desc">Fəxrlərimiz</span>'),
        (r'<span class="dropdown-item-title">Uğurlar</span>', r'<span class="dropdown-item-title" data-i18n="nav-achievements">Uğurlar</span>'),
        (r'<span class="dropdown-item-desc">Nailiyyətlərimiz</span>', r'<span class="dropdown-item-desc" data-i18n="nav-achievements-desc">Nailiyyətlərimiz</span>'),
        (r'<span class="dropdown-item-title">Xəbərlər</span>', r'<span class="dropdown-item-title" data-i18n="nav-news">Xəbərlər</span>'),
        (r'<span class="dropdown-item-desc">Ən son yeniliklər</span>', r'<span class="dropdown-item-desc" data-i18n="nav-news-desc">Ən son yeniliklər</span>'),

        (r'<span class="acc-title">Evrika BETL Nərimanov</span>', r'<span class="acc-title" data-i18n="nav-lisey1">Evrika BETL Nərimanov</span>'),
        (r'<span class="acc-desc">Elm və Texnologiya Mərkəzi</span>', r'<span class="acc-desc" data-i18n="nav-lisey1-desc">Elm və Texnologiya Mərkəzi</span>'),
        (r'<span class="acc-title">Evrika BETL Gənclik</span>', r'<span class="acc-title" data-i18n="nav-lisey2">Evrika BETL Gənclik</span>'),
        (r'<span class="acc-desc">Beynəlxalq Təhsil Kampusu</span>', r'<span class="acc-desc" data-i18n="nav-lisey2-desc">Beynəlxalq Təhsil Kampusu</span>'),
        (r'<span class="acc-desc">Beynəlxalq Təhsil Müəssisəsi</span>', r'<span class="acc-desc" data-i18n="nav-lisey2-desc">Beynəlxalq Təhsil Müəssisəsi</span>'),
        (r'<span class="acc-title">Montessori Kids Academy</span>', r'<span class="acc-title" data-i18n="nav-montessori">Montessori Kids Academy</span>'),
        (r'<span class="acc-desc">Bağça və Erkən İnkişaf</span>', r'<span class="acc-desc" data-i18n="nav-montessori-desc">Bağça və Erkən İnkişaf</span>'),
        (r'<span class="acc-title">Eduhome Hazırlıq</span>', r'<span class="acc-title" data-i18n="nav-eduhome">Eduhome Hazırlıq</span>'),
        (r'<span class="acc-desc">Xaricdə Təhsil və Hazırlıq</span>', r'<span class="acc-desc" data-i18n="nav-eduhome-desc">Xaricdə Təhsil və Hazırlıq</span>'),
        (r'<span class="acc-title">Zümrüd İdman Mərkəzi</span>', r'<span class="acc-title" data-i18n="nav-zumrud">Zümrüd İdman Mərkəzi</span>'),
        (r'<span class="acc-desc">Sağlam Həyat və Fəaliyyət</span>', r'<span class="acc-desc" data-i18n="nav-zumrud-desc">Sağlam Həyat və Fəaliyyət</span>'),
        (r'<span class="dropdown-item-title">Evrika BETL Nərimanov</span>', r'<span class="dropdown-item-title" data-i18n="nav-lisey1">Evrika BETL Nərimanov</span>'),
        (r'<span class="dropdown-item-desc">Elm və Texnologiya Mərkəzi</span>', r'<span class="dropdown-item-desc" data-i18n="nav-lisey1-desc">Elm və Texnologiya Mərkəzi</span>'),
        (r'<span class="dropdown-item-title">Evrika BETL Gənclik</span>', r'<span class="dropdown-item-title" data-i18n="nav-lisey2">Evrika BETL Gənclik</span>'),
        (r'<span class="dropdown-item-desc">Beynəlxalq Təhsil Kampusu</span>', r'<span class="dropdown-item-desc" data-i18n="nav-lisey2-desc">Beynəlxalq Təhsil Kampusu</span>'),
        (r'<span class="dropdown-item-desc">Beynəlxalq Təhsil Müəssisəsi</span>', r'<span class="dropdown-item-desc" data-i18n="nav-lisey2-desc">Beynəlxalq Təhsil Müəssisəsi</span>'),
        (r'<span class="dropdown-item-title">Montessori Kids Academy</span>', r'<span class="dropdown-item-title" data-i18n="nav-montessori">Montessori Kids Academy</span>'),
        (r'<span class="dropdown-item-desc">Bağça və Erkən İnkişaf</span>', r'<span class="dropdown-item-desc" data-i18n="nav-montessori-desc">Bağça və Erkən İnkişaf</span>'),
        (r'<span class="dropdown-item-title">Eduhome Hazırlıq</span>', r'<span class="dropdown-item-title" data-i18n="nav-eduhome">Eduhome Hazırlıq</span>'),
        (r'<span class="dropdown-item-desc">Xaricdə Təhsil və Hazırlıq</span>', r'<span class="dropdown-item-desc" data-i18n="nav-eduhome-desc">Xaricdə Təhsil və Hazırlıq</span>'),
        (r'<span class="dropdown-item-title">Zümrüd İdman Mərkəzi</span>', r'<span class="dropdown-item-title" data-i18n="nav-zumrud">Zümrüd İdman Mərkəzi</span>'),
        (r'<span class="dropdown-item-desc">Sağlam Həyat və Fəaliyyət</span>', r'<span class="dropdown-item-desc" data-i18n="nav-zumrud-desc">Sağlam Həyat və Fəaliyyət</span>'),

        (r'<span class="acc-title">Karyera və Vakansiyalar</span>', r'<span class="acc-title" data-i18n="nav-vac-title">Karyera və Vakansiyalar</span>'),
        (r'<span class="acc-desc">Açıq iş elanları</span>', r'<span class="acc-desc" data-i18n="nav-vac-desc">Açıq iş elanları</span>'),
        (r'<span class="acc-title">Pedaqoji Təcrübə və İnkişaf Mərkəzi</span>', r'<span class="acc-title" data-i18n="nav-ptim-title">Pedaqoji Təcrübə və İnkişaf Mərkəzi</span>'),
        (r'<span class="acc-desc">PTİM</span>', r'<span class="acc-desc" data-i18n="nav-ptim-desc">PTİM</span>'),
        (r'<span class="dropdown-item-title">Karyera və Vakansiyalar</span>', r'<span class="dropdown-item-title" data-i18n="nav-vac-title">Karyera və Vakansiyalar</span>'),
        (r'<span class="dropdown-item-desc">Açıq iş elanları</span>', r'<span class="dropdown-item-desc" data-i18n="nav-vac-desc">Açıq iş elanları</span>'),
        (r'<span class="dropdown-item-title">Pedaqoji Təcrübə və İnkişaf Mərkəzi</span>', r'<span class="dropdown-item-title" data-i18n="nav-ptim-title">Pedaqoji Təcrübə və İnkişaf Mərkəzi</span>'),
        (r'<span class="dropdown-item-desc">PTİM</span>', r'<span class="dropdown-item-desc" data-i18n="nav-ptim-desc">PTİM</span>'),

        # Hero
        (r'TƏDRİS ŞƏBƏKƏMİZ', r'<span data-i18n="school-net">TƏDRİS ŞƏBƏKƏMİZ</span>'),
        (r'Akademik <span style="position: relative; color: var\(--white\); z-index: 1;">istiqamətlərimiz\n\s*<span style="position: absolute; bottom: 8px; left: 0; width: 100%; height: 18px; background: var\(--navy\); z-index: -1; opacity: 0\.3; border-radius: 4px;"></span>\n\s*</span>', r'<span data-i18n="school-acad">Akademik <span style="position: relative; color: var(--white); z-index: 1;">istiqamətlərimiz<span style="position: absolute; bottom: 8px; left: 0; width: 100%; height: 18px; background: var(--navy); z-index: -1; opacity: 0.3; border-radius: 4px;"></span></span></span>'),
        (r'İxtisaslaşmış təhsil müəssisələrimizlə şagirdlərimizi akademik zəfərlərə və <span\n\s*style="color: var\(--white\); font-weight: 800;">qlobal gələcəyə</span> hazırlayırıq\.', r'<span data-i18n="school-desc">İxtisaslaşmış təhsil müəssisələrimizlə şagirdlərimizi akademik zəfərlərə və <span style="color: var(--white); font-weight: 800;">qlobal gələcəyə</span> hazırlayırıq.</span>'),

        # Item 1
        (r'</span> Erkən İnkişaf', r'</span> <span data-i18n="school-early">Erkən İnkişaf</span>'),
        (r'Evrika Montessori<br>Kids Academy', r'<span data-i18n="school-mont">Evrika Montessori<br>Kids Academy</span>'),
        (r'>Azərbaycan bölməsi<', r' data-i18n="badge-az">Azərbaycan bölməsi<'),
        (r'>Türk bölməsi<', r' data-i18n="badge-tr">Türk bölməsi<'),
        (r'>Rus bölməsi<', r' data-i18n="badge-ru">Rus bölməsi<'),
        (r'>İngilis bölməsi<', r' data-i18n="badge-en">İngilis bölməsi<'),
        (r'>Toddler \(1–3 yaş\)<', r' data-i18n="badge-toddler">Toddler (1–3 yaş)<'),
        (r'>Primary \(3–6 yaş\)<', r' data-i18n="badge-primary">Primary (3–6 yaş)<'),
        (r'>Qafur Rəşad 16, Bakı, Azərbaycan<', r' data-i18n="addr-mont">Qafur Rəşad 16, Bakı, Azərbaycan<'),
        (r'>Ətraflı Kəşf Et<', r' data-i18n="btn-explore">Ətraflı Kəşf Et<'),
        (r'>Qeydiyyat\n\s*<i', r' data-i18n="nav-register">Qeydiyyat\n                  <i'),

        # Item 2
        (r'</span> Elm və Texnologiya', r'</span> <span data-i18n="school-tech">Elm və Texnologiya</span>'),
        (r'Evrika Beynəlxalq Elm və Texnologiya Liseyi \(Nərimanov filialı\)', r'<span data-i18n="school-narimanov">Evrika Beynəlxalq Elm və Texnologiya Liseyi (Nərimanov filialı)</span>'),
        (r'>iSteam Proqramı<', r' data-i18n="badge-isteam">iSteam Proqramı<'),
        (r'>68 Fəxrəddin Musayev, Bakı, Azərbaycan<', r' data-i18n="addr-narimanov">68 Fəxrəddin Musayev, Bakı, Azərbaycan<'),

        # Item 3
        (r'Evrika Beynəlxalq Elm və Texnologiya Liseyi \(Gənclik filialı\)', r'<span data-i18n="school-ganjlik">Evrika Beynəlxalq Elm və Texnologiya Liseyi (Gənclik filialı)</span>'),
        (r'>Montessori məktəbi \(ibtidai\)<', r' data-i18n="badge-mont-school">Montessori məktəbi (ibtidai)<'),
        (r'>Yəhya Bakuvi küç\. 42, Zümrüd Yaşayış Kompleksi<', r' data-i18n="addr-zumrud">Yəhya Bakuvi küç. 42, Zümrüd Yaşayış Kompleksi<'),

        # Item 4
        (r'</span> Akademik Dəstək', r'</span> <span data-i18n="school-support">Akademik Dəstək</span>'),
        (r'Evrika Eduhome Hazırlıq Mərkəzi', r'<span data-i18n="school-eduhome">Evrika Eduhome Hazırlıq Mərkəzi</span>'),
        (r'>Xarici Dil Hazırlıqları<', r' data-i18n="badge-lang">Xarici Dil Hazırlıqları<'),
        (r'>Baləmi Dadaşov küçəsi, Zümrüd Residence Kompleksi<', r' data-i18n="addr-eduhome">Baləmi Dadaşov küçəsi, Zümrüd Residence Kompleksi<'),

        # Item 5
        (r'</span> PEŞƏKAR İDMAN', r'</span> <span data-i18n="school-sport">PEŞƏKAR İDMAN</span>'),
        (r'Zumrud Women Club by Evrika Active Life', r'<span data-i18n="school-zumrud-club">Zumrud Women Club by Evrika Active Life</span>'),
        (r'>Ana və uşaqlar<', r' data-i18n="badge-mom-child">Ana və uşaqlar<'),
        (r'>Üzgüçülük<', r' data-i18n="badge-swim">Üzgüçülük<'),
        (r'>Fitness<', r' data-i18n="badge-fitness">Fitness<'),
        (r'>Pilates<', r' data-i18n="badge-pilates">Pilates<'),
        (r'>Yoga və s\.<', r' data-i18n="badge-yoga">Yoga və s.<'),

        # Footer
        (r'<h4>E- JURNAL</h4>', r'<h4 data-i18n="footer-ejournal">E- JURNAL</h4>'),
        (r'color: var\(--accent, #8B1A2B\);">E- JURNAL</h4>', r'color: var(--accent, #8B1A2B);" data-i18n="footer-ejournal">E- JURNAL</h4>'),
        (r'<p style="color: rgba\(255,255,255,0\.4\); font-size: 0\.85rem;">&copy; 2026 Evrika Təhsil Ekosistemi\. Bütün hüquqlar qorunur\.</p>', r'<p style="color: rgba(255,255,255,0.4); font-size: 0.85rem;" data-i18n="footer-copyright">&copy; 2026 Evrika Təhsil Ekosistemi. Bütün hüquqlar qorunur.</p>'),
        (r'href="privacy\.html" style="color: rgba\(255,255,255,0\.3\); text-decoration: none; font-size: 0\.85rem; transition: 0\.3s;">Məxfilik Siyasəti</a>', r'href="privacy.html" style="color: rgba(255,255,255,0.3); text-decoration: none; font-size: 0.85rem; transition: 0.3s;" data-i18n="footer-privacy">Məxfilik Siyasəti</a>'),
        (r'href="terms\.html" style="color: rgba\(255,255,255,0\.3\); text-decoration: none; font-size: 0\.85rem; transition: 0\.3s;">İstifadə Şərtləri</a>', r'href="terms.html" style="color: rgba(255,255,255,0.3); text-decoration: none; font-size: 0.85rem; transition: 0.3s;" data-i18n="footer-terms">İstifadə Şərtləri</a>'),
        (r'data-i18n="footer-contact">ƏLAQƏ</h4>', r'data-i18n="footer-contact-head">ƏLAQƏ</h4>')
    ]

    for p, r_str in nav_replacements:
        html = re.sub(p, r_str, html)

    html = html.replace('Evrika Təhsil Ekosistemi — Qlobal təhsil standartları, innovativ yanaşma və parlaq gələcəkdir.', '<span data-i18n="footer-desc">Evrika Təhsil Ekosistemi — Qlobal təhsil standartları, innovativ yanaşma və parlaq gələcəkdir.</span>')
    html = html.replace('>NAVİQASİYA<', ' data-i18n="footer-nav">NAVİQASİYA<')
    html = html.replace('>ƏLAQƏ<', ' data-i18n="footer-contact-head">ƏLAQƏ<')
    
    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/live_vercel_code/schools.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    fix_live_vercel_schools_page()
    print("Fixed live_vercel_code/schools.html translations!")
