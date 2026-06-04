import re

def fix_parent_rules():
    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/about.html', 'r', encoding='utf-8') as f:
        html = f.read()

    replacements = [
        # Rules Titles
        (r'<h3>Ümumi prinsiplər</h3>', r'<h3 data-i18n="about-r1-title">Ümumi prinsiplər</h3>'),
        (r'<h3>Ünsiyyət və məlumatlandırma</h3>', r'<h3 data-i18n="about-r2-title">Ünsiyyət və məlumatlandırma</h3>'),
        (r'<h3>Tədris və davamiyyət</h3>', r'<h3 data-i18n="about-r3-title">Tədris və davamiyyət</h3>'),
        (r'<h3>Psixoloji yanaşma</h3>', r'<h3 data-i18n="about-r4-title">Psixoloji yanaşma</h3>'),
        (r'<h3>Təhlükəsizlik</h3>', r'<h3 data-i18n="about-r5-title">Təhlükəsizlik</h3>'),
        (r'<h3>Qidalanma</h3>', r'<h3 data-i18n="about-r6-title">Qidalanma</h3>'),
        (r'<h3>Etik Davranış</h3>', r'<h3 data-i18n="about-r7-title">Etik Davranış</h3>'),
        (r'<h3>Etik davranış</h3>', r'<h3 data-i18n="about-r7-title">Etik davranış</h3>'), # case handling
        
        # Rule 1
        (r'(<i class="fas fa-check-circle"></i>\s*)Valideyn Liseyin daxili qaydalarına və tədris yanaşmasına riayət edir', r'\1<span data-i18n="about-r1-l1">Valideyn Liseyin daxili qaydalarına və tədris yanaşmasına riayət edir</span>'),
        (r'(<i class="fas fa-handshake"></i>\s*)Münasibətlər qarşılıqlı hörmət və əməkdaşlıq üzərində qurulur', r'\1<span data-i18n="about-r1-l2">Münasibətlər qarşılıqlı hörmət və əməkdaşlıq üzərində qurulur</span>'),
        
        # Rule 2
        (r'(<i class="fas fa-broadcast-tower"></i>\s*)Rəsmi məlumat kanalları mütəmadi izlənilməlidir', r'\1<span data-i18n="about-r2-l1">Rəsmi məlumat kanalları mütəmadi izlənilməlidir</span>'),
        (r'(<i class="fas fa-user-tie"></i>\s*)Suallar birbaşa Lisey rəhbərliyinə yönləndirilməlidir', r'\1<span data-i18n="about-r2-l2">Suallar birbaşa Lisey rəhbərliyinə yönləndirilməlidir</span>'),
        (r'(<i class="fas fa-exclamation-triangle"></i>\s*)Qeyri-rəsmi məlumatlara əsaslanaraq nəticə çıxarmaq yolverilməzdir', r'\1<span data-i18n="about-r2-l3">Qeyri-rəsmi məlumatlara əsaslanaraq nəticə çıxarmaq yolverilməzdir</span>'),
        
        # Rule 3
        (r'(<i class="fas fa-calendar-check"></i>\s*)Şagirdin dərslərdə davamiyyəti təmin edilməlidir', r'\1<span data-i18n="about-r3-l1">Şagirdin dərslərdə davamiyyəti təmin edilməlidir</span>'),
        (r'(<i class="fas fa-bell"></i>\s*)Gecikmə və ya iştirak etməmə halları əvvəlcədən bildirilməlidir', r'\1<span data-i18n="about-r3-l2">Gecikmə və ya iştirak etməmə halları əvvəlcədən bildirilməlidir</span>'),
        (r'(<i class="fas fa-book-reader"></i>\s*)Valideyn şagirdin dərs məsuliyyətini dəstəkləməlidir', r'\1<span data-i18n="about-r3-l3">Valideyn şagirdin dərs məsuliyyətini dəstəkləməlidir</span>'),
        
        # Rule 4
        (r'(<i class="fas fa-brain"></i>\s*)Liseyin pedaqoji metodlarına hörmətlə yanaşılmalıdır', r'\1<span data-i18n="about-r4-l1">Liseyin pedaqoji metodlarına hörmətlə yanaşılmalıdır</span>'),
        (r'(<i class="fas fa-users-cog"></i>\s*)Şagird qarşısında müəllim haqqında mənfi fikir formalaşdırılmamalıdır', r'\1<span data-i18n="about-r4-l2">Şagird qarşısında müəllim haqqında mənfi fikir formalaşdırılmamalıdır</span>'),
        (r'(<i class="fas fa-heartbeat"></i>\s*)Şagirdin emosional vəziyyəti ilə bağlı məlumatlar paylaşılmalıdır', r'\1<span data-i18n="about-r4-l3">Şagirdin emosional vəziyyəti ilə bağlı məlumatlar paylaşılmalıdır</span>'),
        
        # Rule 5
        (r'(<i class="fas fa-shield-alt"></i>\s*)Təhlükəsizlik qaydalarına riayət edilməlidir', r'\1<span data-i18n="about-r5-l1">Təhlükəsizlik qaydalarına riayət edilməlidir</span>'),
        (r'(<i class="fas fa-video"></i>\s*)Kamera sistemi Lisey qaydalarına uyğun tətbiq olunur', r'\1<span data-i18n="about-r5-l2">Kamera sistemi Lisey qaydalarına uyğun tətbiq olunur</span>'),
        (r'(<i class="fas fa-user-secret"></i>\s*)Digər ailələrin məxfiliyinə hörmət olunmalıdır', r'\1<span data-i18n="about-r5-l3">Digər ailələrin məxfiliyinə hörmət olunmalıdır</span>'),
        
        # Rule 6
        (r'(<i class="fas fa-utensils"></i>\s*)Qidalanma sistemi balanslı və yaşa uyğun təşkil olunur', r'\1<span data-i18n="about-r6-l1">Qidalanma sistemi balanslı və yaşa uyğun təşkil olunur</span>'),
        (r'(<i class="fas fa-notes-medical"></i>\s*)Sağlamlıq və allergiya məlumatları əvvəlcədən bildirilməlidir', r'\1<span data-i18n="about-r6-l2">Sağlamlıq və allergiya məlumatları əvvəlcədən bildirilməlidir</span>'),
        
        # Rule 7
        (r'(<i class="fas fa-comments"></i>\s*)Hörmətli ünsiyyət qorunmalıdır', r'\1<span data-i18n="about-r7-l1">Hörmətli ünsiyyət qorunmalıdır</span>'),
        (r'(<i class="fas fa-gavel"></i>\s*)Mübahisələr rəsmi qaydada həll edilməlidir', r'\1<span data-i18n="about-r7-l2">Mübahisələr rəsmi qaydada həll edilməlidir</span>'),
        (r'(<i class="fas fa-ban"></i>\s*)Liseyin nüfuzuna xələl gətirə biləcək davranışlardan çəkinilməlidir', r'\1<span data-i18n="about-r7-l3">Liseyin nüfuzuna xələl gətirə biləcək davranışlardan çəkinilməlidir</span>'),
    ]

    for p, r in replacements:
        html = re.sub(p, r, html, flags=re.IGNORECASE)

    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/about.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    fix_parent_rules()
    print("Fixed parent rules in about.html")
