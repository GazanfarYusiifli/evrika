import re

def fix_alumni_page():
    paths = [
        '/Users/gazanfaryusifli/Downloads/EvrikaProje/alumni.html',
        '/Users/gazanfaryusifli/Downloads/EvrikaProje/live_vercel_code/alumni.html'
    ]
    
    # Common replacements for navbar and footer
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

        # Desktop Qeydiyyat
        (r'<a href="schools\.html" class="btn btn-primary nav-btn">Qeydiyyat</a>', r'<a href="schools.html" class="btn btn-primary nav-btn" data-i18n="nav-register">Qeydiyyat</a>'),

        # Footer
        (r'<h4>E- JURNAL</h4>', r'<h4 data-i18n="footer-ejournal">E- JURNAL</h4>'),
        (r'color: var\(--accent, #8B1A2B\);">E- JURNAL</h4>', r'color: var(--accent, #8B1A2B);" data-i18n="footer-ejournal">E- JURNAL</h4>'),
        (r'<p style="color: rgba\(255,255,255,0\.4\); font-size: 0\.85rem;">&copy; 2026 Evrika Təhsil Ekosistemi\. Bütün hüquqlar qorunur\.</p>', r'<p style="color: rgba(255,255,255,0.4); font-size: 0.85rem;" data-i18n="footer-copyright">&copy; 2026 Evrika Təhsil Ekosistemi. Bütün hüquqlar qorunur.</p>'),
        (r'href="privacy\.html" style="color: rgba\(255,255,255,0\.3\); text-decoration: none; font-size: 0\.85rem; transition: 0\.3s;">Məxfilik Siyasəti</a>', r'href="privacy.html" style="color: rgba(255,255,255,0.3); text-decoration: none; font-size: 0.85rem; transition: 0.3s;" data-i18n="footer-privacy">Məxfilik Siyasəti</a>'),
        (r'href="terms\.html" style="color: rgba\(255,255,255,0\.3\); text-decoration: none; font-size: 0\.85rem; transition: 0\.3s;">İstifadə Şərtləri</a>', r'href="terms.html" style="color: rgba(255,255,255,0.3); text-decoration: none; font-size: 0.85rem; transition: 0.3s;" data-i18n="footer-terms">İstifadə Şərtləri</a>'),
        (r'data-i18n="footer-contact">ƏLAQƏ</h4>', r'data-i18n="footer-contact-head">ƏLAQƏ</h4>'),
        
        # Lang Switcher - NO ESCAPED QUOTES!
        (r'onmousedown="event\.preventDefault\(\);\s*document\.querySelectorAll\(\'\.lang-text\'\)\.forEach\(e=>e\.innerText=\'AZ\'\);\s*this\.parentElement\.style\.display=\'none\';"',
         r"onmousedown=\"event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='AZ'); this.parentElement.style.display='none'; if(window.updateContent) window.updateContent('az');\"".replace(r'\"', '"')),
        (r'onmousedown="event\.preventDefault\(\);\s*document\.querySelectorAll\(\'\.lang-text\'\)\.forEach\(e=>e\.innerText=\'EN\'\);\s*this\.parentElement\.style\.display=\'none\';"',
         r"onmousedown=\"event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='EN'); this.parentElement.style.display='none'; if(window.updateContent) window.updateContent('en');\"".replace(r'\"', '"')),
        (r'onmousedown="event\.preventDefault\(\);\s*document\.querySelectorAll\(\'\.lang-text\'\)\.forEach\(e=>e\.innerText=\'RU\'\);\s*this\.parentElement\.style\.display=\'none\';"',
         r"onmousedown=\"event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='RU'); this.parentElement.style.display='none'; if(window.updateContent) window.updateContent('ru');\"".replace(r'\"', '"'))
    ]

    for path in paths:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                html = f.read()

            for p, r_str in nav_replacements:
                html = re.sub(p, r_str, html)

            html = html.replace('Evrika Təhsil Ekosistemi — Qlobal təhsil standartları, innovativ yanaşma və parlaq gələcəkdir.', '<span data-i18n="footer-desc">Evrika Təhsil Ekosistemi — Qlobal təhsil standartları, innovativ yanaşma və parlaq gələcəkdir.</span>')
            html = html.replace('>NAVİQASİYA<', ' data-i18n="footer-nav">NAVİQASİYA<')
            html = html.replace('>ƏLAQƏ<', ' data-i18n="footer-contact-head">ƏLAQƏ<')
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Fixed HTML in {path}")
        except FileNotFoundError:
            pass

    # Now add translations to main.js
    main_js_path = '/Users/gazanfaryusifli/Downloads/EvrikaProje/src/main.js'
    with open(main_js_path, 'r', encoding='utf-8') as f:
        js = f.read()

    new_az = r""",
    "alumni-title": "Məzun Tarixçəsi",
    "alumni-desc": "İxtisaslaşmış təhsil müəssisələrimizlə şagirdlərimizi akademik zəfərlərə və qlobal gələcəyə hazırlayırıq."
"""
    new_en = r""",
    "alumni-title": "Alumni History",
    "alumni-desc": "We prepare our students for academic victories and a global future with our specialized educational institutions."
"""
    new_ru = r""",
    "alumni-title": "История Выпускников",
    "alumni-desc": "Мы готовим наших учеников к академическим победам и глобальному будущему в наших специализированных учебных заведениях."
"""

    js = re.sub(r'("form-message-ph": "Müraciətiniz və ya sualınız..."\s*)\}', r'\1' + new_az + r'}', js, count=1)
    js = re.sub(r'("form-message-ph": "Your request or question..."\s*)\}', r'\1' + new_en + r'}', js, count=1)
    js = re.sub(r'("form-message-ph": "Ваш запрос или вопрос..."\s*)\}', r'\1' + new_ru + r'}', js, count=1)

    with open(main_js_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print("Updated main.js with alumni translations")


if __name__ == "__main__":
    fix_alumni_page()
