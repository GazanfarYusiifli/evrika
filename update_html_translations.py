import re
import sys

def modify_file():
    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Detallara bax
    html = re.sub(
        r'(<a class="btn btn-outline".*?>)Detallara bax (<i class="fas fa-arrow-right"></i></a>)',
        r'\1<span data-i18n="btn-details-look">Detallara bax</span> \2',
        html
    )

    # 2. Mükəmməlliyin Rəqəmlərlə İfadəsi
    # We will add data-i18n directly to the text part by wrapping it
    html = re.sub(
        r'Mükəmməlliyin Rəqəmlərlə İfadəsi(<span style="color: #60a5fa;">\.</span>)',
        r'<span data-i18n="stats-title-text">Mükəmməlliyin Rəqəmlərlə İfadəsi</span>\1',
        html
    )

    # 3. GƏLƏCƏYİ BU GÜN VAR EDƏN TƏHSİL EKOSİSTEMİ
    # Line 1723
    html = re.sub(
        r'(<h4 class="banner-title">)(GƏLƏCƏYİ BU GÜN VAR EDƏN) (<span class="highlight">TƏHSİL EKOSİSTEMİ</span></h4>)',
        r'<h4 class="banner-title"><span data-i18n="v2026-title2-part1">\2</span> <span class="highlight" data-i18n="v2026-title2-part2">TƏHSİL EKOSİSTEMİ</span></h4>',
        html
    )

    # 4. Founder quote
    html = re.sub(
        r'(<blockquote class="premium-quote"[^>]*>)\s*"Evrika Təhsil Ekosistemi” mənim üçün yalnız bir təhsil müəssisəsi deyil — vətənimə, millətimə və onun gələcək tərəqqisinə olan sevgimin təzahürüdür\s*(</blockquote>)',
        r'\1\n                 <span data-i18n="founder-quote-text">"Evrika Təhsil Ekosistemi” mənim üçün yalnız bir təhsil müəssisəsi deyil — vətənimə, millətimə və onun gələcək tərəqqisinə olan sevgimin təzahürüdür</span>\n               \2',
        html
    )

    # 5. Footer rights
    html = re.sub(
        r'(<p style="color: rgba\(255,255,255,0\.4\); font-size: 0\.85rem;">)© 2026 Evrika Təhsil Ekosistemi. Bütün hüquqlar qorunur.(</p>)',
        r'\1<span data-i18n="footer-rights">© 2026 Evrika Təhsil Ekosistemi. Bütün hüquqlar qorunur.</span>\2',
        html
    )

    # 6. Privacy Policy
    html = re.sub(
        r'(<a href="privacy\.html" style="[^"]*">)Məxfilik Siyasəti(</a>)',
        r'\1<span data-i18n="footer-privacy">Məxfilik Siyasəti</span>\2',
        html
    )

    # 7. Terms of Use
    html = re.sub(
        r'(<a href="terms\.html" style="[^"]*">)İstifadə Şərtləri(</a>)',
        r'\1<span data-i18n="footer-terms">İstifadə Şərtləri</span>\2',
        html
    )

    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    modify_file()
    print("Done")
