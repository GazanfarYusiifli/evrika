import re

with open('terms.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'<title>.*?</title>', '<title>İstifadə Şərtləri | Evrika Təhsil Ekosistemi</title>', content)

main_content = """    <main>
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
    </main>"""

content = re.sub(r'<main>.*?</main>', main_content, content, flags=re.DOTALL)

with open('terms.html', 'w', encoding='utf-8') as f:
    f.write(content)
