import re

with open('privacy.html', 'r', encoding='utf-8') as f:
    content = f.read()

main_content = """    <main>
      <section class="section" style="padding: 240px 0 100px; text-align:center; position:relative; overflow:hidden; background: #070d1f;">
        <div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 0%,rgba(139,26,43,0.3)0%,transparent 70%);pointer-events:none;"></div>
        <div class="container" style="position:relative;z-index:10;">
          <h1 class="titan-header" style="font-size:4rem;color:var(--white);margin-bottom:20px;font-weight:900;">Məxfilik <span style="color:var(--burgundy);">Siyasəti</span></h1>
        </div>
      </section>

      <section class="section" style="padding: 80px 0; background: #f8f9fa;">
        <div class="container" style="max-width: 900px; background: white; padding: 60px; border-radius: 30px; box-shadow: 0 20px 40px rgba(0,0,0,0.05);">
          
          <p style="color: #555; line-height: 1.8; margin-bottom: 40px; font-size: 1.05rem;">
            Evrika Liseyi istifadəçilərin şəxsi məlumatlarının qorunmasına böyük önəm verir. Bu Məxfilik Siyasəti saytımızdan istifadə zamanı toplanan məlumatların necə istifadə olunduğunu, saxlanıldığını və qorunduğunu izah edir.
          </p>

          <h2 style="color: var(--navy); margin-bottom: 20px; font-weight: 800; font-size: 1.5rem;">Toplanan Məlumatlar</h2>
          <p style="color: #555; line-height: 1.8; margin-bottom: 15px; font-size: 1.05rem;">
            Sayt vasitəsilə aşağıdakı məlumatlar toplana bilər:
          </p>
          <ul style="color: #555; line-height: 1.8; margin-bottom: 30px; font-size: 1.05rem; padding-left: 20px;">
            <li>Ad və soyad</li>
            <li>Telefon nömrəsi</li>
            <li>E-poçt ünvanı</li>
            <li>Şagird qeydiyyat məlumatları</li>
            <li>Ödəniş məlumatları</li>
            <li>Saytdan istifadə statistikası</li>
          </ul>

          <h2 style="color: var(--navy); margin-bottom: 20px; font-weight: 800; font-size: 1.5rem;">Ödəniş Sistemi</h2>
          <p style="color: #555; line-height: 1.8; margin-bottom: 15px; font-size: 1.05rem;">
            Sayt üzərindən onlayn ödəniş xidməti təqdim oluna bilər. Ödəniş zamanı istifadəçilərin bank kartı məlumatları təhlükəsiz ödəniş sistemləri vasitəsilə emal edilir və Evrika Liseyi tərəfindən saxlanılmır.
          </p>
          <p style="color: #555; line-height: 1.8; margin-bottom: 30px; font-size: 1.05rem;">
            Bütün ödəniş əməliyyatları müasir təhlükəsizlik standartlarına uyğun qorunur.
          </p>

          <h2 style="color: var(--navy); margin-bottom: 20px; font-weight: 800; font-size: 1.5rem;">Məlumatların İstifadəsi</h2>
          <p style="color: #555; line-height: 1.8; margin-bottom: 15px; font-size: 1.05rem;">
            Toplanan məlumatlar aşağıdakı məqsədlərlə istifadə olunur:
          </p>
          <ul style="color: #555; line-height: 1.8; margin-bottom: 30px; font-size: 1.05rem; padding-left: 20px;">
            <li>Şagird qeydiyyatı və qəbul prosesi</li>
            <li>Təhsil xidmətlərinin təqdim edilməsi</li>
            <li>Ödənişlərin həyata keçirilməsi və təsdiqlənməsi</li>
            <li>İstifadəçi ilə əlaqə saxlanılması</li>
            <li>Saytın inkişaf etdirilməsi və təhlükəsizliyinin təmin edilməsi</li>
          </ul>

          <h2 style="color: var(--navy); margin-bottom: 20px; font-weight: 800; font-size: 1.5rem;">Məlumatların Qorunması</h2>
          <p style="color: #555; line-height: 1.8; margin-bottom: 30px; font-size: 1.05rem;">
            Evrika Liseyi şəxsi məlumatların təhlükəsizliyini təmin etmək üçün müasir texniki və təşkilati təhlükəsizlik tədbirlərindən istifadə edir.
          </p>

          <h2 style="color: var(--navy); margin-bottom: 20px; font-weight: 800; font-size: 1.5rem;">Üçüncü Tərəflərlə Paylaşım</h2>
          <p style="color: #555; line-height: 1.8; margin-bottom: 30px; font-size: 1.05rem;">
            İstifadəçi məlumatları yalnız qanunvericiliyin tələb etdiyi hallarda və ya ödəniş xidmətlərinin həyata keçirilməsi məqsədilə etibarlı tərəfdaşlarla paylaşılır.
          </p>

          <h2 style="color: var(--navy); margin-bottom: 20px; font-weight: 800; font-size: 1.5rem;">Cookies (Kuki Faylları)</h2>
          <p style="color: #555; line-height: 1.8; margin-bottom: 30px; font-size: 1.05rem;">
            Sayt istifadəçi təcrübəsini yaxşılaşdırmaq və statistika aparmaq məqsədilə cookies texnologiyasından istifadə edə bilər.
          </p>

          <h2 style="color: var(--navy); margin-bottom: 20px; font-weight: 800; font-size: 1.5rem;">İstifadəçi Hüquqları</h2>
          <p style="color: #555; line-height: 1.8; margin-bottom: 30px; font-size: 1.05rem;">
            İstifadəçilər öz şəxsi məlumatlarına baxmaq, onları yeniləmək və ya silinməsini tələb etmək hüququna malikdirlər.
          </p>

          <h2 style="color: var(--navy); margin-bottom: 20px; font-weight: 800; font-size: 1.5rem;">Əlaqə</h2>
          <p style="color: #555; line-height: 1.8; margin-bottom: 30px; font-size: 1.05rem;">
            Məxfilik siyasəti ilə bağlı hər hansı sualınız olduqda bizimlə əlaqə saxlaya bilərsiniz.
          </p>

        </div>
      </section>
    </main>"""

content = re.sub(r'<main>.*?</main>', main_content, content, flags=re.DOTALL)

with open('privacy.html', 'w', encoding='utf-8') as f:
    f.write(content)

