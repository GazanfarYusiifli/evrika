import re
import json

def update_about_html():
    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/about.html', 'r', encoding='utf-8') as f:
        html = f.read()

    replacements = [
        # Hero
        (r'>BİZİM HEKAYƏMIZ<', r' data-i18n="about-eyebrow">BİZİM HEKAYƏMIZ<'),
        (r'>\s*Haqqımızda\s*</h1\s*>', r' data-i18n="about-title">Haqqımızda</h1>'),
        (r'>\s*“Evrika Təhsil Ekosistemi — hər bir şagirdin potensialını gələcəyə çevirən inkişaf mühitidir! Evrika Təhsil Ekosistemi — hər bir şagirdin potensialını üzə çıxarmaq üçün qurulmuş ilham mənbəyidir\.”\s*</p\s*>',
         r' data-i18n="about-desc">“Evrika Təhsil Ekosistemi — hər bir şagirdin potensialını gələcəyə çevirən inkişaf mühitidir! Evrika Təhsil Ekosistemi — hər bir şagirdin potensialını üzə çıxarmaq üçün qurulmuş ilham mənbəyidir.”</p>'),

        # Mission / Vision
        (r'<h2 class="agency-title">MİSSİYAMIZ</h2>', r'<h2 class="agency-title" data-i18n="about-mission-title">MİSSİYAMIZ</h2>'),
        (r'“Milli dəyərlərə sadiq, <span>qlobal düşüncəyə</span> malik, yenilikçi şəxsiyyətlər yetişdirməkdir!”', r'<span data-i18n="about-mission-desc">“Milli dəyərlərə sadiq, <span>qlobal düşüncəyə</span> malik, yenilikçi şəxsiyyətlər yetişdirməkdir!”</span>'),
        (r'<h2 class="agency-title">VİZYONUMUZ</h2>', r'<h2 class="agency-title" data-i18n="about-vision-title">VİZYONUMUZ</h2>'),
        (r'“Gələcəyin yalnız liderlərini deyil, <span>dünyanı dəyişdirə bilən</span>, cəmiyyətə fayda verən şəxsiyyətlər formalaşdırmaqdır!”', r'<span data-i18n="about-vision-desc">“Gələcəyin yalnız liderlərini deyil, <span>dünyanı dəyişdirə bilən</span>, cəmiyyətə fayda verən şəxsiyyətlər formalaşdırmaqdır!”</span>'),

        # Goals Section
        (r'>Nə Edirik\?<', r' data-i18n="about-goals-eyebrow">Nə Edirik?<'),
        (r'>Məqsədimiz</h2\s*>', r' data-i18n="about-goals-title">Məqsədimiz</h2>'),
        (r'>Evrika Təhsil Ekosistemi olaraq məqsədimiz yalnız akademik bilik deyil, həm də etik dəyərlərə malik liderlər yetişdirməkdir\.</p\s*>', r' data-i18n="about-goals-desc">Evrika Təhsil Ekosistemi olaraq məqsədimiz yalnız akademik bilik deyil, həm də etik dəyərlərə malik liderlər yetişdirməkdir.</p>'),

        (r'<h3 class="agc-title">Keyfiyyətli Təhsil</h3>', r'<h3 class="agc-title" data-i18n="about-g1-title">Keyfiyyətli Təhsil</h3>'),
        (r'<p class="agc-text">Hər şagirdin fərdi inkişafını dəstəkləyən, beynəlxalq standartlara uyğun, müasir metodlarla zənginləşdirilmiş tədris mühiti yaradırıq\.</p>', r'<p class="agc-text" data-i18n="about-g1-desc">Hər şagirdin fərdi inkişafını dəstəkləyən, beynəlxalq standartlara uyğun, müasir metodlarla zənginləşdirilmiş tədris mühiti yaradırıq.</p>'),

        (r'<h3 class="agc-title">Qlobal Görüş</h3>', r'<h3 class="agc-title" data-i18n="about-g2-title">Qlobal Görüş</h3>'),
        (r'<p class="agc-text">Şagirdlərimizi 21-ci əsrin çağırışlarına hazırlayır, onları çoxdilli, mültikultural düşüncəyə malik fərdlər kimi yetişdiririk\.</p>', r'<p class="agc-text" data-i18n="about-g2-desc">Şagirdlərimizi 21-ci əsrin çağırışlarına hazırlayır, onları çoxdilli, mültikultural düşüncəyə malik fərdlər kimi yetişdiririk.</p>'),

        (r'<h3 class="agc-title">Etik Dəyərlər</h3>', r'<h3 class="agc-title" data-i18n="about-g3-title">Etik Dəyərlər</h3>'),
        (r'<p class="agc-text">Akademik biliklə yanaşı dürüstlük, məsuliyyət və vətənpərvərlik kimi mənəvi dəyərlərin formalaşmasına xüsusi əhəmiyyət veririk\.</p>', r'<p class="agc-text" data-i18n="about-g3-desc">Akademik biliklə yanaşı dürüstlük, məsuliyyət və vətənpərvərlik kimi mənəvi dəyərlərin formalaşmasına xüsusi əhəmiyyət veririk.</p>'),

        (r'<h3 class="agc-title">Liderlik & İnkişaf</h3>', r'<h3 class="agc-title" data-i18n="about-g4-title">Liderlik & İnkişaf</h3>'),
        (r'<p class="agc-text">Şagirdlərə liderlik, yaradıcılıq və innovasiya bacarıqları aşılayaraq onları gələcəyin arxitektorlarına çeviririk\.</p>', r'<p class="agc-text" data-i18n="about-g4-desc">Şagirdlərə liderlik, yaradıcılıq və innovasiya bacarıqları aşılayaraq onları gələcəyin arxitektorlarına çeviririk.</p>'),

        (r'<h3 class="agc-title">Ailə & Cəmiyyət</h3>', r'<h3 class="agc-title" data-i18n="about-g5-title">Ailə & Cəmiyyət</h3>'),
        (r'<p class="agc-text">Müəllim, şagird və valideyn əməkdaşlığını əsas götürərək güclü bir məktəb icması qururuq\.</p>', r'<p class="agc-text" data-i18n="about-g5-desc">Müəllim, şagird və valideyn əməkdaşlığını əsas götürərək güclü bir məktəb icması qururuq.</p>'),

        (r'<h3 class="agc-title">Elm & Texnologiya</h3>', r'<h3 class="agc-title" data-i18n="about-g6-title">Elm & Texnologiya</h3>'),
        (r'<p class="agc-text">STEAM yanaşması, laboratoriya, kodlaşdırma və robotexnika ilə şagirdlərə gələcəyin texnologiyalarını bu gün öyrədirik\.</p>', r'<p class="agc-text" data-i18n="about-g6-desc">STEAM yanaşması, laboratoriya, kodlaşdırma və robotexnika ilə şagirdlərə gələcəyin texnologiyalarını bu gün öyrədirik.</p>'),

        # Founder
        (r'>\s*TƏSİSÇİNİN \s*<br>', r' data-i18n="about-founder-title-1">TƏSİSÇİNİN <br>'),
        (r'>\s*MESAJI\s*<span', r' data-i18n="about-founder-title-2">MESAJI\n                <span'),
        (r'>"Evrika Təhsil Ekosistemi” mənim üçün yalnız bir təhsil müəssisəsi deyil — vətənimə, millətimə və onun gələcək tərəqqisinə olan sevgimin təzahürüdür', r'<span data-i18n="about-founder-quote">"Evrika Təhsil Ekosistemi” mənim üçün yalnız bir təhsil müəssisəsi deyil — vətənimə, millətimə və onun gələcək tərəqqisinə olan sevgimin təzahürüdür</span>'),
        (r'>EVRİKA TƏHSİL EKOSİSTEMİNİN TƏSİSÇİSİ<', r' data-i18n="about-founder-role">EVRİKA TƏHSİL EKOSİSTEMİNİN TƏSİSÇİSİ<'),

        # Parent Rules
        (r'>Evrika Konsepsiyası</h2\s*>', r' data-i18n="about-rules-title">Evrika Konsepsiyası</h2>'),
        (r'>\s*VALİDEYN QAYDALARI VƏ ÖHDƏLİKLƏRİ\s*</p\s*>', r' data-i18n="about-rules-eyebrow">\n              VALİDEYN QAYDALARI VƏ ÖHDƏLİKLƏRİ\n            </p>'),

        (r'<h3 class="item-title">ÜMUMİ PRİNSİPLƏR</h3>', r'<h3 class="item-title" data-i18n="about-r1-title">ÜMUMİ PRİNSİPLƏR</h3>'),
        (r'<li>Valideyn Liseyin daxili qaydalarına və tədris yanaşmasına riayət edir</li>', r'<li data-i18n="about-r1-l1">Valideyn Liseyin daxili qaydalarına və tədris yanaşmasına riayət edir</li>'),
        (r'<li>Münasibətlər qarşılıqlı hörmət və əməkdaşlıq üzərində qurulur</li>', r'<li data-i18n="about-r1-l2">Münasibətlər qarşılıqlı hörmət və əməkdaşlıq üzərində qurulur</li>'),

        (r'<h3 class="item-title">ÜNSİYYƏT VƏ MƏLUMATLANDIRMA</h3>', r'<h3 class="item-title" data-i18n="about-r2-title">ÜNSİYYƏT VƏ MƏLUMATLANDIRMA</h3>'),
        (r'<li>Rəsmi məlumat kanalları mütəmadi izlənilməlidir</li>', r'<li data-i18n="about-r2-l1">Rəsmi məlumat kanalları mütəmadi izlənilməlidir</li>'),
        (r'<li>Suallar birbaşa Lisey rəhbərliyinə yönləndirilməlidir</li>', r'<li data-i18n="about-r2-l2">Suallar birbaşa Lisey rəhbərliyinə yönləndirilməlidir</li>'),
        (r'<li>Qeyri-rəsmi məlumatlara əsaslanaraq nəticə çıxarmaq yolverilməzdir</li>', r'<li data-i18n="about-r2-l3">Qeyri-rəsmi məlumatlara əsaslanaraq nəticə çıxarmaq yolverilməzdir</li>'),

        (r'<h3 class="item-title">TƏDRİS VƏ DAVAMİYYƏT</h3>', r'<h3 class="item-title" data-i18n="about-r3-title">TƏDRİS VƏ DAVAMİYYƏT</h3>'),
        (r'<li>Şagirdin dərslərdə davamiyyəti təmin edilməlidir</li>', r'<li data-i18n="about-r3-l1">Şagirdin dərslərdə davamiyyəti təmin edilməlidir</li>'),
        (r'<li>Gecikmə və ya iştirak etməmə halları əvvəlcədən bildirilməlidir</li>', r'<li data-i18n="about-r3-l2">Gecikmə və ya iştirak etməmə halları əvvəlcədən bildirilməlidir</li>'),
        (r'<li>Valideyn şagirdin dərs məsuliyyətini dəstəkləməlidir</li>', r'<li data-i18n="about-r3-l3">Valideyn şagirdin dərs məsuliyyətini dəstəkləməlidir</li>'),

        (r'<h3 class="item-title">PSİXOLOJİ YANAŞMA</h3>', r'<h3 class="item-title" data-i18n="about-r4-title">PSİXOLOJİ YANAŞMA</h3>'),
        (r'<li>Liseyin pedaqoji metodlarına hörmətlə yanaşılmalıdır</li>', r'<li data-i18n="about-r4-l1">Liseyin pedaqoji metodlarına hörmətlə yanaşılmalıdır</li>'),
        (r'<li>Şagird qarşısında müəllim haqqında mənfi fikir formalaşdırılmamalıdır</li>', r'<li data-i18n="about-r4-l2">Şagird qarşısında müəllim haqqında mənfi fikir formalaşdırılmamalıdır</li>'),
        (r'<li>Şagirdin emosional vəziyyəti ilə bağlı məlumatlar paylaşılmalıdır</li>', r'<li data-i18n="about-r4-l3">Şagirdin emosional vəziyyəti ilə bağlı məlumatlar paylaşılmalıdır</li>'),

        (r'<h3 class="item-title">TƏHLÜKƏSİZLİK</h3>', r'<h3 class="item-title" data-i18n="about-r5-title">TƏHLÜKƏSİZLİK</h3>'),
        (r'<li>Təhlükəsizlik qaydalarına riayət edilməlidir</li>', r'<li data-i18n="about-r5-l1">Təhlükəsizlik qaydalarına riayət edilməlidir</li>'),
        (r'<li>Kamera sistemi Lisey qaydalarına uyğun tətbiq olunur</li>', r'<li data-i18n="about-r5-l2">Kamera sistemi Lisey qaydalarına uyğun tətbiq olunur</li>'),
        (r'<li>Digər ailələrin məxfiliyinə hörmət olunmalıdır</li>', r'<li data-i18n="about-r5-l3">Digər ailələrin məxfiliyinə hörmət olunmalıdır</li>'),

        (r'<h3 class="item-title">QİDALANMA</h3>', r'<h3 class="item-title" data-i18n="about-r6-title">QİDALANMA</h3>'),
        (r'<li>Qidalanma sistemi balanslı və yaşa uyğun təşkil olunur</li>', r'<li data-i18n="about-r6-l1">Qidalanma sistemi balanslı və yaşa uyğun təşkil olunur</li>'),
        (r'<li>Sağlamlıq və allergiya məlumatları əvvəlcədən bildirilməlidir</li>', r'<li data-i18n="about-r6-l2">Sağlamlıq və allergiya məlumatları əvvəlcədən bildirilməlidir</li>'),

        (r'<h3 class="item-title">ETİK DAVRANIŞ</h3>', r'<h3 class="item-title" data-i18n="about-r7-title">ETİK DAVRANIŞ</h3>'),
        (r'<li>Hörmətli ünsiyyət qorunmalıdır</li>', r'<li data-i18n="about-r7-l1">Hörmətli ünsiyyət qorunmalıdır</li>'),
        (r'<li>Mübahisələr rəsmi qaydada həll edilməlidir</li>', r'<li data-i18n="about-r7-l2">Mübahisələr rəsmi qaydada həll edilməlidir</li>'),
        (r'<li>Liseyin nüfuzuna xələl gətirə biləcək davranışlardan çəkinilməlidir</li>', r'<li data-i18n="about-r7-l3">Liseyin nüfuzuna xələl gətirə biləcək davranışlardan çəkinilməlidir</li>'),

        # Leadership / Team
        (r'>\s*EVRİKA TƏHSİL EKOSİSTEMİ\s*</p\s*>', r' data-i18n="about-team-eyebrow">EVRİKA TƏHSİL EKOSİSTEMİ</p>'),
        (r'>\s*Rəhbərlik\s*</h2\s*>', r' data-i18n="about-team-title">Rəhbərlik</h2>'),
        (r'>\s*PEŞƏKAR KOMANDA\s*</p\s*>', r' data-i18n="about-team2-eyebrow">PEŞƏKAR KOMANDA</p>'),
        (r'>\s*İdarə Heyəti\s*</h2\s*>', r' data-i18n="about-team2-title">İdarə Heyəti</h2>'),

        # Job Titles
        (r'>EVRİKA TƏHSİL EKOSİSTEMİ ÜZRƏ TƏSİSÇİ<', r' data-i18n="job-founder">EVRİKA TƏHSİL EKOSİSTEMİ ÜZRƏ TƏSİSÇİ<'),
        (r'>EVRİKA BEYNƏLXALQ ELM VƏ TEXNOLOGİYA LİSEYİ \( NƏRİMANOV FİLİALI ÜZRƏ\) DİREKTOR<', r' data-i18n="job-dir-nerimanov">EVRİKA BEYNƏLXALQ ELM VƏ TEXNOLOGİYA LİSEYİ ( NƏRİMANOV FİLİALI ÜZRƏ) DİREKTOR<'),
        (r'>EVRİKA BEYNƏLXALQ ELM VƏ TEXNOLOGİYA LİSEYİ \( GƏNCLİK FİLİALI ÜZRƏ \) DİREKTOR<', r' data-i18n="job-dir-genclik">EVRİKA BEYNƏLXALQ ELM VƏ TEXNOLOGİYA LİSEYİ ( GƏNCLİK FİLİALI ÜZRƏ ) DİREKTOR<'),
        (r'>TƏMAYÜL İŞLƏRİ ÜZRƏ DİREKTOR MÜAVİNİ<', r' data-i18n="job-dep-dir-temayul">TƏMAYÜL İŞLƏRİ ÜZRƏ DİREKTOR MÜAVİNİ<'),
        (r'>MALİYYƏ DİREKTORU<', r' data-i18n="job-fin-dir">MALİYYƏ DİREKTORU<'),
        (r'>İNSAN RESURSLARI ÜZRƏ DEPARTAMENT RƏHBƏRİ<', r' data-i18n="job-hr-dir">İNSAN RESURSLARI ÜZRƏ DEPARTAMENT RƏHBƏRİ<'),
        (r'>VALİDEYNLƏRLƏ İŞ ÜZRƏ DİREKTOR MÜAVİNİ<', r' data-i18n="job-dep-dir-parents">VALİDEYNLƏRLƏ İŞ ÜZRƏ DİREKTOR MÜAVİNİ<'),
        (r'>İBTİDAİ TƏHSİL ÜZRƏ DİREKTOR MÜAVİNİ<', r' data-i18n="job-dep-dir-primary">İBTİDAİ TƏHSİL ÜZRƏ DİREKTOR MÜAVİNİ<'),
        (r'>ÜMUMİ ORTA TƏHSİL ÜZRƏ DİREKTOR MÜAVİNİ<', r' data-i18n="job-dep-dir-mid">ÜMUMİ ORTA TƏHSİL ÜZRƏ DİREKTOR MÜAVİNİ<'),
        (r'>İNGİLİS BÖLMƏSİ RƏHBƏRİ<', r' data-i18n="job-eng-head">İNGİLİS BÖLMƏSİ RƏHBƏRİ<'),
        (r'>TÜRK BÖLMƏSİ ÜZRƏ DİR\. MÜAVİNİ<', r' data-i18n="job-dep-dir-turk">TÜRK BÖLMƏSİ ÜZRƏ DİR. MÜAVİNİ<'),
        (r'>İBTİDAİ TƏRBİYƏ İŞLƏRİ MÜAVİNİ<', r' data-i18n="job-dep-dir-primary-edu">İBTİDAİ TƏRBİYƏ İŞLƏRİ MÜAVİNİ<'),
        (r'>YUXARI SİNİF TƏRBİYƏ İŞLƏRİ MÜAVİNİ<', r' data-i18n="job-dep-dir-high-edu">YUXARI SİNİF TƏRBİYƏ İŞLƏRİ MÜAVİNİ<'),
        (r'>İDMAN VƏ DƏRNƏKLƏR MÜAVİNİ<', r' data-i18n="job-dep-dir-sports">İDMAN VƏ DƏRNƏKLƏR MÜAVİNİ<'),
        (r'>TƏHSİL NAZİRLİYİ ÜZRƏ KOORDİNATOR<', r' data-i18n="job-coordinator">TƏHSİL NAZİRLİYİ ÜZRƏ KOORDİNATOR<'),
        (r'>HƏKİM<', r' data-i18n="job-doctor">HƏKİM<'),
        (r'>PSİXOLOQ<', r' data-i18n="job-psychologist">PSİXOLOQ<'),
        (r'>STEAM RƏHBƏRİ<', r' data-i18n="job-steam">STEAM RƏHBƏRİ<'),

        # Footer mini info
        (r'>\s*Evrika Təhsil Ekosistemi — Qlobal təhsil standartları, innovativ yanaşma və parlaq gələcəkdir\.\s*</p\s*>', r' data-i18n="footer-desc">Evrika Təhsil Ekosistemi — Qlobal təhsil standartları, innovativ yanaşma və parlaq gələcəkdir.</p>')
    ]

    for p, r in replacements:
        if not re.search(p, html) and "about-eyebrow" not in r:
            pass # just a check
        html = re.sub(p, r, html)

    # Some replacements need multiple times if they appear twice but usually regex replaces all
    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/about.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    update_about_html()
    print("HTML updated.")
