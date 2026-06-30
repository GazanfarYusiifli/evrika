import re

with open('admin.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update review-score to an input field
score_old = """<textarea class="admin-input exam-review-input" id="review-score" placeholder="Övladınız ... tarixində ... imtahanında ... bal toplayaraq uğur qazanmışdır." style="height:80px; resize:vertical;" oninput="checkExamStatus()"></textarea>"""
score_new = """<input type="number" class="admin-input exam-review-input" id="review-score" placeholder="Şagirdin topladığı balı daxil edin (Məs: 58)" style="width:100%; padding:15px; border-radius:10px; border:1px solid rgba(255,255,255,0.1); background:rgba(0,0,0,0.2); color:white; font-size:16px;" oninput="checkExamStatus()">"""
if score_old in content:
    content = content.replace(score_old, score_new)
else:
    print("Warning: score_old not found!")

# 2. Update sendExamResult for the dynamic string
# In sendExamResult we have:
# <h3 style="color:#0f172a; border-bottom:1px solid #e2e8f0; padding-bottom:8px; font-size:18px;">Şagirdin İmtahan Balı</h3>
# <p style="white-space:pre-wrap; font-size:15px; line-height:1.6; color:#334155;">${rev.score || 'Rəy yoxdur'}</p>

pdf_old = """                    <h3 style="color:#0f172a; border-bottom:1px solid #e2e8f0; padding-bottom:8px; font-size:18px;">Şagirdin İmtahan Balı</h3>
                    <p style="white-space:pre-wrap; font-size:15px; line-height:1.6; color:#334155;">${rev.score || 'Rəy yoxdur'}</p>"""
pdf_new = """                    <h3 style="color:#0f172a; border-bottom:1px solid #e2e8f0; padding-bottom:8px; font-size:18px;">Şagirdin İmtahan Balı</h3>
                    <p style="white-space:pre-wrap; font-size:15px; line-height:1.6; color:#334155;">${rev.score ? `Övladınız ${fullName} Evrika Liseyində keçirilən ${className} üzrə qəbul imtahanında (maksimum 90 bal, keçid balı 45) ${rev.score} bal toplayaraq uğur qazanmışdır.` : 'Rəy yoxdur'}</p>"""
if pdf_old in content:
    content = content.replace(pdf_old, pdf_new)
else:
    print("Warning: pdf_old not found!")

# 3. Add dash-last-payer to the dashboard stats-grid
dash_old = """        <div class="ems-stat-card" style="--accent: var(--success);">
            <div class="ems-stat-icon"><i class="fas fa-ticket-alt"></i></div>
            <div class="stat-lab">Kupon Alan Sayı</div>
            <div class="stat-val" id="dash-ugur">0</div>
        </div>
      </div>"""
dash_new = """        <div class="ems-stat-card" style="--accent: var(--success);">
            <div class="ems-stat-icon"><i class="fas fa-ticket-alt"></i></div>
            <div class="stat-lab">Kupon Alan Sayı</div>
            <div class="stat-val" id="dash-ugur">0</div>
        </div>
        <div class="ems-stat-card" style="--accent: #10b981;">
            <div class="ems-stat-icon"><i class="fas fa-hand-holding-usd"></i></div>
            <div class="stat-lab">Son Ödəniş Edən</div>
            <div class="stat-val" id="dash-last-payer" style="font-size:1.1rem; line-height:1.2;">Yüklənir...</div>
        </div>
      </div>"""
if dash_old in content:
    content = content.replace(dash_old, dash_new)
else:
    print("Warning: dash_old not found!")

# 4. Update renderDashboard to populate dash-last-payer
render_old = """      if(document.getElementById('dash-vac')) document.getElementById('dash-vac').innerText = vacanciesData.filter(v => v.status === 'Aktiv').length || vacanciesData.length;
      
      updateCharts();"""
render_new = """      if(document.getElementById('dash-vac')) document.getElementById('dash-vac').innerText = vacanciesData.filter(v => v.status === 'Aktiv').length || vacanciesData.length;
      
      if(document.getElementById('dash-last-payer')) {
         const latestPayment = rawData.filter(i => (i.epoint_amount || i.amount) && i.payment_status === 'Ödənilib')
                                     .sort((a,b) => new Date(b.epoint_date || b.submissionDate || 0) - new Date(a.epoint_date || a.submissionDate || 0))[0];
         if(latestPayment) {
             const name = latestPayment.fullName || latestPayment['Ad Soyad'] || latestPayment.name || (latestPayment['[2.Şagird] Adı'] ? latestPayment['[2.Şagird] Adı'] + ' ' + (latestPayment['[2.Şagird] Soyadı']||'') : 'Adsız');
             const amt = parseFloat(String(latestPayment.epoint_amount || latestPayment.amount).replace(/[^0-9.]/g, '')) || 0;
             document.getElementById('dash-last-payer').innerHTML = `${name} <br><small style="opacity:0.6; font-size:0.8rem;">(${amt} AZN)</small>`;
         } else {
             document.getElementById('dash-last-payer').innerText = 'Yoxdur';
         }
      }
      
      updateCharts();"""
if render_old in content:
    content = content.replace(render_old, render_new)
else:
    print("Warning: render_old not found!")

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated admin.html with score inputs and last payer widget")
