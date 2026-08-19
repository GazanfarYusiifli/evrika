

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

window.currentRegistrationId = null;
        window.currentPayloadData = null;

        (function() {
          var mainForm = document.getElementById('branchContactForm');
          var paymentAlert = document.getElementById('paymentAlert');

          if (mainForm) {
            var inputs = mainForm.querySelectorAll('input[required], select[required]');
            
            function checkFormFields() {
              var allFilled = true;
              inputs.forEach(function(input) {
                if (!input.value.trim()) {
                  allFilled = false;
                }
              });

              var classSelect = document.getElementById('mf_class');
              var amountText = '35 AZN';
              if (classSelect && classSelect.value === 'Məktəbəqədər') {
                amountText = '25 AZN';
              }
              
              var textContainer = paymentAlert.querySelector('.alert-text');
              if (textContainer) {
                textContainer.innerHTML = '<strong>Diqqət:</strong> Qəbul imtahanında iştirak etmək və buraxılış kuponunu əldə etmək üçün onlayn ödəniş tələb olunur:<br>&bull; Məktəbəqədər - 25 AZN<br>&bull; 1-11 siniflər - 35 AZN';
              }

              if (allFilled) {
                paymentAlert.style.display = 'flex';
              } else {
                paymentAlert.style.display = 'none';
              }
            }

            inputs.forEach(function(input) {
              input.addEventListener('input', checkFormFields);
              input.addEventListener('change', checkFormFields);
            });

            mainForm.addEventListener('submit', async function(event) {
              event.preventDefault();
              var btn = event.target.querySelector('button[type="submit"]');
              var originalBtnContent = btn.innerHTML;
              btn.disabled = true;
              btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> GÖNDƏRİLİR...';

              var firstName = document.getElementById('mf_firstName').value;
              var lastName = document.getElementById('mf_lastName').value;
              var sectorText = document.getElementById('mf_sector').value;
              var grade = document.getElementById('mf_class').value;
              var phoneNum = document.getElementById('mf_phoneNum').value;
              var email = document.getElementById('mf_email').value;
              var currentClass = document.getElementById('mf_currentClass') ? document.getElementById('mf_currentClass').value : '';
              var currentSector = document.getElementById('mf_currentSector') ? document.getElementById('mf_currentSector').value : '';
              var previousSchool = document.getElementById('mf_previousSchool').value;

              // Həqiqi qiymətlərə keçid
              var amountNum = (grade === 'Məktəbəqədər' || grade === 'Məktəbəqədər (5-6 yaş)') ? '25' : '35';

              var note = "Filial: EVRİKA Beynəlxalq<br>Elm və Texnologiya Liseyi<br>(Nərimanov filialı) | Bölmə: " + sectorText + " | Sinif: " + grade + " | E-mail: " + email + " | Əvvəlki müəssisə: " + previousSchool + " | Hazırda oxuduğu sinif: " + currentClass + " | Hazırda oxuduğu bölmə: " + currentSector + " | Ödəniş Məbləği: " + amountNum + " AZN";

              var payloadData = {
                utm_source: sessionStorage.getItem('utm_source') || "",
                utm_medium: sessionStorage.getItem('utm_medium') || "",
                utm_campaign: sessionStorage.getItem('utm_campaign') || "",
                utm_term: sessionStorage.getItem('utm_term') || "",
                utm_content: sessionStorage.getItem('utm_content') || "",
                name: firstName + " " + lastName,
                phone: "+994" + phoneNum,
                source: "Qeydiyyat - Nərimanov filialı",
                status: "Yeni",
                payment_status: "Ödənilməyib",
                amount: amountNum + " AZN",
                note: note,
                date: new Date().toISOString()
              };

              try {
                const res = await fetch('https://gziuhrlvagflokivfgwt.supabase.co/rest/v1/registrations', {
                  method: 'POST',
                  headers: {
                    'apikey': 'sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP',
                    'Authorization': 'Bearer sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP',
                    'Content-Type': 'application/json',
                    'Prefer': 'return=representation'
                  },
                  body: JSON.stringify({ payload: payloadData })
                });
                
                const data = await res.json();
                if(data && data.length > 0) {
                    window.currentRegistrationId = data[0].id;
                    window.currentPayloadData = payloadData;
                }
                
                // amountNum artıq yuxarıda təyin edilib
                
                btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> ÖDƏNİŞƏ YÖNLƏNDİRİLİR...';
                
                try {
                  const epointRes = await fetch('/api/epoint', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                      amount: parseFloat(amountNum),
                      order_id: "EV-" + String(data[0].id).padStart(4, '0'), 
                      description: "Evrika BETL Nərimanov | Şagird: " + firstName + " " + lastName + " | Sinif: " + grade + " | Tel: +994" + phoneNum + " | Sifariş №: EV-" + String(data[0].id).padStart(4, '0'),
                      regId: data[0].id,
                      email: email,
                      name: firstName + ' ' + lastName
                    })
                  });

                  const epointData = await epointRes.json();
                  
                  if (epointData.redirect_url) {
                      localStorage.setItem('last_regId', data[0].id);
                      localStorage.setItem('last_email', email);
                      localStorage.setItem('last_name', firstName + ' ' + lastName);
                      localStorage.setItem('last_epoint_transaction', epointData.transaction);
                      window.location.href = epointData.redirect_url;
                  } else {
                      alert('Ödəniş sistemində xəta baş verdi: ' + (epointData.message || epointData.error || 'Bilinməyən xəta'));
                      btn.disabled = false;
                      btn.innerHTML = originalBtnContent;
                  }
                } catch(epointErr) {
                  console.error(epointErr);
                  alert('Ödəniş xidməti ilə əlaqə qurulmadı. Zəhmət olmasa Vercel serverinizi yoxlayın.');
                  btn.disabled = false;
                  btn.innerHTML = originalBtnContent;
                }
                
              } catch(e) {
                alert('Sistem xətası baş verdi. Yenidən cəhd edin.');
                btn.disabled = false;
                btn.innerHTML = originalBtnContent;
              }
            });
          }
        })();

function toggleMobileAcc(id) {
      var el = document.getElementById(id);
      if (!el) return;
      el.classList.toggle('open');
    }



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