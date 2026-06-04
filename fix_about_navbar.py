import re

def fix_about_navbar():
    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/about.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Logo
    html = re.sub(r'(<a href="index.html" class="logo"[^>]*>)Evrika', r'\1<span data-i18n="join-title1">Evrika</span>', html)
    
    # Top level nav links
    html = re.sub(r'<a href="index\.html">Ana Səhifə</a>', r'<a href="index.html" data-i18n="nav-home">Ana Səhifə</a>', html)
    html = re.sub(r'<a href="about\.html" class="active">Haqqımızda</a>', r'<a href="about.html" class="active" data-i18n="nav-about">Haqqımızda</a>', html)
    html = re.sub(r'<a href="schools\.html">Akademik İstiqamətlər</a>', r'<a href="schools.html" data-i18n="nav-academic">Akademik İstiqamətlər</a>', html)
    html = re.sub(r'<a href="vacancy\.html">Vakansiya &amp; Təcrübə</a>', r'<a href="vacancy.html" data-i18n="nav-vacancy">Vakansiya &amp; Təcrübə</a>', html)
    html = re.sub(r'<a href="journal\.html">Evrika Jurnalı</a>', r'<a href="journal.html" data-i18n="nav-journal">Evrika Jurnalı</a>', html)
    html = re.sub(r'<a href="contact\.html">Əlaqə</a>', r'<a href="contact.html" data-i18n="nav-contact">Əlaqə</a>', html)

    # Register button
    html = re.sub(r'(<a href="https://qebul\.evrika\.edu\.az"[^>]*>\s*)Qeydiyyat\s*</a>', r'\1<span data-i18n="nav-register">Qeydiyyat</span></a>', html)

    # Dropdown items (Haqqımızda)
    html = re.sub(r'<span class="dropdown-item-title">Haqqımızda</span>', r'<span class="dropdown-item-title" data-i18n="nav-about">Haqqımızda</span>', html)
    html = re.sub(r'<span class="dropdown-item-desc">Bizim hekayəmiz</span>', r'<span class="dropdown-item-desc" data-i18n="nav-about-desc">Bizim hekayəmiz</span>', html)
    html = re.sub(r'<span class="dropdown-item-title">Məzunlar</span>', r'<span class="dropdown-item-title" data-i18n="nav-alumni">Məzunlar</span>', html)
    html = re.sub(r'<span class="dropdown-item-desc">Fəxrlərimiz</span>', r'<span class="dropdown-item-desc" data-i18n="nav-alumni-desc">Fəxrlərimiz</span>', html)
    html = re.sub(r'<span class="dropdown-item-title">Uğurlar</span>', r'<span class="dropdown-item-title" data-i18n="nav-achievements">Uğurlar</span>', html)
    html = re.sub(r'<span class="dropdown-item-desc">Nailiyyətlərimiz</span>', r'<span class="dropdown-item-desc" data-i18n="nav-achievements-desc">Nailiyyətlərimiz</span>', html)
    html = re.sub(r'<span class="dropdown-item-title">Xəbərlər</span>', r'<span class="dropdown-item-title" data-i18n="nav-news">Xəbərlər</span>', html)
    html = re.sub(r'<span class="dropdown-item-desc">Ən son yeniliklər</span>', r'<span class="dropdown-item-desc" data-i18n="nav-news-desc">Ən son yeniliklər</span>', html)

    # Dropdown items (Akademik İstiqamətlər)
    html = re.sub(r'<span class="dropdown-item-title">Evrika BETL Nərimanov</span>', r'<span class="dropdown-item-title" data-i18n="nav-lisey1">Evrika BETL Nərimanov</span>', html)
    html = re.sub(r'<span class="dropdown-item-desc">Elm və Texnologiya Mərkəzi</span>', r'<span class="dropdown-item-desc" data-i18n="nav-lisey1-desc">Elm və Texnologiya Mərkəzi</span>', html)
    html = re.sub(r'<span class="dropdown-item-title">Evrika BETL Gənclik</span>', r'<span class="dropdown-item-title" data-i18n="nav-lisey2">Evrika BETL Gənclik</span>', html)
    html = re.sub(r'<span class="dropdown-item-desc">Beynəlxalq Təhsil Kampusu</span>', r'<span class="dropdown-item-desc" data-i18n="nav-lisey2-desc">Beynəlxalq Təhsil Kampusu</span>', html)
    html = re.sub(r'<span class="dropdown-item-title">Montessori Kids Academy</span>', r'<span class="dropdown-item-title" data-i18n="nav-montessori">Montessori Kids Academy</span>', html)
    html = re.sub(r'<span class="dropdown-item-desc">Bağça və Erkən İnkişaf</span>', r'<span class="dropdown-item-desc" data-i18n="nav-montessori-desc">Bağça və Erkən İnkişaf</span>', html)
    html = re.sub(r'<span class="dropdown-item-title">Eduhome Hazırlıq</span>', r'<span class="dropdown-item-title" data-i18n="nav-eduhome">Eduhome Hazırlıq</span>', html)
    html = re.sub(r'<span class="dropdown-item-desc">Xaricdə Təhsil və Hazırlıq</span>', r'<span class="dropdown-item-desc" data-i18n="nav-eduhome-desc">Xaricdə Təhsil və Hazırlıq</span>', html)
    html = re.sub(r'<span class="dropdown-item-title">Zümrüd İdman Mərkəzi</span>', r'<span class="dropdown-item-title" data-i18n="nav-zumrud">Zümrüd İdman Mərkəzi</span>', html)
    html = re.sub(r'<span class="dropdown-item-desc">Sağlam Həyat və Fəaliyyət</span>', r'<span class="dropdown-item-desc" data-i18n="nav-zumrud-desc">Sağlam Həyat və Fəaliyyət</span>', html)

    # Dropdown items (Vakansiya & Təcrübə)
    html = re.sub(r'<span class="dropdown-item-title">Karyera və Vakansiyalar</span>', r'<span class="dropdown-item-title" data-i18n="nav-vac-title">Karyera və Vakansiyalar</span>', html)
    html = re.sub(r'<span class="dropdown-item-desc">Açıq iş elanları</span>', r'<span class="dropdown-item-desc" data-i18n="nav-vac-desc">Açıq iş elanları</span>', html)
    html = re.sub(r'<span class="dropdown-item-title">Pedaqoji Təcrübə və İnkişaf Mərkəzi</span>', r'<span class="dropdown-item-title" data-i18n="nav-ptim-title">Pedaqoji Təcrübə və İnkişaf Mərkəzi</span>', html)
    html = re.sub(r'<span class="dropdown-item-desc">PTİM</span>', r'<span class="dropdown-item-desc" data-i18n="nav-ptim-desc">PTİM</span>', html)

    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/about.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    fix_about_navbar()
    print("Fixed navbar in about.html")
