import re

with open("/Users/gazanfaryusifli/Downloads/Evrika/jurnal.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace everything from <main> to </main>
new_main = """    <main>
      <style>
        .jurnal-hero {
          padding: 240px 0 140px;
          text-align: center;
          position: relative;
          overflow: hidden;
          background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
          color: white;
        }
        .jurnal-hero::before {
          content: ''; position: absolute; top: -50%; left: -20%; width: 100%; height: 100%;
          background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 60%);
          filter: blur(80px);
        }
        .magazine-grid {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
          gap: 40px;
          margin-top: 60px;
        }
        .magazine-card {
          background: white;
          border-radius: 24px;
          overflow: hidden;
          box-shadow: 0 15px 40px rgba(0,0,0,0.08);
          transition: 0.4s;
          border: 1px solid rgba(0,0,0,0.05);
        }
        .magazine-card:hover {
          transform: translateY(-10px);
          box-shadow: 0 30px 60px rgba(30,58,138,0.15);
        }
        .magazine-cover {
          height: 380px;
          background: #f4f5f8;
          display: flex;
          align-items: center;
          justify-content: center;
          position: relative;
          overflow: hidden;
        }
        .magazine-cover i {
          font-size: 5rem;
          color: #1e3a8a;
          opacity: 0.2;
        }
        .magazine-info {
          padding: 30px;
          text-align: left;
        }
        .magazine-date {
          color: #3b82f6;
          font-weight: 700;
          font-size: 0.9rem;
          text-transform: uppercase;
          letter-spacing: 0.1em;
          margin-bottom: 10px;
        }
        .magazine-title {
          font-size: 1.5rem;
          color: #1e3a8a;
          font-weight: 800;
          margin-bottom: 15px;
          line-height: 1.3;
        }
        .magazine-desc {
          color: #666;
          line-height: 1.6;
          margin-bottom: 25px;
        }
        .magazine-btn {
          display: inline-flex;
          align-items: center;
          gap: 10px;
          padding: 12px 25px;
          background: rgba(30,58,138,0.1);
          color: #1e3a8a;
          font-weight: 700;
          border-radius: 50px;
          text-decoration: none;
          transition: 0.3s;
        }
        .magazine-card:hover .magazine-btn {
          background: #1e3a8a;
          color: white;
        }
      </style>

      <section class="jurnal-hero">
        <div class="container" style="position: relative; z-index: 10;">
          <div class="brand-eyebrow modern-glow" style="margin-bottom: 24px; color: rgba(255,255,255,0.8); letter-spacing: 0.6em; text-transform: uppercase; font-weight: 800; font-size: 0.8rem;">AYLIQ NƏŞR</div>
          <h1 class="titan-header reveal" style="font-size: 5rem; line-height: 1.1; margin-bottom: 30px;">
            Evrika <span style="color: #93c5fd;">Məktəbli Jurnalı</span>
          </h1>
          <div style="width: 80px; height: 3px; background: #93c5fd; margin: 20px auto 40px;"></div>
          <p class="reveal" style="max-width: 800px; margin: 0 auto; font-size: 1.25rem; color: rgba(255,255,255,0.9); line-height: 1.8; font-weight: 400; transition-delay: 0.2s;">
            Şagirdlərimizin uğurları, təhsil yenilikləri, yaradıcılıq işləri və lisey həyatından ən maraqlı məqamlar bir yerdə.
          </p>
        </div>
      </section>

      <section class="section" style="padding: 100px 0; background: #f9f9fc;">
        <div class="container">
          <div style="text-align: center; margin-bottom: 50px;" class="reveal">
            <h2 class="titan-header" style="font-size: 3rem; color: #1e3a8a!important; -webkit-text-fill-color: #1e3a8a!important;">Sonuncu <span style="color: #3b82f6!important; -webkit-text-fill-color: #3b82f6!important;">Nəşrlər</span></h2>
          </div>

          <div class="magazine-grid">
            <!-- Issue 1 -->
            <div class="magazine-card reveal">
              <div class="magazine-cover">
                <i class="fas fa-book-open"></i>
              </div>
              <div class="magazine-info">
                <div class="magazine-date">Noyabr 2026</div>
                <h3 class="magazine-title">Elm və Texnologiya Festivalı xüsusi buraxılışı</h3>
                <p class="magazine-desc">Liseyimizdə keçirilən ənənəvi elm festivalının ən yaddaqalan anları, şagirdlərin layihələri və müsahibələr.</p>
                <a href="#" class="magazine-btn">Oxumağa başla <i class="fas fa-arrow-right"></i></a>
              </div>
            </div>

            <!-- Issue 2 -->
            <div class="magazine-card reveal" style="transition-delay: 0.1s;">
              <div class="magazine-cover">
                <i class="fas fa-book-open"></i>
              </div>
              <div class="magazine-info">
                <div class="magazine-date">Oktyabr 2026</div>
                <h3 class="magazine-title">Beynəlxalq Olimpiada Qaliblərimiz</h3>
                <p class="magazine-desc">Riyaziyyat və fizika olimpiadalarında fərqlənən Evrikalılar: Uğur sirləri və gələcək hədəflər.</p>
                <a href="#" class="magazine-btn">Oxumağa başla <i class="fas fa-arrow-right"></i></a>
              </div>
            </div>

            <!-- Issue 3 -->
            <div class="magazine-card reveal" style="transition-delay: 0.2s;">
              <div class="magazine-cover">
                <i class="fas fa-book-open"></i>
              </div>
              <div class="magazine-info">
                <div class="magazine-date">Sentyabr 2026</div>
                <h3 class="magazine-title">Yeni Tədris İlinə Uğurlu Başlanğıc</h3>
                <p class="magazine-desc">İlk zəng, yeni qəbul olan şagirdlərimiz və ilin akademik hədəfləri haqqında geniş məlumat.</p>
                <a href="#" class="magazine-btn">Oxumağa başla <i class="fas fa-arrow-right"></i></a>
              </div>
            </div>
          </div>
          
          <div style="text-align: center; margin-top: 60px;" class="reveal">
            <a href="#" class="btn" style="background: #1e3a8a; color: white; border-radius: 50px; padding: 15px 40px; font-weight: 800;">Bütün Arxiv <i class="fas fa-archive" style="margin-left: 10px;"></i></a>
          </div>

        </div>
      </section>
    </main>"""

content = re.sub(r'<main>.*?</main>', new_main, content, flags=re.DOTALL)

with open("/Users/gazanfaryusifli/Downloads/Evrika/jurnal.html", "w", encoding="utf-8") as f:
    f.write(content)

print("jurnal.html content replaced.")
