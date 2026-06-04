import re

def fix_contact_page():
    paths = [
        '/Users/gazanfaryusifli/Downloads/EvrikaProje/contact.html',
        '/Users/gazanfaryusifli/Downloads/EvrikaProje/live_vercel_code/contact.html'
    ]
    
    # Common replacements for navbar and footer (same as jurnal.html)
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
        
        # Lang Switcher
        (r'onmousedown="event\.preventDefault\(\);\s*document\.querySelectorAll\(\'\.lang-text\'\)\.forEach\(e=>e\.innerText=\'AZ\'\);\s*this\.parentElement\.style\.display=\'none\';"',
         r"onmousedown=\"event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='AZ'); this.parentElement.style.display='none'; if(window.updateContent) window.updateContent('az');\""),
        (r'onmousedown="event\.preventDefault\(\);\s*document\.querySelectorAll\(\'\.lang-text\'\)\.forEach\(e=>e\.innerText=\'EN\'\);\s*this\.parentElement\.style\.display=\'none\';"',
         r"onmousedown=\"event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='EN'); this.parentElement.style.display='none'; if(window.updateContent) window.updateContent('en');\""),
        (r'onmousedown="event\.preventDefault\(\);\s*document\.querySelectorAll\(\'\.lang-text\'\)\.forEach\(e=>e\.innerText=\'RU\'\);\s*this\.parentElement\.style\.display=\'none\';"',
         r"onmousedown=\"event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='RU'); this.parentElement.style.display='none'; if(window.updateContent) window.updateContent('ru');\""),
         
        # Contact specifics
        (r'Bizimlə <span style="position:relative;color:var\(--white\);z-index:1;">Əlaqə', r'<span data-i18n="contact-hero-title">Bizimlə <span style="position:relative;color:var(--white);z-index:1;">Əlaqə</span></span>'),
        (r'<span style="position:absolute;bottom:8px;left:0;width:100%;height:18px;background:var\(--burgundy\);z-index:-1;opacity:0\.3;border-radius:4px;"></span>', ''), # Clear original span since I moved it to json
        (r'Hər bir sualınız və rəyiniz bizim üçün <span style="color:var\(--white\);font-weight:800;">dəyərlidir!</span>', r'<span data-i18n="contact-hero-desc">Hər bir sualınız və rəyiniz bizim üçün <span style="color:var(--white);font-weight:800;">dəyərlidir!</span></span>'),
        
        (r'>Məlumat Mərkəzi<', r' data-i18n="contact-info-center">Məlumat Mərkəzi<'),
        (r'>Mərkəzi Ofis<', r' data-i18n="contact-main-office">Mərkəzi Ofis<'),
        (r'>Qaynar Xətt<', r' data-i18n="contact-hotline">Qaynar Xətt<'),
        (r'>Rəsmi Email<', r' data-i18n="contact-official-email">Rəsmi Email<'),
        (r'>İş vaxtı<', r' data-i18n="contact-work-hours-title">İş vaxtı<'),
        (r'>Bazar ertəsi - Cümə \| 09:00 - 17:30<', r' data-i18n="contact-work-hours-desc">Bazar ertəsi - Cümə | 09:00 - 17:30<'),
        
        (r'>Ad<', r' data-i18n="form-name-label">Ad<'),
        (r'>Telefon<', r' data-i18n="form-phone-label">Telefon<'),
        (r'>E-poçt ünvanı<', r' data-i18n="form-email-label">E-poçt ünvanı<'),
        (r'>Mesaj<', r' data-i18n="form-message-label">Mesaj<'),
        (r'\n\s*Müraciəti Göndər <i class="fas fa-paper-plane" style="margin-left: 15px; font-size: 1rem;"></i>\n\s*</button>', 
         r'\n                  <span data-i18n="form-submit-btn">Müraciəti Göndər <i class="fas fa-paper-plane" style="margin-left: 15px; font-size: 1rem;"></i></span>\n                </button>'),
         
        (r'>STRATEJİ COĞRAFİYA<', r' data-i18n="map-eyebrow">STRATEJİ COĞRAFİYA<'),
        (r'Məkanların <span style="background: linear-gradient', r'<span data-i18n="map-title">Məkanların <span style="background: linear-gradient'),
        (r'Evrika Təhsil Ekosistemi şəhərin ən əlverişli nöqtələrində, müasir infrastrukturla xidmətinizdədir\.', r'<span data-i18n="map-desc">Evrika Təhsil Ekosistemi şəhərin ən əlverişli nöqtələrində, müasir infrastrukturla xidmətinizdədir.</span>')
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
    "contact-hero-title": "Bizimlə <span style=\"position:relative;color:var(--white);z-index:1;\">Əlaqə<span style=\"position:absolute;bottom:8px;left:0;width:100%;height:18px;background:var(--burgundy);z-index:-1;opacity:0.3;border-radius:4px;\"></span></span>",
    "contact-hero-desc": "Hər bir sualınız və rəyiniz bizim üçün <span style=\"color:var(--white);font-weight:800;\">dəyərlidir!</span>",
    "contact-info-center": "Məlumat Mərkəzi",
    "contact-main-office": "Mərkəzi Ofis",
    "contact-hotline": "Qaynar Xətt",
    "contact-official-email": "Rəsmi Email",
    "contact-work-hours-title": "İş vaxtı",
    "contact-work-hours-desc": "Bazar ertəsi - Cümə | 09:00 - 17:30",
    "form-name-label": "Ad",
    "form-phone-label": "Telefon",
    "form-email-label": "E-poçt ünvanı",
    "form-message-label": "Mesaj",
    "form-submit-btn": "Müraciəti Göndər <i class=\"fas fa-paper-plane\" style=\"margin-left: 15px; font-size: 1rem;\"></i>",
    "map-eyebrow": "STRATEJİ COĞRAFİYA",
    "map-title": "Məkanların <span style=\"background: linear-gradient(135deg, #fff 0%, rgba(255,255,255,0.3) 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;\">Dəqiq Təyini</span>",
    "map-desc": "Evrika Təhsil Ekosistemi şəhərin ən əlverişli nöqtələrində, müasir infrastrukturla xidmətinizdədir."
"""
    new_en = r""",
    "contact-hero-title": "Contact <span style=\"position:relative;color:var(--white);z-index:1;\">Us<span style=\"position:absolute;bottom:8px;left:0;width:100%;height:18px;background:var(--burgundy);z-index:-1;opacity:0.3;border-radius:4px;\"></span></span>",
    "contact-hero-desc": "Every question and feedback is <span style=\"color:var(--white);font-weight:800;\">valuable to us!</span>",
    "contact-info-center": "Information Center",
    "contact-main-office": "Main Office",
    "contact-hotline": "Hotline",
    "contact-official-email": "Official Email",
    "contact-work-hours-title": "Working Hours",
    "contact-work-hours-desc": "Monday - Friday | 09:00 - 17:30",
    "form-name-label": "Name",
    "form-phone-label": "Phone",
    "form-email-label": "Email Address",
    "form-message-label": "Message",
    "form-submit-btn": "Submit Request <i class=\"fas fa-paper-plane\" style=\"margin-left: 15px; font-size: 1rem;\"></i>",
    "map-eyebrow": "STRATEGIC GEOGRAPHY",
    "map-title": "Precise <span style=\"background: linear-gradient(135deg, #fff 0%, rgba(255,255,255,0.3) 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;\">Location</span>",
    "map-desc": "Evrika Education Ecosystem is at your service with modern infrastructure in the most convenient points of the city."
"""
    new_ru = r""",
    "contact-hero-title": "Свяжитесь с <span style=\"position:relative;color:var(--white);z-index:1;\">Нами<span style=\"position:absolute;bottom:8px;left:0;width:100%;height:18px;background:var(--burgundy);z-index:-1;opacity:0.3;border-radius:4px;\"></span></span>",
    "contact-hero-desc": "Каждый ваш вопрос и отзыв <span style=\"color:var(--white);font-weight:800;\">важен для нас!</span>",
    "contact-info-center": "Информационный Центр",
    "contact-main-office": "Главный Офис",
    "contact-hotline": "Горячая Линия",
    "contact-official-email": "Официальный Email",
    "contact-work-hours-title": "Рабочие Часы",
    "contact-work-hours-desc": "Понедельник - Пятница | 09:00 - 17:30",
    "form-name-label": "Имя",
    "form-phone-label": "Телефон",
    "form-email-label": "Адрес эл. почты",
    "form-message-label": "Сообщение",
    "form-submit-btn": "Отправить запрос <i class=\"fas fa-paper-plane\" style=\"margin-left: 15px; font-size: 1rem;\"></i>",
    "map-eyebrow": "СТРАТЕГИЧЕСКАЯ ГЕОГРАФИЯ",
    "map-title": "Точное <span style=\"background: linear-gradient(135deg, #fff 0%, rgba(255,255,255,0.3) 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;\">Расположение</span>",
    "map-desc": "Образовательная Экосистема Эврика к вашим услугам с современной инфраструктурой в самых удобных точках города."
"""

    js = re.sub(r'("jurnal-desc": "Jurnalımızın yeni nəşri.*?biləcəksiniz."\s*)\}', r'\1' + new_az + r'}', js, count=1)
    js = re.sub(r'("jurnal-desc": "You will be able.*?here."\s*)\}', r'\1' + new_en + r'}', js, count=1)
    js = re.sub(r'("jurnal-desc": "Здесь вы сможете.*?журнала."\s*)\}', r'\1' + new_ru + r'}', js, count=1)

    with open(main_js_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print("Updated main.js with contact translations")

    # Update updateContent in main.js to support data-i18n-placeholder
    with open(main_js_path, 'r', encoding='utf-8') as f:
        js = f.read()
    
    placeholder_code = """
  // Update placeholders if needed
  document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
    const key = el.getAttribute('data-i18n-placeholder');
    if (translations[lang] && translations[lang][key]) {
      el.placeholder = translations[lang][key];
    }
  });"""
    if 'data-i18n-placeholder' not in js:
        js = js.replace('document.documentElement.lang = lang;', 'document.documentElement.lang = lang;' + placeholder_code)
        with open(main_js_path, 'w', encoding='utf-8') as f:
            f.write(js)
        print("Updated main.js with placeholder translation support")


if __name__ == "__main__":
    fix_contact_page()
