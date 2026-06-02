import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

mapping = {
    # Navbar
    'Ana Səhifə': 'nav-home',
    'Haqqımızda': 'nav-about',
    'Akademik İstiqamətlər': 'nav-academic',
    'Vakansiya & Təcrübə': 'nav-vacancy',
    'Evrika Jurnalı': 'nav-journal',
    'Əlaqə': 'nav-contact',
    'Qeydiyyat': 'nav-register',
    
    # Hero
    'HƏR UŞAQDA BİR GƏLƏCƏK<br/>GİZLİDİR': 'hero-title',
    'Biz o gələcəyi kəşf edir, inkişaf etdirir və uğura çeviririk!': 'hero-subtitle',
    'Kəşf Et': 'btn-explore',
    'İzlə': 'btn-watch',
    
    # Section 1: Montessori
    'Evrika Montessori Kids Academy': 'home-sec1-tag',
    'Erkən İnkişaf': 'home-sec1-badge',
    'Evrika Montessori<br/>Kids Academy': 'home-sec1-title',
    'Uşaqların təbii marağını, yaradıcılığını və müstəqilliyini inkişaf etdirən Montessori metodu əsasında fərdi yanaşma ilə erkən uşaqlıq təhsili.': 'home-sec1-desc',
    'Ətraflı': 'btn-detail',
    
    # Section 2: Lisey
    'Evrika BETL Liseyi': 'home-sec2-tag',
    'Qlobal Təhsil': 'home-sec2-badge',
    'Evrika Beynəlxalq Elm və Texnologiya Liseyi': 'home-sec2-title',
    'Cambridge proqramı, STEAM yönümlü tədris və laboratoriya əsaslı innovasiya mühiti ilə şagirdləri gələcəyə hazırlayan beynəlxalq akademik mərkəz.': 'home-sec2-desc',
    'Nərimanov — Ətraflı': 'btn-nerimanov',
    'Gənclik — Ətraflı': 'btn-genclik',
    
    # Section 3: Eduhome
    'Eduhome Hazırlıq Mərkəzi': 'home-sec3-tag',
    'Akademik Dəstək': 'home-sec3-badge',
    'Eduhome<br/>Təhsil Mərkəzi': 'home-sec3-title',
    'Xaricdə təhsil, universitetlərə hazırlıq, dil kursları və peşəkar akademik mentorluq ilə hər şagirdin potensialını açan hazırlıq mərkəzi.': 'home-sec3-desc',
    
    # Section 4: Zumrud
    'Zümrüd Womens Club': 'home-sec4-tag',
    'Sağlam Həyat': 'home-sec4-badge',
    'Zümrüd<br/>Women Club': 'home-sec4-title',
    'Evrika Active Life tərəfindən qadınlar üçün sağlam həyat tərzi, fitness, yoga və sosial inkişaf fəaliyyətlərini özündə birləşdirən premium idman mərkəzi.': 'home-sec4-desc',
    
    # Ecosystem
    'EVRİKA TƏHSİL EKOSİSTEMİ': 'eco-title1',
    'Akademik istiqamətlərimiz': 'eco-title2',
    'İxtisaslaşmış akademik istiqamətlər və fərdi inkişaf modeli ilə hər yaş dövrünə uyğun təhsil mühiti.': 'eco-desc',
    
    'Evrika Beynəlxalq Elm və Texnologiya Liseyi (Nərimanov filialı)': 'branch-betl-nerimanov-title',
    'Evrika Beynəlxalq Elm və Texnologiya Liseyi (Gənclik filialı)': 'branch-betl-genclik-title',
    'Evrika Eduhome Hazırlıq Mərkəzi': 'branch-eduhome-title',
    'Zumrud Women Club by Evrika Active Life': 'branch-zumrud-title',
    'Detallara bax': 'btn-details-look',
    
    # Quotes
    'Təhsil bizim gələcəyimizdir!': 'pres-title',
    'İlham Əliyev': 'pres-name',
    'Azərbaycan Respublikasının Prezidenti': 'pres-role',
    'Müasir dünyada hər bir ölkənin inkişafı, onun dünya birliyinə inteqrasiyası üçün təhsilin rolu əvəzsizdir.': 'vp-title',
    'Mehriban Əliyeva': 'vp-name',
    'Birinci Vitse-Prezident': 'vp-role',
    'Təhsil hər bir dövlətin, ölkənin, cəmiyyətin həyatının, fəaliyyətinin mühüm bir sahəsidir. Cəmiyyət təhsilsiz inkişaf edə bilməz.': 'leader-title1',
    '“Hər bir xalqın tərəqqisi onun təhsil səviyyəsi ilə müəyyən olunur.”': 'leader-title2',
    'Heydər Əliyev': 'leader-name',
    'Ümummilli Lider': 'leader-role',
    
    # Stats
    'Mükəmməlliyin Rəqəmlərlə İfadəsi.': 'stats-title',
    'Evrika şagirdi': 'stats-desc1',
    'Olimpiada qalibi': 'stats-desc2',
    'Qızıl medal': 'stats-desc3',
    'Qırmızı attestat': 'stats-desc4',
    
    # Values
    'DƏYƏRLƏRİMİZ': 'values-title',
    'AKADEMİK GÜC': 'val1-title',
    'Güclü tədris proqramı və nəticə yönümlü yanaşma': 'val1-desc',
    'XARAKTER': 'val2-title',
    'Dəyərlər, məsuliyyət və şəxsiyyət formalaşması': 'val2-desc',
    'MİLLİ KİMLİK': 'val3-title',
    'Məsuliyyətli vətəndaşlıq və vətənpərvərlik.': 'val3-desc',
    'İNNOVASİYA': 'val4-title',
    'Müasir texnologiyalar və yeni nəsil təhsil modeli': 'val4-desc',
    'BEYNƏLXALQ DÜŞÜNCƏ': 'val5-title',
    'Multikultural dəyərlərə hörmət və qlobal baxış.': 'val5-desc',
    'SOSİAL TƏŞƏBBÜSKARLIQ': 'val6-title',
    'Şəxsi inkişaf, liderlik və özünə inamın formalaşması': 'val6-desc',
    
    # Mission/Vision
    'Missiyamız': 'mission-title',
    'Milli dəyərlərə sadiq, qlobal düşüncəyə malik, yenilikçi şəxsiyyətlər yetişdirməkdir!': 'mission-desc',
    'Vizyonumuz': 'vision-title',
    'Gələcəyin yalnız liderlərini deyil, dünyanı dəyişdirə bilən, cəmiyyətə fayda verən şəxsiyyətlər formalaşdırmaqdır!': 'vision-desc',
    
    'VİZYON 2026': 'v2026-title1',
    'GƏLƏCƏYİ BU GÜN VAR EDƏN TƏHSİL EKOSİSTEMİ': 'v2026-title2',
    'EVRİKA artıq sadəcə məktəb deyil.': 'v2026-desc1',
    'EVRİKA – gələcək quran təhsil ekosistemidir.': 'v2026-desc2',
    
    'Məzunlarımız': 'alumni-sec-title1',
    'Dünyaya Açılan<br/>Uğur Yolumuz!': 'alumni-sec-title2',
    
    'VALİDEYNLƏRİMİZ': 'parents-title1',
    'Uşaqlarımızın Evrikada keçirdiyi hər gün onların gələcəyinə qoyulan ən böyük sərmayədir.': 'parents-desc1',
    
    'TƏSİSÇİNİN<br/>MESAJI': 'founder-title',
    'Xudaqulu Rzayev': 'founder-name',
    'EVRİKA TƏHSİL EKOSİSTEMİNİN TƏSİSÇİSİ': 'founder-role',
    
    'EVRİKA': 'join-title1',
    'EKOSİSTEMİ': 'join-title2',
    'BİZƏ QOŞULUN!': 'join-title3',
    'Müraciət Forması': 'join-form-title',
    
    'XƏBƏRLƏR': 'news-eyebrow',
    'Bütün Xəbərlər': 'news-btn-all',
    'TAM OXU': 'news-btn-read',
    
    'ƏMƏKDAŞLIQLARIMIZ': 'partners-title',
    'Partnyorlarımız': 'partners-subtitle',
}

for el in soup.find_all(True):
    # Only map elements with no children (leaf nodes) or those holding specific inner html
    # Because innerHTML may have <br> tags.
    inner = el.decode_contents().strip()
    if inner in mapping:
        el['data-i18n'] = mapping[inner]
        continue
    
    # Try text match
    text = el.get_text(strip=True)
    if not el.find_all() and text in mapping:
        el['data-i18n'] = mapping[text]

# Special cases for inputs / placeholders
form_mapping = {
    'Övladınızın adı': 'form-child-name',
    'Övladınızın soyadı': 'form-child-surname',
    'Müraciət etmək istədiyiniz Təhsil Mərkəzi': 'form-center',
    'Müraciət etmək istədiyiniz bölmə': 'form-section',
    'Müraciət etmək istədiyiniz sinif': 'form-class',
    'Gəldiyiniz təhsil müəssisəsi': 'form-school',
    'Telefon': 'form-phone',
    'E-mail': 'form-email'
}
for el in soup.find_all('label'):
    text = el.get_text(strip=True)
    if text in form_mapping:
        el['data-i18n'] = form_mapping[text]

for el in soup.find_all('button'):
    text = el.get_text(strip=True)
    if text == 'Göndər':
        el['data-i18n'] = 'form-submit'

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
