import fs from 'fs';

const montessoriPath = '/Users/gazanfaryusifli/Downloads/Evrika/montessori.html';
let content = fs.readFileSync(montessoriPath, 'utf8');

const newContent = `
  <style>
    .about-wrap { display:grid; grid-template-columns:1fr 1fr; gap:80px; align-items:center; }
    @media (max-width: 992px) { .about-wrap { grid-template-columns: 1fr; } }
    .img-placeholder { width:100%; height:500px; background:rgba(255,255,255,0.03); border:1px solid var(--border); border-radius:28px; display:flex; align-items:center; justify-content:center; }
    
    .bento-grid {
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      grid-template-rows: repeat(2, 400px);
      gap: 25px;
      margin-top: 80px;
    }
    .bento-item {
      position: relative;
      border-radius: 40px;
      overflow: hidden;
      background: #0a1128;
      border: 1px solid rgba(255,255,255,0.05);
      transition: all 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      cursor: pointer;
      transform-style: preserve-3d;
      perspective: 1000px;
    }
    .bento-1 { grid-column: span 3; grid-row: span 1; }
    .bento-2 { grid-column: span 3; grid-row: span 1; }
    .bento-3 { grid-column: span 2; grid-row: span 1; }
    .bento-4 { grid-column: span 2; grid-row: span 1; }
    .bento-5 { grid-column: span 2; grid-row: span 1; }

    .bento-item img { width: 100%; height: 100%; object-fit: cover; opacity: 0.85; filter: brightness(0.9); transition: all 0.8s ease; }
    .bento-item:hover img { opacity: 1; filter: brightness(1.1); transform: scale(1.1); }
    
    .bento-overlay {
      position: absolute; inset: 0;
      background: linear-gradient(to top, rgba(7, 13, 31, 0.95) 10%, transparent 70%);
      padding: 40px; display: flex; flex-direction: column; justify-content: flex-end; z-index: 2;
    }
    .bento-item:hover {
      transform: translateY(-10px) rotateX(2deg) rotateY(-2deg);
      border-color: var(--accent-light);
      box-shadow: 0 30px 60px rgba(0,0,0,0.6), 0 0 20px rgba(139, 26, 43, 0.3);
    }
    
    .bento-icon { font-size: 2.2rem; color: var(--accent-light); margin-bottom: 20px; transform: translateZ(30px); transition: 0.4s; }
    .bento-item:hover .bento-icon { transform: translateZ(50px) scale(1.2); color: #fff; }
    
    .bento-title { font-size: 1.6rem; font-weight: 900; color: #fff; margin-bottom: 15px; transform: translateZ(20px); }
    .bento-desc { font-size: 0.95rem; color: var(--text-muted); line-height: 1.6; opacity: 0.8; max-width: 90%; transform: translateZ(10px); }
    .bento-item:hover .bento-desc { opacity: 1; color: #fff; }

    @media (max-width: 1024px) {
      .bento-grid { grid-template-columns: 1fr; grid-template-rows: auto; }
      .bento-item { grid-column: span 1 !important; height: 350px; }
    }

    .section-red { 
      background: #8B1A2B; position: relative; overflow: hidden; 
      border-radius: 80px 80px 0 0; margin-top: -80px; z-index: 5;
    }
    .section-red::before {
      content: ""; position: absolute; inset: 0;
      background-image: radial-gradient(circle at 20% 30%, rgba(255,255,255,0.05) 0%, transparent 50%);
      pointer-events: none;
    }
    .levels-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-top: 50px; }
    .level-card {
      background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px);
      border: 1px solid rgba(255, 255, 255, 0.1); padding: 45px 35px;
      border-radius: 40px; transition: all 0.5s cubic-bezier(0.2, 0, 0.2, 1);
      cursor: pointer; text-align: left; display: flex; flex-direction: column; height: 100%;
    }
    .level-card:hover {
      background: rgba(255, 255, 255, 0.1); border-color: rgba(255, 255, 255, 0.3);
      transform: translateY(-15px) scale(1.03); box-shadow: 0 30px 60px rgba(0,0,0,0.3), 0 0 20px rgba(255,255,255,0.1);
    }
    .level-icon { font-size: 3rem; color: #fff; margin-bottom: 25px; transition: 0.4s; }
    .level-card:hover .level-icon { transform: scale(1.1) rotate(-5deg); filter: drop-shadow(0 0 10px rgba(255,255,255,0.5)); }
    .level-card h4 { font-size: 1.5rem; color: #fff; margin-bottom: 15px; font-weight: 900; }
    .level-card p { font-size: 0.95rem; color: rgba(255,255,255,0.7); line-height: 1.7; margin-bottom: 20px; transition: 0.3s; }
    .level-card:hover p { color: #fff; }

    @media (max-width: 1100px) { .levels-grid { grid-template-columns: repeat(2, 1fr) !important; } }
    @media (max-width: 600px) { .levels-grid { grid-template-columns: 1fr !important; } }

    .category-header { text-align: center; margin-bottom: 80px; }
    .category-title { font-size: 3rem; font-weight: 900; color: #fff; letter-spacing: -2px; text-transform: uppercase; }
    .category-title em { color: var(--accent-light); font-style: normal; }

    .clubs-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 25px; }
    .club-card {
      background: #8B1A2B; border: 1px solid rgba(255, 255, 255, 0.1);
      padding: 50px 30px; border-radius: 40px; transition: all 0.6s cubic-bezier(0.16, 1, 0.3, 1);
      text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.2); cursor: pointer;
    }
    .club-card:hover { background: #a31e32; transform: translateY(-15px) scale(1.02); box-shadow: 0 40px 80px rgba(0,0,0,0.4); }
    .club-icon { font-size: 2.5rem; color: #fff; margin-bottom: 25px; display: block; transition: 0.4s; }
    .club-card:hover .club-icon { transform: scale(1.2); }
    .club-name { font-size: 0.85rem; font-weight: 900; color: #fff; letter-spacing: 3px; text-transform: uppercase; }
  </style>

  <!-- ── HERO ── -->
  <section class="hero">
    <div class="hero-bg" style="background-image: url('https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&q=80&w=1600')"></div>
    <div class="hero-mesh"></div>
    <div class="hero-grid"></div>
    <div class="hero-inner">
      <div class="hero-content reveal-left">
        <div class="hero-tag"><i class="fas fa-child"></i> EVRİKA MONTESSORİ UŞAQ AKADEMİYASI</div>
        <h1 class="hero-h1" style="font-size: 3.5rem;">Sevgi ilə başlayan inkişaf,<br><span class="accent">gələcəyin təməlidir</span></h1>
        <p class="hero-p">1–6 yaş uşaqlar üçün Montessori əsaslı, beynəlxalq yanaşma ilə qurulmuş erkən inkişaf mühiti.</p>
        <div class="hero-btns">
          <a href="#about" class="btn-primary">Haqqımızda <i class="fas fa-arrow-right"></i></a>
          <a href="register-montessori.html" class="btn-glass">Qeydiyyatdan keç</a>
        </div>
      </div>
    </div>
    <svg style="position:absolute; bottom:0; left:0; width:100%; height:80px; fill:var(--navy); z-index:10;" viewBox="0 0 1440 320">
      <path d="M0,192L48,197.3C96,203,192,213,288,192C384,171,480,117,576,112C672,107,768,149,864,154.7C960,160,1056,128,1152,112C1248,96,1344,96,1392,96L1440,96L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path>
    </svg>
  </section>

  <!-- ── ERKƏN İNKİŞAF ── -->
  <section id="about" class="section">
    <div class="container">
      <div class="about-wrap">
        <div class="about-text-side reveal-left">
          <div class="sec-eyebrow">Erkən inkişaf</div>
          <h2 class="sec-h2">Uşağın həyatının ilk 6 ili onun <em>gələcək inkişafının</em> əsasını təşkil edir.</h2>
          <p class="sec-lead">Dil, düşüncə və sosial bacarıqlar bu dövrdə formalaşır.</p>
          <p style="color:var(--text-muted); line-height:1.8;">Evrika-da bu mərhələ şüurlu inkişaf kimi qurulur. Valideyn inkişaf prosesinin fəal bir hissəsidir.</p>
        </div>
        <div class="about-img-side reveal-right" style="position:relative;">
          <div class="img-placeholder" style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(10px); border-radius:30px; overflow:hidden;">
             <img src="https://images.unsplash.com/photo-1587691592099-24045742c181?auto=format&fit=crop&q=80&w=800" style="width: 100%; height: 100%; object-fit: cover;" alt="Montessori Inkişafı">
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ── MONTESSORI YANAŞMASI & BÖLMƏLƏR ── -->
  <section class="section" style="background: var(--navy-mid);">
    <div class="container">
      <div class="sec-header reveal-left">
        <h2 class="sec-h2" style="color: #fff;">Montessori <em style="color: var(--accent-light); font-style: normal;">Yanaşması</em></h2>
        <p class="sec-p reveal-right" style="color: rgba(255,255,255,0.8);">Müstəqil düşünmə, fokus, seçim etmə və sosial inkişaf Montessori metodunun əsasını təşkil edir. Uşaqlar kəşf edərək öyrənir.</p>
      </div>

      <div class="bento-grid">
        <div class="bento-item bento-1 reveal">
          <img src="https://images.unsplash.com/photo-1514090458221-65bb69cf63e6?auto=format&fit=crop&q=80&w=800" alt="Bölmələr">
          <div class="bento-overlay">
            <i class="fas fa-globe-europe bento-icon"></i>
            <h3 class="bento-title">Çoxdilli Tədris Bölmələri</h3>
            <p class="bento-desc">Azərbaycan, Rus, İngilis və Türk bölmələri üzrə tədris.</p>
          </div>
        </div>
        
        <div class="bento-item bento-2 reveal" style="transition-delay: 0.1s;">
          <img src="https://images.unsplash.com/photo-1588072432836-e10032774350?auto=format&fit=crop&q=80&w=800" alt="Təhsil Proqramı">
          <div class="bento-overlay">
            <i class="fas fa-book-reader bento-icon"></i>
            <h3 class="bento-title">Təhsil Proqramı</h3>
            <p class="bento-desc">Montessori metodu, Cambridge proqramına giriş, art dərsləri və interaktiv fəaliyyətlər.</p>
          </div>
        </div>

        <div class="bento-item bento-3 reveal" style="transition-delay: 0.2s;">
          <div class="bento-overlay" style="background: linear-gradient(135deg, rgba(139,26,43,0.9), rgba(7,13,31,0.9));">
            <i class="fas fa-brain bento-icon"></i>
            <h3 class="bento-title">İnkişaf Sahələri</h3>
            <p class="bento-desc">Praktiki həyat, sensor inkişaf, dil, riyazi düşüncə və ətraf mühit.</p>
          </div>
        </div>

        <div class="bento-item bento-4 reveal" style="transition-delay: 0.3s;">
          <img src="https://images.unsplash.com/photo-1574706597711-2eb9a2bb7f7f?auto=format&fit=crop&q=80&w=800" alt="Qidalanma">
          <div class="bento-overlay">
            <i class="fas fa-apple-alt bento-icon"></i>
            <h3 class="bento-title">Qidalanma</h3>
            <p class="bento-desc">Gündəlik 5 dəfə sağlam və balanslı qidalanma.</p>
          </div>
        </div>

        <div class="bento-item bento-5 reveal" style="transition-delay: 0.4s;">
          <div class="bento-overlay" style="background: linear-gradient(135deg, rgba(76,96,171,0.9), rgba(7,13,31,0.9));">
            <i class="fas fa-shield-alt bento-icon"></i>
            <h3 class="bento-title">Mühit</h3>
            <p class="bento-desc">Təhlükəsiz, rahat və tam uşaq mərkəzli mühit.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ── YAŞ QRUPLARI ── -->
  <section class="section section-red">
    <div class="container">
      <div class="sec-header reveal-left">
        <h2 class="sec-h2" style="color: #fff;">Yaş <em style="color: #1a2b5a; font-style: normal;">Qrupları</em></h2>
      </div>

      <div class="levels-grid" style="grid-template-columns: repeat(2, 1fr);">
        <div class="level-card reveal">
          <i class="fas fa-baby level-icon"></i>
          <h4>Toddler (1–3 yaş)</h4>
          <p>Erkən inkişaf mərhələsi. Özünəxidmət bacarıqlarının, hərəkət koordinasiyasının və ilkin nitqin formalaşdırılması.</p>
        </div>

        <div class="level-card reveal" style="transition-delay: 0.1s;">
          <i class="fas fa-child level-icon"></i>
          <h4>Primary (3–6 yaş)</h4>
          <p>Məktəbə hazırlıq mərhələsi. Qrup şəklində işləmək, ilkin riyazi düşüncə, dil bacarıqları və ətraf aləmin fəal kəşfi.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ── DƏRNƏKLƏR ── -->
  <section class="section stack-wrapper" style="background: #070d1f; padding: 120px 0;">
    <div class="container">
      <div class="category-header reveal">
        <h2 class="category-title">Aktiv <em>Dərnəklər</em></h2>
      </div>
      <div class="clubs-grid">
        <div class="club-card reveal"><i class="fas fa-running club-icon"></i><h4 class="club-name">Gimnastika</h4></div>
        <div class="club-card reveal" style="transition-delay: 0.1s;"><i class="fas fa-swimmer club-icon"></i><h4 class="club-name">Üzgüçülük</h4></div>
        <div class="club-card reveal" style="transition-delay: 0.2s;"><i class="fas fa-futbol club-icon"></i><h4 class="club-name">Futbol</h4></div>
        <div class="club-card reveal" style="transition-delay: 0.3s;"><i class="fas fa-music club-icon"></i><h4 class="club-name">Piano</h4></div>
        <div class="club-card reveal" style="transition-delay: 0.4s;"><i class="fas fa-chess-knight club-icon"></i><h4 class="club-name">Şahmat</h4></div>
      </div>
    </div>
  </section>

  <!-- ── CTA ── -->
  <section class="section" style="background: linear-gradient(135deg, rgba(139,26,43,0.05), transparent);">
    <div class="container" style="text-align: center; max-width: 800px;">
      <h2 class="sec-h2" style="margin-bottom: 25px;">Övladınız üçün doğru başlanğıcı seçin.</h2>
      <p style="font-size: 1.2rem; color: var(--text-muted); margin-bottom: 40px;">
        <i class="fas fa-map-marker-alt" style="color: var(--accent); margin-right: 8px;"></i> Nərimanov, Qafur Rəşad 16 (Zümrüd Residence) <br>
        <i class="fas fa-phone-alt" style="color: var(--accent); margin-right: 8px; margin-top: 15px;"></i> 010 300 50 50
      </p>
      <a href="register-montessori.html" class="btn-primary" style="font-size: 1.2rem; padding: 18px 50px;">Qeydiyyatdan keçin <i class="fas fa-arrow-right"></i></a>
    </div>
  </section>
`;

const startIndex = content.indexOf('<section class="hero">');
const endIndex = content.indexOf('<footer class="site-footer"');

if (startIndex !== -1 && endIndex !== -1) {
  content = content.substring(0, startIndex) + newContent + '\n\n    ' + content.substring(endIndex);
  fs.writeFileSync(montessoriPath, content, 'utf8');
  console.log('Successfully updated montessori.html');
} else {
  console.log('Could not find boundaries');
}
