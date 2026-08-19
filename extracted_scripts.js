





!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '854979317627172');
fbq('track', 'PageView');

(function() {
    var params = new URLSearchParams(window.location.search);
    var utms = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'];
    utms.forEach(function(utm) {
        if (params.has(utm)) {
            sessionStorage.setItem(utm, params.get(utm));
        }
    });
})();

window.onerror = function(msg, url, line, col, err) {
        alert("SİSTEM XƏTASI: " + msg + " \nSətir: " + line);
        return false;
    };

    function toggleTheme() {
        const html = document.documentElement;
        const icon = document.getElementById('theme-icon');
        if (html.getAttribute('data-theme') === 'light') {
            html.removeAttribute('data-theme');
            icon.className = 'fas fa-sun';
            icon.nextElementSibling.innerText = 'Aydınlıq Modu';
            localStorage.setItem('evrika_admin_theme', 'dark');
        } else {
            html.setAttribute('data-theme', 'light');
            icon.className = 'fas fa-moon';
            icon.nextElementSibling.innerText = 'Qaranlıq Mod';
            localStorage.setItem('evrika_admin_theme', 'light');
        }
    }

    if (localStorage.getItem('evrika_admin_theme') === 'light') {
        document.documentElement.setAttribute('data-theme', 'light');
        window.addEventListener('DOMContentLoaded', () => {
            const icon = document.getElementById('theme-icon');
            if(icon) {
                icon.className = 'fas fa-moon';
                icon.nextElementSibling.innerText = 'Qaranlıq Mod';
            }
        });
    }


    let savedPass = localStorage.getItem('evrika_admin_passwords');
    let MODULE_PASSORDS = savedPass ? JSON.parse(savedPass) : { 'crm':'crm123', 'hr':'hr123', 'finance':'fin123', 'site':'site123', 'exam':'exam123' };

    setTimeout(() => {
        if(document.getElementById('setting-pass-crm')) {
            document.getElementById('setting-pass-crm').value = MODULE_PASSORDS['crm'] || 'crm123';
            document.getElementById('setting-pass-hr').value = MODULE_PASSORDS['hr'] || 'hr123';
            document.getElementById('setting-pass-finance').value = MODULE_PASSORDS['finance'] || 'fin123';
            document.getElementById('setting-pass-site').value = MODULE_PASSORDS['site'] || 'site123';
            document.getElementById('setting-pass-exam').value = MODULE_PASSORDS['exam'] || 'exam123';
        }
    }, 500);

    window.saveAdminPasswords = () => {
        MODULE_PASSORDS['crm'] = document.getElementById('setting-pass-crm').value || 'crm123';
        MODULE_PASSORDS['hr'] = document.getElementById('setting-pass-hr').value || 'hr123';
        MODULE_PASSORDS['finance'] = document.getElementById('setting-pass-finance').value || 'fin123';
        MODULE_PASSORDS['site'] = document.getElementById('setting-pass-site').value || 'site123';
        MODULE_PASSORDS['exam'] = document.getElementById('setting-pass-exam').value || 'exam123';
        localStorage.setItem('evrika_admin_passwords', JSON.stringify(MODULE_PASSORDS));
        showSettingsStatus('Şifrələr uğurla yadda saxlanıldı!', '#10b981');
    };
    let currentModuleKey = '';

    window.unlockModule = (mk) => {
        currentModuleKey = mk;
        const overlay = document.getElementById('hub-login-overlay');
        const icon = document.getElementById('login-icon');
        const title = document.getElementById('login-title');
        const input = document.getElementById('hub-pass-input');
        
        const config = {
            'crm': { name: 'CRM & ANALİTİKA', icon: 'fa-layer-group', color: '#ef4444' },
            'hr': { name: 'HR PANEL', icon: 'fa-user-tie', color: '#3b82f6' },
            'finance': { name: 'FİNANS PANEL', icon: 'fa-chart-line', color: '#10b981' },
            'site': { name: 'SAYT İDARƏETMƏ', icon: 'fa-magic', color: '#f59e0b' },
            'exam': { name: 'İMTAHAN PANELİ', icon: 'fa-file-signature', color: '#8b5cf6' }
        };

        const c = config[mk];
        document.documentElement.style.setProperty('--accent', c.color);
        icon.innerHTML = `<i class="fas ${c.icon}"></i>`;
        title.innerText = c.name;
        overlay.style.display = 'flex';
        input.value = '';
        input.focus();
        document.getElementById('login-error').style.opacity = '0';
    };

    window.closeHubLogin = () => {
        document.getElementById('hub-login-overlay').style.display = 'none';
    };

    window.attemptUnlock = () => {
        const pass = document.getElementById('hub-pass-input').value;
        const card = document.getElementById('login-card');
        const error = document.getElementById('login-error');

        if (pass === MODULE_PASSORDS[currentModuleKey]) {
            overlaySuccessfulLogin();
        } else {
            error.style.opacity = '1';
            card.style.animation = 'loginShake 0.4s ease';
            setTimeout(() => card.style.animation = '', 400);
        }
    };

    function overlaySuccessfulLogin() {
        const mk = currentModuleKey;
        document.getElementById('hub-login-overlay').style.opacity = '0';
        document.getElementById('ems-hub').style.opacity = '0';
        
        // Filter sidebar links/titles for the specific module
        document.querySelectorAll('[data-module]').forEach(el => {
            el.style.display = (el.getAttribute('data-module') === mk ? 'flex' : 'none');
        });

        setTimeout(() => {
            document.getElementById('hub-login-overlay').style.display='none';
            document.getElementById('ems-hub').style.display='none';
            document.getElementById('main-sidebar').style.display='flex';
            const startTabs = { 'crm':'dashboard', 'hr':'hr-panel', 'finance':'finance', 'site':'ugurlar', 'exam':'exam-results' };
            switchTab(startTabs[mk]);
            loadData();
            loadManagement();
        }, 500);
    }

    // Enter key support
    document.getElementById('hub-pass-input').addEventListener('keypress', (e) => {
        if (e.key === 'Enter') attemptUnlock();
    });

    const API_URL='https://gziuhrlvagflokivfgwt.supabase.co/rest/v1', API_KEY='sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP', HEADERS={ 'apikey':API_KEY, 'Authorization':'Bearer '+API_KEY, 'Content-Type':'application/json' };
    let rawData=[], filteredData=[], vacanciesData=[], newsData=[], ugurlarData=[], rawCalls=[], tasksData=JSON.parse(localStorage.getItem('evrika_tasks'))||[];

    // --- CALL CENTER LOGIC ---
    let supabaseClient = null;
    if (window.supabase) {
        supabaseClient = window.supabase.createClient('https://gziuhrlvagflokivfgwt.supabase.co', API_KEY);
    }
    
    window.fetchCalls = async () => {
        try {
            const res = await fetch(`${API_URL}/calls?select=*&order=created_at.desc`, { headers: HEADERS });
            if (res.ok) {
                rawCalls = await res.json();
                renderCalls();
            }
        } catch (e) { console.error("Error fetching calls", e); }
    };
    
    window.renderCalls = () => {
        if (!document.getElementById('calls-tbody')) return;
        let today = 0, answered = 0, missed = 0, totalDur = 0;
        const todayStr = new Date().toISOString().split('T')[0];
        
        let html = '';
        rawCalls.forEach(c => {
            const isToday = (c.created_at || '').startsWith(todayStr);
            if (isToday) today++;
            if (c.status === 'completed') { answered++; totalDur += c.duration || 0; }
            if (c.status === 'missed') missed++;
            
            let statusHtml = '';
            if(c.status === 'ringing') statusHtml = `<span style="background:rgba(59,130,246,0.1); color:#3b82f6; padding:4px 8px; border-radius:6px;"><i class="fas fa-bell fa-shake"></i> Zəng gəlir...</span>`;
            else if(c.status === 'completed') statusHtml = `<span style="background:rgba(16,185,129,0.1); color:#10b981; padding:4px 8px; border-radius:6px;"><i class="fas fa-check"></i> Cavablandırıldı</span>`;
            else if(c.status === 'missed') statusHtml = `<span style="background:rgba(239,68,68,0.1); color:#ef4444; padding:4px 8px; border-radius:6px;"><i class="fas fa-phone-slash"></i> Buraxılmış</span>`;
            else statusHtml = `<span style="background:rgba(255,255,255,0.1); padding:4px 8px; border-radius:6px;">${c.status}</span>`;
            
            let name = c.customer_name || 'Naməlum Müştəri';
            if (name === 'Naməlum Müştəri' && window.allFetchedData) {
                // Try to lookup
                const p = c.phone.replace(/[^0-9]/g, '');
                const found = window.allFetchedData.find(d => (d.phone && d.phone.replace(/[^0-9]/g,'') === p) || (d['Valideynin Nömrəsi'] && String(d['Valideynin Nömrəsi']).replace(/[^0-9]/g,'') === p));
                if (found) name = found.fullName || found.name || found['Ad Soyad'] || name;
            }
            
            const rec = c.recording_url ? `<a href="${c.recording_url}" target="_blank" style="color:var(--accent);"><i class="fas fa-play-circle"></i> Dinlə</a>` : '-';
            
            html += `<tr>
                <td><div style="font-weight:800; color:white;">${name}</div><div style="font-family:monospace; color:var(--text-muted); font-size:0.8rem;">${c.phone}</div></td>
                <td>${statusHtml}</td>
                <td><div style="font-weight:800;">${c.duration} san</div></td>
                <td><div style="color:var(--text-muted); font-size:0.8rem;">${new Date(c.created_at).toLocaleString('az')}</div></td>
                <td>${rec}</td>
            </tr>`;
        });
        
        document.getElementById('calls-tbody').innerHTML = html || '<tr><td colspan="5" style="text-align:center;">Zəng yoxdur</td></tr>';
        document.getElementById('calls-today').innerText = today;
        document.getElementById('calls-answered').innerText = answered;
        document.getElementById('calls-missed').innerText = missed;
        document.getElementById('calls-avg-duration').innerText = answered > 0 ? Math.round(totalDur / answered) + ' san' : '0 san';
    };
    
    // Setup Supabase Realtime
    if (supabaseClient) {
        supabaseClient.channel('calls-channel')
            .on('postgres_changes', { event: 'INSERT', schema: 'public', table: 'calls' }, payload => {
                rawCalls.unshift(payload.new);
                renderCalls();
                if (payload.new.status === 'ringing') {
                    document.getElementById('incoming-call-popup').style.display = 'block';
                    document.getElementById('call-popup-number').innerText = payload.new.phone;
                    document.getElementById('call-popup-name').innerText = 'Daxil olan zəng (Twilio/Zadarma)';
                    let audio = new Audio('https://actions.google.com/sounds/v1/alarms/phone_ringing.ogg');
                    audio.play().catch(e => {}); // Ignore play preventions
                }
            })
            .on('postgres_changes', { event: 'UPDATE', schema: 'public', table: 'calls' }, payload => {
                const idx = rawCalls.findIndex(c => c.provider_call_id === payload.new.provider_call_id);
                if (idx !== -1) {
                    rawCalls[idx] = payload.new;
                    renderCalls();
                    if (payload.new.status === 'completed' || payload.new.status === 'missed') {
                        document.getElementById('incoming-call-popup').style.display = 'none';
                    }
                }
            })
            .subscribe();
    }
    // --- END CALL CENTER LOGIC ---

    const statusMap = { 'Yeni': { color:'#f59e0b', bg:'rgba(245,158,11,0.1)' }, 'Baxılıb': { color:'#3b82f6', bg:'rgba(59,130,246,0.1)' }, 'Əlaqə': { color:'#8b5cf6', bg:'rgba(139,92,246,0.1)' }, 'Qəbul': { color:'#10b981', bg:'rgba(16,185,129,0.1)' }, 'İmtina': { color:'#ef4444', bg:'rgba(239,68,68,0.1)' } };

    function getGranularSource(item) {
      if(!item) return 'Bilinmir';
      let s = item.source;
      if (s === 'Qeydiyyat - Montessori') s = 'Qeydiyyat - Montessori Kids';
      // Aggressive keyword scan across all application fields
      if (!s || s === 'Vebsayt' || s === 'Veb' || s === 'Naməlum' || s === 'Əlaqə Səhifəsi') {
        const allText = Object.values(item).join(' ').toLowerCase();
        if (allText.includes('liseyi 1') || allText.includes('lisey 1')) s = 'lisey1';
        else if (allText.includes('liseyi 2') || allText.includes('lisey 2')) s = 'lisey2';
        else if (allText.includes('montessori')) s = 'montessori';
        else if (allText.includes('victory') || allText.includes('eduhome')) s = 'victory';
        else if (allText.includes('zümrüd') || allText.includes('zumrud')) s = 'zumrud';
        else if (allText.includes('əlaqə') || allText.includes('contact')) s = 'contact';
        else if (allText.includes('whatsapp')) s = 'whatsapp';
        else if (allText.includes('instagram')) s = 'instagram';
        else if (allText.includes('linkedin')) s = 'linkedin';
        else if (allText.includes('facebook')) s = 'facebook';
      }
      if (item.position) s = 'career';
      return s;
    }

    async function loadData() {
      try {
        const res = await fetch(`${API_URL}/registrations?select=*&order=id.desc`, { headers: HEADERS });
        if(res.ok) { 
            let fetchedData = (await res.json()).map(r => ({ ...r.payload, _db_id_: r.id, created_at: r.created_at })); 
            window.allFetchedData = fetchedData;
            rawData = fetchedData.filter(r => {
                // Əgər ödənişli müraciətdirsə və hələ ödənilməyibsə, CRM-ə düşməsin
                if ((r.amount || r.epoint_amount || r.epoint_transaction) && r.payment_status !== 'Ödənilib') return false;
                if (r.is_scan_log) return false;
                return true;
            });
            filteredData = [...rawData]; 
            
            // Calculate new apps badge
            const newCount = rawData.filter(item => (item.status || '').toLowerCase() === 'yeni').length;
            const badge = document.getElementById('new-apps-badge');
            if (badge) {
                if (newCount > 0) {
                    badge.innerText = newCount;
                    badge.style.display = 'inline-block';
                } else {
                    badge.style.display = 'none';
                }
            }
        }
      } catch(e) {}
      renderDashboard(); renderApps(); renderFinance(); renderVacancyApps(); loadUgurlar(); loadVacancies(); loadNews(); loadManagement(); loadMezunlar();
    }

    window.filterData = () => {
      const q = document.getElementById('search-input').value.toLowerCase();
      const source = document.getElementById('filter-source').value;
      const status = document.getElementById('filter-status').value;

      filteredData = rawData.filter(item => {
        const fullName = (item.fullName || item['Ad Soyad'] || item.name || 
                          item['[1.Əlaqə] Valideyn Adı'] || 
                          (item['[2.Şagird] Adı'] ? item['[2.Şagird] Adı'] + ' ' + (item['[2.Şagird] Soyadı'] || '') : '') ||
                          'Adsız').toLowerCase();
        
        const phone = (item.phone || item.tel || item['[1.Əlaqə] Əlaqə Nömrəsi'] || '').toLowerCase();
        
        const matchesSearch = fullName.includes(q) || phone.includes(q);
        
        let s = getGranularSource(item);
        const MAP = { 
          'lisey1':'Nərimanov filialı', 'lisey2':'Gənclik filialı', 'montessori':'Montessori', 
          'victory':'Victory', 'zumrud':'Zümrüd', 'contact':'Əlaqə', 
          'career':'Karyera', 'whatsapp':'WhatsApp', 'instagram':'Instagram', 'email':'Email' 
        };
        const sourceLabel = MAP[s] || s || 'Email';
        
        let matchesSource = true;
        if (source !== 'all') {
          if (source === 'Vebsayt') {
            matchesSource = ['Nərimanov filialı', 'Gənclik filialı', 'Montessori', 'Victory', 'Zümrüd', 'Əlaqə', 'Email'].includes(sourceLabel);
          } else if (source === 'Karyera') {
            matchesSource = sourceLabel === 'Karyera';
          }
        }
        
        let matchesStatus = true;
        if (status !== 'all') {
           matchesStatus = (item.status || 'Yeni') === status;
        }
        
        return matchesSearch && matchesSource && matchesStatus;
      });
      renderApps();
    };

    window.exportToCSV = () => {
      if (filteredData.length === 0) return alert('Export etmək üçün məlumat yoxdur!');
      
      const csvRows = [];
      const headers = ['ID', 'Ad Soyad', 'Telefon', 'Mənbə', 'Tarix', 'Status'];
      csvRows.push(headers.join(','));
      
      filteredData.forEach(item => {
        const id = 'EV-' + String(item._db_id_).padStart(4,'0');
        const fullName = (item.fullName || item['Ad Soyad'] || item.name || 
                          item['[1.Əlaqə] Valideyn Adı'] || 
                          (item['[2.Şagird] Adı'] ? item['[2.Şagird] Adı'] + ' ' + (item['[2.Şagird] Soyadı'] || '') : '') ||
                          'Adsız').replace(/,/g, '');
        const phone = (item.phone || item.tel || item['[1.Əlaqə] Əlaqə Nömrəsi'] || '-').replace(/,/g, '');
        
        const s = getGranularSource(item);
        const MAP = { 
          'lisey1':'Nərimanov filialı', 'lisey2':'Gənclik filialı', 'montessori':'Montessori', 
          'victory':'Victory', 'zumrud':'Zümrüd', 'contact':'Əlaqə', 
          'career':'Karyera', 'whatsapp':'WhatsApp', 'instagram':'Instagram', 'email':'Email' 
        };
        const sourceLabel = MAP[s] || s || 'Email';
        
        const date = new Date(item.submissionDate || Date.now()).toLocaleDateString('az');
        const st = item.status || 'Yeni';
        
        csvRows.push([id, fullName, phone, sourceLabel, date, st].join(','));
      });
      
      const csvString = "\uFEFF" + csvRows.join("\n");
      const blob = new Blob([csvString], { type: 'text/csv;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.setAttribute('href', url);
      a.setAttribute('download', 'muracietler.csv');
      a.style.visibility = 'hidden';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    };

    function renderApps() {
      const tb = document.getElementById('crm-tbody'); if(!tb) return;
      tb.innerHTML = filteredData.map((item, i) => {
        let st = item.status || 'Yeni';
        if (typeof statusMap !== 'undefined' && !statusMap[st]) st = 'Yeni';
        const s = getGranularSource(item);
        const MAP = { 
          'lisey1':'Nərimanov filialı', 'lisey2':'Gənclik filialı', 'montessori':'Montessori', 
          'victory':'Victory', 'zumrud':'Zümrüd', 'contact':'Əlaqə', 
          'career':'Karyera', 'whatsapp':'WhatsApp', 'instagram':'Instagram', 'email':'Email' 
        };
        const sourceLabel = MAP[s] || s || 'Email';

        // Robust name extraction
        const fullName = item.fullName || item['Ad Soyad'] || item.name || 
                        item['[1.Əlaqə] Valideyn Adı'] || 
                        (item['[2.Şagird] Adı'] ? item['[2.Şagird] Adı'] + ' ' + (item['[2.Şagird] Soyadı'] || '') : null) ||
                        'Adsız';
        
        // Robust phone extraction
        const phone = item.phone || item.tel || item['[1.Əlaqə] Əlaqə Nömrəsi'] || '-';

        const utmCampaign = item.utm_campaign || '-';

        return `<tr>
          <td>
            <div style="font-weight:800; color:white; font-size:0.95rem;">${fullName}</div>
            <div style="font-size:0.7rem; color:var(--text-muted); opacity:0.7;">ID: #EV-${String(item._db_id_).padStart(4,'0')}</div>
          </td>
          <td style="font-weight:600; font-size:0.9rem;">${phone}</td>
          <td><span class="kanban-card-tag" style="background:rgba(139,26,43,0.1); color:var(--burgundy); border:1px solid rgba(139,26,43,0.2); padding:6px 12px; border-radius:8px; font-weight:700;">${sourceLabel}</span></td>
          <td style="font-size:0.85rem; color:var(--accent); font-weight:600;">${utmCampaign}</td>
          <td>${item.payment_status ? `<span style="font-weight:bold; font-size:0.75rem; color:${item.payment_status==='Ödənilib' ? '#10B981' : '#EF4444'}; background:${item.payment_status==='Ödənilib' ? 'rgba(16,185,129,0.1)' : 'rgba(239,68,68,0.1)'}; padding:4px 8px; border-radius:6px;">${item.payment_status}</span>` : '<span style="color:var(--text-muted); font-size:0.8rem;">-</span>'}</td>
          <td style="font-size:0.85rem; color:var(--text-muted);">${new Date(item.created_at || item.submissionDate || Date.now()).toLocaleString('az')}</td>
          <td>
            <select onchange="updateStatus(${i}, this.value)" 
                    style="background:${statusMap[st].bg}; color:${statusMap[st].color}; border:1px solid ${statusMap[st].color}44; cursor:pointer;" 
                    class="status-select">
              ${Object.keys(statusMap).map(s=>`<option value="${s}" ${s===st?'selected':''}>${s}</option>`).join('')}
            </select>
          </td>
          <td><button class="btn-view" onclick="viewDetails(${i})" style="padding:10px 20px;"><i class="fas fa-eye"></i></button></td>
        </tr>`;
      }).join('');
    }

    
    window.switchFinanceTab = (tab) => {
        document.getElementById('finance-view-report').style.display = tab === 'report' ? 'block' : 'none';
        document.getElementById('finance-view-history').style.display = tab === 'history' ? 'block' : 'none';
        
        document.getElementById('btn-tab-report').style.background = tab === 'report' ? 'var(--accent)' : 'rgba(255,255,255,0.05)';
        document.getElementById('btn-tab-report').style.border = tab === 'report' ? 'none' : '1px solid rgba(255,255,255,0.1)';
        
        document.getElementById('btn-tab-history').style.background = tab === 'history' ? 'var(--accent)' : 'rgba(255,255,255,0.05)';
        document.getElementById('btn-tab-history').style.border = tab === 'history' ? 'none' : '1px solid rgba(255,255,255,0.1)';
    };

        window.renderFinance = () => {
        const historyTb = document.getElementById('finance-history-tbody');
        const shortTb = document.getElementById('finance-short-tbody');
        
        if(!historyTb || !shortTb) return;
        
        const payments = rawData.filter(p => p.epoint_amount || (p.amount && p.payment_status === 'Ödənilib'))
                             .sort((a,b) => new Date(b.epoint_date || b.created_at || b.submissionDate || 0) - new Date(a.epoint_date || a.created_at || a.submissionDate || 0));
        
        const historyHtml = payments.map(p => {
            const fullName = p.fullName || p['Ad Soyad'] || p.name || (p['[2.Şagird] Adı'] ? p['[2.Şagird] Adı'] + ' ' + (p['[2.Şagird] Soyadı']||'') : 'Adsız');
            const description = p.description || 'Təhsil Ödənişi';
            
            const cardBrand = (p.epoint_card_type || 'BANK KARTI').toUpperCase();
            let brandIcon = 'fas fa-credit-card';
            if(cardBrand.includes('VISA')) brandIcon = 'fab fa-cc-visa';
            else if(cardBrand.includes('MASTER')) brandIcon = 'fab fa-cc-mastercard';
            
            let cardNum = p.epoint_card_number;
            if(!cardNum && p.epoint_bank_response) {
               const match = String(p.epoint_bank_response).match(/CARD_NUMBER:\s*(\S+)/i);
               if(match) cardNum = match[1];
            }
            const cardLast4 = cardNum ? cardNum : '**** **** **** ****';
            const payMethod = p.epoint_bank || 'Epoint Onlayn Ödəniş';
            const txId = p.epoint_transaction || p.epoint_rrn || '---';
            const executedBy = p.executed_by || 'API';
            const amount = p.epoint_amount || p.amount || 0;
            const parsedAmount = parseFloat(String(amount).replace(/[^0-9.]/g, '')) || 0;
            const commission = p.epoint_commission ? parseFloat(String(p.epoint_commission).replace(/[^0-9.]/g, '')) : parseFloat((parsedAmount * 0.03).toFixed(2));
            const date = p.epoint_date ? new Date(p.epoint_date).toLocaleString('az') : new Date(p.created_at || p.submissionDate || Date.now()).toLocaleString('az');
            
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
                <div style="font-weight:900; font-size:1rem; color:var(--success);">${parsedAmount} <span style="font-size:0.75rem;">₼</span></div>
                <div style="font-size:0.65rem; color:var(--text-muted); margin-top:3px;">Komissiya: <span style="font-weight:700;">₼ 0.00</span></div>
                <div style="font-size:0.65rem; color:var(--text-muted); margin-top:1px;">Epoint Əməliyyat komissiyası: <span style="color:var(--warning); font-weight:700;">₼ ${commission}</span></div>
              </td>
              <td>
                <div style="font-size:0.8rem; font-weight:700; color:white; font-family:monospace;">Sifariş №: EV-${String(p.order_id || p._db_id_ || '').padStart(4, '0')}</div>
                <div style="font-size:0.75rem; font-weight:600; color:var(--text-muted); margin-top:2px;">RRN: ${p.epoint_rrn || txId}</div>
                <div style="font-size:0.65rem; font-weight:600; color:var(--text-muted); margin-top:2px;">${date}</div>
              </td>
                           <td>
                <div style="font-size:0.75rem; font-weight:800; color:white; text-transform:uppercase;">EPOINT MÜHƏRRİKİ</div>
                <div style="font-size:0.65rem; color:var(--success); margin-top:3px;"><i class="fas fa-check-circle"></i> Uğurlu</div>
              </td>
              <td>
                <button class="btn-view" style="padding:10px 15px; font-size:0.7rem; background:rgba(59,130,246,0.1); color:var(--royal-blue); border-color:rgba(59,130,246,0.2);" onclick="openFinanceDetails('${p._db_id_ || p.order_id || p.epoint_transaction}')"><i class="fas fa-eye" style="margin-right:5px;"></i> Detallar</button>
              </td>
            </tr>`;
        }).join('');
        
        const shortHtml = payments.slice(0, 5).map(p => {
            const fullName = p.fullName || p['Ad Soyad'] || p.name || 'Adsız';
            const amount = p.epoint_amount || p.amount || 0;
            const date = p.epoint_date ? new Date(p.epoint_date).toLocaleString('az') : new Date(p.created_at || p.submissionDate || Date.now()).toLocaleString('az');
            return `<tr>
              <td><div style="font-weight:700; color:white;">${fullName}</div></td>
              <td><div style="color:var(--success); font-weight:800;">${amount} ₼</div></td>
              <td><div style="color:var(--text-muted); font-size:0.8rem;">${date}</div></td>
            </tr>`;
        }).join('');
        
        historyTb.innerHTML = historyHtml;
        shortTb.innerHTML = shortHtml;
        
        const total = payments.reduce((sum, p) => sum + (parseFloat(String(p.epoint_amount || p.amount || 0).replace(/[^0-9.]/g, '')) || 0), 0);
        const totalCommission = payments.reduce((sum, p) => sum + (parseFloat(String(p.epoint_commission).replace(/[^0-9.]/g, '')) || (parseFloat(String(p.epoint_amount || p.amount || 0).replace(/[^0-9.]/g, '')) || 0) * 0.03), 0);
        
        const monthlyIncomeEl = document.getElementById('finance-monthly-income');
        const commEl = document.getElementById('finance-commission');
        const txEl = document.getElementById('finance-tx-count');
        
        if(monthlyIncomeEl) monthlyIncomeEl.innerHTML = `${total.toFixed(2)} <small style="font-size:1.2rem; opacity:0.4;">AZN</small>`;
        if(commEl) commEl.innerHTML = `${totalCommission.toFixed(2)} <small style="font-size:1.2rem; opacity:0.4;">AZN</small>`;
        if(txEl) txEl.innerHTML = `${payments.length} <small style="font-size:0.8rem; font-weight:normal; opacity:0.6;">Ədəd</small>`;
    };

    window.renderKupon = () => {
        const tb = document.getElementById('kupon-tbody');
        if(!tb) return;
        
        const branchFilter = document.getElementById('filter-kupon-branch') ? document.getElementById('filter-kupon-branch').value : 'all';
        
        let coupons = rawData.filter(i => (i.epoint_amount || i.amount) && i.payment_status === 'Ödənilib');
        
        if (branchFilter !== 'all') {
            coupons = coupons.filter(i => {
                const s = getGranularSource(i) || '';
                if (branchFilter === 'lisey1') return s === 'lisey1' || s.includes('Nərimanov');
                if (branchFilter === 'lisey2') return s === 'lisey2' || s.includes('Gənclik');
                if (branchFilter === 'montessori') return s === 'montessori' || s.includes('Montessori');
                if (branchFilter === 'victory') return s === 'victory' || s.includes('Victory');
                if (branchFilter === 'zumrud') return s === 'zumrud' || s.includes('Zümrüd') || s.includes('zumrud');
                return s === branchFilter;
            });
        }
        
        coupons = coupons.sort((a,b) => new Date(b.epoint_date || b.created_at || b.submissionDate || 0) - new Date(a.epoint_date || a.created_at || a.submissionDate || 0));

        const MAP = { 
          'lisey1':'Nərimanov filialı', 'lisey2':'Gənclik filialı', 'montessori':'Montessori', 
          'victory':'Victory', 'zumrud':'Zümrüd'
        };

        tb.innerHTML = coupons.map((p, idx) => {
            const fullName = p.fullName || p['Ad Soyad'] || p.name || (p['[2.Şagird] Adı'] ? p['[2.Şagird] Adı'] + ' ' + (p['[2.Şagird] Soyadı']||'') : 'Adsız');
            const amount = p.epoint_amount || p.amount || 0;
            const phone = p.phone || p.tel || p['[1.Əlaqə] Əlaqə Nömrəsi'] || '-';
            const date = p.epoint_date ? new Date(p.epoint_date).toLocaleString('az') : new Date(p.created_at || p.submissionDate || Date.now()).toLocaleString('az');
            
            const s = getGranularSource(p);
            const sourceLabel = MAP[s] || String(s).replace('Qeydiyyat - ', '') || 'Email';
            
            return `<tr>
              <td>
                 <div style="font-weight:800; color:white; font-size:0.9rem;">${fullName}</div>
                 <div style="font-size:0.7rem; color:var(--text-muted); margin-top:3px;">${p.description || 'Sınaq / Təhsil Ödənişi'} <span style="color:var(--warning); margin-left:5px;">• ${sourceLabel}</span></div>
              </td>
              <td>
                 <div style="color:var(--success); font-weight:800; font-size:1rem;">${amount} ₼</div>
                 <div style="font-size:0.7rem; font-family:monospace; color:white; margin-top:3px;">Sifariş №: EV-${String(p.order_id || p._db_id_ || '').replace('EV-', '').padStart(4, '0')}</div>
              </td>
              <td><div style="font-weight:600; font-size:0.85rem;">${phone}</div></td>
              <td><div style="color:var(--text-muted); font-size:0.8rem; font-weight:600;">${date}</div></td>
              <td>
                <div style="display:flex; gap:10px; align-items:center;">
                  <button class="btn-view" style="padding:10px 15px; font-size:0.75rem;" onclick="openFinanceDetails('${p._db_id_ || p.order_id || p.epoint_transaction}')"><i class="fas fa-eye" style="margin-right:5px;"></i> Detallar</button>
                  ${(p.status === 'QR İstifadə Edilib' || p.status === 'İştirak Etdi') ? 
                    `<div style="color:var(--success); font-size:0.8rem; font-weight:800; background:rgba(34,197,94,0.1); padding:8px 12px; border-radius:8px;"><i class="fas fa-check-circle"></i> İçəri Keçib</div>` : 
                    `<button class="btn-view" style="background:var(--success); color:white; border:none; padding:10px 15px; font-size:0.75rem;" onclick="markQrScanned('${p._db_id_}')"><i class="fas fa-qrcode" style="margin-right:5px;"></i> İçəri Keçir</button>`}
                </div>
              </td>
            </tr>`;
        }).join('');
    };

    window.markQrScanned = async (dbId) => {
        if(!confirm("Bu şagirdi içəri keçirmək (QR təsdiqi) istədiyinizə əminsiniz?")) return;
        
        const itemIdx = rawData.findIndex(r => r._db_id_ == dbId);
        if(itemIdx === -1) return alert("Tapılmadı");
        
        let payload = JSON.parse(JSON.stringify(rawData[itemIdx]));
        payload.status = 'QR İstifadə Edilib';
        if(!payload.note) payload.note = "";
        payload.note += " | MANUALLY CHECKED IN: " + new Date().toLocaleString('az');

        try {
            const res = await fetch(`${API_URL}/registrations?id=eq.${dbId}`, {
                method: 'PATCH',
                headers: HEADERS,
                body: JSON.stringify({ payload })
            });
            
            if(res.ok) {
                alert("Uğurla 'İçəri Keçib' olaraq qeyd edildi!");
                rawData[itemIdx].status = 'QR İstifadə Edilib';
                if(!rawData[itemIdx].note) rawData[itemIdx].note = "";
                rawData[itemIdx].note += " | MANUALLY CHECKED IN: " + new Date().toLocaleString('az');
                renderKupon();
            } else {
                alert("Sistem xətası baş verdi.");
            }
        } catch(err) {
            alert("Sistem xətası: " + err.message);
        }
    };

    window.checkEpointStatus = async () => {
        const txId = document.getElementById('epoint-check-id').value.trim();
        if(!txId) return alert("Sifariş № daxil edin");
        
        const pub = "i000201608";
        const pvt = "HNIbtyFLu3PbxXlVykJEwOR1";
        
        let txHash = txId;
        if (txId.startsWith('EV-') || !isNaN(txId)) {
            const parsedId = String(txId).replace('EV-', '').padStart(4, '0');
            const foundItem = rawData.find(r => r.order_id === 'EV-' + parsedId || String(r._db_id_).padStart(4, '0') === parsedId || String(r._db_id_) === txId);
            if (foundItem && foundItem.epoint_transaction) {
                txHash = foundItem.epoint_transaction;
            } else {
                document.getElementById('epoint-result').style.display = 'block';
                document.getElementById('epoint-result').innerHTML = `<div style="color:var(--error); font-weight:800; padding:10px; background:rgba(239,68,68,0.1); border-radius:8px;"><i class="fas fa-exclamation-triangle"></i> Bu sifariş (Sifariş № ${txId}) üçün Epoint tranzaksiya şifrəsi (Hash) tapılmadı. Ödəniş səhifəsi açılmamış və ya yarımçıq qalmış ola bilər.</div>`;
                return;
            }
        }

        const dataObj = { public_key: pub, transaction: txHash };
        const dataJson = JSON.stringify(dataObj);
        const dataB64 = btoa(unescape(encodeURIComponent(dataJson)));
        
        const signString = pvt + dataB64 + pvt;
        
        const msgBuffer = new TextEncoder().encode(signString);
        const hashBuffer = await crypto.subtle.digest('SHA-1', msgBuffer);
        const hashArray = Array.from(new Uint8Array(hashBuffer));
        const signatureStr = btoa(String.fromCharCode.apply(null, hashArray));
        
        document.getElementById('epoint-result').style.display = 'block';
        document.getElementById('epoint-result').innerHTML = '<div style="color:var(--text-muted);"><i class="fas fa-spinner fa-spin"></i> Gözləyin...</div>';
        
        try {
            const formData = new URLSearchParams();
            formData.append('data', dataB64);
            formData.append('signature', signatureStr);
            
            const res = await fetch("https://epoint.az/api/1/get-status", {
                method: "POST",
                headers: { "Content-Type": "application/x-www-form-urlencoded" },
                body: formData.toString()
            });
            const result = await res.json();
            
            let color = 'white';
            if(result.status === 'success') color = 'var(--success)';
            else if(result.status === 'error') color = 'var(--error)';
            
            document.getElementById('epoint-result').innerHTML = `
                <div style="font-size:1.1rem; font-weight:800; color:${color}; margin-bottom:10px;">STATUS: ${result.status ? result.status.toUpperCase() : 'BİLİNMİR'}</div>
                <div style="font-size:0.85rem; color:var(--text-muted); white-space:pre-wrap; background:rgba(0,0,0,0.2); padding:15px; border-radius:8px;">${JSON.stringify(result, null, 2)}</div>
            `;
        } catch(e) {
            document.getElementById('epoint-result').innerHTML = `<div style="color:var(--error); font-weight:800;">Xəta: ${e.message}</div>`;
        }
    };

    window.renderEpointReports = () => {
        const tb = document.getElementById('epoint-reports-tbody');
        if(!tb) return;
        
        const sourceData = window.allFetchedData || rawData;
        const txs = sourceData.filter(i => i.epoint_transaction || i.epoint_amount || i.payment_status)
                           .sort((a,b) => new Date(b.epoint_date || b.created_at || b.submissionDate || 0) - new Date(a.epoint_date || a.created_at || a.submissionDate || 0));
                           
        let totalAmount = 0;
        let totalCount = 0;
        let totalCommission = 0;
        
        tb.innerHTML = txs.map((p, idx) => {
            const fullName = p.fullName || p['Ad Soyad'] || p.name || (p['[2.Şagird] Adı'] ? p['[2.Şagird] Adı'] + ' ' + (p['[2.Şagird] Soyadı']||'') : 'Adsız');
            const amount = parseFloat(String(p.epoint_amount || p.amount || 0).replace(/[^0-9.]/g, '')) || 0;
            const isSuccess = p.payment_status === 'Ödənilib';
            
            const comm = p.epoint_commission ? parseFloat(String(p.epoint_commission).replace(/[^0-9.]/g, '')) : parseFloat((amount * 0.03).toFixed(2));
            if (isSuccess) {
                totalAmount += amount;
                totalCount++;
                totalCommission += comm;
            }
            
            const date = p.epoint_date ? new Date(p.epoint_date).toLocaleString('az') : new Date(p.created_at || p.submissionDate || Date.now()).toLocaleString('az');
            const txId = p.epoint_transaction || '---';
            const rrnCode = p.epoint_rrn || p.rrn || txId;
            const orderId = p.order_id || p._db_id_ || '---';
            
            return `<tr>
              <td>
                 <div style="font-weight:800; color:white; font-size:0.9rem; font-family:monospace;">Sifariş №: EV-${String(orderId).replace('EV-', '').padStart(4, '0')}</div>
                 <div style="font-size:0.7rem; color:var(--text-muted); margin-top:3px; font-family:monospace;">RRN: ${rrnCode}</div>
              </td>
              <td>
                 <div style="font-weight:800; color:white; font-size:0.9rem;">${fullName}</div>
                 <div style="font-size:0.7rem; color:var(--text-muted); margin-top:3px;">${p.description || 'Sınaq / Təhsil Ödənişi'}</div>
              </td>
              <td>
                 <div style="color:${isSuccess ? 'var(--success)' : 'var(--text-muted)'}; font-weight:800; font-size:1rem;">${amount.toFixed(2)} ₼</div>
                 ${isSuccess ? `<div style="font-size:0.65rem; color:var(--text-muted); margin-top:3px;">Komissiya: <span style="font-weight:700;">₼ 0.00</span></div><div style="font-size:0.65rem; color:var(--text-muted); margin-top:1px;">Epoint Əməliyyat komissiyası: <span style="color:var(--warning); font-weight:700;">₼ ${comm.toFixed(2)}</span></div>` : ''}
              </td>
              <td><div style="color:var(--text-muted); font-size:0.8rem; font-weight:600;">${date}</div></td>
              <td>
                 <span style="padding:5px 10px; border-radius:6px; font-size:0.75rem; font-weight:800; ${isSuccess ? 'background:rgba(16,185,129,0.1); color:var(--success);' : 'background:rgba(239,68,68,0.1); color:var(--error);'}">
                    ${isSuccess ? '<i class="fas fa-check-circle"></i> ÖDƏNİLİB' : '<i class="fas fa-times-circle"></i> UĞURSUZ'}
                 </span>
              </td>
            </tr>`;
        }).join('');
        
        document.getElementById('epoint-total-amount').innerText = totalAmount.toFixed(2) + ' ₼';
        document.getElementById('epoint-total-count').innerText = totalCount;
        document.getElementById('epoint-total-commission').innerText = totalCommission.toFixed(2) + ' ₼';
    };

    window.renderExamResults = () => {
        const tbParticipated = document.getElementById('exam-students-list-participated');
        const tbKupon = document.getElementById('exam-students-list-kupon');
        if(!tbParticipated || !tbKupon) return;
        
        // Check for epoint_amount or explicit payment_status
        const allExamStudents = rawData.filter(i => i.epoint_amount || (i.amount && i.payment_status === 'Ödənilib'))
                                   .sort((a,b) => new Date(b.created_at || 0) - new Date(a.created_at || 0));
        
        let doneCount = 0;
        
        const MAP = { 
          'lisey1':'Nərimanov', 'lisey2':'Gənclik', 'montessori':'Montessori', 
          'victory':'Victory', 'zumrud':'Zümrüd'
        };

        const renderRow = (p, isParticipated) => {
            const fullName = p['[2.Şagird] Adı'] ? (p['[2.Şagird] Adı'] + ' ' + (p['[2.Şagird] Soyadı']||'')) : (p['Ad Soyad'] || p.fullName || p.name || p.firstName || p['[1.Əlaqə] Valideyn Adı'] || p['Valideyn'] || 'Adsız Şagird');
            const className = p.Sinif || p['Sinif'] || p.class_name || p['Neçənci sinif üçün imtahan verəcək?'] || (p.note && p.note.match(/Sinif:\s*([^|]+)/) ? p.note.match(/Sinif:\s*([^|]+)/)[1].trim() : 'Qeyd edilməyib');
            const rev = p.exam_reviews || {};
            const isDone = rev.score && rev.academic && rev.psycho;
            
            const s = getGranularSource(p);
            const filial = MAP[s] || String(s).replace('Qeydiyyat - ', '') || 'Bilinmir';

            if (isParticipated && isDone) doneCount++;
            
            return `<div ${isParticipated ? `onclick="loadExamStudent('${p._db_id_}')" style="cursor:pointer;"` : `style="opacity:0.5; pointer-events:none;" title="Yalnız imtahanda iştirak edənlərə rəy yazıla bilər"`} class="exam-student-card" style="display: flex; justify-content: space-between; align-items: center; background: rgba(255,255,255,0.02); border: 1px solid var(--border); padding: 15px; border-radius: 12px; transition: 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.05)'; this.style.transform='translateY(-2px)'" onmouseout="this.style.background='rgba(255,255,255,0.02)'; this.style.transform='none'">
                <div style="flex:1;">
                   <div style="font-weight:800; font-size:1rem; color:white; margin-bottom:8px;">${fullName}</div>
                   <div style="display:flex; gap:10px; font-size:0.8rem; flex-wrap:wrap;">
                       <span style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); padding:4px 10px; border-radius:8px; color:var(--text-muted);"><i class="fas fa-layer-group" style="margin-right:5px; color:var(--burgundy);"></i> ${className}</span>
                       <span style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); padding:4px 10px; border-radius:8px; color:var(--text-muted);"><i class="fas fa-map-marker-alt" style="margin-right:5px; color:var(--royal-blue);"></i> ${filial}</span>
                   </div>
                </div>
                <div style="display:flex; align-items:center; justify-content:center; width:50px;">
                    <span style="color:var(--${isDone ? 'success' : 'warning'}); font-size:1.5rem;" title="${isDone ? 'Tamamlanıb' : 'Gözləyir'}">
                        <i class="fas fa-${isDone ? 'check-circle' : 'clock'}"></i>
                    </span>
                </div>
            </div>`;
        };

        const participated = allExamStudents.filter(i => i.status === 'QR İstifadə Edilib' || i.status === 'İştirak Etdi');
        const kuponOnly = allExamStudents.filter(i => i.status !== 'QR İstifadə Edilib' && i.status !== 'İştirak Etdi');

        tbParticipated.innerHTML = participated.length ? participated.map(p => renderRow(p, true)).join('') : '<div style="text-align:center; padding:20px; color:var(--text-muted);"><i class="fas fa-info-circle"></i> Hələ imtahanda iştirak edən şagird yoxdur.</div>';
        tbKupon.innerHTML = kuponOnly.length ? kuponOnly.map(p => renderRow(p, false)).join('') : '<div style="text-align:center; padding:20px; color:var(--text-muted);"><i class="fas fa-check-circle"></i> Bütün kupon alanlar imtahanda iştirak edib!</div>';
        
        document.getElementById('exam-stat-total').innerText = allExamStudents.length;
        document.getElementById('exam-stat-participated').innerText = participated.length;
        document.getElementById('exam-stat-done').innerText = doneCount;
        document.getElementById('exam-stat-waiting').innerText = participated.length - doneCount;
    };

    window.loadExamStudent = (dbId) => {
        const item = rawData.find(r => r._db_id_ == dbId);
        if(!item) return;
        const panel = document.getElementById('exam-review-panel');
        panel.style.opacity = '1';
        panel.style.pointerEvents = 'all';
        
        const fullName = item['[2.Şagird] Adı'] ? (item['[2.Şagird] Adı'] + ' ' + (item['[2.Şagird] Soyadı']||'')) : (item['Ad Soyad'] || item.fullName || item.name || item.firstName || item['[1.Əlaqə] Valideyn Adı'] || item['Valideyn'] || 'Adsız Şagird');
        document.getElementById('exam-student-name').innerText = fullName;
        document.getElementById('exam-current-student-id').value = dbId;
        
        const rev = item.exam_reviews || {};
        document.getElementById('review-score').value = rev.score || '';
        document.getElementById('review-academic').value = rev.academic || '';
        document.getElementById('review-psycho').value = rev.psycho || '';
        
        window.checkExamStatus();
    };

    window.checkExamStatus = () => {
        const score = document.getElementById('review-score').value.trim();
        const academic = document.getElementById('review-academic').value.trim();
        const psycho = document.getElementById('review-psycho').value.trim();
        
        document.getElementById('status-score').innerText = score ? 'Yazılıb' : 'Gözləyir';
        document.getElementById('status-score').style.background = score ? 'var(--success)' : 'var(--warning)';
        
        document.getElementById('status-academic').innerText = academic ? 'Yazılıb' : 'Gözləyir';
        document.getElementById('status-academic').style.background = academic ? 'var(--success)' : 'var(--warning)';
        
        document.getElementById('status-psycho').innerText = psycho ? 'Yazılıb' : 'Gözləyir';
        document.getElementById('status-psycho').style.background = psycho ? 'var(--success)' : 'var(--warning)';
        
        const btns = document.querySelectorAll('.exam-send-btn');
        if (score && academic && psycho) {
            btns.forEach(btn => {
                btn.disabled = false;
                btn.style.background = 'var(--success)';
                btn.style.color = 'white';
                btn.style.cursor = 'pointer';
            });
        } else {
            btns.forEach(btn => {
                btn.disabled = true;
                btn.style.background = 'var(--text-muted)';
                btn.style.color = 'rgba(255,255,255,0.5)';
                btn.style.cursor = 'not-allowed';
            });
        }
    };

    window.saveExamReviews = async () => {
        const dbId = document.getElementById('exam-current-student-id').value;
        const item = rawData.find(r => r._db_id_ == dbId);
        if(!item) return;
        
        const rev = {
            score: document.getElementById('review-score').value.trim(),
            academic: document.getElementById('review-academic').value.trim(),
            psycho: document.getElementById('review-psycho').value.trim()
        };
        
        item.exam_reviews = rev;
        const updatedPayload = { ...item };
        delete updatedPayload._db_id_;
        
        const btn = document.querySelector('button[onclick="saveExamReviews()"]');
        const origText = btn.innerText;
        btn.innerText = 'Saxlanılır...';
        
        try {
            const res = await fetch(`${API_URL}/registrations?id=eq.${dbId}`, {
                method: 'PATCH',
                headers: HEADERS,
                body: JSON.stringify({ payload: updatedPayload })
            });
            if(res.ok) {
                btn.innerText = 'Uğurlu ✓';
                setTimeout(() => btn.innerText = origText, 2000);
                renderExamResults();
            } else {
                alert('Xəta baş verdi');
                btn.innerText = origText;
            }
        } catch(e) { console.error(e); btn.innerText = origText; }
    };

    window.sendExamResult = (type) => {
        const dbId = document.getElementById('exam-current-student-id').value;
        const item = rawData.find(r => r._db_id_ == dbId);
        if(!item) return;
        
        const targetBtnId = type === 'wa' ? 'exam-send-wa-btn' : 'exam-send-mail-btn';
        const btn = document.getElementById(targetBtnId);
        const origHtml = btn.innerHTML;
        btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Hazırlanır...';
        btn.disabled = true;
        
        const fullName = item['[2.Şagird] Adı'] ? (item['[2.Şagird] Adı'] + ' ' + (item['[2.Şagird] Soyadı']||'')) : (item['Ad Soyad'] || item.fullName || item.name || item.firstName || item['[1.Əlaqə] Valideyn Adı'] || item['Valideyn'] || 'Adsız Şagird');
        const className = item.Sinif || item['Sinif'] || item.class_name || item['Neçənci sinif üçün imtahan verəcək?'] || (item.note && item.note.match(/Sinif:\s*([^|]+)/) ? item.note.match(/Sinif:\s*([^|]+)/)[1].trim() : 'Qeyd edilməyib');
        const rev = item.exam_reviews || {};
        
        const html = `
            <div style="padding:40px; font-family:sans-serif; color:#1e293b; max-width:800px; margin:auto;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:40px; border-bottom:2px solid #9c1c31; padding-bottom:20px;">
                    <h1 style="color:#9c1c31; margin:0; font-size:28px;">EVRİKA LİSEYİ</h1>
                    <img src="https://evrikaliseyi.edu.az/assets/loqoYeni.PNG" style="height:60px;" alt="Evrika Loqo">
                </div>
                
                <div style="background-color: #f8fafc; padding: 15px 20px; border-radius: 8px; margin-bottom: 30px; border: 1px solid #e2e8f0;">
                    <table style="width:100%; font-size:15px; color:#334155; border-collapse: collapse;">
                        <tr>
                            <td style="padding-bottom:8px; width:45%;"><strong>Şagirdin Adı və Soyadı:</strong></td>
                            <td style="padding-bottom:8px;">${fullName}</td>
                        </tr>
                        <tr>
                            <td style="padding-bottom:8px;"><strong>Müraciət Etdiyi Müəssisə:</strong></td>
                            <td style="padding-bottom:8px;">${getGranularSource(item)}</td>
                        </tr>
                        <tr>
                            <td style="padding-bottom:8px;"><strong>Bölmə (Sektor):</strong></td>
                            <td style="padding-bottom:8px;">${item.sector_name || item['Bölmə'] || item.Bölmə || (item.note && item.note.match(/Bölmə:\s*([^|]+)/) ? item.note.match(/Bölmə:\s*([^|]+)/)[1].trim() : 'Qeyd edilməyib')}</td>
                        </tr>
                        <tr>
                            <td style="padding-bottom:0;"><strong>Müraciət Etdiyi Sinif:</strong></td>
                            <td style="padding-bottom:0;">${className}</td>
                        </tr>
                    </table>
                </div>

                <p style="font-size:16px; margin-bottom:20px;">Hörmətli valideyn,</p>

                <p style="font-size:16px; line-height:1.6; margin-bottom:30px;">
                    Övladınız <strong>${fullName}</strong> Evrika Liseyində keçirilən qəbul imtahanında iştirak etmiş və <strong>90 mümkün baldan ${rev.score || 0} bal</strong> toplamışdır. Qəbul üçün müəyyən edilmiş keçid göstəricisi <strong>45 bal</strong> təşkil edir.
                </p>

                <p style="font-size:16px; line-height:1.6; margin-bottom:30px;">Şagirdin nəticələri akademik və psixoloji qiymətləndirmə çərçivəsində təhlil edilmişdir.</p>

                <div style="margin-bottom:25px;">
                    <h3 style="color:#0f172a; font-size:18px; margin-bottom:10px;"><strong>Akademik Qiymətləndirmə:</strong></h3>
                    <p style="white-space:pre-wrap; font-size:15px; line-height:1.6; color:#334155; margin:0;">${rev.academic || 'Rəy yoxdur'}</p>
                </div>
                
                <div style="margin-bottom:30px;">
                    <h3 style="color:#0f172a; font-size:18px; margin-bottom:10px;"><strong>Psixoloji Müayinə Protokolu:</strong></h3>
                    <p style="white-space:pre-wrap; font-size:15px; line-height:1.6; color:#334155; margin:0;">${rev.psycho || 'Rəy yoxdur'}</p>
                </div>

                

                <div style="font-size:16px; line-height:1.6; margin-bottom:40px;">
                    Hörmətlə,<br>
                    <strong>Evrika Liseyi – Qəbul Komissiyası</strong>
                </div>

                <div style="margin-top:50px; padding-top:20px; border-top:1px dashed #cbd5e1; font-size:12px; color:#94a3b8;">
                    <em>*Bu məlumat Evrika Liseyinin qiymətləndirmə sistemi tərəfindən avtomatik olaraq yaradılmışdır.</em>
                </div>
            </div>
        `;
        
        const opt = {
          margin:       0.5,
          filename:     `${fullName}-Neticeler.pdf`,
          image:        { type: 'jpeg', quality: 0.98 },
          html2canvas:  { scale: 2, useCORS: true },
          jsPDF:        { unit: 'in', format: 'a4', orientation: 'portrait' }
        };
        
        if (window.html2pdf) {
             const worker = html2pdf().set(opt).from(html);
             
             worker.save().then(() => {
                 worker.output('blob').then(async (pdfBlob) => {
                     let fileUrl = '';
                     try {
                         const fileName = `neticeler/${dbId}-${Date.now()}.pdf`;
                         const uploadUrl = `https://gziuhrlvagflokivfgwt.supabase.co/storage/v1/object/ems-documents/${fileName}`;
                         
                         const uploadRes = await fetch(uploadUrl, {
                             method: 'POST',
                             headers: {
                                 'apikey': API_KEY,
                                 'Authorization': 'Bearer ' + API_KEY,
                                 'Content-Type': 'application/pdf'
                             },
                             body: pdfBlob
                         });
                         
                         if (uploadRes.ok) {
                             fileUrl = `https://gziuhrlvagflokivfgwt.supabase.co/storage/v1/object/public/ems-documents/${fileName}`;
                         }
                     } catch(err) {
                         console.error("PDF upload error:", err);
                     }
                     
                     const phone = item.phone || item['[1.Valideyn] Əlaqə nömrəsi'] || '';
                     let studentEmail = item.email || '';
                     if(!studentEmail && item.note) {
                         const match = item.note.match(/E-mail:\s*([^\s|<]+)/i);
                         if(match) studentEmail = match[1];
                     }

                     const msgText = `Salam, hörmətli valideyn. Övladınızın imtahan nəticəsi:${fileUrl ? ' ' + fileUrl : ''}`;

                     if (type === 'wa' && phone) {
                         const cleanPhone = phone.replace(/[^0-9]/g, '');
                         const text = encodeURIComponent(msgText);
                         window.open(`https://wa.me/${cleanPhone}?text=${text}`, '_blank');
                     }

                     if (type === 'mail' && studentEmail) {
                         const mailSubject = encodeURIComponent(`EVRİKA İmtahan Nəticəsi: ${fullName}`);
                         const mailBody = encodeURIComponent(msgText);
                         window.open(`mailto:${studentEmail}?subject=${mailSubject}&body=${mailBody}`, '_blank');
                     }
                     
                     btn.innerHTML = '<i class="fas fa-check"></i> Göndərildi';
                     btn.style.background = '#3B82F6';
                     setTimeout(() => {
                         btn.innerHTML = origHtml;
                         btn.disabled = false;
                         btn.style.background = 'var(--success)';
                     }, 3000);
                 });
             });
        } else {
             alert('html2pdf kitabxanası yüklənməyib.');
             btn.innerHTML = origHtml;
             btn.disabled = false;
        }
    };

    window.switchTab = (t) => {
      document.querySelectorAll('.content').forEach(c => c.style.display = 'none');
      if(document.getElementById('view-'+t)) document.getElementById('view-'+t).style.display = 'block';
      const titles = { 'dashboard':'Dashboard',  'analytics':'Sayt Analitikası', 'speed':'Sayt Sürəti', 'apps':'Müraciətlər', 'exam-results':'Nəticələr & Rəylər', 'kanban':'Kanban Board', 'tasks':'Tapşırıqlar', 'employees':'Əməkdaşlar', 'hr-panel':'Vakansiyalar', 'finance':'Maliyyə Paneli', 'epoint-reports':'Köçürmələrin Tarixçəsi', 'kupon':'Kupon Alanlar', 'ugurlar':'Uğurlar & Məzun', 'news':'Xəbərlər', 'popup':'POP UP Yönətimi', 'leadership':'Rəhbərlik', 'settings':'Sistem Ayarları', 'parents':'Valideynlərimiz' };
      document.getElementById('topbar-title').innerText = titles[t] || 'EVRIKA EMS';
      
      // Handle the active class for sidebar links
      document.querySelectorAll('.sb-link').forEach(l => l.classList.remove('active'));
      const activeLink = document.querySelector(`.sb-link[onclick="switchTab('${t}')"]`);
      if (activeLink) activeLink.classList.add('active');

      if(t==='hr-panel') renderVacancyApps();
      if(t==='apps') renderApps();
      if(t==='dashboard') renderDashboard();
      if(t==='finance') renderFinance();
      if(t==='epoint-reports') renderEpointReports();
      if(t==='call-center') fetchCalls();
      if(t==='exam-results') renderExamResults();
      if(t==='kupon') renderKupon();
      if(t==='mezunlar') loadMezunlar();
      if(t==='ugurlar') loadUgurlar();
      if(t==='leadership') loadManagement();
      if(t==='employees') loadEmployees();
      if(t==='news') loadNews();
      if(t==='parents') loadParents();
      if(t==='partners') loadPartners();
      if(t==='popup') loadPopups();
      if(t==='settings') loadExamFee();
      if(t==='dashboard') updateCharts();
    };

    
    window.openFinanceDetails = (order_id) => {
        // find index in filteredData
        const idx = filteredData.findIndex(i => (i._db_id_ == order_id || i.order_id == order_id || (i.epoint_transaction && i.epoint_transaction == order_id)));
        if(idx >= 0) {
            viewDetails(idx, true);
        } else {
            // fallback to rawData
            const rIdx = rawData.findIndex(i => (i._db_id_ == order_id || i.order_id == order_id || (i.epoint_transaction && i.epoint_transaction == order_id)));
            if(rIdx >= 0) {
                // temporarily put it in filteredData to view
                filteredData.push(rawData[rIdx]);
                viewDetails(filteredData.length - 1, true);
            } else {
                alert('Detallar tapılmadı');
            }
        }
    };

    window.viewDetails = (idx, isFinance = false) => {
      const isExam = document.getElementById('view-exam-results') && document.getElementById('view-exam-results').style.display === 'block';
      let originalItem = filteredData[idx];
      if ((originalItem.status || '').toLowerCase() === 'yeni') {
          updateStatus(idx, 'Baxılıb');
          originalItem.status = 'Baxılıb';
      }
      let item = JSON.parse(JSON.stringify(originalItem));
      const content = document.getElementById('modal-content');
      
      // Do not split name, keep as AD SOYAD
      if (item.name) {
          item['Ad Soyad'] = item.name;
          delete item.name;
      }
      
      // Parse structured note if it comes from the form
      if (item.note && typeof item.note === 'string' && item.note.includes('|')) {
          let pieces = item.note.split('|');
          pieces.forEach(p => {
              let kv = p.split(':');
              if (kv.length >= 2) {
                  let k = kv.shift().trim();
                  item[k] = kv.join(':').trim();
              }
          });
          delete item.note;
      }

      const groups = {
        'ŞƏXSİ MƏLUMATLAR': [],
        'ƏLAQƏ VƏ TƏMAS': [],
        'TƏHSİL VƏ İSTİQAMƏT': [],
        'ÖDƏNİŞ DETALLARI': [],
        'MARKETİNQ (UTM)': [],
        'FAYLLAR': []
      };

      for(let key in item) {
        if(key.startsWith('_')) continue;
        const val = item[key];
        const upperKey = key.toLocaleUpperCase('az-AZ');
        if(upperKey === 'PAYMENT_STATUS' || upperKey === 'DAXILI ÖDƏNIŞ STATUSU') continue;
        
        let cleanKey = key.replace(/\[.*?\]\s*/g, '').replace(/_/g, ' ');
        
        let displayVal = val;
        if (upperKey === 'ƏVVƏLKİ MÜƏSSİSƏ' || upperKey.includes('ƏVVƏL OXUDUĞU') || upperKey.includes('GƏLDİYİNİZ TƏHSİL')) cleanKey = 'Hazırda Təhsil Aldığı Müəssisə';
        if ((upperKey === 'DATE' || upperKey === 'TARIX' || upperKey === 'CREATED_AT') && typeof val === 'string') {
            try {
                let d = new Date(val);
                if (!isNaN(d.getTime())) {
                    displayVal = d.toLocaleString('az-AZ', { day:'2-digit', month:'2-digit', year:'numeric', hour:'2-digit', minute:'2-digit', second:'2-digit' }).replace(',', '');
                }
            } catch(e){}
        }

        
        // Translate some common English keys
        if (upperKey === 'PHONE') cleanKey = 'Telefon';
        if (upperKey === 'AD SOYAD') cleanKey = 'Ad Soyad';
        if (upperKey === 'EMAIL' || upperKey === 'E-MAIL') cleanKey = 'E-mail';
        if (upperKey === 'SOURCE') cleanKey = 'Mənbə';
        if (upperKey === 'STATUS') cleanKey = 'Status';
        if (upperKey === 'DATE') cleanKey = 'Tarix';
        if (upperKey === 'NOTE') cleanKey = 'Qeyd';
        if (upperKey === 'EPOINT_AMOUNT' || upperKey === 'AMOUNT') cleanKey = 'Ödəniş Məbləği';
        if (upperKey === 'EPOINT_DATE') cleanKey = 'Ödəniş Tarixi';
        if (upperKey === 'EPOINT_CARD_NUMBER') cleanKey = 'Ödəyici Kartı (Maska)';
        if (upperKey === 'EPOINT_CARD_TYPE') cleanKey = 'Kartın Növü';
        if (upperKey === 'EPOINT_BANK') cleanKey = 'Bank Adı';
        if (upperKey === 'EPOINT_CURRENCY') cleanKey = 'Valyuta';
        if (upperKey === 'EPOINT_TRANSACTION') cleanKey = 'Tranzaksiya ID';
        if (upperKey === 'EPOINT_RRN' || upperKey === 'RRN') cleanKey = 'RRN Kodu';
        if (upperKey === 'APPROVAL_CODE' || upperKey === 'EPOINT_APPROVAL_CODE') cleanKey = 'Təsdiq Kodu';
        if (upperKey === 'CARD_NUMBER' || upperKey === 'EPOINT_CARD_NUMBER') cleanKey = 'Kart Nömrəsi (Maska)';
        if (upperKey === 'CARDNAME' || upperKey === 'EPOINT_CARD_NAME') cleanKey = 'Kart Sahibi';
        if (upperKey === 'RESULT_CODE' || upperKey === 'EPOINT_RESULT_CODE') cleanKey = 'Nəticə Kodu';
        if (upperKey === '3DSECURE' || upperKey === 'EPOINT_3DSECURE') cleanKey = '3D Təhlükəsizlik';
        if (upperKey === 'RESULT_PS') cleanKey = 'Ödəniş Statusu (Epoint)';
        if (upperKey === 'RESULT' || upperKey === 'EPOINT_BANK_RESPONSE') cleanKey = 'Bankın Cavabı';
        if (upperKey === 'PAYMENT_STATUS') cleanKey = 'Daxili Ödəniş Statusu';
        
        const dataPair = { rawKey: key, label: cleanKey.toUpperCase(), value: displayVal };

        if (upperKey === 'CV_FILE_BASE64') {
          groups['FAYLLAR'].push({ rawKey: key, label: 'Bax / Yüklə (' + (item.cv_file_name || 'Fayl') + ')', value: val, isBase64: true, filename: item.cv_file_name || 'cv_file' });
        } else if (typeof val === 'string' && upperKey !== 'CV_FILE_NAME' && (val.includes('supabase.co/storage') || val.match(/\.(jpg|jpeg|png|gif|pdf)/i))) {
          groups['FAYLLAR'].push(dataPair);
        } else if (upperKey.includes('EPOINT') || upperKey.includes('EPOİNT') || upperKey === 'AMOUNT' || upperKey.includes('PAYMENT') || ['RRN', 'APPROVAL_CODE', 'CARD_NUMBER', 'CARDNAME', 'RESULT_CODE', '3DSECURE', 'RESULT_PS', 'RESULT'].includes(upperKey) || upperKey === 'DATE' || upperKey === 'TARIX' || upperKey === 'CREATED_AT' || upperKey === 'MƏNBƏ' || upperKey === 'STATUS' || upperKey === 'ORDER_ID') {
          groups['ÖDƏNİŞ DETALLARI'].push(dataPair);
        } else if (upperKey.includes('PHONE') || upperKey.includes('TEL') || upperKey.includes('MAIL') || upperKey.includes('MAİL') || upperKey === 'ƏLAQƏ') {
          groups['ƏLAQƏ VƏ TƏMAS'].push(dataPair);
        } else if (upperKey.includes('AD') || upperKey.includes('SOYAD') || upperKey.includes('NAME') || upperKey.includes('CANDIDATE') || upperKey.includes('STUDENT')) {
          groups['ŞƏXSİ MƏLUMATLAR'].push(dataPair);
        } else if (upperKey.includes('FİLİAL') || upperKey.includes('BÖLMƏ') || upperKey.includes('SİNİF') || upperKey.includes('SEKTOR') || upperKey.includes('TƏHSİL') || upperKey.includes('MÜƏSSİSƏ') || upperKey.includes('MƏKTƏB') || upperKey.includes('BAĞÇA') || upperKey.includes('HAZIRDA OXUDUĞU') || upperKey.includes('MƏRKƏZ')) {
          groups['TƏHSİL VƏ İSTİQAMƏT'].push(dataPair);
        } else if (upperKey.startsWith('UTM_')) {
          groups['MARKETİNQ (UTM)'].push(dataPair);
        } else {
          groups['ÖDƏNİŞ DETALLARI'].push(dataPair);
        }
      }

      let html = '';
      for (const [title, items] of Object.entries(groups)) {
        if (items.length === 0) continue;
        
        html += `
          <div class="detail-group">
            <div class="detail-group-header">${title}</div>
            <div class="detail-grid-v2">
              ${items.map(pair => {
                if (title === 'FAYLLAR') {
                  if (pair.isBase64) {
                      const isImg = pair.value.startsWith('data:image/');
                      return `
                        <div class="detail-image-card" onclick="downloadBase64('${pair.value}', '${pair.filename}')">
                          ${isImg ? `<img src="${pair.value}" alt="${pair.label}">` : `<div style="height:100%; display:flex; align-items:center; justify-content:center; color:white;"><i class="fas fa-file-pdf fa-2x"></i></div>`}
                          <div class="detail-image-label">${pair.label}</div>
                        </div>
                      `;
                  }
                  const isImg = !pair.value.toLowerCase().endsWith('.pdf');
                  return `
                    <div class="detail-image-card" onclick="window.open('${pair.value}', '_blank')">
                      ${isImg ? `<img src="${pair.value}" alt="${pair.label}">` : `<div style="height:100%; display:flex; align-items:center; justify-content:center; color:white;"><i class="fas fa-file-pdf fa-2x"></i></div>`}
                      <div class="detail-image-label">${pair.label}</div>
                    </div>
                  `;
                }
                return `
                  <div class="detail-box">
                    <div class="detail-box-label">${pair.label}</div>
                    <div class="detail-box-value">${pair.value || '-'}</div>
                  </div>
                `;
              }).join('')}
            </div>
          </div>
        `;
      }

      const srcStr = (getGranularSource(item) + ' ' + JSON.stringify(item)).toLowerCase();
      const isQrBranch = srcStr.includes('nərimanov') || srcStr.includes('gənclik') || srcStr.includes('lisey1') || srcStr.includes('lisey2') || srcStr.includes('lisey 1') || srcStr.includes('lisey 2');
      
      if (item._db_id_ && isQrBranch) {
          const verifyUrl = encodeURIComponent(`https://evrikaliseyi.edu.az/verify.html?id=${item._db_id_}`);
          const qrUrl = `https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=${verifyUrl}`;
          const isScanned = item.status === 'QR İstifadə Edilib';
          html += `
          <div class="detail-group">
            <div class="detail-group-header">İMTƏHANA GİRİŞ (QR KOD)</div>
            <div style="display:flex; align-items:center; gap:20px; padding:20px; background:rgba(255,255,255,0.02); border-radius:12px; border:1px solid var(--border); position: relative;">
              ${isScanned ? '<div style="position:absolute; top:20px; right:20px; background:var(--error); color:white; padding:5px 10px; border-radius:8px; font-weight:900; font-size:0.8rem; letter-spacing:1px; animation: badgePulse 2s infinite;"><i class="fas fa-exclamation-triangle"></i> QR ARTIQ İSTİFADƏ EDİLİB!</div>' : ''}
              <div style="background:white; padding:10px; border-radius:10px; opacity:${isScanned ? '0.3' : '1'};">
                <img src="${qrUrl}" alt="QR" style="width:100px; height:100px; display:block;">
              </div>
              <div>
                <div style="font-weight:900; font-size:1.2rem; margin-bottom:5px; color:white; letter-spacing:1px;">KOD: EV-${String(item._db_id_).padStart(4,'0')}</div>
                <div style="color:var(--text-muted); font-size:0.9rem; margin-bottom: 5px;">Ödəniş Statusu: <span style="color:${item.payment_status === 'Ödənilib' ? '#10b981' : '#ef4444'}; font-weight:800; background:${item.payment_status === 'Ödənilib' ? 'rgba(16,185,129,0.1)' : 'rgba(239,68,68,0.1)'}; padding:4px 8px; border-radius:6px; margin-left:5px;">${item.payment_status || 'Ödənilməyib'}</span></div>
                ${isScanned ? '<div style="color:#ef4444; font-weight:900; font-size:0.9rem;"><i class="fas fa-check-double"></i> Bu kodla giriş edilib</div>' : ''}
              </div>
            </div>
          </div>
          `;
      }

      content.innerHTML = html;
      document.getElementById('detail-modal').classList.add('active');
    };
    window.closeModal = () => document.getElementById('detail-modal').classList.remove('active');

    window.renderVacancyApps = () => {
       const tb = document.getElementById('vac-apps-tbody'); if(!tb) return;
       const apps = rawData.filter(i => i.source === 'Karyera' || i.position);
       if(document.getElementById('vac-app-count')) document.getElementById('vac-app-count').innerText = apps.length + ' Müraciət';
       tb.innerHTML = apps.map(a => `<tr><td>${a.fullName || 'Adsız'}</td><td>${a.phone || '-'}</td><td>${a.position || '-'}</td><td>${a.submissionDate || '-'}</td><td>${a.status || 'Yeni'}</td><td><button onclick="viewDetails(${rawData.indexOf(a)})" class="btn-view">Bax</button></td></tr>`).join('');
    };

    window.loadUgurlar = async () => {
      const res = await fetch(`${API_URL}/ugurlar?select=*&order=id.desc`, { headers: HEADERS });
      if(res.ok) { ugurlarData = (await res.json()).map(r => ({ ...r.payload, _db_id_: r.id })); }
      const tb = document.getElementById('ug-tbody'); if(tb) tb.innerHTML = ugurlarData.map((u, i) => `<tr><td><img src="${u.img}" style="width:40px;height:40px;object-fit:cover;border-radius:8px;"></td><td>${u.name}</td><td>${u.uni}</td><td><div style="display:flex; gap:8px;"><button class="btn-view" style="padding:8px 12px; background:rgba(255,255,255,0.05);" onclick="editUgur(${i})"><i class="fas fa-edit"></i></button><button class="btn-danger" style="padding:8px 12px;" onclick="deleteUgur('${u._db_id_}')"><i class="fas fa-trash"></i></button></div></td></tr>`).join('');
      if(document.getElementById('dash-ugur')) document.getElementById('dash-ugur').innerText = ugurlarData.length;
    }

    window.editUgur = (idx) => {
        const u = ugurlarData[idx];
        document.getElementById('ug-id').value = u._db_id_;
        document.getElementById('ug-name').value = u.name;
        document.getElementById('ug-uni').value = u.uni || '';

        document.getElementById('ug-img').value = u.img;
        const pv = document.getElementById('ug-img-preview'); if(u.img) { pv.src = u.img; pv.style.display='block'; } else { pv.style.display='none'; }
        document.getElementById('ug-form-title').innerText = "Uğura Düzəliş Et";
        document.getElementById('ug-submit-btn').innerText = "Dəyişikliyi Saxla";
    };

    window.resetUgurForm = () => {
        document.getElementById('ug-form').reset();
        document.getElementById('ug-id').value = "";
        document.getElementById('ug-uni').value = "";
        document.getElementById('ug-img-preview').style.display='none';
        document.getElementById('ug-form-title').innerText = "Yeni Uğur Əlavə Et";
        document.getElementById('ug-submit-btn').innerText = "Yadda Saxla";
    };

    window.handleUgurSubmit = async (e) => {
        e.preventDefault();
        const id = document.getElementById('ug-id').value;
        const btn = document.getElementById('ug-submit-btn');
        const payload = { 
            name: document.getElementById('ug-name').value, 
            uni: document.getElementById('ug-uni').value, 
            detail: "",
            img: document.getElementById('ug-img').value 
        };
        btn.disabled = true;
        btn.innerText = "Gözləyin...";
        const url = id ? `${API_URL}/ugurlar?id=eq.${id}` : `${API_URL}/ugurlar`;
        const method = id ? 'PATCH' : 'POST';
        
        try {
            const res = await fetch(url, { method, headers: HEADERS, body: JSON.stringify({ payload }) });
            if(res.ok) { 
                resetUgurForm(); 
                loadUgurlar(); 
                alert("Uğurla yadda saxlanıldı!"); 
            } else {
                const errText = await res.text();
                alert("Xəta baş verdi: " + errText + "\\nZəhmət olmasa bazada 'ugurlar' cədvəlinin mövcudluğunu və quraşdırmasını yoxlayın.");
            }
        } catch (err) {
            alert("Sistem xətası: " + err.message);
        }
        
        btn.disabled = false;
        btn.innerText = id ? "Dəyişikliyi Saxla" : "Yadda Saxla";
    };

    window.deleteUgur = async (id) => {
        if(!confirm('Bu uğur silinsin?')) return;
        await fetch(`${API_URL}/ugurlar?id=eq.${id}`, { method: 'DELETE', headers: HEADERS });
        loadUgurlar();
    };
    window.deleteVacancy = async (id) => {
        if(!confirm('Bu vakansiya silinsin?')) return;
        await fetch(`${API_URL}/vacancies?id=eq.${id}`, { method: 'DELETE', headers: HEADERS });
        loadVacancies();
    };

    window.addVacancy = async (e) => {
        e.preventDefault();
        const payload = {
            title: document.getElementById('vac-title').value,
            location: document.getElementById('vac-dept').value,
            time: document.getElementById('vac-type').value,
            desc: document.getElementById('vac-desc').value,
            responsibilities: document.getElementById('vac-resp').value,
            requirements: document.getElementById('vac-reqs').value,
            status: 'Aktiv'
        };
        const btn = e.target.querySelector('button');
        const origText = btn.innerText;
        btn.innerText = "Gözləyin..."; btn.disabled = true;
        try {
            await fetch(`${API_URL}/vacancies`, {
                method: 'POST',
                headers: HEADERS,
                body: JSON.stringify({ payload })
            });
            e.target.reset();
            loadVacancies();
        } finally {
            btn.innerText = origText; btn.disabled = false;
        }
    };

    window.loadVacancies = async () => {
      const res = await fetch(`${API_URL}/vacancies?select=*&order=id.desc`, { headers: HEADERS });
      if(res.ok) vacanciesData = (await res.json()).map(r => ({ ...r.payload, _db_id_: r.id }));
      const tb = document.getElementById('vac-tbody'); if(tb) tb.innerHTML = vacanciesData.map(v => `<tr><td>${v.title}</td><td>${v.location}</td><td>${v.time}</td><td><button class="btn-danger" onclick="deleteVacancy('${v._db_id_}')">Sil</button></td></tr>`).join('');
      renderDashboard();
    }

    window.loadNews = async () => {
      const res = await fetch(`${API_URL}/news?select=*&order=id.desc`, { headers: HEADERS });
      if(res.ok) newsData = (await res.json()).map(r => ({ ...r.payload, _db_id_: r.id }));
      const tb = document.getElementById('news-tbody'); 
      if(tb) tb.innerHTML = newsData.map((n, i) => `<tr><td><img src="${n.img}" style="width:40px;height:40px;object-fit:cover;border-radius:4px;"></td><td>${n.title}</td><td>${n.date}</td><td><div style="display:flex; gap:8px;"><button class="btn-view" style="padding:8px 12px; background:rgba(255,255,255,0.05);" onclick="editNews(${i})"><i class="fas fa-edit"></i></button><button class="btn-danger" style="padding:8px 12px;" onclick="deleteNews('${n._db_id_}')"><i class="fas fa-trash"></i></button></div></td></tr>`).join('');
    }

    window.editNews = (idx) => {
        const n = newsData[idx];
        document.getElementById('news-id').value = n._db_id_;
        document.getElementById('news-title').value = n.title;
        document.getElementById('news-img').value = n.img;
        document.getElementById('news-text').value = n.text || '';
        document.getElementById('news-form-title').innerText = "Xəbərə Düzəliş Et";
        document.getElementById('news-submit-btn').innerText = "Dəyişikliyi Saxla";
        window.scrollTo({ top: 0, behavior: 'smooth' });
    };

    window.resetNewsForm = () => {
        document.getElementById('news-form').reset();
        document.getElementById('news-id').value = '';
        document.getElementById('news-form-title').innerText = "Yeni Xəbər Paylaş";
        document.getElementById('news-submit-btn').innerText = "Paylaş";
    };

    window.handleNewsSubmit = async (e) => {
        e.preventDefault();
        const id = document.getElementById('news-id').value;
        const btn = document.getElementById('news-submit-btn');
        const payload = {
            title: document.getElementById('news-title').value,
            img: document.getElementById('news-img').value,
            text: document.getElementById('news-text').value,
            date: new Date().toLocaleDateString('az-AZ')
        };
        btn.disabled = true;
        const url = id ? `${API_URL}/news?id=eq.${id}` : `${API_URL}/news`;
        const method = id ? 'PATCH' : 'POST';
        const res = await fetch(url, { method, headers: HEADERS, body: JSON.stringify({ payload }) });
        if(res.ok) { resetNewsForm(); loadNews(); alert("Xəbər uğurla saxlanıldı!"); }
        btn.disabled = false;
    };

    window.deleteNews = async (id) => {
        if(!confirm('Silinsin?')) return;
        await fetch(`${API_URL}/news?id=eq.${id}`, { method: 'DELETE', headers: HEADERS });
        loadNews();
    };

    // --- MEZUNLAR LOGIC ---
    let mezunlarData = [];
    window.loadMezunlar = async () => {
       const res = await fetch(`${API_URL}/mezunlar?select=*&order=id.desc`, { headers: HEADERS });
       if(res.ok) mezunlarData = (await res.json()).map(r => ({ ...r.payload, _db_id_: r.id }));
       const tb = document.getElementById('mz-tbody'); if(tb) tb.innerHTML = mezunlarData.map((m, i) => `<tr><td><img src="${m.img}" style="width:40px;height:40px;object-fit:cover;border-radius:50%;"></td><td>${m.name}</td><td>${m.uni}</td><td><div style="display:flex; gap:8px;"><button class="btn-view" style="padding:8px 12px; background:rgba(255,255,255,0.05);" onclick="editMezun(${i})"><i class="fas fa-edit"></i></button><button class="btn-danger" style="padding:8px 12px;" onclick="deleteMezun('${m._db_id_}')"><i class="fas fa-trash"></i></button></div></td></tr>`).join('');
       if(document.getElementById('dash-mz')) document.getElementById('dash-mz').innerText = mezunlarData.length;
    };

    window.editMezun = (idx) => {
        const m = mezunlarData[idx];
        document.getElementById('mz-id').value = m._db_id_;
        document.getElementById('mz-name').value = m.name;
        document.getElementById('mz-uni').value = m.uni;
        document.getElementById('mz-img').value = m.img;
        const pv = document.getElementById('mz-img-preview'); if(m.img) { pv.src = m.img; pv.style.display='block'; } else { pv.style.display='none'; }
        document.getElementById('mz-form-title').innerText = "Məzuna Düzəliş Et";
        document.getElementById('mz-submit-btn').innerText = "Dəyişikliyi Saxla";
    };

    window.handleMezunSubmit = async (e) => {
        e.preventDefault();
        const id = document.getElementById('mz-id').value;
        const btn = document.getElementById('mz-submit-btn');
        const payload = { name: document.getElementById('mz-name').value, uni: document.getElementById('mz-uni').value, img: document.getElementById('mz-img').value };
        btn.disabled = true;
        btn.innerText = "Gözləyin...";
        const url = id ? `${API_URL}/mezunlar?id=eq.${id}` : `${API_URL}/mezunlar`;
        const method = id ? 'PATCH' : 'POST';
        
        try {
            const res = await fetch(url, { method, headers: HEADERS, body: JSON.stringify({ payload }) });
            if(res.ok) { 
                resetMezunForm(); 
                loadMezunlar(); 
                alert("Məzun uğurla yadda saxlanıldı!");
            } else {
                const errText = await res.text();
                alert("Xəta baş verdi: " + errText);
            }
        } catch(err) {
            alert("Sistem xətası: " + err.message);
        }
        
        btn.disabled = false;
        btn.innerText = id ? "Dəyişikliyi Saxla" : "Yadda Saxla";
    };

    window.deleteMezun = async (id) => {
        if(!confirm('Silinsin?')) return;
        await fetch(`${API_URL}/mezunlar?id=eq.${id}`, { method: 'DELETE', headers: HEADERS });
        loadMezunlar();
    };

    window.resetMezunForm = () => { 
        document.getElementById('mz-form').reset(); 
        document.getElementById('mz-id').value = "";
        document.getElementById('mz-img-preview').style.display='none';
        document.getElementById('mz-form-title').innerText = "Yeni Məzun Əlavə Et";
        document.getElementById('mz-submit-btn').innerText = "Yadda Saxla";
    };

    // --- MANAGEMENT LOGIC ---
    let managementData = [];
    window.loadManagement = async () => {
       try {
         const res = await fetch(`${API_URL}/management?select=*&order=id.asc`, { headers: HEADERS });
         if(res.ok) {
           managementData = (await res.json()).map(r => ({ ...r.payload, _db_id_: r.id }));
           const tb = document.getElementById('led-tbody'); if(tb) tb.innerHTML = managementData.map((m, i) => `<tr><td><img src="${m.img}" style="width:40px;height:40px;object-fit:cover;border-radius:50%;"></td><td>${m.name}</td><td>${m.role}</td><td><div style="display:flex; gap:8px;"><button class="btn-view" style="padding:8px 12px; background:rgba(255,255,255,0.05);" onclick="editManagement(${i})"><i class="fas fa-edit"></i></button><button class="btn-danger" style="padding:8px 12px;" onclick="deleteManagement('${m._db_id_}')"><i class="fas fa-trash"></i></button></div></td></tr>`).join('');
         } else if (res.status === 404) {
           console.error("Supabase Error: 'management' table not found.");
         }
       } catch (e) {
         console.error("Management loading failed:", e);
       }
    };

    window.editManagement = (idx) => {
        const m = managementData[idx];
        document.getElementById('led-id').value = m._db_id_;
        document.getElementById('led-name').value = m.name;
        document.getElementById('led-role').value = m.role;
        document.getElementById('led-category').value = m.category || 'board';
        document.getElementById('led-quote').value = m.quote || '';
        document.getElementById('led-img').value = m.img;
        document.getElementById('led-form-title').innerText = "Üzvə Düzəliş Et";
        document.getElementById('led-submit-btn').innerText = "Dəyişikliyi Saxla";
    };

    window.handleManagementSubmit = async (e) => {
        e.preventDefault();
        const id = document.getElementById('led-id').value;
        const btn = document.getElementById('led-submit-btn');
        const payload = { 
            name: document.getElementById('led-name').value, 
            role: document.getElementById('led-role').value,
            category: document.getElementById('led-category').value,
            quote: document.getElementById('led-quote').value,
            img: document.getElementById('led-img').value 
        };
        btn.disabled = true;
        const url = id ? `${API_URL}/management?id=eq.${id}` : `${API_URL}/management`;
        const method = id ? 'PATCH' : 'POST';
        const res = await fetch(url, { method, headers: HEADERS, body: JSON.stringify({ payload }) });
        if(res.ok) { 
            resetManagementForm(); 
            loadManagement(); 
            alert("Uğurla yadda saxlanıldı!");
        } else {
            alert("Xəta baş verdi! Cədvəlin mövcudluğunu yoxlayın.");
        }
        btn.disabled = false;
    };

    window.deleteManagement = async (id) => {
        if(!confirm('Silinsin?')) return;
        await fetch(`${API_URL}/management?id=eq.${id}`, { method: 'DELETE', headers: HEADERS });
        loadManagement();
    };

    window.resetManagementForm = () => { 
        document.getElementById('led-form').reset(); 
        document.getElementById('led-id').value = "";
        document.getElementById('led-form-title').innerText = "Yeni Rəhbərlik Üzvi";
        document.getElementById('led-submit-btn').innerText = "Yadda Saxla";
    };

    // --- REUSABLE IMAGE UPLOAD WITH AUTO BG REMOVAL ---
    window.uploadImage = async (input, targetId) => {
        if(input.files.length === 0) return;

        const label = input.parentElement;
        const oldHtml = label.innerHTML;
        label.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';

        let uploadedUrls = [];

        for (let i = 0; i < input.files.length; i++) {
            let file = input.files[i];

            // 1. Check File Size (Max 10MB)
            if (file.size > 10 * 1024 * 1024) {
                alert(`Xəta: ${file.name} ölçüsü çox böyükdür (Maksimum 10MB).`);
                continue;
            }

            // --- BACKGROUND REMOVAL LOGIC (For white backgrounds) ---
            try {
                if (targetId === 'partner-logo' || targetId === 'led-img') {
                    const img = new Image();
                    img.src = URL.createObjectURL(file);
                    await new Promise(r => img.onload = r);
                    
                    const canvas = document.createElement('canvas');
                    canvas.width = img.width;
                    canvas.height = img.height;
                    const ctx = canvas.getContext('2d');
                    ctx.drawImage(img, 0, 0);
                    
                    const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
                    const data = imageData.data;
                    
                    // Simple Chroma Key for White/Near-White
                    // Also removes edges to improve transparency
                    for (let j = 0; j < data.length; j += 4) {
                        const avg = (data[j] + data[j+1] + data[j+2]) / 3;
                        if (avg > 235) { // Threshold for "near white"
                            data[j+3] = 0; 
                        }
                    }
                    ctx.putImageData(imageData, 0, 0);
                    
                    const blob = await new Promise(r => canvas.toBlob(r, 'image/png'));
                    file = new File([blob], file.name.replace(/\.[^/.]+$/, "") + ".png", { type: "image/png" });
                }
            } catch(e) { console.error("BG removal failed, uploading original:", e); }
            
            const safeName = file.name.replace(/[^a-zA-Z0-9.\-_]/g, '_');
            const fileName = `uploads/${Date.now()}_${i}_${safeName}`;
            const res = await fetch(`https://gziuhrlvagflokivfgwt.supabase.co/storage/v1/object/ems-documents/${fileName}`, {
                method: 'POST',
                headers: { 'apikey': API_KEY, 'Authorization': 'Bearer '+API_KEY },
                body: file
            });
            
            if(res.ok) {
                uploadedUrls.push(`https://gziuhrlvagflokivfgwt.supabase.co/storage/v1/object/public/ems-documents/${fileName}`);
            } else {
                console.error("Upload failed for", file.name, await res.text());
                alert(`Xəta: ${file.name} yüklənə bilmədi.`);
            }
        }
        
        if (uploadedUrls.length > 0) {
            const targetEl = document.getElementById(targetId);
            if (input.multiple && targetEl.value) {
                // If appending to existing multiple selections
                targetEl.value = targetEl.value + ',' + uploadedUrls.join(',');
            } else {
                targetEl.value = uploadedUrls.join(',');
            }
        }

        label.innerHTML = oldHtml;
        input.value = "";
    };


    // --- POPUP MANAGEMENT LOGIC ---
    let popupData = [];
    window.loadPopups = async () => {
        try {
            const res = await fetch(`${API_URL}/popups?select=*&order=id.desc`, { headers: HEADERS });
            if(res.ok) {
                popupData = (await res.json()).map(r => ({ ...r.payload, _db_id_: r.id }));
                const tb = document.getElementById('popup-tbody');
                if(tb) tb.innerHTML = popupData.map((p, i) => `
                    <tr>
                        <td><img src="${p.img}" style="width:60px; height:auto; border-radius:4px;"></td>
                        <td>${p.title}</td>
                        <td>
                            <select onchange="togglePopupStatus('${p._db_id_}', this.value, ${i})" style="background:${p.status==='active'?'rgba(16,185,129,0.1)':'rgba(239,68,68,0.1)'}; color:${p.status==='active'?'#10b981':'#ef4444'}; border:1px solid transparent; padding:5px; border-radius:5px;">
                                <option value="active" ${p.status==='active'?'selected':''}>Aktiv</option>
                                <option value="inactive" ${p.status==='inactive'?'selected':''}>Deaktiv</option>
                            </select>
                        </td>
                        <td>
                            <div style="display:flex; gap:8px;">
                                <button class="btn-view" style="padding:8px 12px; background:rgba(255,255,255,0.05);" onclick="editPopup(${i})"><i class="fas fa-edit"></i></button>
                                <button class="btn-danger" style="padding:8px 12px;" onclick="deletePopup('${p._db_id_}')"><i class="fas fa-trash"></i></button>
                            </div>
                        </td>
                    </tr>
                `).join('');
            }
        } catch(e) { console.error("Popup loading failed", e); }
    };

    window.editPopup = (idx) => {
        const p = popupData[idx];
        document.getElementById('popup-id').value = p._db_id_;
        document.getElementById('popup-title').value = p.title;
        document.getElementById('popup-img').value = p.img;
        document.getElementById('popup-link').value = p.link || '';
        document.getElementById('popup-status').value = p.status || 'active';
        document.getElementById('popup-form-title').innerText = "Pop-up-a Düzəliş Et";
        document.getElementById('popup-submit-btn').innerText = "Dəyişikliyi Saxla";
        window.scrollTo({ top: 0, behavior: 'smooth' });
    };

    window.resetPopupForm = () => {
        document.getElementById('popup-form').reset();
        document.getElementById('popup-id').value = '';
        document.getElementById('popup-form-title').innerText = "Yeni Pop-up Əlavə Et";
        document.getElementById('popup-submit-btn').innerText = "Yadda Saxla";
    };

    window.handlePopupSubmit = async (e) => {
        e.preventDefault();
        const id = document.getElementById('popup-id').value;
        const btn = document.getElementById('popup-submit-btn');
        const payload = {
            title: document.getElementById('popup-title').value,
            desc: document.getElementById('popup-desc').value,
            img: document.getElementById('popup-img').value,
            link: document.getElementById('popup-link').value,
            status: document.getElementById('popup-status').value,
            date: new Date().toLocaleDateString('az-AZ')
        };
        btn.disabled = true;
        const url = id ? `${API_URL}/popups?id=eq.${id}` : `${API_URL}/popups`;
        const method = id ? 'PATCH' : 'POST';
        try {
            const res = await fetch(url, { method, headers: HEADERS, body: JSON.stringify({ payload }) });
            if(res.ok) { resetPopupForm(); loadPopups(); alert("Pop-up uğurla saxlanıldı!"); }
            else { alert("Cədvəl tapılmadı. Pop-up üçün bazada cədvəl lazımdır."); }
        } catch(err) { console.error(err); }
        btn.disabled = false;
    };

    window.deletePopup = async (id) => {
        if(!confirm('Silinsin?')) return;
        await fetch(`${API_URL}/popups?id=eq.${id}`, { method: 'DELETE', headers: HEADERS });
        loadPopups();
    };

    window.togglePopupStatus = async (id, newStatus, idx) => {
        const item = popupData[idx];
        const updatedPayload = { ...item, status: newStatus };
        delete updatedPayload._db_id_;
        try {
            await fetch(`${API_URL}/popups?id=eq.${id}`, {
                method: 'PATCH',
                headers: HEADERS,
                body: JSON.stringify({ payload: updatedPayload })
            });
            loadPopups();
        } catch(e) {}
    };


    // --- HR / EMPLOYEE MANAGEMENT ---
    let employeeData = [];
    async function loadEmployees() {
        const res = await fetch(`${API_URL}/employees`, { headers: HEADERS });
        if(res.ok) {
            employeeData = (await res.json()).map(i => ({...i.payload, _db_id_: i.id}));
            renderEmployees();
        }
    }

    function renderEmployees() {
        const tbody = document.getElementById('hr-tbody');
        if(!tbody) return;
        tbody.innerHTML = employeeData.map((e, idx) => `
            <tr>
                <td><b style="color:white">${e.name}</b><div style="font-size:0.7rem; color:var(--text-muted)">ID: EV-${1000 + idx}</div></td>
                <td>${e.position}</td>
                <td>${e.salary} AZN</td>
                <td><span style="background:${e.status==='active' ? 'rgba(16,185,129,0.1)' : 'rgba(239,68,68,0.1)'}; color:${e.status==='active' ? 'var(--success)' : 'var(--error)'}; padding:4px 10px; border-radius:30px; font-size:0.7rem;">${e.status==='active' ? 'Aktiv' : (e.status==='on_leave' ? 'Məzuniyyət' : 'Çıxıb')}</span></td>
                <td>
                    <button onclick="editEmployee(${idx})" class="btn-view" style="padding:8px;"><i class="fas fa-edit"></i></button>
                    <button onclick="deleteEmployee('${e._db_id_}')" class="btn-view" style="padding:8px; color:var(--error);"><i class="fas fa-trash"></i></button>
                </td>
            </tr>
        `).join('');

        // Update HR Stats
        document.getElementById('hr-total').innerText = employeeData.length;
        document.getElementById('hr-teachers').innerText = employeeData.filter(e => e.category === 'teacher').length;
        document.getElementById('hr-technical').innerText = employeeData.filter(e => e.category === 'technical').length;
    }

    window.resetEmployeeForm = () => {
        document.getElementById('emp-form').reset();
        document.getElementById('emp-id').value = '';
        document.getElementById('emp-form-title').innerText = 'Yeni Əməkdaş Əlavə Et';
        document.getElementById('emp-submit-btn').innerText = 'Yadda Saxla';
    };

    window.editEmployee = (idx) => {
        const e = employeeData[idx];
        document.getElementById('emp-id').value = e._db_id_;
        document.getElementById('emp-name').value = e.name;
        document.getElementById('emp-position').value = e.position;
        document.getElementById('emp-category').value = e.category;
        document.getElementById('emp-salary').value = e.salary;
        document.getElementById('emp-status').value = e.status;
        document.getElementById('emp-form-title').innerText = 'Əməkdaşa Düzəliş';
        document.getElementById('emp-submit-btn').innerText = 'Dəyişikliyi Saxla';
        window.scrollTo({ top: 0, behavior: 'smooth' });
    };

    window.handleEmployeeSubmit = async (ev) => {
        ev.preventDefault();
        const btn = document.getElementById('emp-submit-btn');
        const id = document.getElementById('emp-id').value;
        const payload = {
            name: document.getElementById('emp-name').value,
            position: document.getElementById('emp-position').value,
            category: document.getElementById('emp-category').value,
            salary: document.getElementById('emp-salary').value,
            status: document.getElementById('emp-status').value
        };
        
        btn.disabled = true;
        btn.innerText = "Gözləyin...";
        
        try {
            const url = id ? `${API_URL}/employees?id=eq.${id}` : `${API_URL}/employees`;
            const method = id ? 'PATCH' : 'POST';
            const res = await fetch(url, { method, headers: HEADERS, body: JSON.stringify({ payload }) });
            
            if(res.ok) { 
                resetEmployeeForm(); 
                loadEmployees(); 
                alert("Uğurla yadda saxlanıldı!");
            } else {
                const err = await res.text();
                alert("Xəta: " + err + "\n\nZəhmət olmasa 'employees' cədvəlinin mövcudluğunu yoxlayın.");
            }
        } catch (e) {
            alert("Sistem xətası: " + e.message);
        } finally {
            btn.disabled = false;
            btn.innerText = id ? "Dəyişikliyi Saxla" : "Yadda Saxla";
        }
    };

    window.deleteEmployee = async (id) => {
        if(!confirm('Bu əməkdaş silinsin?')) return;
        await fetch(`${API_URL}/employees?id=eq.${id}`, { method: 'DELETE', headers: HEADERS });
        loadEmployees();
    };

    // --- PARTNERS MANAGEMENT ---
    let partnerData = [];
    window.loadPartners = async () => {
        try {
            const res = await fetch(`${API_URL}/partners?select=*&order=sort_order.asc`, { headers: HEADERS });
            if(res.ok) {
                partnerData = await res.json();
                const tbody = document.getElementById('partner-tbody');
                if(tbody) tbody.innerHTML = partnerData.map((p, idx) => `
                    <tr>
                        <td>
                            ${p.logo_url ? `<img src="${p.logo_url}" style="height:30px; max-width:80px; object-fit:contain; filter:brightness(1.5);">` : `<span style="opacity:0.3; font-size:0.7rem;">Yoxdur</span>`}
                        </td>
                        <td><b style="color:white">${p.name}</b></td>
                        <td>${p.sort_order}</td>
                        <td>
                            <div style="display:flex; gap:8px;">
                                <button onclick="editPartner(${idx})" class="btn-view" style="padding:8px 12px; background:rgba(255,255,255,0.05);"><i class="fas fa-edit"></i></button>
                                <button onclick="deletePartner('${p.id}')" class="btn-danger" style="padding:8px 12px;"><i class="fas fa-trash"></i></button>
                            </div>
                        </td>
                    </tr>
                `).join('');
            }
        } catch(e) { console.error(e); }
    };

    window.updatePartnerPreview = () => {
        const name = document.getElementById('partner-name').value || 'NÜMUNƏ AD';
        const logo = document.getElementById('partner-logo').value;
        const nameLabel = document.getElementById('preview-name-label');
        const logoBox = document.getElementById('preview-logo-box');
        
        if (nameLabel) nameLabel.innerText = name;
        if (logoBox) {
            if(logo) {
                logoBox.innerHTML = `<img src="${logo}" style="max-height: 100%; max-width: 100%; object-fit: contain;">`;
            } else {
                logoBox.innerHTML = `<i class="fas fa-handshake" style="font-size: 2.5rem; color: #ddd;"></i>`;
            }
        }
    };

    window.handlePartnerSubmit = async (e) => {
        e.preventDefault();
        const id = document.getElementById('partner-id').value;
        const btn = document.getElementById('partner-submit-btn');
        const data = {
            name: document.getElementById('partner-name').value,
            logo_url: document.getElementById('partner-logo').value,
            description: document.getElementById('partner-description').value,
            sort_order: parseInt(document.getElementById('partner-order').value) || 0
        };

        btn.disabled = true;
        const url = id ? `${API_URL}/partners?id=eq.${id}` : `${API_URL}/partners`;
        const method = id ? 'PATCH' : 'POST';
        
        try {
            const res = await fetch(url, { method, headers: HEADERS, body: JSON.stringify(data) });
            if(res.ok) {
                resetPartnerForm();
                loadPartners();
                alert("Uğurla yadda saxlanıldı!");
            }
        } catch(e) { alert("Xəta baş verdi!"); }
        btn.disabled = false;
    };

    window.editPartner = (idx) => {
        const p = partnerData[idx];
        document.getElementById('partner-id').value = p.id;
        document.getElementById('partner-name').value = p.name;
        document.getElementById('partner-logo').value = p.logo_url || '';
        document.getElementById('partner-description').value = p.description || '';
        document.getElementById('partner-order').value = p.sort_order;
        document.getElementById('partner-form-title').innerText = "Partnyoru Redaktə Et";
        document.getElementById('partner-submit-btn').innerText = "Düzəlişi Saxla";
        updatePartnerPreview();
        window.scrollTo({ top: 0, behavior: 'smooth' });
    };

    window.deletePartner = async (id) => {
        if(!confirm('Bu partnyor silinsin?')) return;
        await fetch(`${API_URL}/partners?id=eq.${id}`, { method: 'DELETE', headers: HEADERS });
        loadPartners();
    };

    window.resetPartnerForm = () => {
        document.getElementById('partner-form').reset();
        document.getElementById('partner-id').value = '';
        document.getElementById('partner-form-title').innerText = "Yeni Partnyor Əlavə Et";
        document.getElementById('partner-submit-btn').innerText = "Yadda Saxla";
    };

    function renderDashboard() {
      if(document.getElementById('dash-total')) document.getElementById('dash-total').innerText = rawData.length;
      if(document.getElementById('dash-new')) document.getElementById('dash-new').innerText = rawData.filter(i=>(i.status||'Yeni')==='Yeni').length;
      if(document.getElementById('dash-ugur')) {
         const kuponCount = rawData.filter(i => (i.epoint_amount || i.amount) && i.payment_status === 'Ödənilib').length;
         document.getElementById('dash-ugur').innerText = kuponCount;
      }
      if(document.getElementById('dash-vac')) document.getElementById('dash-vac').innerText = vacanciesData.filter(v => v.status === 'Aktiv').length || vacanciesData.length;
      
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
      
      updateCharts(); // Ensure charts update with data
    }

    // --- PARENTS TESTIMONIALS LOGIC ---
    let parentsData = [];
    window.loadParents = async () => {
        try {
            const res = await fetch(`${API_URL}/parent_testimonials?select=*&order=id.desc`, { headers: HEADERS });
            if(res.ok) {
                parentsData = (await res.json()).map(r => ({ ...r.payload, _db_id_: r.id }));
                const tb = document.getElementById('par-tbody');
                if(tb) tb.innerHTML = parentsData.map((p, i) => `
                    <tr>
                        <td>
                            <div style="display:flex; align-items:center; gap:10px;">
                                <img src="${p.avatar || 'https://via.placeholder.com/40'}" style="width:40px; height:40px; border-radius:50%; object-fit:cover;">
                                <div>
                                    <div style="font-weight:700; color:white;">${p.name}</div>
                                    <div style="font-size:0.7rem; color:var(--text-muted);">${p.status}</div>
                                </div>
                            </div>
                        </td>
                        <td>
                            <span style="background:${p.type==='video'?'rgba(245,158,11,0.1)':'rgba(59,130,246,0.1)'}; color:${p.type==='video'?'#f59e0b':'#3b82f6'}; padding:4px 10px; border-radius:20px; font-size:0.7rem;">
                                ${p.type==='video'?'Video':'Foto'}
                            </span>
                        </td>
                        <td style="max-width:200px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; font-size:0.8rem; color:var(--text-muted);">
                            ${p.quote || (p.type==='video' ? 'Video Testimonial' : 'Photo Testimonial')}
                        </td>
                        <td>
                            <div style="display:flex; gap:8px;">
                                <button class="btn-view" style="padding:8px;" onclick="editParent(${i})"><i class="fas fa-edit"></i></button>
                                <button class="btn-danger" style="padding:8px;" onclick="deleteParent('${p._db_id_}')"><i class="fas fa-trash"></i></button>
                            </div>
                        </td>
                    </tr>
                `).join('');
            }
        } catch(e) { console.error("Parents loading failed:", e); }
    };

    window.toggleParentMediaFields = () => {
        const typeEl = document.getElementById('par-type');
        const mediaField = document.getElementById('par-media-field');
        const thumbField = document.getElementById('par-thumb-field');
        
        if (!typeEl || (!mediaField && !thumbField)) return;

        const type = typeEl.value;
        if (mediaField) mediaField.style.display = (type === 'text' ? 'none' : 'block');
        if (thumbField) thumbField.style.display = (type === 'video' ? 'flex' : 'none');
    };

    window.editParent = (idx) => {
        const p = parentsData[idx];
        document.getElementById('par-id').value = p._db_id_;
        document.getElementById('par-name').value = p.name;
        document.getElementById('par-status').value = p.status;
        document.getElementById('par-quote').value = p.quote || '';
        document.getElementById('par-type').value = p.type || 'photo';
        document.getElementById('par-avatar').value = p.avatar || '';
        document.getElementById('par-media-url').value = p.media_url || '';
        document.getElementById('par-thumb').value = p.thumbnail_url || '';
        
        toggleParentMediaFields();
        document.getElementById('par-form-title').innerText = "Rəyə Düzəliş Et";
        document.getElementById('par-submit-btn').innerText = "Dəyişikliyi Saxla";
        document.getElementById('par-form').scrollIntoView({ behavior:'smooth' });
    };

    window.resetParentForm = () => {
        document.getElementById('par-form').reset();
        document.getElementById('par-id').value = "";
        document.getElementById('par-form-title').innerText = "Yeni Valideyn Rəyi Əlavə Et";
        document.getElementById('par-submit-btn').innerText = "Yadda Saxla";
        toggleParentMediaFields();
    };

    window.handleParentSubmit = async (e) => {
        e.preventDefault();
        const id = document.getElementById('par-id').value;
        const btn = document.getElementById('par-submit-btn');
        const payload = {
            name: document.getElementById('par-name').value,
            status: document.getElementById('par-status').value,
            quote: document.getElementById('par-quote').value,
            type: document.getElementById('par-type').value,
            avatar: document.getElementById('par-avatar').value,
            media_url: document.getElementById('par-media-url').value,
            thumbnail_url: document.getElementById('par-thumb').value
        };
        
        btn.disabled = true;
        btn.innerText = "Gözləyin...";
        
        try {
            const url = id ? `${API_URL}/parent_testimonials?id=eq.${id}` : `${API_URL}/parent_testimonials`;
            const method = id ? 'PATCH' : 'POST';
            const res = await fetch(url, { method, headers: HEADERS, body: JSON.stringify({ payload }) });
            
            if(res.ok) {
                resetParentForm();
                loadParents();
                alert("Uğurla yadda saxlanıldı!");
            } else {
                alert("Xəta baş verdi! Cədvəlin ('parent_testimonials') bazada olduğundan emin olun.");
            }
        } catch (e) { alert("Sistem xətası: " + e.message); }
        finally {
            btn.disabled = false;
            btn.innerText = id ? "Dəyişikliyi Saxla" : "Yadda Saxla";
        }
    };

    window.deleteParent = async (id) => {
        if(!confirm('Bu rəy silinsin?')) return;
        await fetch(`${API_URL}/parent_testimonials?id=eq.${id}`, { method: 'DELETE', headers: HEADERS });
        loadParents();
    };

    function updateCharts() {
      const sourceCounts = {};
      const SOURCE_MAP = {
        'lisey1': 'EVRİKA Nərimanov filialı (Qeydiyyat)',
        'lisey2': 'EVRİKA Gənclik filialı (Qeydiyyat)',
        'montessori': 'Montessori Academy (Qeydiyyat)',
        'victory': 'Victory Colleges (Qeydiyyat)',
        'zumrud': 'Zümrüd Women Club (Qeydiyyat)',
        'career': 'Karyera və Vakansiyalar',
        'contact': 'Bizimlə Əlaqə (Səhifədən)',
        'whatsapp': 'WhatsApp',
        'instagram': 'Instagram',
        'linkedin': 'LinkedIn',
        'facebook': 'Facebook',
        'email': 'Email',
        'phone': 'Telefon Zəngi'
      };

      // Categories to always show in the list
      const PRIMARY_KEYS = ['lisey1', 'lisey2', 'montessori', 'victory', 'zumrud', 'contact', 'career', 'whatsapp', 'instagram', 'linkedin', 'facebook', 'email'];
      PRIMARY_KEYS.forEach(k => sourceCounts[SOURCE_MAP[k]] = 0);

      rawData.forEach(item => {
        const s = getGranularSource(item);
        const mapped = SOURCE_MAP[s] || s || 'Email'; 
        const finalLabel = mapped === 'Digər Mənbələr' || mapped === 'Vebsayt' ? 'Email' : mapped;
        sourceCounts[finalLabel] = (sourceCounts[finalLabel] || 0) + 1;
      });

      const ctx = document.getElementById('pieChart').getContext('2d');
      if (window.myPieChart) window.myPieChart.destroy();
      
      const labels = Object.keys(sourceCounts).filter(k => sourceCounts[k] > 0 || PRIMARY_KEYS.map(pk => SOURCE_MAP[pk]).includes(k));
      const dataValues = labels.map(l => sourceCounts[l]);
      const colors = ['#8B1A2B', '#3B82F6', '#10B981', '#F59E0B', '#A855F7', '#EC4899', '#06B6D4', '#64748B', '#F87171', '#FB923C'];

      window.myPieChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: labels,
          datasets: [{ data: dataValues, backgroundColor: colors, borderWidth: 0, hoverOffset: 20 }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { position: 'bottom', labels: { color: 'rgba(255,255,255,0.6)', font: { size: 10, weight: '600' }, padding: 20, usePointStyle: true } },
            title: { display: true, text: 'MÜRACİƏT MƏNBƏLƏRİ', color: 'white', font: { size: 14, weight: '800' }, padding: { bottom: 20 } }
          },
          cutout: '60%',
          layout: { padding: 30 }
        }
      });

      // Populate Source Stats List (Show ALL primary, even if 0)
      const listEl = document.getElementById('source-stats-list');
      if (listEl) {
        listEl.innerHTML = PRIMARY_KEYS.map((k, idx) => {
          const label = SOURCE_MAP[k];
          const count = sourceCounts[label] || 0;
          return `
            <div style="display: flex; align-items: center; justify-content: space-between; background: rgba(255,255,255,0.02); padding: 15px 20px; border-radius: 12px; border-left: 4px solid ${colors[idx % colors.length]};">
              <span style="font-size: 0.8rem; font-weight: 700; color: rgba(255,255,255,0.7);">${label}</span>
              <span style="font-size: 1.1rem; font-weight: 900; color: white;">${count}</span>
            </div>
          `;
        }).join('');
      }

      // Update Line Chart (Applications over time - simplified)
      const lineCtx = document.getElementById('lineChart').getContext('2d');
      if (window.myLineChart) window.myLineChart.destroy();
      window.myLineChart = new Chart(lineCtx, {
        type: 'line',
        data: {
          labels: ['Yan', 'Fev', 'Mar', 'Apr', 'May', 'İyun'],
          datasets: [{
            label: 'Müraciət Dinamikası',
            data: [12, 19, 13, 25, 22, 30],
            borderColor: '#8B1A2B',
            tension: 0.4,
            fill: true,
            backgroundColor: 'rgba(139, 26, 43, 0.1)'
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { display: false } },
          scales: {
            y: { grid: { color: 'rgba(255,255,255,0.05)' }, border: { display: false }, ticks: { color: 'rgba(255,255,255,0.4)' } },
            x: { grid: { display: false }, border: { display: false }, ticks: { color: 'rgba(255,255,255,0.4)' } }
          }
        }
      });
    }

    async function updateStatus(idx, newStatus) {
      const item = filteredData[idx];
      const dbId = item._db_id_;
      if (!dbId) return;

      const oldStatus = (item.status || '').toLowerCase();
      const newStatusLower = (newStatus || '').toLowerCase();

      const updatedPayload = { ...item, status: newStatus };
      delete updatedPayload._db_id_; // Remove temp ID before sync

      try {
        const res = await fetch(`${API_URL}/registrations?id=eq.${dbId}`, {
          method: 'PATCH',
          headers: HEADERS,
          body: JSON.stringify({ payload: updatedPayload })
        });
        if (res.ok) {
           item.status = newStatus;
           
           // Update rawData to keep it in sync
           const rawItem = rawData.find(r => r._db_id_ === dbId);
           if (rawItem) rawItem.status = newStatus;

           // Update notification badge instantly
           const badge = document.getElementById('new-apps-badge');
           if (badge) {
               let currentCount = parseInt(badge.innerText) || 0;
               if (oldStatus === 'yeni' && newStatusLower !== 'yeni') {
                   currentCount = Math.max(0, currentCount - 1);
               } else if (oldStatus !== 'yeni' && newStatusLower === 'yeni') {
                   currentCount++;
               }
               badge.innerText = currentCount;
               badge.style.display = currentCount > 0 ? 'inline-block' : 'none';
           }

           renderApps(); // Refresh table view without losing filters
           renderDashboard(); // Refresh dashboard stats
        }
      } catch (e) { alert("Xəta baş verdi!"); }
    }

    async function loadExamFee() {
      try {
        const res = await fetch(`${API_URL}/settings?key=eq.exam_fee`, { headers: HEADERS });
        if (res.ok) {
          const data = await res.json();
          if (data.length > 0) {
            document.getElementById('setting-exam-fee').value = data[0].value;
          }
        }
      } catch (e) { console.error("Setting loading error", e); }
    }

    async function saveExamFee() {
      const fee = document.getElementById('setting-exam-fee').value;
      const statusEl = document.getElementById('settings-status');
      if (!fee) return;

      try {
        // Upsert logic for Supabase settings table
        // We'll try to update first, if it fails or returns 0, we can insert. 
        // Or just use POST with Prefer: resolution=merge-duplicates if supported.
        const res = await fetch(`${API_URL}/settings`, {
          method: 'POST',
          headers: { ...HEADERS, 'Prefer': 'resolution=merge-duplicates' },
          body: JSON.stringify({ key: 'exam_fee', value: fee })
        });

        if (res.ok || res.status === 201) {
          statusEl.innerText = "Məbləğ uğurla yadda saxlanıldı!";
          statusEl.style.color = "var(--success)";
          statusEl.style.opacity = "1";
          setTimeout(() => statusEl.style.opacity = "0", 3000);
        } else {
          throw new Error("Sync failed");
        }
      } catch (e) {
        statusEl.innerText = "Xəta baş verdi!";
        statusEl.style.color = "var(--error)";
                statusEl.style.opacity = "1";
        setTimeout(() => statusEl.style.opacity = "0", 3000);
      }
    }

    function toggleLang(btn) {
      const b = document.getElementById('lang-code');
      b.textContent = b.textContent === 'AZ' ? 'EN' : 'AZ';
    }

    loadData();

document.addEventListener('DOMContentLoaded', () => {
            if (typeof updateContent === 'function') {
                updateContent(localStorage.getItem('evrika-lang') || 'az');
            }
            
            // Load saved Meta settings
            const savedAccount = localStorage.getItem('meta_ad_account');
            const savedToken = localStorage.getItem('meta_access_token');
            if(savedAccount) document.getElementById('setting-meta-account').value = savedAccount;
            if(savedToken) document.getElementById('setting-meta-token').value = savedToken;
            
            if(savedAccount && savedToken) {
                fetchMetaAdsData(savedAccount, savedToken);
            }
        });

        function saveMetaPixel() {
            const pixel = document.getElementById('setting-meta-pixel').value;
            const account = document.getElementById('setting-meta-account').value;
            const token = document.getElementById('setting-meta-token').value;
            
            localStorage.setItem('meta_pixel_id', pixel);
            localStorage.setItem('meta_ad_account', account);
            localStorage.setItem('meta_access_token', token);
            
            alert('Meta Ads ayarları yadda saxlanıldı! Məlumatlar çəkilir...');
            fetchMetaAdsData(account, token);
        }

        async function fetchMetaAdsData(accountId, token) {
            try {
                // Determine actual account ID format (Meta uses act_ prefix)
                const actId = accountId.startsWith('act_') ? accountId : 'act_' + accountId;
                
                // Fetch Insights (Spend, Clicks, Impressions, CPC)
                const insightsUrl = `https://graph.facebook.com/v19.0/${actId}/insights?fields=spend,clicks,impressions,cpc,actions&date_preset=last_30d&access_token=${token}`;
                const res = await fetch(insightsUrl);
                const data = await res.json();
                
                if(data.data && data.data.length > 0) {
                    const stats = data.data[0];
                    document.getElementById('meta-stat-spend').textContent = '$' + (stats.spend || '0.00');
                    document.getElementById('meta-stat-clicks').textContent = stats.clicks || '0';
                    document.getElementById('meta-stat-impressions').textContent = stats.impressions || '0';
                    document.getElementById('meta-stat-cpc').textContent = '$' + (stats.cpc || '0.00');
                    
                    // Parse Actions for Leads
                    let leads = 0;
                    if(stats.actions) {
                        const leadAction = stats.actions.find(a => a.action_type === 'lead');
                        if(leadAction) leads = leadAction.value;
                    }
                    document.getElementById('meta-stat-leads').textContent = leads;
                }

                // Fetch Campaigns
                const campaignsUrl = `https://graph.facebook.com/v19.0/${actId}/campaigns?fields=name,status,insights{spend,actions}&limit=5&access_token=${token}`;
                const campRes = await fetch(campaignsUrl);
                const campData = await campRes.json();
                
                if(campData.data) {
                    const tbody = document.getElementById('meta-campaign-tbody');
                    tbody.innerHTML = '';
                    campData.data.forEach((camp, index) => {
                        let spend = '$0.00';
                        let leads = '0';
                        
                        if(camp.insights && camp.insights.data && camp.insights.data.length > 0) {
                            spend = '$' + (camp.insights.data[0].spend || '0.00');
                            if(camp.insights.data[0].actions) {
                                const leadAction = camp.insights.data[0].actions.find(a => a.action_type === 'lead');
                                if(leadAction) leads = leadAction.value;
                            }
                        }
                        
                        const statusColor = camp.status === 'ACTIVE' ? 'var(--success)' : 'var(--warning)';
                        const statusDot = `<i class="fas fa-circle" style="font-size:0.5rem; margin-right:5px; vertical-align:middle;"></i>`;
                        
                        tbody.innerHTML += `
                          <tr>
                            <td style="padding: 15px 20px; font-weight: 700; font-size: 0.85rem; border-bottom: 1px solid rgba(255,255,255,0.03);">${index + 1}. ${camp.name}</td>
                            <td style="padding: 15px 20px; border-bottom: 1px solid rgba(255,255,255,0.03);"><span style="color:${statusColor}; font-weight:700; font-size:0.75rem;">${statusDot}${camp.status}</span></td>
                            <td style="padding: 15px 20px; font-weight: 700; color: #EF4444; border-bottom: 1px solid rgba(255,255,255,0.03);">${spend}</td>
                            <td style="padding: 15px 20px; font-weight: 700; color: #10B981; border-bottom: 1px solid rgba(255,255,255,0.03);">${leads} Lead</td>
                            <td style="padding: 15px 20px; font-weight: 700; border-bottom: 1px solid rgba(255,255,255,0.03);">-</td>
                          </tr>
                        `;
                    });
                }
            } catch(e) {
                console.error("Meta Graph API error:", e);
                document.getElementById('meta-campaign-tbody').innerHTML = `<tr><td colspan="5" style="padding: 15px; color: #EF4444; text-align: center;">Məlumatı çəkmək mümkün olmadı. Access Token və Ad Account ID-nin düzgünlüyünü yoxlayın.</td></tr>`;
            }
        }
        function downloadBase64(base64Data, filename) {
            const link = document.createElement('a');
            link.href = base64Data;
            link.download = filename;
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }