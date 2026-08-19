

!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '315832961885795');
fbq('track', 'PageView');

(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXXX');



window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-XXXXXXXX');

(function() {
    var params = new URLSearchParams(window.location.search);
    var utms = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'];
    utms.forEach(function(utm) {
        if (params.has(utm)) {
            sessionStorage.setItem(utm, params.get(utm));
        }
    });
})();

// Optimization: Start fetching data immediately, in parallel with DOM parsing
        const ALUMNI_API_URL = 'https://gziuhrlvagflokivfgwt.supabase.co/rest/v1';
        const ALUMNI_API_KEY = 'sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP';

        // Define static fallback array first
        const STATIC_ALUMNI = [
          { img: "assets/mezunlar/mezun_1.png", name: "Evrika Məzunu", uni: "" },
          { img: "assets/mezunlar/mezun_2.png", name: "Evrika Məzunu", uni: "" },
          { img: "assets/mezunlar/mezun_3.png", name: "Evrika Məzunu", uni: "" },
          { img: "assets/mezunlar/mezun_4.png", name: "Evrika Məzunu", uni: "" },
          { img: "assets/mezunlar/mezun_5.jpeg", name: "Evrika Məzunu", uni: "" },
          { img: "assets/mezunlar/mezun_6.jpeg", name: "Evrika Məzunu", uni: "" },
          { img: "assets/mezunlar/mezun_7.jpeg", name: "Evrika Məzunu", uni: "" },
          { img: "assets/mezunlar/mezun_8.jpeg", name: "Evrika Məzunu", uni: "" },
          { img: "assets/mezunlar/mezun_9.jpeg", name: "Evrika Məzunu", uni: "" },
          { img: "assets/mezunlar/mezun_10.jpeg", name: "Evrika Məzunu", uni: "" },
          { img: "assets/mezunlar/mezun_11.jpeg", name: "Evrika Məzunu", uni: "" },
          { img: "assets/mezunlar/mezun_12.jpeg", name: "Evrika Məzunu", uni: "" },
          { img: "assets/mezunlar/mezun_13.jpeg", name: "Evrika Məzunu", uni: "" },
          { img: "assets/mezunlar/mezun_14.jpeg", name: "Evrika Məzunu", uni: "" },
          { img: "assets/mezunlar/mezun_15.jpeg", name: "Evrika Məzunu", uni: "" },
          { img: "assets/mezunlar/mezun_16.jpeg", name: "Evrika Məzunu", uni: "" },
          { img: "assets/mezunlar/mezun_17.jpeg", name: "Evrika Məzunu", uni: "" },
          { img: "assets/mezunlar/mezun_18.jpeg", name: "Evrika Məzunu", uni: "" },
          { img: "assets/mezunlar/mezun_19.jpeg", name: "Evrika Məzunu", uni: "" },
          { img: "assets/mezunlar/mezun_20.jpeg", name: "Evrika Məzunu", uni: "" },
        ];

        async function fetchAlumniForHome() {
          try {
            const res = await fetch(`${ALUMNI_API_URL}/mezunlar?select=*&order=id.desc&limit=30`, { 
              headers: { 'apikey': ALUMNI_API_KEY, 'Authorization': 'Bearer ' + ALUMNI_API_KEY } 
            });
            if (res.ok) {
              const data = await res.json();
              return data.map(r => r.payload);
            }
          } catch (e) { console.error(e); }
          // Static fallback if DB is empty or fails
          return STATIC_ALUMNI;
        }

        const alumniDataPromise = fetchAlumniForHome();

        // Render alumni immediately with static fallback, update when API responds

        function renderAlumniTracks(data) {
          const renderGroupIdx = (items) => {
            if (!items || items.length === 0) return '';
            return '<div class="alumni-group">' + items.map(a => `
                    <div class="al-card">
                      <img src="${a.img}" alt="Məzun" >
                    </div>
                 `).join('') + '</div>';
          };
          // Use full data to ensure no empty slots on large screens
          const t1Items = [...data];
          // Shift the second track so it doesn't look identical vertically
          const t2Items = [...data.slice(5), ...data.slice(0, 5)];
          
          // Render 4 groups to be absolutely sure it's wide enough for any screen
          const track1HTML = renderGroupIdx(t1Items) + renderGroupIdx(t1Items) + renderGroupIdx(t1Items) + renderGroupIdx(t1Items);
          const track2HTML = renderGroupIdx(t2Items) + renderGroupIdx(t2Items) + renderGroupIdx(t2Items) + renderGroupIdx(t2Items);
          const el1 = document.getElementById('alumni-track-1-idx');
          const el2 = document.getElementById('alumni-track-2-idx');
          if (el1) el1.innerHTML = track1HTML;
          if (el2) el2.innerHTML = track2HTML;
        }

        // Show static data immediately
        if (document.readyState === 'loading') {
          document.addEventListener('DOMContentLoaded', () => renderAlumniTracks(STATIC_ALUMNI));
        } else {
          renderAlumniTracks(STATIC_ALUMNI);
        }

        // Then update with real API data when ready
        alumniDataPromise.then(data => {
          if (data && data.length > 0) renderAlumniTracks(data);
        });

window.updateSector = function() {
              try {
                var branchSelect = document.getElementById('branchSelect');
                var sectorSelect = document.getElementById('sectorSelect');
                var branch = branchSelect.value;
                
                sectorSelect.innerHTML = '';
                
                var defOpt = document.createElement('option');
                defOpt.value = '';
                defOpt.disabled = true;
                defOpt.selected = true;
                defOpt.setAttribute('data-i18n', 'form-opt-section2');
                const evrikaLang = localStorage.getItem('evrika-lang') || 'az';
                defOpt.innerHTML = (window.translations && window.translations[evrikaLang] && window.translations[evrikaLang]['form-opt-section2']) 
                                   ? window.translations[evrikaLang]['form-opt-section2'] 
                                   : 'Bölmə seçin';
                sectorSelect.appendChild(defOpt);
                
                if (branch === 'nerimanov') {
                  sectorSelect.innerHTML += '<option value="az" data-i18n="sector-az">Azərbaycan bölməsi</option>';
                  sectorSelect.innerHTML += '<option value="rus" data-i18n="sector-ru">Rus bölməsi</option>';
                  sectorSelect.innerHTML += '<option value="ing" data-i18n="sector-en">İngilis bölməsi</option>';
                } else if (branch === 'genclik') {
                  sectorSelect.innerHTML += '<option value="az" data-i18n="sector-az">Azərbaycan bölməsi</option>';
                  sectorSelect.innerHTML += '<option value="rus" data-i18n="sector-ru">Rus bölməsi</option>';
                  sectorSelect.innerHTML += '<option value="ing" data-i18n="sector-en">İngilis bölməsi</option>';
                  sectorSelect.innerHTML += '<option value="turk" data-i18n="sector-tr">Türk bölməsi</option>';
                  sectorSelect.innerHTML += '<option value="montessori" data-i18n="sector-mont">Montessori məktəbi (ibtidai)</option>';
                } else if (branch === 'montessori') {
                  sectorSelect.innerHTML += '<option value="az" data-i18n="sector-az">Azərbaycan bölməsi</option>';
                  sectorSelect.innerHTML += '<option value="turk" data-i18n="sector-tr">Türk bölməsi</option>';
                  sectorSelect.innerHTML += '<option value="rus" data-i18n="sector-ru">Rus bölməsi</option>';
                  sectorSelect.innerHTML += '<option value="ing" data-i18n="sector-en">İngilis bölməsi</option>';
                } else if (branch === 'eduhome') {
                  sectorSelect.innerHTML += '<option value="sat" data-i18n="sector-sat">SAT hazırlığı</option>';
                  sectorSelect.innerHTML += '<option value="ielts" data-i18n="sector-ielts">IELTS hazırlığı</option>';
                  sectorSelect.innerHTML += '<option value="toefl" data-i18n="sector-toefl">TOEFL hazırlığı</option>';
                  sectorSelect.innerHTML += '<option value="dim" data-i18n="sector-dim">DİM hazırlığı</option>';
                  sectorSelect.innerHTML += '<option value="other" data-i18n="sector-other">Digər</option>';
                }
                if(window.updateContent) {
                  window.updateContent(localStorage.getItem('evrika-lang') || 'az');
                }
              } catch(e) {
                console.error(e);
              }
            };

            (function() {
              var mainForm = document.getElementById('mainContactForm');
              if (mainForm) {
                mainForm.addEventListener('submit', async function(event) {
                  event.preventDefault();
                  var btn = event.target.querySelector('button[type="submit"]');
                  var originalBtnContent = btn.innerHTML;
                  btn.disabled = true;
                  btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Göndərilir...';

                  var firstName = document.getElementById('mf_firstName').value;
                  var lastName = document.getElementById('mf_lastName').value;
                  
                  var branchSelect = document.getElementById('branchSelect');
                  var branchText = branchSelect.options[branchSelect.selectedIndex] ? branchSelect.options[branchSelect.selectedIndex].text : '';
                  
                  var sectorSelect = document.getElementById('sectorSelect');
                  var sectorText = sectorSelect.options[sectorSelect.selectedIndex] ? sectorSelect.options[sectorSelect.selectedIndex].text : '';
                  
                  var grade = document.getElementById('mf_class').value;
                  var phonePrefix = document.getElementById('mf_phoneCode').value;
                  var phoneNum = document.getElementById('mf_phoneNum').value;
                  var email = document.getElementById('mf_email').value;
                  var previousSchool = document.getElementById('mf_previousSchool').value;

                  var note = "Mərkəz: " + branchText + " | Bölmə: " + sectorText + " | Sinif: " + grade + " | E-mail: " + email + " | Əvvəlki müəssisə: " + previousSchool;

                  var payloadData = {
                    name: firstName + " " + lastName,
                    phone: phonePrefix + phoneNum,
                    source: "Ana Səhifə - Form",
                    status: "Yeni",
                    note: note,
                    date: new Date().toISOString()
                  };

                  try {
                    await fetch('https://gziuhrlvagflokivfgwt.supabase.co/rest/v1/registrations', {
                      method: 'POST',
                      headers: {
                        'apikey': 'sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP',
                        'Authorization': 'Bearer sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP',
                        'Content-Type': 'application/json'
                      },
                      body: JSON.stringify({ payload: payloadData })
                    });
                    alert('Müraciətiniz uğurla göndərildi! Sizinlə tezliklə əlaqə saxlayacağıq.');
                    event.target.reset();
                    sectorSelect.innerHTML = '<option value="" disabled selected>Əvvəlcə mərkəz seçin</option>';
                  } catch(e) {
                    alert('Xəta baş verdi. Zəhmət olmasa yenidən cəhd edin.');
                  } finally {
                    btn.disabled = false;
                    btn.innerHTML = originalBtnContent;
                  }
                });
              }
            })();



// Initialize Swiper for Hero
        const swiper = new Swiper('.heroSwiper', {
          loop: false,
          parallax: true,
          speed: 1200,
          autoplay: false,
          pagination: {
            el: '.swiper-pagination',
            clickable: true,
          },
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
          },
        });

        // ── Hero Slider Controls ──────────────────────────────────
        const SLIDE_DELAY = 5000; // ms
        let progressTimer = null;
        let progressStart = null;
        let heroPaused = false;
        function setRing(fraction) {
          const ring = document.getElementById('progressRing');
          if (ring) {
            const r = parseFloat(ring.getAttribute('r'));
            const circumference = 2 * Math.PI * r;
            ring.style.strokeDashoffset = circumference * (1 - fraction);
          }
        }

        function startRing(onComplete) {
          clearInterval(progressTimer);
          progressStart = Date.now();
          progressTimer = setInterval(() => {
            if (heroPaused) return;
            const elapsed = Date.now() - progressStart;
            const fraction = Math.min(elapsed / SLIDE_DELAY, 1);
            setRing(fraction);
            if (fraction >= 1) {
              clearInterval(progressTimer);
              setRing(0);
              if (onComplete) onComplete();
            }
          }, 40);
        }

        function resetRing() {
          clearInterval(progressTimer);
          setRing(0);
        }

        function advanceAndRestart() {
          if (swiper.isEnd) {
            swiper.slideTo(0);
          } else {
            swiper.slideNext();
          }
          // ring restart handled in slideChange
        }

        // Slide change → restart ring for new slide
        swiper.on('slideChange', () => {
          resetRing();
          const navbar = document.querySelector('.navbar');
          if (swiper.activeIndex === 0) {
            // Slide 1: wait for video to end, then start 5s countdown
            const vid = document.getElementById('heroReklam');
            if (vid) {
              vid.currentTime = 0;
              vid.play();
            }
          } else {
            if (!heroPaused) startRing(advanceAndRestart);
          }
        });

        // Slide 1: video ends → start 5s countdown
        const heroVideo = document.getElementById('heroReklam');
        if (heroVideo) {
          heroVideo.addEventListener('ended', () => {
            if (!heroPaused) startRing(advanceAndRestart);
          });
        }

        // Toggle pause/play
        function toggleHeroPlay() {
          const icon = document.getElementById('heroPlayIcon');
          heroPaused = !heroPaused;
          const vid = document.getElementById('heroReklam');
          const isSlide1 = swiper.activeIndex === 0;

          if (heroPaused) {
            icon.className = 'fas fa-play';
            clearInterval(progressTimer);
            // Slide 1 → pause video; others → ring already stopped
            if (isSlide1 && vid) vid.pause();
          } else {
            icon.className = 'fas fa-pause';
            if (isSlide1 && vid) {
              // Resume video; ring starts when video.ended fires
              vid.play();
            } else {
              // Resume ring countdown
              progressStart = Date.now();
              startRing(advanceAndRestart);
            }
          }
        }

        // Prev / Next helpers
        function heroSlidePrev() {
          resetRing();
          swiper.slidePrev();
          setTimeout(() => {
            const vid = document.getElementById('heroReklam');
            if (swiper.activeIndex === 0 && vid) {
              vid.currentTime = 0; vid.play();
            } else if (!heroPaused) {
              startRing(advanceAndRestart);
            }
          }, 150);
        }
        function heroSlideNext() {
          resetRing();
          swiper.slideNext();
          setTimeout(() => {
            if (swiper.activeIndex === 0) {
              const vid = document.getElementById('heroReklam');
              if (vid) { vid.currentTime = 0; vid.play(); }
            } else if (!heroPaused) {
              startRing(advanceAndRestart);
            }
          }, 150);
        }


        window.openVideoModal = (url) => {
          const modal = document.getElementById('videoModal');
          const modalVid = document.getElementById('modalVideo');
          const modalIf = document.getElementById('modalIframe');
          const wrapper = document.querySelector('.modern-video-wrapper');
          const navbar = document.querySelector('.navbar');
          if (!modal || !modalVid || !modalIf || !wrapper) return;

          // Helper to get YouTube Embed URL
          const getYoutubeEmbed = (link) => {
            if (!link) return '';
            const regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/;
            const match = link.match(regExp);
            return (match && match[2].length === 11) ? `https://www.youtube.com/embed/${match[2]}?autoplay=1` : '';
          };

          // Helper to get Instagram Embed URL
          const getInstagramEmbed = (link) => {
            if (!link || !link.includes('instagram.com')) return '';
            try {
              let u = new URL(link);
              let path = u.pathname;
              if (path.endsWith('/')) path = path.slice(0, -1);
              if (path.includes('/p/') || path.includes('/reel/') || path.includes('/tv/')) {
                return `https://www.instagram.com${path}/embed/`;
              }
            } catch(e) {}
            return '';
          };

          const ytEmbed = getYoutubeEmbed(url);
          const igEmbed = getInstagramEmbed(url);

          // Reset styles
          wrapper.style.background = '#000';
          wrapper.style.padding = '4px';
          wrapper.style.maxWidth = '1000px';
          wrapper.style.width = '90vw';
          wrapper.style.aspectRatio = '';
          modalIf.style.marginTop = '0';
          modalIf.style.height = '100%';
          modalIf.style.width = '100%';

          if (ytEmbed || igEmbed) {
            modalVid.style.display = 'none';
            modalVid.pause();
            modalIf.src = ytEmbed || igEmbed;
            modalIf.style.display = 'block';
            
            if (igEmbed) {
                // Seamless Instagram Look: Remove black bars and crop UI
                wrapper.style.background = 'transparent';
                wrapper.style.padding = '0';
                wrapper.style.boxShadow = 'none';
                
                if (url.includes('/reel/')) {
                    wrapper.style.maxWidth = '420px';
                    wrapper.style.aspectRatio = '9/16';
                    // Crop the Instagram header and footer
                    modalIf.style.height = '115%'; 
                    modalIf.style.marginTop = '-45px';
                } else {
                    wrapper.style.maxWidth = '600px';
                    wrapper.style.aspectRatio = '1/1';
                    modalIf.style.height = '112%';
                    modalIf.style.marginTop = '-40px';
                }
            } else {
                wrapper.style.aspectRatio = '16/9';
            }
          } else {
            modalIf.style.display = 'none';
            modalIf.src = '';
            modalVid.src = url;
            modalVid.style.display = 'block';
          }
          
          modal.style.display = 'flex';
          document.body.style.overflow = 'hidden';
          if (navbar) navbar.classList.add('nav-hidden');
          
          if (!ytEmbed && !igEmbed) {
              modalVid.play().catch(e => console.log('Video play failed:', e));
          }
        };

        window.openParentVideo = window.openVideoModal;

        window.closeVideoModal = () => {
          const modal = document.getElementById('videoModal');
          const modalVid = document.getElementById('modalVideo');
          const modalIf = document.getElementById('modalIframe');
          const navbar = document.querySelector('.navbar');
          if (modal) modal.style.display = 'none';
          if (modalVid) { modalVid.pause(); modalVid.src = ''; }
          if (modalIf) modalIf.src = '';
          document.body.style.overflow = '';
          if (navbar) navbar.classList.remove('nav-hidden');
        };
        document.addEventListener('keydown', (e) => {
          if (e.key === 'Escape') closeVideoModal();
        });



        // Initialize Swiper for Modern Stats
        const modernStatsSwiper = new Swiper('.modernStatsSwiper', {
          slidesPerView: 1,
          spaceBetween: 40,
          loop: true,
          autoplay: {
            delay: 4500,
            disableOnInteraction: false,
          },
          pagination: {
            el: '.modernStatsSwiper .swiper-pagination',
            clickable: true,
          },
          breakpoints: {
            768: { slidesPerView: 2, spaceBetween: 40 }
          }
        });

        // Initialize Swiper for Parent Testimonials
        async function initParentTestimonials() {
          const API_URL = 'https://gziuhrlvagflokivfgwt.supabase.co/rest/v1';
          const API_KEY = 'sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP';
          const HEADERS = { 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY };
          
          const wrapper = document.getElementById('parent-testimonials-wrapper');
          if (!wrapper) return;

          try {
            const res = await fetch(`${API_URL}/parent_testimonials?select=*&order=id.desc`, { headers: HEADERS });
            if (res.ok) {
              const data = await res.json();
              if (data.length > 0) {
                let instagramCount = 0;
                wrapper.innerHTML = data.map((item, idx) => {
                  const p = item.payload;
                  const isVideo = p.type === 'video';
                  const isDark = idx % 2 !== 0;
                  
                  // Extract YouTube or Instagram ID for the cover if it's a video
                  let coverImg = p.thumbnail_url || p.avatar || 'https://via.placeholder.com/400';
                  if (isVideo && p.media_url) {
                      const ytMatch = p.media_url.match(/(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))([^&?]+)/);
                      if (ytMatch && ytMatch[1]) {
                          coverImg = `https://img.youtube.com/vi/${ytMatch[1]}/maxresdefault.jpg`;
                      }
                      
                      const igMatch = p.media_url.match(/(?:instagram\.com\/(?:p|reel|tv)\/)([^/?#&]+)/);
                      if (igMatch && igMatch[1]) {
                          instagramCount++;
                          // Alternating between cover 1 and cover 2 for variety
                          coverImg = (instagramCount % 2 === 1) ? 'assets/parent_video_cover.png' : 'assets/parent_video_cover_2.png';
                      }
                  }

                  // Specific cover for Şahbaz Xuduoğlu
                  if (p.name && p.name.includes('Şahbaz Xuduoğlu')) {
                      coverImg = 'assets/parent_video_cover_2.png';
                  }

                  // Auto-format status if it's just a year
                  let displayStatus = p.status || '';
                  if (/^\d{4}$/.test(displayStatus.trim())) {
                      displayStatus = `${displayStatus}-cu ildən bəri Evrika Liseyi valideynidir`;
                  }

                  return `
                    <div class="swiper-slide">
                      <div class="parent-testimonial-card ${isDark ? 'card-dark' : ''}">
                        <div class="parent-card-media">
                          <img src="${coverImg}" alt="${p.name}">
                          ${isVideo ? `
                            <div class="play-btn-small" onclick="openParentVideo('${p.media_url}')">
                              <i class="fas fa-play"></i>
                            </div>
                          ` : ''}
                        </div>
                        <div class="parent-card-text">
                           <div class="parent-quote-wrapper">
                             <div class="parent-quote">"${p.quote || ''}"</div>
                           </div>
                           <div class="parent-meta-box">
                             <h4 style="margin: 0; font-size: 1.2rem; font-weight: 800;">${p.name}</h4>
                             <p style="margin: 5px 0 0; font-size: 0.85rem; font-weight: 600;">${displayStatus}</p>
                           </div>
                        </div>
                      </div>
                    </div>
                  `;
                }).join('');
              } else {
                wrapper.innerHTML = '<div class="swiper-slide"><div class="parent-testimonial-card">Hələ ki rəy əlavə edilməyib.</div></div>';
              }
            }
          } catch (e) {
            console.error(e);
          }

          new Swiper('.parentTestimonialSwiper', {
            slidesPerView: 1,
            spaceBetween: 20,
            loop: true,
            autoplay: { delay: 7000, disableOnInteraction: false },
            navigation: {
              nextEl: '.parent-next',
              prevEl: '.parent-prev',
            },
            breakpoints: {
              1024: { slidesPerView: 1.5 }
            }
          });
        }

        function renderPartners(partners) {
          const grid = document.getElementById('partners-grid-content');
          if (!grid) return;
          const repeated = [...partners, ...partners, ...partners, ...partners, ...partners];
          grid.innerHTML = repeated.map(p => {
            const logo = p.logo_url || p.logo;
            let imgStyle = '';
            if (p.name === 'APEIA' || (p.logo_url && p.logo_url.includes('aotmalogo'))) imgStyle = 'transform: scale(1.6);';
            return `
            <div class="partner-item">
              <img src="${logo}" alt="${p.name}" ${imgStyle ? `style="${imgStyle}"` : ''}>
              <span class="partner-name">${p.name}</span>
              ${p.description ? `
                <div class="partner-overlay">
                  <div style="font-weight: 800; color: white; font-size: 0.85rem; text-transform: uppercase; margin-bottom: 5px;">${p.name}</div>
                  <div class="partner-info-text">${p.description}</div>
                </div>
              ` : ''}
            </div>
            `;
          }).join('');
        }

        async function initPartners() {
          const API_URL = 'https://gziuhrlvagflokivfgwt.supabase.co/rest/v1';
          const API_KEY = 'sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP';
          const HEADERS = { 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY };
          try {
            const res = await fetch(`${API_URL}/partners?select=*&order=sort_order.asc`, { headers: HEADERS });
            if (res.ok) {
              const data = await res.json();
              renderPartners(data);
            }
          } catch (e) {
            console.error('Failed to load partners from Supabase:', e);
          }
        }

        async function initNews() {
          const API_URL = 'https://gziuhrlvagflokivfgwt.supabase.co/rest/v1';
          const API_KEY = 'sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP';
          const HEADERS = { 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY };
          const container = document.getElementById('dynamic-news-container');
          if (!container) return;
          try {
            const res = await fetch(`${API_URL}/news?select=*&order=id.desc&limit=3`, { headers: HEADERS });
            if (res.ok) {
              const data = await res.json();
              if (data.length > 0) {
                container.innerHTML = data.map(item => {
                  const n = item.payload;
                  const firstImg = n.img ? n.img.split(',')[0].trim() : '';
                  const dateStr = n.date || "";
                  const parts = dateStr.split(/[-./]/);
                  const months = ["Yan", "Fev", "Mar", "Apr", "May", "İyn", "İyl", "Avq", "Sen", "Okt", "Noy", "Dek"];
                  
                  let day = "13", month = "Apr";
                  if(parts.length === 3) {
                      if(parts[0].length === 4) {
                          day = parts[2];
                          month = months[parseInt(parts[1]) - 1] || "Ay";
                      } else {
                          day = parts[0];
                          month = months[parseInt(parts[1]) - 1] || "Ay";
                      }
                  }
                  
                  return `
                  <a href="news-detail.html?id=${item.id}" class="news-card" style="text-decoration:none;">
                      <div class="card-media">
                          <img src="${firstImg}" alt="${n.title}" loading="lazy">
                          <div class="date-badge">
                              <strong>${day}</strong>
                              <span>${month}</span>
                          </div>
                      </div>
                      <div class="card-body">
                          <div class="card-cat">${n.category || 'Xəbər'}</div>
                          <h3 class="card-title">${n.title}</h3>
                          <p class="card-desc">${n.text || ''}</p>
                          <div class="card-footer">
                              <span data-i18n="news-read-more">Ətraflı Oxu</span> <i class="fas fa-arrow-right"></i>
                          </div>
                      </div>
                  </a>
                `}).join('');
              }
            }
          } catch(e) { console.error(e); }
        }

        async function initPopups() {
          const API_URL = 'https://gziuhrlvagflokivfgwt.supabase.co/rest/v1';
          const API_KEY = 'sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP';
          const HEADERS = { 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY };
          
          if (sessionStorage.getItem('evrika_popup_seen')) return;

          try {
            const res = await fetch(`${API_URL}/popups?select=*&order=id.desc`, { headers: HEADERS });
            if (res.ok) {
              const data = await res.json();
              const activePopup = data.find(p => p.payload && p.payload.status === 'active');
              if (activePopup) {
                const p = activePopup.payload;
                
                const modal = document.createElement('div');
                modal.className = "welcome-modal-overlay";
                modal.id = "welcomeModal";
                
                let linkHTML = p.link ? `<a class="welcome-modal-btn" href="${p.link}">Ətraflı</a>` : '';
                
                modal.innerHTML = `
                  <div class="welcome-modal-content">
                    <div class="welcome-modal-close" id="close-campaign-popup">
                      <i class="fas fa-times"></i>
                    </div>
                    ${p.img ? `<img alt="${p.title}" class="welcome-modal-image" src="${p.img}"/>` : ''}
                    <div class="welcome-modal-body">
                      <h2 class="welcome-modal-title">${p.title}</h2>
                      ${p.desc ? `<p class="welcome-modal-desc">${p.desc}</p>` : ''}
                      ${linkHTML}
                    </div>
                  </div>
                `;
                document.body.appendChild(modal);
                
                // Show modal with animation
                setTimeout(() => {
                  modal.classList.add('active');
                }, 1000);
                
                document.getElementById('close-campaign-popup').onclick = () => {
                   modal.classList.remove('active');
                   setTimeout(() => modal.remove(), 600);
                   sessionStorage.setItem('evrika_popup_seen', 'true');
                };

              }
            }
          } catch(e) {}
        }

        // Global Init
        document.addEventListener('DOMContentLoaded', () => {
           initParentTestimonials();
           initPartners();
           initNews();
           initPopups();
        });

        // Functional unified in above global scope

        initParentTestimonials();

        // Initialize Swiper for State Symbols/Quotes
        const quotesSwiper = new Swiper('.quotesSwiper', {
          slidesPerView: 1,
          spaceBetween: 40,
          effect: "fade",
          fadeEffect: { crossFade: true },
          loop: true,
          autoplay: {
            delay: 3000,
            disableOnInteraction: false
          },
          navigation: {
            nextEl: '.quotes-next',
            prevEl: '.quotes-prev',
          },
          pagination: {
            el: '.quotesSwiper .swiper-pagination',
            clickable: true,
          }
        });

        // Initialize Swiper for Testimonials
        const testimonialSwiper = new Swiper('.simpleTestimonialSwiper', {
          slidesPerView: 1,
          spaceBetween: 40,
          loop: true,
          autoplay: {
            delay: 5000,
            disableOnInteraction: false,
          },
          navigation: {
            nextEl: '.testimonial-next',
            prevEl: '.testimonial-prev',
          },
          breakpoints: {
            768: { slidesPerView: 2, spaceBetween: 40 },
            1024: { slidesPerView: 3, spaceBetween: 40 }
          }
        });

        // Specific School Metadata for Differentiation
        const schoolRegistry = {
          lisey1: { name: 'Evrika BETL Nərimanov', icon: 'fa-microscope', color: '#8B1A2B' },
          lisey2: { name: 'Evrika BETL Gənclik', icon: 'fa-atom', color: '#8B1A2B' },
          montessori: { name: 'Montessori Kids Academy', icon: 'fa-child', color: '#4C60AB' },
          eduhome: { name: 'Victory Colleges by Evrika', icon: 'fa-graduation-cap', color: '#8B1A2B' },
          zumrud: { name: 'Zümrüd Women Club', icon: 'fa-swimmer', color: '#4C60AB' },
          general: { name: 'Ümumi Qeydiyyat', icon: 'fa-school', color: '#8B1A2B' }
        };

        // Unique Registration Modal Logic
        function openRegistrationModal(titleText, schoolId) {
          const modal = document.getElementById('registrationModal');
          const title = document.getElementById('reg-school-title');
          const iconContainer = document.getElementById('reg-school-icon');
          const themeLine = document.getElementById('reg-theme-line');
          const submitBtn = modal.querySelector('.reg-submit-btn');
          const hiddenInput = document.getElementById('reg-school-id');
          const navbar = document.querySelector('.navbar');
          
          if (!modal || !title) return;

          // Get metadata
          const schoolData = schoolRegistry[schoolId] || schoolRegistry.general;
          
          // Update Content
          title.textContent = schoolData.name;
          if (hiddenInput) hiddenInput.value = schoolId;
          if (iconContainer) {
            iconContainer.innerHTML = `<i class="fas ${schoolData.icon}"></i>`;
            iconContainer.style.color = schoolData.color;
            iconContainer.style.background = `${schoolData.color}10`; // 10% opacity
          }
          if (themeLine) themeLine.style.background = schoolData.color;
          if (submitBtn) {
            submitBtn.style.background = schoolData.color;
            submitBtn.style.boxShadow = `0 10px 30px ${schoolData.color}40`;
          }
          
          modal.style.display = 'flex';
          document.body.style.overflow = 'hidden';
          if (navbar) navbar.classList.add('nav-hidden');
          
          // Animate in
          setTimeout(() => {
            modal.classList.add('active');
          }, 10);
        }

        function closeRegistrationModal() {
          const modal = document.getElementById('registrationModal');
          const navbar = document.querySelector('.navbar');
          if (!modal) return;
          
          modal.classList.remove('active');
          setTimeout(() => {
            modal.style.display = 'none';
            document.body.style.overflow = '';
            if (navbar && window.scrollY <= 100) navbar.classList.remove('nav-hidden');
          }, 400);
        }



        // Reveal Animations
        document.addEventListener('DOMContentLoaded', () => {
          const reveals = document.querySelectorAll('.reveal');
          setTimeout(() => {
            reveals.forEach(r => r.classList.add('visible'));
          }, 100);
        });

document.addEventListener('DOMContentLoaded', () => {
            if (typeof updateContent === 'function') {
                updateContent(localStorage.getItem('evrika-lang') || 'az');
            }

            // Welcome Modal Logic (Temporarily always shown for review)
            setTimeout(() => {
                if (typeof openWelcomeModal === 'function' && !sessionStorage.getItem('evrika_welcome_shown')) {
                    openWelcomeModal();
                    sessionStorage.setItem('evrika_welcome_shown', 'true');
                }
            }, 500); // Faster trigger for review
        });

function toggleMobileAcc(id) {
      var el = document.getElementById(id);
      if (!el) return;
      el.classList.toggle('open');
    }

function acceptCookies() {
      localStorage.setItem('evrika_cookies_accepted', 'true');
      hideCookieModal();
    }
    function rejectCookies() {
      localStorage.setItem('evrika_cookies_accepted', 'false');
      hideCookieModal();
    }
    function hideCookieModal() {
      const banner = document.getElementById('premium-cookie-banner');
      banner.style.opacity = '0';
      document.getElementById('cookie-modal-content').style.transform = 'scale(0.9)';
      setTimeout(() => { banner.style.display = 'none'; }, 400);
    }
    document.addEventListener('DOMContentLoaded', () => {
      if (!localStorage.getItem('evrika_cookies_accepted')) {
        setTimeout(() => {
          const banner = document.getElementById('premium-cookie-banner');
          banner.style.display = 'flex';
          // trigger reflow
          void banner.offsetWidth;
          banner.style.opacity = '1';
          document.getElementById('cookie-modal-content').style.transform = 'scale(1)';
        }, 1500);
      }
    });

document.addEventListener("DOMContentLoaded", async function() {
        const grid = document.getElementById('home-news-grid');
        if(!grid) return;
        try {
            const API_URL = 'https://gziuhrlvagflokivfgwt.supabase.co/rest/v1';
            const API_KEY = 'sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP';
            const res = await fetch(`${API_URL}/news?select=*&order=id.desc&limit=3`, {
                headers: { 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY }
            });
            if(res.ok) {
                const data = await res.json();
                if(!data.length) {
                    grid.innerHTML = '<div style="text-align:center; width:100%; grid-column:1/-1; opacity:0.5; font-size:1.2rem;">Hələ ki, heç bir xəbər yoxdur.</div>';
                    return;
                }
                grid.innerHTML = data.map(row => {
                    const n = row.payload;
                    const dateStr = n.date || "";
                    const parts = dateStr.split(/[-./]/);
                    const months = ["Yan", "Fev", "Mar", "Apr", "May", "İyn", "İyl", "Avq", "Sen", "Okt", "Noy", "Dek"];
                    
                    let day = "13", month = "Apr";
                    if(parts.length === 3) {
                        if(parts[0].length === 4) {
                            day = parts[2];
                            month = months[parseInt(parts[1]) - 1] || "Ay";
                        } else {
                            day = parts[0];
                            month = months[parseInt(parts[1]) - 1] || "Ay";
                        }
                    }
                    const firstImg = (n.img || "").split(',')[0].trim();
                    return `
                        <a href="news-detail.html?id=${row.id}" class="news-card">
                            <div class="card-media">
                                <img src="${firstImg}" alt="${n.title}" loading="lazy">
                                <div class="date-badge">
                                    <strong>${day}</strong>
                                    <span>${month}</span>
                                </div>
                            </div>
                            <div class="card-body">
                                <div class="card-cat">EVRİKA YENİLİK</div>
                                <h3 class="card-title">${n.title}</h3>
                                <p class="card-desc">${n.text}</p>
                                <div class="card-footer">TAM OXU <i class="fas fa-arrow-right"></i></div>
                            </div>
                        </a>
                    `;
                }).join('');
            }
        } catch(e) {}
    });



Whelp("init", {
		app_id: "fdbc088cd36f5d0531bd6672933d00b2"
	});
	
	// Ensure Whelp doesn't auto open on mobile by intercepting its state
	if (window.innerWidth <= 768) {
	    // Poll and force close if it opens automatically without user interaction
	    let userClicked = false;
	    window.addEventListener('touchstart', (e) => { userClicked = true; }, {once: true});
	    let wTimer = setInterval(() => {
	        if (!userClicked && typeof Whelp === 'function') {
	            try { Whelp('close'); } catch(e) {}
	        } else if (userClicked) {
	            clearInterval(wTimer);
	        }
	    }, 300);
	    setTimeout(() => clearInterval(wTimer), 8000);
	}