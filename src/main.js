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
    "nav-alumni": "Məzunlar",
    "nav-achievements": "Uğurlar",
    "nav-vacancy": "Vakansiya",
    "nav-contact": "Əlaqə",
    "nav-register": "Qeydiyyat",
    "hero-title": "HƏR UŞAQDA BİR GƏLƏCƏK<br>GİZLİDİR",
    "hero-subtitle": "Biz o gələcəyi kəşf edir, inkişaf etdirir və uğura çeviririk!",
    "btn-explore": "Kəşf Et",
    "btn-watch": "İzlə",
    "alumni-eyebrow": "BİZİM ÜZ AĞIMIZ",
    "alumni-title": "Məzun Tarixçəsi",
    "alumni-desc": "İxtisaslaşmış təhsil müəssisələrimizlə şagirdlərimizi akademik zəfərlərə və qlobal gələcəyə hazırlayırıq.",
    "about-eyebrow": "BİZİM HEKAYƏMIZ",
    "about-title": "Haqqımızda",
    "about-desc": "Evrika Təhsil Ekosistemi — hər bir şagirdin potensialını üzə çıxarmaq üçün qurulmuş ilham mənbəyidir.",
    "ach-eyebrow": "REKORD NƏTİCƏLƏR",
    "ach-title": "Uğurlarımız",
    "ach-desc": "15 illik təcrübəmiz və minlərlə uğurlu məzunumuzla fəxr edirik. Akademik zəfərimiz şagirdlərimizin gələcəyidir.",
    "vac-eyebrow": "BİZİM KOMANDAMIZA QOŞUL",
    "vac-title": "Karyera və Vakansiyalar",
    "vac-desc": "Təhsildə innovasiyalar yaratmaq üçün istedadlı və peşəkar mütəxəssislərlə birlikdə çalışırıq.",
    "footer-desc": "Innovativ təhsil, qlobal gələcək. Biz şagirdlərimizin uğuru üçün hər gün çalışırıq.",
    "footer-nav": "NAVİQASİYA",
    "footer-contact": "Əlaqə Məlumatları",
    "footer-rights": "© 2026 Evrika Təhsil Ekosistemi. Bütün hüquqlar qorunur.",
    "footer-privacy": "Məxfilik Siyasəti",
    "footer-terms": "İstifadə Şərtləri",
    "modal-title": "Gələcəyin uğuru burada başlayır..",
    "modal-desc": "2026/27-ci tədris ili üzrə <strong>şagird qəbulu</strong> davam edir.",
    "modal-btn": "Qeydiyyatdan keç",
    "team-leadership": "Rəhbərlik",
    "team-board": "İdarə Heyəti"
  },
  en: {
    "nav-home": "Home",
    "nav-about": "About Us",
    "nav-academic": "Academic Directions",
    "nav-alumni": "Alumni",
    "nav-achievements": "Success",
    "nav-vacancy": "Vacancies",
    "nav-contact": "Contact",
    "nav-register": "Registration",
    "hero-title": "EVERY CHILD HAS A FUTURE<br>HIDDEN WITHIN",
    "hero-subtitle": "We discover that future, develop it, and turn it into success!",
    "btn-explore": "Explore",
    "btn-watch": "Watch",
    "alumni-eyebrow": "OUR PRIDE",
    "alumni-title": "Alumni History",
    "alumni-desc": "We prepare our students for academic triumphs and a global future with our specialized educational institutions.",
    "about-eyebrow": "OUR STORY",
    "about-title": "About Us",
    "about-desc": "Evrika Education Ecosystem — a source of inspiration built to unlock every student's potential.",
    "ach-eyebrow": "RECORD RESULTS",
    "ach-title": "The Peak of Success",
    "ach-desc": "We are proud of our 20 years of experience and thousands of successful graduates. Our academic victory is the future of our students.",
    "vac-eyebrow": "JOIN OUR TEAM",
    "vac-title": "Careers & Vacancies",
    "vac-desc": "We work with talented and professional specialists to create innovations in education.",
    "footer-desc": "Innovative education, global future. We work every day for the success of our students.",
    "footer-nav": "Navigation",
    "footer-contact": "Contact Information",
    "footer-rights": "© 2026 Evrika Education Ecosystem. All rights reserved.",
    "footer-privacy": "Privacy Policy",
    "footer-terms": "Terms of Use",
    "modal-title": "Discover the Future with Us!",
    "modal-desc": "You are in the right place to uncover your child's unique talents and provide a global education. Registration for 2026/2027 is now open.",
    "modal-btn": "Register Now",
    "team-leadership": "Leadership",
    "team-board": "Board of Directors"
  },
  ru: {
    "nav-home": "Главная",
    "nav-about": "О нас",
    "nav-academic": "Академические направления",
    "nav-alumni": "Выпускники",
    "nav-achievements": "Успехи",
    "nav-vacancy": "Вакансии",
    "nav-contact": "Контакт",
    "nav-register": "Регистрация",
    "hero-title": "В КАЖДОМ РЕБЕНКЕ СКРЫТО БУДУЩЕЕ",
    "hero-subtitle": "Мы раскрываем это будущее, развиваем его и превращаем в успех!",
    "btn-explore": "Регистрация",
    "btn-watch": "Смотреть",
    "alumni-eyebrow": "НАША ГОРДОСТЬ",
    "alumni-title": "История выпускников",
    "alumni-desc": "Мы готовим наших учеников к академическим триумфам и глобальному будущему в наших специализированных учебных заведениях.",
    "about-eyebrow": "НАША ИСТОРИЯ",
    "about-title": "О нас",
    "about-desc": "Образовательная экосистема Эврика — это источник вдохновения, созданный для раскрытия потенциала каждого ученика.",
    "ach-eyebrow": "РЕКОРДНЫЕ РЕЗУЛЬТАТЫ",
    "ach-title": "Вершина нашего успеха",
    "ach-desc": "Мы гордимся нашим 20-летним опытом и тысячами успешных выпускников. Наша академическая победа — это будущее наших учеников.",
    "vac-eyebrow": "ПРИСОЕДИНЯЙТЕСЬ К НАШЕЙ КОМАНДЕ",
    "vac-title": "Карьера и вакансии",
    "vac-desc": "Мы работаем с талантливыми и профессиональными специалистами над созданием инноваций в образовании.",
    "footer-desc": "Инновационное образование, глобальное будущее. Мы работаем каждый день для успеха наших учеников.",
    "footer-nav": "Навигация",
    "footer-contact": "Контактная информация",
    "footer-rights": "© 2026 Образовательная экосистема Эврика. Все права защищены.",
    "footer-privacy": "Политика конфиденциальности",
    "footer-terms": "Условия использования",
    "modal-title": "Откройте будущее вместе с нами!",
    "modal-desc": "Вы находитесь в правильном месте, чтобы раскрыть уникальные таланты вашего ребенка. Регистрация на 2026/2027 учебный год уже открыта.",
    "modal-btn": "Зарегистрироваться",
    "team-leadership": "Руководство",
    "team-board": "Правление"
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
