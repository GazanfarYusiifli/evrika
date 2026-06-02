import re

with open('contact.html', 'r', encoding='utf-8') as f:
    base_content = f.read()

# For Privacy
privacy_content = base_content
privacy_content = re.sub(r'<title>.*?</title>', '<title>Məxfilik Siyasəti | Evrika Təhsil Ekosistemi</title>', privacy_content)

main_privacy = """
    <main>
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
    </main>
"""

# Replace everything from <!-- Contact Hero --> to <!-- Footer -->
privacy_content = re.sub(r'<!-- Contact Hero -->.*?<!-- Footer -->', main_privacy + '\n<!-- Footer -->', privacy_content, flags=re.DOTALL)

with open('privacy.html', 'w', encoding='utf-8') as f:
    f.write(privacy_content)

# For Terms
terms_content = base_content
terms_content = re.sub(r'<title>.*?</title>', '<title>İstifadə Şərtləri | Evrika Təhsil Ekosistemi</title>', terms_content)

main_terms = """
    <main>
      <section class="section" style="padding: 240px 0 100px; text-align:center; position:relative; overflow:hidden; background: #070d1f;">
        <div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 0%,rgba(76,96,171,0.3)0%,transparent 70%);pointer-events:none;"></div>
        <div class="container" style="position:relative;z-index:10;">
          <h1 class="titan-header" style="font-size:4rem;color:var(--white);margin-bottom:20px;font-weight:900;">İstifadə <span style="color:var(--burgundy);">Şərtləri</span></h1>
          <p style="color:rgba(255,255,255,0.7);font-size:1.2rem;max-width:600px;margin:0 auto;">Son yenilənmə: May 2026</p>
        </div>
      </section>

      <section class="section" style="padding: 80px 0; background: #f8f9fa;">
        <div class="container" style="max-width: 900px; background: white; padding: 60px; border-radius: 30px; box-shadow: 0 20px 40px rgba(0,0,0,0.05);">
          
          <h2 style="color: var(--navy); margin-bottom: 20px; font-weight: 800;">1. Şərtlərin Qəbulu</h2>
          <p style="color: #555; line-height: 1.8; margin-bottom: 30px; font-size: 1.05rem;">
            Evrika Təhsil Ekosisteminin veb saytına (bundan sonra "Sayt") daxil olmaqla, bu İstifadə Şərtləri, bütün qüvvədə olan qanunlar və qaydalarla razılaşdığınızı bəyan edirsiniz. Şərtlərlə razılaşmırsınızsa, saytdan istifadəni dərhal dayandırmalısınız.
          </p>

          <h2 style="color: var(--navy); margin-bottom: 20px; font-weight: 800;">2. Əqli Mülkiyyət</h2>
          <p style="color: #555; line-height: 1.8; margin-bottom: 30px; font-size: 1.05rem;">
            Saytda olan bütün məzmun, o cümlədən dizayn, mətn, qrafika, loqotiplər, videolar və proqram təminatı Evrika Təhsil Ekosisteminə məxsusdur və müəllif hüquqları qanunları ilə qorunur. Məzmunun hər hansı icazəsiz istifadəsi qanunla qadağandır.
          </p>

          <h2 style="color: var(--navy); margin-bottom: 20px; font-weight: 800;">3. İstifadədə Məhdudiyyətlər</h2>
          <p style="color: #555; line-height: 1.8; margin-bottom: 30px; font-size: 1.05rem;">
            Saytdan kommersiya məqsədləri ilə icazəsiz istifadə edə, materialları köçürə, dəyişdirə və ya yaya bilməzsiniz. Saytın işinə zərər verə biləcək zərərli proqram kodlarının (viruslar və s.) yerləşdirilməsi qəti qadağandır.
          </p>

          <h2 style="color: var(--navy); margin-bottom: 20px; font-weight: 800;">4. Məsuliyyətin Rəddi</h2>
          <p style="color: #555; line-height: 1.8; margin-bottom: 30px; font-size: 1.05rem;">
            Saytda təqdim olunan materiallar "olduğu kimi" təmin edilir. Evrika məlumatların daimi düzgünlüyünə zəmanət vermir və saytdan istifadədən yaranan birbaşa və ya dolayısı zərərlərə görə məsuliyyət daşımır.
          </p>

        </div>
      </section>
    </main>
"""

terms_content = re.sub(r'<!-- Contact Hero -->.*?<!-- Footer -->', main_terms + '\n<!-- Footer -->', terms_content, flags=re.DOTALL)

with open('terms.html', 'w', encoding='utf-8') as f:
    f.write(terms_content)

