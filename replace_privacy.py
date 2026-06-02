import re

with open('privacy.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace title
content = re.sub(r'<title>.*?</title>', '<title>Məxfilik Siyasəti | Evrika Təhsil Ekosistemi</title>', content)

main_content = """    <main>
      <section class="section" style="padding: 240px 0 100px; text-align:center; position:relative; overflow:hidden; background: #070d1f;">
        <div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 0%,rgba(139,26,43,0.3)0%,transparent 70%);pointer-events:none;"></div>
        <div class="container" style="position:relative;z-index:10;">
          <h1 class="titan-header" style="font-size:4rem;color:var(--white);margin-bottom:20px;font-weight:900;">Məxfilik <span style="color:var(--burgundy);">Siyasəti</span></h1>
          <p style="color:rgba(255,255,255,0.7);font-size:1.2rem;max-width:600px;margin:0 auto;">Son yenilənmə: May 2026</p>
        </div>
      </section>

      <section class="section" style="padding: 80px 0; background: #f8f9fa;">
        <div class="container" style="max-width: 900px; background: white; padding: 60px; border-radius: 30px; box-shadow: 0 20px 40px rgba(0,0,0,0.05);">
          
          <h2 style="color: var(--navy); margin-bottom: 20px; font-weight: 800;">1. Məlumatların Toplanması</h2>
          <p style="color: #555; line-height: 1.8; margin-bottom: 30px; font-size: 1.05rem;">
            Evrika Təhsil Ekosistemi olaraq, sizə daha yaxşı xidmət göstərmək üçün müəyyən fərdi məlumatları (ad, soyad, e-poçt ünvanı, telefon nömrəsi və s.) toplayırıq. Bu məlumatlar yalnız qeydiyyat, əlaqə və xidmət keyfiyyətinin artırılması məqsədilə istifadə olunur.
          </p>

          <h2 style="color: var(--navy); margin-bottom: 20px; font-weight: 800;">2. Kukilərin (Cookies) İstifadəsı</h2>
          <p style="color: #555; line-height: 1.8; margin-bottom: 30px; font-size: 1.05rem;">
            Veb saytımız sizin təcrübənizi fərdiləşdirmək, saytın trafikini analiz etmək və təhlükəsizliyi təmin etmək üçün kukilərdən (cookies) istifadə edir. Kukilər kompüterinizdə saxlanılan kiçik mətn fayllarıdır və onlardan imtina etmək hüququna sahibsiniz.
          </p>

          <h2 style="color: var(--navy); margin-bottom: 20px; font-weight: 800;">3. Məlumatların Təhlükəsizliyi</h2>
          <p style="color: #555; line-height: 1.8; margin-bottom: 30px; font-size: 1.05rem;">
            Şəxsi məlumatlarınızın təhlükəsizliyi bizim üçün prioritetdir. Saytımız müasir şifrələmə (SSL/TLS) texnologiyalarından və təhlükəsiz verilənlər bazalarından istifadə edərək məlumatlarınızı qoruyur. Sizin məlumatlarınız heç bir halda üçüncü tərəflərə satılmır və ya qeyri-qanuni paylanmır.
          </p>

          <h2 style="color: var(--navy); margin-bottom: 20px; font-weight: 800;">4. Üçüncü Tərəf Bağlantıları</h2>
          <p style="color: #555; line-height: 1.8; margin-bottom: 30px; font-size: 1.05rem;">
            Saytımızda digər veb saytlara keçidlər (linklər) ola bilər. Bu bağlantılara daxil olduğunuz zaman həmin saytların öz məxfilik siyasətləri tətbiq olunur. Biz üçüncü tərəf saytlarının məzmununa və ya təhlükəsizliyinə görə məsuliyyət daşımırıq.
          </p>

          <h2 style="color: var(--navy); margin-bottom: 20px; font-weight: 800;">5. Dəyişikliklər və Əlaqə</h2>
          <p style="color: #555; line-height: 1.8; margin-bottom: 30px; font-size: 1.05rem;">
            Bu Məxfilik Siyasəti zaman-zaman yenilənə bilər. Dəyişikliklər olduqda bu səhifədə elan ediləcək. Hər hansı sualınız olarsa, <strong>info@evrikaliseyi.edu.az</strong> ünvanı ilə bizimlə əlaqə saxlaya bilərsiniz.
          </p>

        </div>
      </section>
    </main>"""

content = re.sub(r'<main>.*?</main>', main_content, content, flags=re.DOTALL)

with open('privacy.html', 'w', encoding='utf-8') as f:
    f.write(content)
