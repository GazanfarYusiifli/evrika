import re

def fix_lisey_page():
    paths = [
        '/Users/gazanfaryusifli/Downloads/EvrikaProje/lisey.html',
        '/Users/gazanfaryusifli/Downloads/EvrikaProje/live_vercel_code/lisey.html'
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
        
        # Lang Switcher
        (r'onmousedown="event\.preventDefault\(\);\s*document\.querySelectorAll\(\'\.lang-text\'\)\.forEach\(e=>e\.innerText=\'AZ\'\);\s*this\.parentElement\.style\.display=\'none\';"',
         r"onmousedown=\"event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='AZ'); this.parentElement.style.display='none'; if(window.updateContent) window.updateContent('az');\"".replace(r'\"', '"')),
        (r'onmousedown="event\.preventDefault\(\);\s*document\.querySelectorAll\(\'\.lang-text\'\)\.forEach\(e=>e\.innerText=\'EN\'\);\s*this\.parentElement\.style\.display=\'none\';"',
         r"onmousedown=\"event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='EN'); this.parentElement.style.display='none'; if(window.updateContent) window.updateContent('en');\"".replace(r'\"', '"')),
        (r'onmousedown="event\.preventDefault\(\);\s*document\.querySelectorAll\(\'\.lang-text\'\)\.forEach\(e=>e\.innerText=\'RU\'\);\s*this\.parentElement\.style\.display=\'none\';"',
         r"onmousedown=\"event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='RU'); this.parentElement.style.display='none'; if(window.updateContent) window.updateContent('ru');\"".replace(r'\"', '"')),

        # Lisey specific replacements
        (r'<div class="hero-tag reveal">NƏRİMANOV FİLİALI</div>', r'<div class="hero-tag reveal" data-i18n="lisey-branch">NƏRİMANOV FİLİALI</div>'),
        (r'<h1 class="hero-h1 reveal">Evrika Beynəlxalq <br> <span class="accent">Elm və Texnologiya Liseyi</span></h1>', r'<h1 class="hero-h1 reveal" data-i18n="lisey-title">Evrika Beynəlxalq <br> <span class="accent">Elm və Texnologiya Liseyi</span></h1>'),
        (r'<p class="hero-p reveal">15 illik akademik təcrübəyə əsaslanan Evrika Liseyi, məktəbəqədər mərhələdən XI sinfə qədər hərtərəfli inkişafı təmin edən müasir və nəticə yönümlü təhsil modelidir.</p>', r'<p class="hero-p reveal" data-i18n="lisey-hero-desc">15 illik akademik təcrübəyə əsaslanan Evrika Liseyi, məktəbəqədər mərhələdən XI sinfə qədər hərtərəfli inkişafı təmin edən müasir və nəticə yönümlü təhsil modelidir.</p>'),
        (r'<a href="schools.html" class="btn-primary reveal"> Qeydiyyat <i class="fas fa-arrow-right"></i></a>', r'<a href="schools.html" class="btn-primary reveal"><span data-i18n="nav-register">Qeydiyyat</span> <i class="fas fa-arrow-right"></i></a>'),

        (r'<div class="sec-eyebrow reveal">Haqqımızda</div>', r'<div class="sec-eyebrow reveal" data-i18n="nav-about">Haqqımızda</div>'),
        (r'<h2 class="sec-h2 reveal">Milli Kurikulum, <em>Cambridge</em> və <em>STEAM/iSTEM</em></h2>', r'<h2 class="sec-h2 reveal" data-i18n="lisey-about-title">Milli Kurikulum, <em>Cambridge</em> və <em>STEAM/iSTEM</em></h2>'),
        (r'<p class="sec-lead reveal">Məktəbəqədər hazırlıq və I–XI siniflər üzrə təşkil olunan tədris prosesi Milli kurikulum, Beynəlxalq Cambridge proqramı və STEAM/iSTEM modeli əsasında qurulur.</p>', r'<p class="sec-lead reveal" data-i18n="lisey-about-p1">Məktəbəqədər hazırlıq və I–XI siniflər üzrə təşkil olunan tədris prosesi Milli kurikulum, Beynəlxalq Cambridge proqramı və STEAM/iSTEM modeli əsasında qurulur.</p>'),
        (r'<p class="sec-lead reveal" style="margin-top:20px;">Uşaq mərkəzli yanaşma, davamlı monitorinq və fərdi inkişaf prinsipləri şagirdlərdə analitik düşüncə, şəxsiyyət inkişafı və gələcəyə hazırlığı formalaşdırır.</p>', r'<p class="sec-lead reveal" style="margin-top:20px;" data-i18n="lisey-about-p2">Uşaq mərkəzli yanaşma, davamlı monitorinq və fərdi inkişaf prinsipləri şagirdlərdə analitik düşüncə, şəxsiyyət inkişafı və gələcəyə hazırlığı formalaşdırır.</p>'),

        (r'<h2 class="sec-h2-modern">Təhsil <em>Pillələrimiz</em></h2>', r'<h2 class="sec-h2-modern" data-i18n="lisey-levels-title">Təhsil <em>Pillələrimiz</em></h2>'),
        (r'<p class="sec-p">Məktəbəhazırlıqdan IX sinfə qədər hər bir pillədə fərdi yanaşma və beynəlxalq standartlar.</p>', r'<p class="sec-p" data-i18n="lisey-levels-desc">Məktəbəhazırlıqdan IX sinfə qədər hər bir pillədə fərdi yanaşma və beynəlxalq standartlar.</p>'),

        (r'<h3>Məktəbəhazırlıq</h3>', r'<h3 data-i18n="lisey-lvl1-title">Məktəbəhazırlıq</h3>'),
        (r'<p>5-6 yaşlı uşaqlar üçün iSteam və STEAM əsaslı kəşfiyyat dünyası\.\.\.</p>', r'<p data-i18n="lisey-lvl1-desc">5-6 yaşlı uşaqlar üçün iSteam və STEAM əsaslı kəşfiyyat dünyası...</p>'),
        
        (r'<h3>İbtidai Təhsil</h3>', r'<h3 data-i18n="lisey-lvl2-title">İbtidai Təhsil</h3>'),
        (r'<p>1-4-cü siniflərdə məntiqi təfəkkürün və təməl bacarıqların formalaşdırılması\.\.\.</p>', r'<p data-i18n="lisey-lvl2-desc">1-4-cü siniflərdə məntiqi təfəkkürün və təməl bacarıqların formalaşdırılması...</p>'),

        (r'<h3>Ümumi Orta Təhsil</h3>', r'<h3 data-i18n="lisey-lvl3-title">Ümumi Orta Təhsil</h3>'),
        (r'<p>5-9-cu siniflərdə dərinləşdirilmiş fənlər və aylıq monitorinqlər\.\.\.</p>', r'<p data-i18n="lisey-lvl3-desc">5-9-cu siniflərdə dərinləşdirilmiş fənlər və aylıq monitorinqlər...</p>'),

        (r'<h3>Tam Orta Təhsil</h3>', r'<h3 data-i18n="lisey-lvl4-title">Tam Orta Təhsil</h3>'),
        (r'<p>10-11-ci siniflərdə ixtisaslaşma, SAT, IELTS və universitet hazırlığı\.\.\.</p>', r'<p data-i18n="lisey-lvl4-desc">10-11-ci siniflərdə ixtisaslaşma, SAT, IELTS və universitet hazırlığı...</p>'),

        (r'<div class="level-btn">Daha çox oxu <i class="fas fa-arrow-right"></i></div>', r'<div class="level-btn"><span data-i18n="lisey-read-more">Daha çox oxu</span> <i class="fas fa-arrow-right"></i></div>'),

        (r'<span class="sec-tag" style="margin: 0 auto 20px;">AKADEMİK</span>', r'<span class="sec-tag" style="margin: 0 auto 20px;" data-i18n="lisey-acad-eyebrow">AKADEMİK</span>'),
        (r'<h2 class="sec-h2-modern">Bölmələr və <em>bilinqval təhsil</em></h2>', r'<h2 class="sec-h2-modern" data-i18n="lisey-acad-title">Bölmələr və <em>bilinqval təhsil</em></h2>'),
        (r'<p class="sec-p" style="margin: 20px auto 0;">2026/2027-ci tədris ilindən Azərbaycan və Rus bölmələrində bilinqval siniflər fəaliyyət göstərir\.</p>', r'<p class="sec-p" style="margin: 20px auto 0;" data-i18n="lisey-acad-desc">2026/2027-ci tədris ilindən Azərbaycan və Rus bölmələrində bilinqval siniflər fəaliyyət göstərir.</p>'),

        (r'<h3 class="prog-h">Azərbaycan <br>Bölməsi</h3>', r'<h3 class="prog-h" data-i18n="lisey-sec-az">Azərbaycan <br>Bölməsi</h3>'),
        (r'<h3 class="prog-h">Rus <br>Bölməsi</h3>', r'<h3 class="prog-h" data-i18n="lisey-sec-ru">Rus <br>Bölməsi</h3>'),
        (r'<h3 class="prog-h">İngilis <br>Bölməsi</h3>', r'<h3 class="prog-h" data-i18n="lisey-sec-en">İngilis <br>Bölməsi</h3>'),

        (r'<h3 style="font-size:2rem; margin-bottom:50px; color:#fff; font-weight:900; letter-spacing:-1px;">Tədris Olunan <em>Xarici Dillər</em></h3>', r'<h3 style="font-size:2rem; margin-bottom:50px; color:#fff; font-weight:900; letter-spacing:-1px;" data-i18n="lisey-langs-title">Tədris Olunan <em>Xarici Dillər</em></h3>'),
        (r'<span>İngilis</span>', r'<span data-i18n="lisey-lang-en">İngilis</span>'),
        (r'<span>Alman</span>', r'<span data-i18n="lisey-lang-de">Alman</span>'),
        (r'<span>Fransız</span>', r'<span data-i18n="lisey-lang-fr">Fransız</span>'),
        (r'<span>Rus</span>', r'<span data-i18n="lisey-lang-ru">Rus</span>'),
        (r'<span>Çin</span>', r'<span data-i18n="lisey-lang-cn">Çin</span>'),

        (r'<div class="sec-eyebrow reveal">EVRİKA / ACADEMIC</div>', r'<div class="sec-eyebrow reveal" data-i18n="lisey-steam-eyebrow">EVRİKA / ACADEMIC</div>'),
        (r'<h2 class="sec-h2 reveal"><em>iSteam</em> və <em>STEAM</em></h2>', r'<h2 class="sec-h2 reveal" data-i18n="lisey-steam-title"><em>iSteam</em> və <em>STEAM</em></h2>'),
        (r'<p class="sec-lead reveal">Yüksək texnoloji yanaşma, iSteam əsaslı tədris, robototexnika və yaradıcı mühəndislik prinsipləri üzərində qurulub\.</p>', r'<p class="sec-lead reveal" data-i18n="lisey-steam-p1">Yüksək texnoloji yanaşma, iSteam əsaslı tədris, robototexnika və yaradıcı mühəndislik prinsipləri üzərində qurulub.</p>'),
        (r'<p class="sec-lead reveal" style="margin-top:20px;">Liseyimizdə tədris prosesi müasir iSteam \(Beynəlxalq STEAM\) proqramı üzərində qurulub\. Bu yanaşma Cambridge proqramı ilə inteqrasiya olunaraq şagirdlərdə mühəndislik düşüncəsi, kodlaşdırma və problem həlletmə bacarıqlarını inkişaf etdirir\.</p>', r'<p class="sec-lead reveal" style="margin-top:20px;" data-i18n="lisey-steam-p2">Liseyimizdə tədris prosesi müasir iSteam (Beynəlxalq STEAM) proqramı üzərində qurulub. Bu yanaşma Cambridge proqramı ilə inteqrasiya olunaraq şagirdlərdə mühəndislik düşüncəsi, kodlaşdırma və problem həlletmə bacarıqlarını inkişaf etdirir.</p>'),

        (r'<h3 class="category-title">YARADICILIQ <em>KLUBLARI</em></h3>', r'<h3 class="category-title" data-i18n="lisey-clubs-art">YARADICILIQ <em>KLUBLARI</em></h3>'),
        (r'<div class="club-name">MUSİQİ</div>', r'<div class="club-name" data-i18n="lisey-club-music">MUSİQİ</div>'),
        (r'<div class="club-name">ART</div>', r'<div class="club-name" data-i18n="lisey-club-art">ART</div>'),
        (r'<div class="club-name">ŞAHMAT</div>', r'<div class="club-name" data-i18n="lisey-club-chess">ŞAHMAT</div>'),
        (r'<div class="club-name">PİANO</div>', r'<div class="club-name" data-i18n="lisey-club-piano">PİANO</div>'),

        (r'<h3 class="category-title">İDMAN <em>KLUBLARI</em></h3>', r'<h3 class="category-title" data-i18n="lisey-clubs-sport">İDMAN <em>KLUBLARI</em></h3>'),
        (r'<div class="club-name">ÜZGÜÇÜLÜK</div>', r'<div class="club-name" data-i18n="lisey-club-swim">ÜZGÜÇÜLÜK</div>'),
        (r'<div class="club-name">FUTBOL</div>', r'<div class="club-name" data-i18n="lisey-club-football">FUTBOL</div>'),
        (r'<div class="club-name">BASKETBOL</div>', r'<div class="club-name" data-i18n="lisey-club-basketball">BASKETBOL</div>'),
        (r'<div class="club-name">VOLEYBOL</div>', r'<div class="club-name" data-i18n="lisey-club-volleyball">VOLEYBOL</div>'),
        (r'<div class="club-name">CÜDO</div>', r'<div class="club-name" data-i18n="lisey-club-judo">CÜDO</div>'),
        (r'<div class="club-name">OXATMA</div>', r'<div class="club-name" data-i18n="lisey-club-archery">OXATMA</div>'),
        (r'<div class="club-name">GİMNASTİKA</div>', r'<div class="club-name" data-i18n="lisey-club-gymnastics">GİMNASTİKA</div>'),

        (r'<div class="sec-eyebrow reveal" style="justify-content:center;">DƏSTƏK VƏ TƏHLÜKƏSİZLİK</div>', r'<div class="sec-eyebrow reveal" style="justify-content:center;" data-i18n="lisey-support-eyebrow">DƏSTƏK VƏ TƏHLÜKƏSİZLİK</div>'),
        (r'<h2 class="sec-h2 reveal" style="text-align:center; max-width:800px; margin:0 auto 60px;">Xidmətlərimiz və <em>İnfrastruktur</em></h2>', r'<h2 class="sec-h2 reveal" style="text-align:center; max-width:800px; margin:0 auto 60px;" data-i18n="lisey-support-title">Xidmətlərimiz və <em>İnfrastruktur</em></h2>'),

        (r'<h3 class="bento-title">Qidalanma</h3>', r'<h3 class="bento-title" data-i18n="lisey-sup-food">Qidalanma</h3>'),
        (r'<p class="bento-desc">Bədənin qidası yemək, ağlın qidası elmdir! 3 dəfəlik sağlam menyu\.\.\.</p>', r'<p class="bento-desc" data-i18n="lisey-sup-food-desc">Bədənin qidası yemək, ağlın qidası elmdir! 3 dəfəlik sağlam menyu...</p>'),

        (r'<h3 class="bento-title">Nəqliyyat</h3>', r'<h3 class="bento-title" data-i18n="lisey-sup-trans">Nəqliyyat</h3>'),
        (r'<p class="bento-desc">Təhlükəsiz və rahat şəkildə evdən məktəbə çatdırılma xidməti\.\.\.</p>', r'<p class="bento-desc" data-i18n="lisey-sup-trans-desc">Təhlükəsiz və rahat şəkildə evdən məktəbə çatdırılma xidməti...</p>'),

        (r'<h3 class="bento-title">Təhlükəsizlik</h3>', r'<h3 class="bento-title" data-i18n="lisey-sup-sec">Təhlükəsizlik</h3>'),
        (r'<p class="bento-desc">24 saat peşəkar mühafizə və turniket nəzarət sistemi\.\.\.</p>', r'<p class="bento-desc" data-i18n="lisey-sup-sec-desc">24 saat peşəkar mühafizə və turniket nəzarət sistemi...</p>'),

        (r'<h3 class="bento-title">Psixoloji Xidmət</h3>', r'<h3 class="bento-title" data-i18n="lisey-sup-psy">Psixoloji Xidmət</h3>'),
        (r'<p class="bento-desc">Şagirdlərin emosional və sosial sağlamlıq xidmətləri\.\.\.</p>', r'<p class="bento-desc" data-i18n="lisey-sup-psy-desc">Şagirdlərin emosional və sosial sağlamlıq xidmətləri...</p>'),

        (r'<h3 class="bento-title">Tibbi Xidmət</h3>', r'<h3 class="bento-title" data-i18n="lisey-sup-med">Tibbi Xidmət</h3>'),
        (r'<p class="bento-desc">İxtisaslı həkim nəzarəti və ilk tibbi yardım təminatı\.\.\.</p>', r'<p class="bento-desc" data-i18n="lisey-sup-med-desc">İxtisaslı həkim nəzarəti və ilk tibbi yardım təminatı...</p>'),

        (r'<h3 class="reveal" style="font-size: clamp\(1\.8rem, 4vw, 2\.8rem\); font-weight: 900; margin-bottom: 20px; line-height: 1\.2;">“Bu günün doğru seçimi, sabahın uğurudur\.”</h3>', r'<h3 class="reveal" style="font-size: clamp(1.8rem, 4vw, 2.8rem); font-weight: 900; margin-bottom: 20px; line-height: 1.2;" data-i18n="lisey-cta-quote">“Bu günün doğru seçimi, sabahın uğurudur.”</h3>'),
        (r'<p class="reveal" style="font-size: 1\.1rem; color: rgba\(255,255,255,0\.8\); margin-bottom: 40px; max-width: 600px; margin-left: auto; margin-right: auto;">Evrika Elm və Texnologiya Liseyi — ELM VƏ TEXNOLOGİYA dünyasına xoş gəlmisiniz!</p>', r'<p class="reveal" style="font-size: 1.1rem; color: rgba(255,255,255,0.8); margin-bottom: 40px; max-width: 600px; margin-left: auto; margin-right: auto;" data-i18n="lisey-cta-desc">Evrika Elm və Texnologiya Liseyi — ELM VƏ TEXNOLOGİYA dünyasına xoş gəlmisiniz!</p>'),
        (r'<a href="schools.html" class="btn-primary reveal">Qeydiyyatdan Keç</a>', r'<a href="schools.html" class="btn-primary reveal" data-i18n="lisey-cta-btn">Qeydiyyatdan Keç</a>'),

        (r'<h4 style="font-size: 1\.1rem; margin-bottom: 15px; color: rgba\(255,255,255,0\.6\);">Filalımızın Ünvanı</h4>', r'<h4 style="font-size: 1.1rem; margin-bottom: 15px; color: rgba(255,255,255,0.6);" data-i18n="lisey-cta-address">Filalımızın Ünvanı</h4>'),
        (r'<h4 style="font-size: 1\.1rem; margin-bottom: 15px; color: rgba\(255,255,255,0\.6\);">Sosial Media</h4>', r'<h4 style="font-size: 1.1rem; margin-bottom: 15px; color: rgba(255,255,255,0.6);" data-i18n="lisey-cta-social">Sosial Media</h4>'),
        (r'<p style="font-size: 1\.2rem; font-weight: 700;">Bizi İnstagramda İzləyin<br><span style="font-weight: 400; font-size: 0\.95rem; opacity: 0\.7;">@evrikaliseyi</span></p>', r'<p style="font-size: 1.2rem; font-weight: 700;"><span data-i18n="lisey-cta-insta-title">Bizi İnstagramda İzləyin</span><br><span style="font-weight: 400; font-size: 0.95rem; opacity: 0.7;">@evrikaliseyi</span></p>'),
        (r'<a href="https://www\.instagram\.com/evrikaliseyi/" target="_blank" class="btn-primary" style="background: rgba\(255,255,255,0\.1\); margin-top: 20px;">İnstagram Səhifəmiz</a>', r'<a href="https://www.instagram.com/evrikaliseyi/" target="_blank" class="btn-primary" style="background: rgba(255,255,255,0.1); margin-top: 20px;" data-i18n="lisey-cta-insta-btn">İnstagram Səhifəmiz</a>'),
    ]

    for path in paths:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                html = f.read()

            for p, r_str in nav_replacements:
                html = re.sub(p, r_str, html)

            html = html.replace('Evrika Təhsil Ekosistemi — Qlobal təhsil standartları, innovativ yanaşma və parlaq gələcəkdir.', '<span data-i18n="footer-desc">Evrika Təhsil Ekosistemi — Qlobal təhsil standartları, innovativ yanaşma və parlaq gələcəkdir.</span>')
            html = html.replace('Innovativ təhsil, qlobal gələcək. Biz şagirdlərimizin uğuru üçün hər gün çalışırıq.', '<span data-i18n="footer-desc">Innovativ təhsil, qlobal gələcək. Biz şagirdlərimizin uğuru üçün hər gün çalışırıq.</span>')
            html = html.replace('>NAVİQASİYA<', ' data-i18n="footer-nav">NAVİQASİYA<')
            html = html.replace('>ƏLAQƏ<', ' data-i18n="footer-contact-head">ƏLAQƏ<')
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Fixed HTML in {path}")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    fix_lisey_page()
