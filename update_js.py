import re

with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_js = """    window.renderFinance = () => {
        const historyTb = document.getElementById('finance-history-tbody');
        const shortTb = document.getElementById('finance-short-tbody');
        
        if(!historyTb || !shortTb) return;
        
        const payments = rawData.filter(i => i.epoint_amount || (i.amount && i.payment_status === 'Ödənilib'))
                                .sort((a,b) => new Date(b.epoint_date || b.submissionDate || 0) - new Date(a.epoint_date || a.submissionDate || 0));
        
        const historyHtml = payments.map(p => {
            const fullName = p.fullName || p['Ad Soyad'] || p.name || (p['[2.Şagird] Adı'] ? p['[2.Şagird] Adı'] + ' ' + (p['[2.Şagird] Soyadı']||'') : 'Adsız');
            const description = p.description || 'Təhsil Ödənişi';
            
            const cardBrand = (p.epoint_card_type || 'BANK KARTI').toUpperCase();
            let brandIcon = 'fas fa-credit-card';
            if(cardBrand.includes('VISA')) brandIcon = 'fab fa-cc-visa';
            else if(cardBrand.includes('MASTER')) brandIcon = 'fab fa-cc-mastercard';
            
            const cardLast4 = p.epoint_card_number ? p.epoint_card_number : '**** **** **** ****';
            const payMethod = p.epoint_bank || 'Epoint Onlayn Ödəniş';
            const rrn = p.epoint_transaction || '---';
            const executedBy = p.executed_by || 'API';
            const amount = p.epoint_amount || p.amount || 0;
            const commission = p.epoint_commission || (Number(amount)*0.02).toFixed(2);
            const date = p.epoint_date ? new Date(p.epoint_date).toLocaleString('az') : new Date(p.submissionDate || Date.now()).toLocaleString('az');
            
            return `<tr>
              <td>
                <div style="font-weight:800; font-size:0.9rem; color:white;">${fullName}</div>
                <div style="font-size:0.7rem; color:var(--text-muted); opacity:0.8; margin-top:3px;">${description}</div>
              </td>
              <td>
                <div style="display:flex; align-items:center; gap:12px;">
                  <i class="${brandIcon}" style="font-size:1.8rem; color:var(--text-muted); opacity:0.8;"></i>
                  <div>
                    <div style="font-size:0.85rem; font-weight:800; letter-spacing:1px; font-family:monospace;">${cardLast4}</div>
                    <div style="font-size:0.65rem; color:var(--text-muted); text-transform:uppercase; margin-top:2px;">${cardBrand} | ${payMethod}</div>
                  </div>
                </div>
              </td>
              <td>
                <div style="font-weight:900; font-size:1rem; color:var(--success);">${amount} <span style="font-size:0.75rem;">₼</span></div>
                <div style="font-size:0.65rem; color:var(--text-muted); margin-top:3px;">Komissiya: <span style="color:var(--warning); font-weight:700;">${commission} ₼</span></div>
              </td>
              <td>
                <div style="font-size:0.8rem; font-weight:700; color:white; font-family:monospace;">RRN: ${rrn}</div>
                <div style="font-size:0.7rem; font-weight:600; color:var(--text-muted); margin-top:3px;">${date}</div>
              </td>
              <td>
                <div style="font-size:0.75rem; font-weight:800; color:white; text-transform:uppercase;">EPOINT MÜHƏRRİKİ</div>
                <div style="font-size:0.65rem; color:var(--success); margin-top:3px;"><i class="fas fa-check-circle"></i> Uğurlu</div>
              </td>
            </tr>`;
        }).join('');
        
        const shortHtml = payments.slice(0, 5).map(p => {
            const fullName = p.fullName || p['Ad Soyad'] || p.name || 'Adsız';
            const amount = p.epoint_amount || p.amount || 0;
            const date = p.epoint_date ? new Date(p.epoint_date).toLocaleString('az') : new Date(p.submissionDate || Date.now()).toLocaleString('az');
            return `<tr>
              <td><div style="font-weight:700; color:white;">${fullName}</div></td>
              <td><div style="color:var(--success); font-weight:800;">${amount} ₼</div></td>
              <td><div style="color:var(--text-muted); font-size:0.8rem;">${date}</div></td>
            </tr>`;
        }).join('');
        
        historyTb.innerHTML = historyHtml;
        shortTb.innerHTML = shortHtml;
        
        const total = payments.reduce((sum, p) => sum + Number(p.epoint_amount || p.amount || 0), 0);
        const totalCommission = payments.reduce((sum, p) => sum + Number(p.epoint_commission || (Number(p.epoint_amount||p.amount||0)*0.02)), 0);
        
        const monthlyIncomeEl = document.getElementById('finance-monthly-income');
        const commEl = document.getElementById('finance-commission');
        const txEl = document.getElementById('finance-tx-count');
        
        if(monthlyIncomeEl) monthlyIncomeEl.innerHTML = `${total.toFixed(2)} <small style="font-size:1.2rem; opacity:0.4;">AZN</small>`;
        if(commEl) commEl.innerHTML = `${totalCommission.toFixed(2)} <small style="font-size:1.2rem; opacity:0.4;">AZN</small>`;
        if(txEl) txEl.innerHTML = `${payments.length} <small style="font-size:0.8rem; font-weight:normal; opacity:0.6;">Ədəd</small>`;
    };"""

html = re.sub(r'window\.renderFinance\s*=\s*\(\)\s*=>\s*\{.*?(?=window\.switchTab\s*=)', new_js + '\n\n    ', html, flags=re.DOTALL)

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(html)
