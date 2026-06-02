import re

html_file = 'index.html'
js_file = 'src/main.js'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Let's use regex to replace specific tags with data-i18n equivalents.

replacements = [
    # Stats
    (r'<h2 class="stats-title" style="[^"]*">Mükəmməlliyin Rəqəmlərlə İfadəsi\.</h2>', r'<h2 class="stats-title" style="margin-bottom: 50px; font-weight: 800; font-size: clamp(2rem, 4vw, 2.5rem); letter-spacing: -0.03em;" data-i18n="stats-title">Mükəmməlliyin Rəqəmlərlə İfadəsi.</h2>'),
    
    # Mission/Vision
    (r'<p style="font-size: 1.15rem; color: rgba\(255,255,255,0\.9\); line-height: 1\.8;">\s*Milli dəyərlərə sadiq, qlobal düşüncəyə malik, yenilikçi şəxsiyyətlər yetişdirməkdir!\s*</p>', r'<p style="font-size: 1.15rem; color: rgba(255,255,255,0.9); line-height: 1.8;" data-i18n="mission-desc">Milli dəyərlərə sadiq, qlobal düşüncəyə malik, yenilikçi şəxsiyyətlər yetişdirməkdir!</p>'),
    (r'<p style="font-size: 1\.15rem; color: rgba\(255,255,255,0\.9\); line-height: 1\.8;">\s*Gələcəyin yalnız liderlərini deyil, dünyanı dəyişdirə bilən, cəmiyyətə fayda verən şəxsiyyətlər formalaşdırmaqdır!\s*</p>', r'<p style="font-size: 1.15rem; color: rgba(255,255,255,0.9); line-height: 1.8;" data-i18n="vision-desc">Gələcəyin yalnız liderlərini deyil, dünyanı dəyişdirə bilən, cəmiyyətə fayda verən şəxsiyyətlər formalaşdırmaqdır!</p>'),
    
    # Vision 2026
    (r'<div class="brand-eyebrow modern-glow"[^>]*>VİZYON 2026</div>', r'<div class="brand-eyebrow modern-glow" style="margin-bottom: 24px; color: rgba(255,255,255,0.7); opacity: 1; letter-spacing: 0.6em; text-transform: uppercase; font-weight: 800; font-size: 0.8rem;" data-i18n="v2026-title1">VİZYON 2026</div>'),
    (r'<h2 class="titan-header"[^>]*>GƏLƏCƏYİ BU GÜN VAR EDƏN TƏHSİL EKOSİSTEMİ</h2>', r'<h2 class="titan-header" style="font-size: clamp(2rem, 5vw, 4.5rem); margin-bottom: 30px; letter-spacing: -0.04em;" data-i18n="v2026-title2">GƏLƏCƏYİ BU GÜN VAR EDƏN TƏHSİL EKOSİSTEMİ</h2>'),
    (r'<p class="subtitle-pro"[^>]*>EVRİKA artıq sadəcə məktəb deyil\.</p>', r'<p class="subtitle-pro" style="max-width: 600px; margin: 0 auto 10px; font-size: 1.5rem; font-weight: 400; opacity: 1;" data-i18n="v2026-desc1">EVRİKA artıq sadəcə məktəb deyil.</p>'),
    (r'<p class="subtitle-pro"[^>]*>EVRİKA – gələcək quran təhsil ekosistemidir\.</p>', r'<p class="subtitle-pro" style="max-width: 600px; margin: 0 auto; font-size: 1.5rem; font-weight: 400; opacity: 1;" data-i18n="v2026-desc2">EVRİKA – gələcək quran təhsil ekosistemidir.</p>'),
    
    # Alumni
    (r'<h2 class="titan-header"[^>]*>Dünyaya Açılan<br>Uğur Yolumuz!</h2>', r'<h2 class="titan-header" style="font-size:clamp(3rem,6vw,4.5rem);color:#071333;line-height:1.1;margin-bottom:20px;letter-spacing:-0.04em;" data-i18n="alumni-sec-title2">Dünyaya Açılan<br>Uğur Yolumuz!</h2>'),
    
    # Founder Message
    (r'<h2 style="font-size:clamp\(2\.5rem, 5vw, 4rem\); font-weight:900; line-height:1; color:var\(--burgundy\); letter-spacing:-0\.04em;">TƏSİSÇİNİN<br>MESAJI</h2>', r'<h2 style="font-size:clamp(2.5rem, 5vw, 4rem); font-weight:900; line-height:1; color:var(--burgundy); letter-spacing:-0.04em;" data-i18n="founder-title">TƏSİSÇİNİN<br>MESAJI</h2>'),
    (r'<p style="font-size: clamp\(1\.2rem, 2vw, 1\.6rem\); line-height: 1\.6; color: #333; font-weight: 500;">\s*<span style="font-size:4rem; color:var\(--burgundy\); line-height:0; vertical-align:middle; margin-right:10px;">“</span><br>\s*"Evrika Təhsil Ekosistemi” mənim üçün yalnız bir təhsil müəssisəsi deyil — vətənimə, millətimə və onun gələcək tərəqqisinə olan sevgimin təzahürüdür\s*</p>', r'<p style="font-size: clamp(1.2rem, 2vw, 1.6rem); line-height: 1.6; color: #333; font-weight: 500;" data-i18n="founder-quote"><span style="font-size:4rem; color:var(--burgundy); line-height:0; vertical-align:middle; margin-right:10px;">“</span><br>"Evrika Təhsil Ekosistemi” mənim üçün yalnız bir təhsil müəssisəsi deyil — vətənimə, millətimə və onun gələcək tərəqqisinə olan sevgimin təzahürüdür</p>'),
    
    # All News Button
    (r'<a href="news.html" class="glass-btn"[^>]*>Bütün Xəbərlər</a>', r'<a href="news.html" class="glass-btn" style="display:inline-flex;align-items:center;gap:12px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);color:white;padding:15px 35px;border-radius:100px;text-decoration:none;font-weight:700;font-size:1.1rem;transition:0.4s;box-shadow:0 10px 30px rgba(0,0,0,0.2);" onmouseover="this.style.background=\'var(--burgundy)\'; this.style.borderColor=\'var(--burgundy)\';" onmouseout="this.style.background=\'rgba(255,255,255,0.05)\'; this.style.borderColor=\'rgba(255,255,255,0.1)\';" data-i18n="news-btn-all">Bütün Xəbərlər</a>'),
    
    # Footer elements
    (r'<a href="index.html" class="logo"[^>]*>EVRİKA</a>', r'<a href="index.html" class="logo" style="color: var(--accent, #8B1A2B); font-size: 1.8rem; font-weight: 900; text-decoration: none; display: block; margin-bottom: 25px;" data-i18n="join-title1">EVRİKA</a>'),
    (r'<p style="color: rgba\(255,255,255,0\.6\); line-height: 1\.7; margin-bottom: 30px; font-size: 0\.95rem; max-width: 320px;">Evrika Təhsil Ekosistemi — Qlobal təhsil standartları, innovativ yanaşma və parlaq gələcəkdir\.</p>', r'<p style="color: rgba(255,255,255,0.6); line-height: 1.7; margin-bottom: 30px; font-size: 0.95rem; max-width: 320px;" data-i18n="footer-desc">Evrika Təhsil Ekosistemi — Qlobal təhsil standartları, innovativ yanaşma və parlaq gələcəkdir.</p>'),
    (r'<h4 style="text-transform: uppercase; letter-spacing: 0\.15em; margin-bottom: 30px; font-size: 0\.9rem; font-weight: 800; color: var\(--accent, #8B1A2B\);">NAVİQASİYA</h4>', r'<h4 style="text-transform: uppercase; letter-spacing: 0.15em; margin-bottom: 30px; font-size: 0.9rem; font-weight: 800; color: var(--accent, #8B1A2B);" data-i18n="footer-nav">NAVİQASİYA</h4>'),
    (r'<h4 style="text-transform: uppercase; letter-spacing: 0\.15em; margin-bottom: 30px; font-size: 0\.9rem; font-weight: 800; color: var\(--accent, #8B1A2B\);">Əlaqə</h4>', r'<h4 style="text-transform: uppercase; letter-spacing: 0.15em; margin-bottom: 30px; font-size: 0.9rem; font-weight: 800; color: var(--accent, #8B1A2B);" data-i18n="footer-contact-head">Əlaqə</h4>'),
    (r'<p style="color: rgba\(255,255,255,0\.4\); font-size: 0\.85rem;">&copy; 2026 Evrika Təhsil Ekosistemi\. Bütün hüquqlar qorunur\.</p>', r'<p style="color: rgba(255,255,255,0.4); font-size: 0.85rem;" data-i18n="footer-rights">&copy; 2026 Evrika Təhsil Ekosistemi. Bütün hüquqlar qorunur.</p>'),
    (r'<a href="#" style="color: rgba\(255,255,255,0\.4\); text-decoration: none; font-size: 0\.85rem; transition: 0\.3s;"[^>]*>Məxfilik Siyasəti</a>', r'<a href="#" style="color: rgba(255,255,255,0.4); text-decoration: none; font-size: 0.85rem; transition: 0.3s;" onmouseover="this.style.color=\'white\'" onmouseout="this.style.color=\'rgba(255,255,255,0.4)\'" data-i18n="footer-privacy">Məxfilik Siyasəti</a>'),
    (r'<a href="#" style="color: rgba\(255,255,255,0\.4\); text-decoration: none; font-size: 0\.85rem; transition: 0\.3s;"[^>]*>İstifadə Şərtləri</a>', r'<a href="#" style="color: rgba(255,255,255,0.4); text-decoration: none; font-size: 0.85rem; transition: 0.3s;" onmouseover="this.style.color=\'white\'" onmouseout="this.style.color=\'rgba(255,255,255,0.4)\'" data-i18n="footer-terms">İstifadə Şərtləri</a>'),
    
    # Navbar submenus
    (r'<span class="dropdown-item-desc">Bizim hekayəmiz</span>', r'<span class="dropdown-item-desc" data-i18n="nav-about-desc">Bizim hekayəmiz</span>'),
    (r'<span class="dropdown-item-title">Məzunlar</span>', r'<span class="dropdown-item-title" data-i18n="nav-alumni">Məzunlar</span>'),
    (r'<span class="dropdown-item-desc">Fəxrlərimiz</span>', r'<span class="dropdown-item-desc" data-i18n="nav-alumni-desc">Fəxrlərimiz</span>'),
    (r'<span class="dropdown-item-title">Uğurlar</span>', r'<span class="dropdown-item-title" data-i18n="nav-achievements">Uğurlar</span>'),
    (r'<span class="dropdown-item-desc">Nailiyyətlərimiz</span>', r'<span class="dropdown-item-desc" data-i18n="nav-achievements-desc">Nailiyyətlərimiz</span>'),
    (r'<span class="dropdown-item-title">Xəbərlər</span>', r'<span class="dropdown-item-title" data-i18n="nav-news">Xəbərlər</span>'),
    (r'<span class="dropdown-item-desc">Ən son yeniliklər</span>', r'<span class="dropdown-item-desc" data-i18n="nav-news-desc">Ən son yeniliklər</span>'),
    
    (r'<span class="dropdown-item-title">Evrika BETL Nərimanov</span>', r'<span class="dropdown-item-title" data-i18n="nav-lisey1">Evrika BETL Nərimanov</span>'),
    (r'<span class="dropdown-item-desc">Elm və Texnologiya Mərkəzi</span>', r'<span class="dropdown-item-desc" data-i18n="nav-lisey1-desc">Elm və Texnologiya Mərkəzi</span>'),
    (r'<span class="dropdown-item-title">Evrika BETL Gənclik</span>', r'<span class="dropdown-item-title" data-i18n="nav-lisey2">Evrika BETL Gənclik</span>'),
    (r'<span class="dropdown-item-desc">Beynəlxalq Təhsil Müəssisəsi</span>', r'<span class="dropdown-item-desc" data-i18n="nav-lisey2-desc">Beynəlxalq Təhsil Müəssisəsi</span>'),
    (r'<span class="dropdown-item-title">Montessori Kids Academy</span>', r'<span class="dropdown-item-title" data-i18n="nav-montessori">Montessori Kids Academy</span>'),
    (r'<span class="dropdown-item-desc">Bağça və Erkən İnkişaf</span>', r'<span class="dropdown-item-desc" data-i18n="nav-montessori-desc">Bağça və Erkən İnkişaf</span>'),
    (r'<span class="dropdown-item-title">Eduhome Hazırlıq</span>', r'<span class="dropdown-item-title" data-i18n="nav-eduhome">Eduhome Hazırlıq</span>'),
    (r'<span class="dropdown-item-desc">Xaricdə Təhsil və Hazırlıq</span>', r'<span class="dropdown-item-desc" data-i18n="nav-eduhome-desc">Xaricdə Təhsil və Hazırlıq</span>'),
    (r'<span class="dropdown-item-title">Zümrüd İdman Mərkəzi</span>', r'<span class="dropdown-item-title" data-i18n="nav-zumrud">Zümrüd İdman Mərkəzi</span>'),
    (r'<span class="dropdown-item-desc">Sağlam Həyat və Fəaliyyət</span>', r'<span class="dropdown-item-desc" data-i18n="nav-zumrud-desc">Sağlam Həyat və Fəaliyyət</span>'),
    
    (r'<span class="dropdown-item-title">Karyera və Vakansiyalar</span>', r'<span class="dropdown-item-title" data-i18n="nav-vac-title">Karyera və Vakansiyalar</span>'),
    (r'<span class="dropdown-item-desc">Açıq iş elanları</span>', r'<span class="dropdown-item-desc" data-i18n="nav-vac-desc">Açıq iş elanları</span>'),
    (r'<span class="dropdown-item-title">Pedaqoji Təcrübə və İnkişaf Mərkəzi</span>', r'<span class="dropdown-item-title" data-i18n="nav-ptim-title">Pedaqoji Təcrübə və İnkişaf Mərkəzi</span>'),
    (r'<span class="dropdown-item-desc">PTİM</span>', r'<span class="dropdown-item-desc" data-i18n="nav-ptim-desc">PTİM</span>'),
    
    (r'<h3 class="section-title"[^>]*>Akademik istiqamətlərimiz</h3>', r'<h3 class="section-title" style="margin-bottom: 20px; font-weight: 800; font-size: 2.2rem; color: #071333;" data-i18n="eco-title2">Akademik istiqamətlərimiz</h3>'),
    (r'<a href="([^"]*)" class="secondary-btn"[^>]*>Detallara bax</a>', r'<a href="\1" class="secondary-btn" data-i18n="btn-details-look">Detallara bax</a>')
]

for pat, rep in replacements:
    html = re.sub(pat, rep, html)

html = re.sub(r'<a href="([^"]*)" class="secondary-btn"[^>]*>Detallara bax</a>', r'<a href="\1" class="secondary-btn" data-i18n="btn-details-look">Detallara bax</a>', html)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

# Add keys to JS
