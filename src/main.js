import './style.css';

// --- System Core ---
const DOM = {
  navbar: document.querySelector('.navbar'),
  reveal: document.querySelectorAll('.reveal'),
  counters: document.querySelectorAll('.achievement-number'),
  cards: document.querySelectorAll('.modern-card'),
  modal: document.getElementById('school-modal'),
  modalBody: document.getElementById('modal-body'),
  closeModal: document.querySelector('.close-modal'),
  form: document.getElementById('crm-form'),
  quotes: document.querySelectorAll('.quote-item'),
};

// --- Modern Scroll Reveal ---
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -50px 0px'
};

const revealOnScroll = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      revealOnScroll.unobserve(entry.target);
    }
  });
}, observerOptions);

DOM.reveal.forEach(el => revealOnScroll.observe(el));

// --- Dynamic Counter Logic ---
const animateValue = (obj, start, end, duration) => {
  let startTimestamp = null;
  const step = (timestamp) => {
    if (!startTimestamp) startTimestamp = timestamp;
    const progress = Math.min((timestamp - startTimestamp) / duration, 1);
    const value = Math.floor(progress * (end - start) + start);
    obj.innerHTML = value.toLocaleString();
    if (progress < 1) {
      window.requestAnimationFrame(step);
    }
  };
  window.requestAnimationFrame(step);
};

const counterObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting && !entry.target.classList.contains('active')) {
      const target = parseInt(entry.target.getAttribute('data-target'));
      animateValue(entry.target, 0, target, 2000);
      entry.target.classList.add('active');
    }
  });
}, { threshold: 0.1 });

DOM.counters.forEach(c => counterObserver.observe(c));


// --- School Ecosystem Data ---
const schools = {
  1: {
    badge: "Akademik Mərkəz",
    name: "Evrika Liseyi",
    desc: "Yerli kurikulumun ən yüksək standartları ilə tədris aparan liseyimiz, şagirdləri beynəlxalq və dövlət imtahanlarına (DİM) peşəkar səviyyədə hazırlayır. Burada akademik dəqiqlik innovativ laboratoriyalarla birləşir.",
    points: [
      "Təkmilləşdirilmiş Elm və Riyaziyyat",
      "Olimpiada Mərkəzi Hazırlığı",
      "Müasir STEM Laboratoriyaları"
    ],
    img: "https://files.cdn-files-a.com/uploads/10086696/2000_695e52c388a8e.jpg",
    cta: "Qəbul Üçün Müraciət Et"
  },
  3: {
    badge: "Erkən İnkişaf",
    name: "Evrika Montessori Kids Academy",
    desc: "Uşaqların fərdi bacarıqlarını kəşf etmək üçün Montessori metodikası və müasir pedaqogikanın vəhdəti. Biz şagirdlərimizə müstəqil öyrənmə və tənqidi təfəkkür aşılayırıq.",
    points: [
      "Fərdi Montessori Metodikası",
      "Yaradıcı İncəsənət və Musiqi",
      "Xarici Dil Mühiti"
    ],
    img: "https://files.cdn-files-a.com/uploads/10086696/2000_695d46cadbf37.png",
    cta: "Akademiya ilə Əlaqə"
  },
  4: {
    badge: "Akademik Dəstək",
    name: "Eduhome Hazırlıq Mərkəzi",
    desc: "Xaricdə təhsil və beynəlxalq sertifikatlar üzrə ixtisaslaşmış mərkəzimiz şagirdlərə qlobal təhsil qapılarını açır. SAT, IELTS və Duolingo hazırlığı peşəkar mentorlarla aparılır.",
    points: [
      "SAT və IELTS Hazırlığı",
      "Beynəlxalq Universitet Qəbulu",
      "Karyera Planlama və Konsaltinq"
    ],
    img: "https://files.cdn-files-a.com/uploads/10086696/2000_6970fa193770e.png",
    cta: "Konsultasiya Rezerv Et"
  },
  5: {
    badge: "Peşəkar İdman",
    name: "Zümrüd İdman Mərkəzi",
    desc: "Şagirdlərin fiziki sağlamlığı və nizam-intizamı üçün nəzərdə tutulmuş müasir kompleks. Burada gələcəyin çempionları həm fərdi, həm də komanda idman növlərində formalaşırlar.",
    points: [
      "Üzgüçülük və Gimnastika",
      "Komanda İdman Növləri",
      "Peşəkar Məşqçi Heyəti"
    ],
    img: "https://images.unsplash.com/photo-1571902943202-507ec2618e8f?auto=format&fit=crop&q=80&w=1200",
    cta: "Məşqə Qatıl"
  }
};

const openModal = (id) => {
  const data = schools[id];
  if (!data) return;

  DOM.modalBody.innerHTML = `
    <div class="modal-hero">
      <img src="${data.img}" alt="${data.name}">
      <div class="modal-badge">${data.badge}</div>
    </div>
    <div class="modal-info">
      <h2 style="color: var(--navy); font-size: 2.5rem; font-weight: 900; margin-bottom: 20px; line-height: 1.1;">${data.name}</h2>
      <p style="font-size: 1.2rem; color: var(--text-dark); line-height: 1.8; margin-bottom: 30px;">${data.desc}</p>
      
      <div class="feature-bullets" style="margin-bottom: 40px;">
        ${data.points.map(p => `
          <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px; padding: 15px 25px; background: rgba(76, 96, 171,0.03); border-radius: 15px; border-left: 5px solid var(--burgundy);">
            <i class="fas fa-check-circle" style="color: var(--burgundy);"></i>
            <span style="font-weight: 700; color: var(--navy); font-size: 1.05rem;">${p}</span>
          </div>
        `).join('')}
      </div>

      <div style="display: flex; gap: 20px;">
        <a href="register-${id === '1' ? 'lisey1' : id === '3' ? 'montessori' : id === '4' ? 'eduhome' : id === '5' ? 'zumrud' : 'lisey1'}.html" class="btn btn-primary" style="flex: 2; justify-content: center;">${data.cta}</a>
        <button class="btn btn-outline" style="flex: 1; justify-content: center;" onclick="document.getElementById('school-modal').classList.remove('active'); setTimeout(() => document.getElementById('school-modal').style.display = 'none', 400);">Bağla</button>
      </div>
    </div>
  `;
  
  DOM.modal.style.display = 'flex';
  setTimeout(() => DOM.modal.classList.add('active'), 10);
};


// --- Strategic Feature Data ---
const featureData = {
  math: {
    title: "Riyaziyyat və Elm Strategiyası",
    desc: "Evrika təhsil modelinin özəyini STEM mühiti və sistemli riyazi yanaşma təşkil edir. Şagirdlərimiz mühəndis düşüncə tərzi ilə gələcəyin texnoloji dünyasına hazırlanırlar.",
    points: ["Müasir Fizika-Riyaziyyat proqramı", "Kodlaşdırma və Robototexnika laboratoriyaları", "Data Analitika və Məntiq mərkəzi"],
    img: "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?auto=format&fit=crop&q=80&w=1200"
  },
  olympiad: {
    title: "Olimpiada Hazırlıq Mərkəzi",
    desc: "Bizim proqram şagirdlərin intellektual sərhədlərini aşmaq üçün nəzərdə tutulub. Yerli və Beynəlxalq fənn olimpiadalarında illərlə formalaşmış uğur ənənəmizi davam etdiririk.",
    points: ["Beynəlxalq dərəcəli mentor heyəti", "Fərdi inkişaf akademik trekləri", "Xarici universitetlərə imtiyazlı qəbul"],
    img: "https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&q=80&w=1200"
  },
  scholarship: {
    title: "Təqaüd və Qəbul Fürsətləri",
    desc: "Parlaq zəka sahiblərinə dəstək olmaq bizim missiyamızdır. Evrika Daxili Təqaüd proqramı sayəsində onlarla istedadlı gənc hər il ödənişsiz təhsil imkanı qazanır.",
    points: ["Akademik nailiyyət təqaüdləri", "Sosial aktivlik və Liderlik bonusları", "Asanlaşdırılmış qəbul proseduru"],
    img: "https://images.unsplash.com/photo-1517486808906-6ca8b3f04846?auto=format&fit=crop&q=80&w=1200"
  },
  extended: {
    title: "Uzadılmış Gün və Fərdi İnkişaf",
    desc: "Təhsil sadəcə dərslə məhdudlaşmır. Biz şagirdlərimizin asudə vaxtını peşəkar mentorların nəzarəti altında, həm öyrənərək, həm də əylənərək keçirməsini təmin edirik.",
    points: ["Ev tapşırıqlarının mentorla icrası", "Yaradıcılıq və Digital Art dərnəkləri", "İngilis dili danışıq klubları"],
    img: "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?auto=format&fit=crop&q=80&w=1200"
  }
};

const openFeatureModal = (featureId) => {
  const data = featureData[featureId];
  if (!data) return;

  DOM.modalBody.innerHTML = `
    <div class="modal-hero">
      <img src="${data.img}" alt="${data.title}">
    </div>
    <div class="modal-info">
      <h2 style="margin-bottom: 20px; color: var(--navy); font-size: 2.2rem;">${data.title}</h2>
      <p style="font-size: 1.15rem; color: var(--text-dark); line-height: 1.8; margin-bottom: 30px;">${data.desc}</p>
      <div class="feature-bullets" style="margin-bottom: 40px;">
        ${data.points.map(p => `
          <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 12px; padding: 12px 20px; background: rgba(76, 96, 171,0.03); border-radius: 12px; border-left: 4px solid var(--burgundy);">
            <i class="fas fa-check-circle" style="color: var(--burgundy);"></i>
            <span style="font-weight: 600; color: var(--navy);">${p}</span>
          </div>
        `).join('')}
      </div>
      <div style="display: flex; gap: 16px;">
        <button class="btn btn-primary" style="flex: 1;" onclick="document.getElementById('school-modal').classList.remove('active'); setTimeout(() => document.getElementById('school-modal').style.display = 'none', 400);">Daha ətraflı sorğu</button>
      </div>
    </div>
  `;
  DOM.modal.style.display = 'flex';
  setTimeout(() => DOM.modal.classList.add('active'), 10);
};

// Institutional Card Expansion Logic (Mobile Support)
document.querySelectorAll('.exp-card').forEach(card => {
  card.addEventListener('click', (e) => {
    if (e.target.closest('.expanded-info')) return;
    if (window.innerWidth <= 1024) {
      const isActive = card.classList.contains('touch-active');
      document.querySelectorAll('.exp-card').forEach(c => c.classList.remove('touch-active'));
      if (!isActive) card.classList.add('touch-active');
      e.preventDefault();
    }
  });
});

// Open Modals for Strategic Features
document.querySelectorAll('.square-card').forEach(card => {
  const btn = card.querySelector('.feature-more-link');
  if (btn) {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      openFeatureModal(card.dataset.feature);
    });
  }
});

if (DOM.closeModal && DOM.modal) {
  DOM.closeModal.addEventListener('click', () => {
    DOM.modal.classList.remove('active');
    setTimeout(() => DOM.modal.style.display = 'none', 400);
  });
}

// Close modal on escape
window.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && DOM.modal && DOM.modal.classList.contains('active')) {
    DOM.modal.classList.remove('active');
    setTimeout(() => DOM.modal.style.display = 'none', 400);
  }
});

// --- UI Logic ---
if (DOM.navbar) {
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      DOM.navbar.classList.add('scrolled');
      DOM.navbar.classList.remove('navbar-inverse');
    } else {
      DOM.navbar.classList.remove('scrolled');
      if (document.querySelector('.hero-video-slider')) {
        DOM.navbar.classList.add('navbar-inverse');
      }
    }
  });
}

// Quote Slider
let currentIdx = 0;
if (DOM.quotes && DOM.quotes.length > 0) {
  setInterval(() => {
    DOM.quotes[currentIdx].classList.remove('active');
    currentIdx = (currentIdx + 1) % DOM.quotes.length;
    DOM.quotes[currentIdx].classList.add('active');
  }, 8000);
}

// --- Global Form Validation & Security ---
const setupFormValidation = () => {
  const forms = document.querySelectorAll('form');
  forms.forEach(form => {
    form.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' && e.target.tagName !== 'TEXTAREA') {
        e.preventDefault();
      }
    });

    form.querySelectorAll('input').forEach(input => {
      const name = input.name.toLowerCase();
      const type = input.type.toLowerCase();
      
      if (type === 'tel' || name.includes('phone') || name.includes('nömrə') || name.includes('mobil')) {
        input.addEventListener('input', (e) => {
          e.target.value = e.target.value.replace(/[^0-9+]/g, '');
        });
      }
      
      if (name.includes('name') || name.includes('adı') || name.includes('soyad')) {
        input.addEventListener('input', (e) => {
          e.target.value = e.target.value.replace(/[0-9]/g, '');
        });
      }
    });
  });
};

// --- Form Validation Init removed from here, consolidated below ---

const validateEmail = (email) => {
  return String(email).toLowerCase().match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/);
};

// --- Unified Production-Grade Supabase Submission ---
window.submitToSupabase = async (formData, btn, originalText) => {
  const SUBG_ID = 'miwvdhwrmxoetszkxlzy';
  const API_KEY = 'sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV';
  const STORAGE_URL = `https://${SUBG_ID}.supabase.co/storage/v1/object/ems-documents`;
  const DB_URL = `https://${SUBG_ID}.supabase.co/rest/v1/registrations`;

  const crmForm = {};
  const fileUploadTasks = [];

  for(let [key, val] of formData.entries()) { 
    if (val instanceof File && val.name && val.size > 0) {
      const fileExt = val.name.split('.').pop();
      const fileName = `${Date.now()}_${Math.random().toString(36).substring(7)}.${fileExt}`;
      const filePath = `registration_docs/${fileName}`;
      
      fileUploadTasks.push(async () => {
        const res = await fetch(`${STORAGE_URL}/${filePath}`, {
          method: 'POST',
          headers: {
            'apikey': API_KEY,
            'Authorization': `Bearer ${API_KEY}`,
            'x-upsert': 'true'
          },
          body: val
        });
        if(res.ok) {
           crmForm[key] = `https://${SUBG_ID}.supabase.co/storage/v1/object/public/ems-documents/${filePath}`;
        }
      });
    } else {
      crmForm[key] = val;
      if (key.toLowerCase().includes('email') && val.trim() !== "" && !validateEmail(val)) {
         alert('Zəhmət olmasa düzgün email ünvanı daxil edin');
         btn.disabled = false; btn.innerHTML = originalText;
         return false;
      }
    }
  }

  await Promise.all(fileUploadTasks.map(task => task()));
  crmForm['submissionDate'] = new Date().toISOString();
  crmForm['status'] = 'Yeni';
  
  // Default payment status
  if (window.location.pathname.includes('register-lisey') || window.location.pathname.includes('register-ptim')) {
      crmForm['payment_status'] = 'Ödənilməyib';
  }

  try {
    const res = await fetch(DB_URL, {
      method: 'POST',
      headers: {
        'apikey': API_KEY,
        'Authorization': `Bearer ${API_KEY}`,
        'Content-Type': 'application/json',
        'Prefer': 'return=representation'
      },
      body: JSON.stringify({ payload: crmForm })
    });
    
    if(res.ok) {
      btn.innerHTML = '<i class="fas fa-check"></i> Uğurla Göndərildi!';
      btn.style.background = '#10B981';
      
      const responseData = await res.json();
      const insertedRow = responseData[0];

      if (window.location.pathname.includes('register-lisey')) {
          // Trigger simulated payment flow
          setTimeout(() => {
              btn.innerHTML = originalText; btn.style.background = ''; btn.disabled = false;
              if (window.showPaymentModal) {
                  window.showPaymentModal(crmForm, insertedRow.id);
              }
          }, 1000);
          return true;
      }

      setTimeout(() => {
        btn.innerHTML = originalText; btn.style.background = ''; btn.disabled = false;
        if (window.location.pathname.includes('register-')) {
           window.location.href = 'index.html?success=true';
        }
      }, 2000);
      return true;
    } else { throw new Error(); }
  } catch (err) {
    btn.innerHTML = '<i class="fas fa-exclamation-triangle"></i> Xəta Baş Verdi';
    setTimeout(() => { btn.innerHTML = originalText; btn.disabled = false; }, 3000);
    return false;
  }
};

window.showPaymentModal = (crmForm, dbId) => {
    const amount = crmForm['[3.Təhsil] Qeydiyyat Səviyyəsi'] === 'Məktəbəqədər (5-6 yaş)' ? '20' : '30';
    const email = crmForm.email || 'Email qeyd olunmayıb';
    const phone = crmForm.phone || crmForm.tel || crmForm['[1.Əlaqə] Əlaqə Nömrəsi'] || 'Nömrə qeyd olunmayıb';

    const overlay = document.createElement('div');
    overlay.style.position = 'fixed';
    overlay.style.top = '0'; overlay.style.left = '0'; overlay.style.width = '100%'; overlay.style.height = '100%';
    overlay.style.background = 'rgba(0,0,0,0.8)'; overlay.style.backdropFilter = 'blur(10px)';
    overlay.style.zIndex = '999999'; overlay.style.display = 'flex'; overlay.style.alignItems = 'center'; overlay.style.justifyContent = 'center';

    const modal = document.createElement('div');
    modal.style.background = '#050a18'; modal.style.border = '1px solid rgba(255,255,255,0.1)';
    modal.style.borderRadius = '24px'; modal.style.padding = '40px'; modal.style.width = '100%'; modal.style.maxWidth = '450px';
    modal.style.color = 'white'; modal.style.boxShadow = '0 20px 50px rgba(0,0,0,0.5)';
    modal.style.position = 'relative';

    modal.innerHTML = `
        <h3 style="font-weight: 900; font-size: 1.6rem; margin-bottom: 10px; color: #fff;">Qeydiyyatı Tamamla</h3>
        <p style="color: rgba(255,255,255,0.6); font-size: 0.9rem; margin-bottom: 25px;">İmtahana giriş kuponunu əldə etmək üçün ödənişi tamamlayın.</p>
        
        <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 20px; margin-bottom: 25px;">
            <div style="display:flex; justify-content:space-between; margin-bottom:10px;">
                <span style="color:rgba(255,255,255,0.5);">Məbləğ:</span>
                <span style="font-weight:800; color:#10B981; font-size:1.2rem;">${amount} AZN</span>
            </div>
            <div style="display:flex; justify-content:space-between; font-size:0.85rem;">
                <span style="color:rgba(255,255,255,0.5);">Namizəd:</span>
                <span style="font-weight:700;">${crmForm['[2.Şagird] Adı'] || crmForm.name || 'Bilinmir'}</span>
            </div>
        </div>

        <div style="display: flex; flex-direction: column; gap: 15px; margin-bottom: 30px;">
            <input type="text" placeholder="Kartın Nömrəsi (0000 0000 0000 0000)" class="admin-input" style="background:#0f172a; border:1px solid rgba(255,255,255,0.1); padding:15px; border-radius:12px; color:white; width:100%;">
            <div style="display: flex; gap: 15px;">
                <input type="text" placeholder="AA/İİ" class="admin-input" style="flex:1; background:#0f172a; border:1px solid rgba(255,255,255,0.1); padding:15px; border-radius:12px; color:white;">
                <input type="text" placeholder="CVV" class="admin-input" style="flex:1; background:#0f172a; border:1px solid rgba(255,255,255,0.1); padding:15px; border-radius:12px; color:white;">
            </div>
        </div>

        <button id="pay-btn" style="width:100%; padding:18px; border:none; border-radius:12px; background:linear-gradient(135deg, #8B1A2B 0%, #b32a3e 100%); color:white; font-weight:800; font-size:1.1rem; cursor:pointer; transition:0.3s;">
            <i class="fas fa-lock" style="margin-right:8px;"></i> İndi Ödə
        </button>
        <button id="cancel-btn" style="width:100%; padding:15px; border:none; background:transparent; color:rgba(255,255,255,0.5); font-weight:600; font-size:0.9rem; cursor:pointer; margin-top:10px;">
            Daha Sonra Ödə
        </button>
    `;

    overlay.appendChild(modal);
    document.body.appendChild(overlay);

    document.getElementById('cancel-btn').onclick = () => {
        document.body.removeChild(overlay);
        window.location.href = 'index.html?success=true';
    };

    document.getElementById('pay-btn').onclick = async function() {
        this.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> İşlənir...';
        this.style.opacity = '0.7';
        this.disabled = true;

        // Simulate API call to payment gateway
        setTimeout(async () => {
            // Update CRM Payment Status
            crmForm['payment_status'] = 'Ödənilib';
            const SUBG_ID = 'miwvdhwrmxoetszkxlzy';
            const API_KEY = 'sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV';
            
            await fetch(`https://${SUBG_ID}.supabase.co/rest/v1/registrations?id=eq.${dbId}`, {
                method: 'PATCH',
                headers: {
                    'apikey': API_KEY,
                    'Authorization': `Bearer ${API_KEY}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ payload: crmForm })
            });

            // Call Vercel API to send actual Email
            try {
                await fetch('/api/send-email', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        email: email,
                        name: crmForm['[2.Şagird] Adı'] || crmForm.name || 'Namizəd',
                        dbId: dbId
                    })
                });
            } catch (err) {
                console.error("Failed to send email API:", err);
            }

            // Show Success Ticket
            modal.innerHTML = `
                <div style="text-align:center;">
                    <div style="width:80px; height:80px; background:rgba(16,185,129,0.1); color:#10B981; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:2.5rem; margin:0 auto 20px;">
                        <i class="fas fa-check"></i>
                    </div>
                    <h3 style="font-weight: 900; font-size: 1.6rem; margin-bottom: 10px; color: #fff;">Ödəniş Uğurlu!</h3>
                    <p style="color: rgba(255,255,255,0.6); font-size: 0.95rem; margin-bottom: 30px; line-height:1.6;">
                        İmtahana giriş kuponunuz və QR kod <b>${email}</b> ünvanına uğurla göndərildi.
                    </p>

                    <button onclick="window.location.href='index.html'" style="width:100%; padding:18px; border:none; border-radius:12px; background:rgba(255,255,255,0.1); color:white; font-weight:800; font-size:1rem; cursor:pointer; transition:0.3s;">
                        Ana Səhifəyə Qayıt
                    </button>
                </div>
            `;
        }, 2000);
    };
};

// Form Listeners
if (DOM.form) {
  DOM.form.addEventListener('submit', (e) => {
    e.preventDefault();
    const btn = DOM.form.querySelector('button');
    const originalText = btn.innerHTML;
    btn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> Göndərilir...';
    btn.disabled = true;
    const formData = new FormData(DOM.form);
    if (!formData.get('source')) formData.append('source', 'Lisey');
    submitToSupabase(formData, btn, originalText);
  });
}

const mobileToggle = document.getElementById('mobile-toggle');
const mobileClose = document.getElementById('mobile-close');
const mobileNav = document.getElementById('mobile-nav');

if (mobileToggle && mobileNav) {
  mobileToggle.addEventListener('click', (e) => {
    e.stopPropagation();
    mobileNav.classList.add('active');
    document.body.style.overflow = 'hidden';
  });
}

if (mobileClose && mobileNav) {
  mobileClose.addEventListener('click', () => {
    mobileNav.classList.remove('active');
    document.body.style.overflow = '';
  });
}

// Close mobile menu on outside click
document.addEventListener('click', (e) => {
  if (mobileNav && mobileNav.classList.contains('active') && !mobileNav.contains(e.target) && e.target !== mobileToggle) {
    mobileNav.classList.remove('active');
    document.body.style.overflow = '';
  }
});

// Close on ESC key
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && mobileNav && mobileNav.classList.contains('active')) {
    mobileNav.classList.remove('active');
    document.body.style.overflow = '';
  }
});

const translations = {
  az: {
    "nav-home": "Ana Səhifə",
    "nav-about": "Haqqımızda",
    "nav-academic": "Akademik İstiqamətlər",
    "nav-vacancy": "Vakansiya & Təcrübə",
    "nav-journal": "Evrika Jurnalı",
    "nav-contact": "Əlaqə",
    "nav-register": "Qeydiyyat",
    "hero-title": "HƏR UŞAQDA BİR GƏLƏCƏK<br>GİZLİDİR",
    "hero-subtitle": "Biz o gələcəyi kəşf edir, inkişaf etdirir və uğura çeviririk!",
    "btn-explore": "Kəşf Et",
    "btn-watch": "İzlə",
    "home-sec1-tag": "Evrika Montessori Kids Academy",
    "home-sec1-badge": "Erkən İnkişaf",
    "home-sec1-title": "Evrika Montessori<br>Kids Academy",
    "home-sec1-desc": "Uşaqların təbii marağını, yaradıcılığını və müstəqilliyini inkişaf etdirən Montessori metodu əsasında fərdi yanaşma ilə erkən uşaqlıq təhsili.",
    "btn-detail": "Ətraflı",
    "home-sec2-tag": "Evrika BETL Liseyi",
    "home-sec2-badge": "Qlobal Təhsil",
    "home-sec2-title": "Evrika Beynəlxalq Elm və Texnologiya Liseyi",
    "home-sec2-desc": "Cambridge proqramı, STEAM yönümlü tədris və laboratoriya əsaslı innovasiya mühiti ilə şagirdləri gələcəyə hazırlayan beynəlxalq akademik mərkəz.",
    "btn-nerimanov": "Nərimanov — Ətraflı",
    "btn-genclik": "Gənclik — Ətraflı",
    "home-sec3-tag": "Eduhome Hazırlıq Mərkəzi",
    "home-sec3-badge": "Akademik Dəstək",
    "home-sec3-title": "Eduhome<br>Təhsil Mərkəzi",
    "home-sec3-desc": "Xaricdə təhsil, universitetlərə hazırlıq, dil kursları və peşəkar akademik mentorluq ilə hər şagirdin potensialını açan hazırlıq mərkəzi.",
    "home-sec4-tag": "Zümrüd Womens Club",
    "home-sec4-badge": "Sağlam Həyat",
    "home-sec4-title": "Zümrüd<br>Women Club",
    "home-sec4-desc": "Evrika Active Life tərəfindən qadınlar üçün sağlam həyat tərzi, fitness, yoga və sosial inkişaf fəaliyyətlərini özündə birləşdirən premium idman mərkəzi.",
    "eco-title1": "EVRİKA TƏHSİL EKOSİSTEMİ",
    "eco-title2": "Akademik istiqamətlərimiz",
    "eco-desc": "İxtisaslaşmış akademik istiqamətlər və fərdi inkişaf modeli ilə hər yaş dövrünə uyğun təhsil mühiti.",
    "branch-montessori-title": "Evrika Montessori Kids Academy",
    "branch-betl-nerimanov-title": "Evrika Beynəlxalq Elm və Texnologiya Liseyi (Nərimanov filialı)",
    "branch-betl-genclik-title": "Evrika Beynəlxalq Elm və Texnologiya Liseyi (Gənclik filialı)",
    "branch-eduhome-title": "Evrika Eduhome Hazırlıq Mərkəzi",
    "branch-zumrud-title": "Zumrud Women Club by Evrika Active Life",
    "btn-details-look": "Detallara bax",
    "pres-title": "Təhsil bizim gələcəyimizdir!",
    "pres-name": "İlham Əliyev",
    "pres-role": "Azərbaycan Respublikasının Prezidenti",
    "vp-title": "Müasir dünyada hər bir ölkənin inkişafı, onun dünya birliyinə inteqrasiyası üçün təhsilin rolu əvəzsizdir.",
    "vp-name": "Mehriban Əliyeva",
    "vp-role": "Birinci Vitse-Prezident",
    "leader-title1": "Təhsil hər bir dövlətin, ölkənin, cəmiyyətin həyatının, fəaliyyətinin mühüm bir sahəsidir. Cəmiyyət təhsilsiz inkişaf edə bilməz.",
    "leader-title2": "“Hər bir xalqın tərəqqisi onun təhsil səviyyəsi ilə müəyyən olunur.”",
    "leader-name": "Heydər Əliyev",
    "leader-role": "Ümummilli Lider",
    "stats-title": "Mükəmməlliyin Rəqəmlərlə İfadəsi<span style=\"color: #60a5fa;\">.</span>",
    "stats-title-text": "Mükəmməlliyin Rəqəmlərlə İfadəsi",
    "stats-desc1": "Evrika şagirdi",
    "stats-desc2": "Olimpiada qalibi",
    "stats-desc3": "Qızıl medal",
    "stats-desc4": "Qırmızı attestat",
    "values-eyebrow": "EVRİKA TƏHSİL EKOSİSTEMİ",
    "values-title": "DƏYƏRLƏRİMİZ",
    "val1-title": "AKADEMİK GÜC",
    "val1-desc": "Güclü tədris proqramı və nəticə yönümlü yanaşma",
    "val2-title": "XARAKTER",
    "val2-desc": "Dəyərlər, məsuliyyət və şəxsiyyət formalaşması",
    "val3-title": "MİLLİ KİMLİK",
    "val3-desc": "Məsuliyyətli vətəndaşlıq və vətənpərvərlik.",
    "val4-title": "İNNOVASİYA",
    "val4-desc": "Müasir texnologiyalar və yeni nəsil təhsil modeli",
    "val5-title": "BEYNƏLXALQ DÜŞÜNCƏ",
    "val5-desc": "Multikultural dəyərlərə hörmət və qlobal baxış.",
    "val6-title": "SOSİAL TƏŞƏBBÜSKARLIQ",
    "val6-desc": "Şəxsi inkişaf, liderlik və özünə inamın formalaşması",
    "mission-title": "Missiyamız",
    "mission-desc": "Milli dəyərlərə sadiq, qlobal düşüncəyə malik, yenilikçi şəxsiyyətlər yetişdirməkdir!",
    "vision-title": "Vizyonumuz",
    "vision-desc": "Gələcəyin yalnız liderlərini deyil, dünyanı dəyişdirə bilən, cəmiyyətə fayda verən şəxsiyyətlər formalaşdırmaqdır!",
    "v2026-title1": "VİZYON 2026",
    "v2026-title2": "GƏLƏCƏYİ BU GÜN VAR EDƏN TƏHSİL EKOSİSTEMİ",
    "v2026-title2-part1": "GƏLƏCƏYİ BU GÜN VAR EDƏN",
    "v2026-title2-part2": "TƏHSİL EKOSİSTEMİ",
    "v2026-desc1": "EVRİKA artıq sadəcə məktəb deyil.",
    "v2026-desc2": "EVRİKA – gələcək quran təhsil ekosistemidir.",
    "alumni-sec-title1": "Məzunlarımız",
    "alumni-sec-title2": "Dünyaya Açılan<br>Uğur Yolumuz!",
    "parents-title1": "VALİDEYNLƏRİMİZ",
    "parents-desc1": "Uşaqlarımızın Evrikada keçirdiyi hər gün onların gələcəyinə qoyulan ən böyük sərmayədir.",
    "founder-title": "TƏSİSÇİNİN<br>MESAJI",
    "founder-quote": "<span style=\"font-size:4rem; color:var(--burgundy); line-height:0; vertical-align:middle; margin-right:10px;\">“</span><br>\"Evrika Təhsil Ekosistemi” mənim üçün yalnız bir təhsil müəssisəsi deyil — vətənimə, millətimə və onun gələcək tərəqqisinə olan sevgimin təzahürüdür",
    "founder-quote-text": "\"Evrika Təhsil Ekosistemi” mənim üçün yalnız bir təhsil müəssisəsi deyil — vətənimə, millətimə və onun gələcək tərəqqisinə olan sevgimin təzahürüdür",
    "founder-name": "Xudaqulu Rzayev",
    "founder-role": "EVRİKA TƏHSİL EKOSİSTEMİNİN TƏSİSÇİSİ",
    "join-title1": "EVRİKA",
    "join-title2": "EKOSİSTEMİ",
    "join-title3": "BİZƏ QOŞULUN!",
    "join-form-title": "Müraciət Forması",
    "form-child-name": "Övladınızın adı",
    "form-child-surname": "Övladınızın soyadı",
    "form-center": "Müraciət etmək istədiyiniz Təhsil Mərkəzi",
    "form-section": "Müraciət etmək istədiyiniz bölmə",
    "form-class": "Müraciət etmək istədiyiniz sinif",
    "form-school": "Gəldiyiniz təhsil müəssisəsi",
    "form-phone": "Telefon",
    "form-email": "E-mail",
    "form-submit": "Göndər",
    "news-eyebrow": "XƏBƏRLƏR",
    "news-btn-all": "Bütün Xəbərlər",
    "news-btn-read": "TAM OXU",
    "partners-title": "ƏMƏKDAŞLIQLARIMIZ",
    "partners-subtitle": "Partnyorlarımız",
    "footer-desc": "Evrika Təhsil Ekosistemi — Qlobal təhsil standartları, innovativ yanaşma və parlaq gələcəkdir.",
    "footer-nav": "NAVİQASİYA",
    "footer-contact-head": "Əlaqə",
    "footer-rights": "© 2026 Evrika Təhsil Ekosistemi. Bütün hüquqlar qorunur.",
    "footer-privacy": "Məxfilik Siyasəti",
    "footer-terms": "İstifadə Şərtləri",
    "nav-about-desc": "Bizim hekayəmiz",
    "nav-alumni": "Məzunlar",
    "nav-alumni-desc": "Fəxrlərimiz",
    "nav-achievements": "Uğurlar",
    "nav-achievements-desc": "Nailiyyətlərimiz",
    "nav-news": "Xəbərlər",
    "nav-news-desc": "Ən son yeniliklər",
    "nav-lisey1": "Evrika BETL Nərimanov",
    "nav-lisey1-desc": "Elm və Texnologiya Mərkəzi",
    "nav-lisey2": "Evrika BETL Gənclik",
    "nav-lisey2-desc": "Beynəlxalq Təhsil Müəssisəsi",
    "nav-montessori": "Montessori Kids Academy",
    "nav-montessori-desc": "Bağça və Erkən İnkişaf",
    "nav-eduhome": "Eduhome Hazırlıq",
    "nav-eduhome-desc": "Xaricdə Təhsil və Hazırlıq",
    "nav-zumrud": "Zümrüd İdman Mərkəzi",
    "nav-zumrud-desc": "Sağlam Həyat və Fəaliyyət",
    "nav-vac-title": "Karyera və Vakansiyalar",
    "nav-vac-desc": "Açıq iş elanları",
    "nav-ptim-title": "Pedaqoji Təcrübə və İnkişaf Mərkəzi",
    "nav-ptim-desc": "PTİM"
  },
  en: {
    "nav-home": "Home",
    "nav-about": "About Us",
    "nav-academic": "Academic Branches",
    "nav-vacancy": "Careers & Internship",
    "nav-journal": "Evrika Journal",
    "nav-contact": "Contact",
    "nav-register": "Registration",
    "hero-title": "A FUTURE IS HIDDEN<br>IN EVERY CHILD",
    "hero-subtitle": "We discover that future, develop it, and turn it into success!",
    "btn-explore": "Explore",
    "btn-watch": "Watch",
    "home-sec1-tag": "Evrika Montessori Kids Academy",
    "home-sec1-badge": "Early Development",
    "home-sec1-title": "Evrika Montessori<br>Kids Academy",
    "home-sec1-desc": "Early childhood education with an individualized approach based on the Montessori method, developing children's natural curiosity, creativity, and independence.",
    "btn-detail": "Details",
    "home-sec2-tag": "Evrika BETL Lyceum",
    "home-sec2-badge": "Global Education",
    "home-sec2-title": "Evrika International Science and Technology Lyceum",
    "home-sec2-desc": "An international academic center preparing students for the future with the Cambridge program, STEAM-oriented teaching, and a laboratory-based innovation environment.",
    "btn-nerimanov": "Narimanov — Details",
    "btn-genclik": "Ganjlik — Details",
    "home-sec3-tag": "Eduhome Prep Center",
    "home-sec3-badge": "Academic Support",
    "home-sec3-title": "Eduhome<br>Education Center",
    "home-sec3-desc": "A preparation center unlocking every student's potential with study abroad programs, university prep, language courses, and professional academic mentoring.",
    "home-sec4-tag": "Zumrud Womens Club",
    "home-sec4-badge": "Healthy Life",
    "home-sec4-title": "Zumrud<br>Women Club",
    "home-sec4-desc": "A premium sports center by Evrika Active Life combining healthy lifestyle, fitness, yoga, and social development activities for women.",
    "eco-title1": "EVRIKA EDUCATION ECOSYSTEM",
    "eco-title2": "Our Academic Branches",
    "eco-desc": "An educational environment suitable for every age with specialized academic directions and an individual development model.",
    "branch-montessori-title": "Evrika Montessori Kids Academy",
    "branch-betl-nerimanov-title": "Evrika International Science and Technology Lyceum (Narimanov branch)",
    "branch-betl-genclik-title": "Evrika International Science and Technology Lyceum (Ganjlik branch)",
    "branch-eduhome-title": "Evrika Eduhome Preparation Center",
    "branch-zumrud-title": "Zumrud Women Club by Evrika Active Life",
    "btn-details-look": "View details",
    "pres-title": "Education is our future!",
    "pres-name": "Ilham Aliyev",
    "pres-role": "President of the Republic of Azerbaijan",
    "vp-title": "In the modern world, the role of education is irreplaceable for the development of every country and its integration into the global community.",
    "vp-name": "Mehriban Aliyeva",
    "vp-role": "First Vice-President",
    "leader-title1": "Education is an important area of the life and activity of every state, country, and society. A society cannot develop without education.",
    "leader-title2": "“The progress of every nation is determined by its level of education.”",
    "leader-name": "Heydar Aliyev",
    "leader-role": "National Leader",
    "stats-title": "Excellence Expressed in Numbers<span style=\"color: #60a5fa;\">.</span>",
    "stats-title-text": "Excellence Expressed in Numbers",
    "stats-desc1": "Evrika students",
    "stats-desc2": "Olympiad winners",
    "stats-desc3": "Gold medals",
    "stats-desc4": "Red diplomas",
    "values-eyebrow": "EVRIKA EDUCATION ECOSYSTEM",
    "values-title": "OUR VALUES",
    "val1-title": "ACADEMIC STRENGTH",
    "val1-desc": "Strong curriculum and results-oriented approach",
    "val2-title": "CHARACTER",
    "val2-desc": "Values, responsibility, and personality development",
    "val3-title": "NATIONAL IDENTITY",
    "val3-desc": "Responsible citizenship and patriotism",
    "val4-title": "INNOVATION",
    "val4-desc": "Modern technologies and a new generation education model",
    "val5-title": "INTERNATIONAL MINDSET",
    "val5-desc": "Respect for multicultural values and a global perspective",
    "val6-title": "SOCIAL ENTREPRENEURSHIP",
    "val6-desc": "Personal development, leadership, and building self-confidence",
    "mission-title": "Our Mission",
    "mission-desc": "To raise innovative individuals loyal to national values with a global mindset!",
    "vision-title": "Our Vision",
    "vision-desc": "To shape individuals who are not only future leaders but also capable of changing the world and benefiting society!",
    "v2026-title1": "VISION 2026",
    "v2026-title2": "THE EDUCATION ECOSYSTEM CREATING THE FUTURE TODAY",
    "v2026-title2-part1": "THE EDUCATION ECOSYSTEM CREATING",
    "v2026-title2-part2": "THE FUTURE TODAY",
    "v2026-desc1": "EVRIKA is no longer just a school.",
    "v2026-desc2": "EVRIKA – is a future-building education ecosystem.",
    "alumni-sec-title1": "Our Alumni",
    "alumni-sec-title2": "Our Path of Success<br>Opening to the World!",
    "parents-title1": "OUR PARENTS",
    "parents-desc1": "Every day our children spend at Evrika is the greatest investment in their future.",
    "founder-title": "FOUNDER'S<br>MESSAGE",
    "founder-quote": "<span style=\"font-size:4rem; color:var(--burgundy); line-height:0; vertical-align:middle; margin-right:10px;\">“</span><br>For me, the Evrika Education Ecosystem is not just an educational institution — it is the manifestation of my love for my country, my nation, and its future progress",
    "founder-quote-text": "\"Evrika Education Ecosystem” for me is not just an educational institution — it is the manifestation of my love for my country, my nation, and its future progress",
    "founder-name": "Khudaqulu Rzayev",
    "founder-role": "FOUNDER OF EVRIKA EDUCATION ECOSYSTEM",
    "join-title1": "EVRIKA",
    "join-title2": "ECOSYSTEM",
    "join-title3": "JOIN US!",
    "join-form-title": "Application Form",
    "form-child-name": "Child's First Name",
    "form-child-surname": "Child's Last Name",
    "form-center": "Education Center you want to apply to",
    "form-section": "Section you want to apply to",
    "form-class": "Grade you want to apply to",
    "form-school": "Previous educational institution",
    "form-phone": "Phone",
    "form-email": "E-mail",
    "form-submit": "Submit",
    "news-eyebrow": "NEWS",
    "news-btn-all": "All News",
    "news-btn-read": "READ MORE",
    "partners-title": "OUR PARTNERSHIPS",
    "partners-subtitle": "Our Partners",
    "footer-desc": "Evrika Education Ecosystem — Global education standards, innovative approach, and a bright future.",
    "footer-nav": "NAVIGATION",
    "footer-contact-head": "Contact",
    "footer-rights": "© 2026 Evrika Education Ecosystem. All rights reserved.",
    "footer-privacy": "Privacy Policy",
    "footer-terms": "Terms of Use",
    "nav-about-desc": "Our Story",
    "nav-alumni": "Alumni",
    "nav-alumni-desc": "Our Pride",
    "nav-achievements": "Achievements",
    "nav-achievements-desc": "Our Success",
    "nav-news": "News",
    "nav-news-desc": "Latest Updates",
    "nav-lisey1": "Evrika ISTE Narimanov",
    "nav-lisey1-desc": "Science and Technology Center",
    "nav-lisey2": "Evrika ISTE Ganjlik",
    "nav-lisey2-desc": "International Education Institution",
    "nav-montessori": "Montessori Kids Academy",
    "nav-montessori-desc": "Kindergarten & Early Development",
    "nav-eduhome": "Eduhome Prep",
    "nav-eduhome-desc": "Study Abroad & Prep",
    "nav-zumrud": "Zumrud Sports Center",
    "nav-zumrud-desc": "Healthy Life & Activities",
    "nav-vac-title": "Careers and Vacancies",
    "nav-vac-desc": "Open Job Positions",
    "nav-ptim-title": "Pedagogical Practice and Development Center",
    "nav-ptim-desc": "PTDC"
  },
  ru: {
    "nav-home": "Главная",
    "nav-about": "О нас",
    "nav-academic": "Академические направления",
    "nav-vacancy": "Вакансии и Стажировки",
    "nav-journal": "Журнал Эврика",
    "nav-contact": "Контакт",
    "nav-register": "Регистрация",
    "hero-title": "В КАЖДОМ РЕБЕНКЕ СКРЫТО<br>БУДУЩЕЕ",
    "hero-subtitle": "Мы раскрываем это будущее, развиваем его и превращаем в успех!",
    "btn-explore": "Узнать",
    "btn-watch": "Смотреть",
    "home-sec1-tag": "Evrika Montessori Kids Academy",
    "home-sec1-badge": "Раннее развитие",
    "home-sec1-title": "Evrika Montessori<br>Kids Academy",
    "home-sec1-desc": "Дошкольное образование с индивидуальным подходом на основе метода Монтессори, развивающее естественное любопытство, творчество и независимость.",
    "btn-detail": "Подробнее",
    "home-sec2-tag": "Evrika BETL Лицей",
    "home-sec2-badge": "Глобальное образование",
    "home-sec2-title": "Международный Лицей Науки и Технологий Эврика",
    "home-sec2-desc": "Международный академический центр, готовящий студентов к будущему с помощью программы Cambridge, STEAM-обучения и инновационной лабораторной среды.",
    "btn-nerimanov": "Нариманов — Подробнее",
    "btn-genclik": "Гянджлик — Подробнее",
    "home-sec3-tag": "Подготовительный Центр Eduhome",
    "home-sec3-badge": "Академическая поддержка",
    "home-sec3-title": "Eduhome<br>Образовательный Центр",
    "home-sec3-desc": "Подготовительный центр, раскрывающий потенциал каждого студента с программами обучения за рубежом, подготовки к университету и профессионального наставничества.",
    "home-sec4-tag": "Zumrud Womens Club",
    "home-sec4-badge": "Здоровая жизнь",
    "home-sec4-title": "Zumrud<br>Women Club",
    "home-sec4-desc": "Премиальный спортивный центр от Evrika Active Life, сочетающий здоровый образ жизни, фитнес, йогу и социальное развитие для женщин.",
    "eco-title1": "ОБРАЗОВАТЕЛЬНАЯ ЭКОСИСТЕМА ЭВРИКА",
    "eco-title2": "Наши академические направления",
    "eco-desc": "Образовательная среда, подходящая для любого возраста, со специализированными академическими направлениями.",
    "branch-montessori-title": "Детская Академия Монтессори Эврика",
    "branch-betl-nerimanov-title": "Международный Лицей Науки и Технологий Эврика (Нариманов)",
    "branch-betl-genclik-title": "Международный Лицей Науки и Технологий Эврика (Гянджлик)",
    "branch-eduhome-title": "Подготовительный Центр Eduhome",
    "branch-zumrud-title": "Женский клуб Zumrud от Evrika Active Life",
    "btn-details-look": "Посмотреть детали",
    "pres-title": "Образование - наше будущее!",
    "pres-name": "Ильхам Алиев",
    "pres-role": "Президент Азербайджанской Республики",
    "vp-title": "В современном мире роль образования незаменима для развития каждой страны и ее интеграции.",
    "vp-name": "Мехрибан Алиева",
    "vp-role": "Первый Вице-Президент",
    "leader-title1": "Образование – важная сфера жизни. Общество не может развиваться без образования.",
    "leader-title2": "«Прогресс каждой нации определяется уровнем ее образования.»",
    "leader-name": "Гейдар Алиев",
    "leader-role": "Общенациональный Лидер",
    "stats-title": "Совершенство в цифрах.",
    "stats-title-text": "Совершенство в цифрах",
    "stats-desc1": "Учеников Эврика",
    "stats-desc2": "Победителей олимпиад",
    "stats-desc3": "Золотых медалей",
    "stats-desc4": "Красных аттестатов",
    "values-eyebrow": "ОБРАЗОВАТЕЛЬНАЯ ЭКОСИСТЕМА ЭВРИКА",
    "values-title": "НАШИ ЦЕННОСТИ",
    "val1-title": "АКАДЕМИЧЕСКАЯ СИЛА",
    "val1-desc": "Сильная учебная программа и подход, ориентированный на результат",
    "val2-title": "ХАРАКТЕР",
    "val2-desc": "Ценности, ответственность и развитие личности",
    "val3-title": "НАЦИОНАЛЬНАЯ ИДЕНТИЧНОСТЬ",
    "val3-desc": "Ответственное гражданство и патриотизм",
    "val4-title": "ИННОВАЦИИ",
    "val4-desc": "Современные технологии и модель образования нового поколения",
    "val5-title": "МЕЖДУНАРОДНОЕ МЫШЛЕНИЕ",
    "val5-desc": "Уважение к мультикультурным ценностям и глобальная перспектива",
    "val6-title": "СОЦИАЛЬНОЕ ПРЕДПРИНИМАТЕЛЬСТВО",
    "val6-desc": "Личностное развитие, лидерство и уверенность",
    "mission-title": "Наша Миссия",
    "mission-desc": "Воспитывать инновационных людей, верных национальным ценностям, с глобальным мышлением!",
    "vision-title": "Наше Видение",
    "vision-desc": "Формировать личностей, способных изменить мир и принести пользу обществу!",
    "v2026-title1": "ВИДЕНИЕ 2026",
    "v2026-title2": "ОБРАЗОВАТЕЛЬНАЯ ЭКОСИСТЕМА, СОЗДАЮЩАЯ БУДУЩЕЕ",
    "v2026-title2-part1": "ОБРАЗОВАТЕЛЬНАЯ ЭКОСИСТЕМА,",
    "v2026-title2-part2": "СОЗДАЮЩАЯ БУДУЩЕЕ",
    "v2026-desc1": "ЭВРИКА - это больше, чем просто школа.",
    "v2026-desc2": "ЭВРИКА – экосистема, строящая будущее.",
    "alumni-sec-title1": "Наши Выпускники",
    "alumni-sec-title2": "Наш путь успеха,<br>открытый миру!",
    "parents-title1": "НАШИ РОДИТЕЛИ",
    "parents-desc1": "Каждый день, проведенный нашими детьми в Эврике — величайшая инвестиция.",
    "founder-title": "ПОСЛАНИЕ<br>УЧРЕДИТЕЛЯ",
    "founder-quote": "“<br>Для меня Образовательная Экосистема Эврика — это не просто учебное заведение...",
    "founder-quote-text": "«Образовательная Экосистема Эврика» для меня не просто учебное заведение — это проявление моей любви к моей стране, моему народу и его будущему прогрессу",
    "founder-name": "Худагулу Рзаев",
    "founder-role": "УЧРЕДИТЕЛЬ",
    "join-title1": "ЭВРИКА",
    "join-title2": "ЭКОСИСТЕМА",
    "join-title3": "ПРИСОЕДИНЯЙТЕСЬ!",
    "join-form-title": "Форма заявки",
    "form-child-name": "Имя ребенка",
    "form-child-surname": "Фамилия ребенка",
    "form-center": "Желаемый учебный центр",
    "form-section": "Желаемое отделение",
    "form-class": "Желаемый класс",
    "form-school": "Предыдущая школа",
    "form-phone": "Телефон",
    "form-email": "E-mail",
    "form-submit": "Отправить",
    "news-eyebrow": "НОВОСТИ",
    "news-btn-all": "Все новости",
    "news-btn-read": "ЧИТАТЬ",
    "partners-title": "НАШЕ СОТРУДНИЧЕСТВО",
    "partners-subtitle": "Наши партнеры",
    "footer-desc": "Образовательная Экосистема Эврика — Глобальные стандарты, инновационный подход и блестящее будущее.",
    "footer-nav": "НАВИГАЦИЯ",
    "footer-contact-head": "Контакт",
    "footer-rights": "© 2026 Образовательная Экосистема Эврика. Все права защищены.",
    "footer-privacy": "Политика конфиденциальности",
    "footer-terms": "Условия использования",
    "nav-about-desc": "Наша история",
    "nav-alumni": "Выпускники",
    "nav-alumni-desc": "Наша гордость",
    "nav-achievements": "Успехи",
    "nav-achievements-desc": "Наши достижения",
    "nav-news": "Новости",
    "nav-news-desc": "Последние обновления",
    "nav-lisey1": "Эврика МЛНТ Нариманов",
    "nav-lisey1-desc": "Центр науки и технологий",
    "nav-lisey2": "Эврика МЛНТ Гянджлик",
    "nav-lisey2-desc": "Международное учебное заведение",
    "nav-montessori": "Montessori Kids Academy",
    "nav-montessori-desc": "Детский сад и раннее развитие",
    "nav-eduhome": "Eduhome Prep",
    "nav-eduhome-desc": "Обучение за рубежом и подготовка",
    "nav-zumrud": "Zumrud Sports Center",
    "nav-zumrud-desc": "Здоровая жизнь и активность",
    "nav-vac-title": "Карьера и вакансии",
    "nav-vac-desc": "Открытые вакансии",
    "nav-ptim-title": "Центр педагогической практики и развития",
    "nav-ptim-desc": "ЦППР"
  }
};

window.updateContent = function(lang) {
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (translations[lang] && translations[lang][key]) {
      el.innerHTML = translations[lang][key];
    }
  });
  localStorage.setItem('evrika-lang', lang);
  document.documentElement.lang = lang;
};

window.toggleLang = function(btn) {
  const code = btn.querySelector('#lang-code');
  const currentLang = code.textContent.toLowerCase();
  let nextLang = 'az';
  
  if (currentLang === 'az') nextLang = 'en';
  else if (currentLang === 'en') nextLang = 'ru';
  else nextLang = 'az';
  
  // Update all indicators (desktop and mobile)
  const codeSpans = document.querySelectorAll('#lang-code');
  codeSpans.forEach(span => span.textContent = nextLang.toUpperCase());
  
  window.updateContent(nextLang);
};

// Initialize language on load


// Sync across open tabs
window.addEventListener('storage', (e) => {
  if (e.key === 'evrika-lang') {
    const newLang = e.newValue || 'az';
    const codeSpans = document.querySelectorAll('#lang-code');
    codeSpans.forEach(span => span.textContent = newLang.toUpperCase());
    window.updateContent(newLang);
  }
});

let lastScrollY = window.scrollY;
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    if (!navbar) return;
    const currentScrollY = window.scrollY;
    if (currentScrollY > 80) {
        navbar.classList.add('scrolled');
        if (currentScrollY > lastScrollY && !(mobileNav && mobileNav.classList.contains('active'))) {
            navbar.classList.add('nav-hidden');
        } else {
            navbar.classList.remove('nav-hidden');
        }
    } else {
        navbar.classList.remove('scrolled', 'nav-hidden');
    }
    lastScrollY = Math.max(0, currentScrollY);
}, { passive: true });

// --- Active Link Logic ---
const setActiveLink = () => {
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.nav-links a');
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath === 'index.html' && href === './')) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });
};



// Cookie Consent Initializer Removed

// --- Final Init ---
document.addEventListener('DOMContentLoaded', () => {
    setActiveLink();
    setupFormValidation();
    const savedLang = localStorage.getItem('evrika-lang') || 'az';
    const codeSpans = document.querySelectorAll('#lang-code');
    codeSpans.forEach(span => span.textContent = savedLang.toUpperCase());
    window.updateContent(savedLang);
});

setInterval(setupFormValidation, 2000);

console.log('💎 Evrika Pro Optimized v4.0 Initialized');
