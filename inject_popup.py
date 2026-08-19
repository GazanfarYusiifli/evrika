import re

file = 'admin.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. HTML Injection
html_injection = """
    <!-- POPUP MODULE -->
    <div id="view-popup" class="content" style="display: none;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 30px;">
         <h2 style="font-weight: 800; font-size: 1.8rem;">POP UP İdarəetməsi</h2>
         <button class="btn-primary" onclick="resetPopupForm()" style="background:var(--burgundy);"><i class="fas fa-plus"></i> Yeni Pop Up</button>
      </div>

      <div style="display:grid; grid-template-columns:1fr 2fr; gap:30px; align-items:start;">
         <!-- Form -->
         <div class="panel" style="padding: 25px;">
            <h3 id="popup-form-title" style="margin-bottom:20px; font-weight:800; border-bottom:1px solid rgba(255,255,255,0.05); padding-bottom:10px;">Yeni Pop Up Əlavə Et</h3>
            <form id="popup-form" onsubmit="handlePopupSubmit(event)">
               <input type="hidden" id="popup-id">
               <div class="form-group">
                  <label>Başlıq</label>
                  <input type="text" id="popup-title" class="form-control" placeholder="Məsələn: Qəbul Kampaniyası 2026" required>
               </div>
               <div class="form-group">
                  <label>Keçid Linki (istəyə bağlı)</label>
                  <input type="text" id="popup-link" class="form-control" placeholder="Məsələn: https://evrikaliseyi.edu.az/register">
               </div>
               <div class="form-group">
                  <label>Şəkil (URL və ya Base64)</label>
                  <input type="text" id="popup-img" class="form-control" placeholder="Şəkil URL-i daxil edin və ya fayl seçin" required>
                  <input type="file" id="popup-img-file" class="form-control" style="margin-top:10px;" accept="image/*">
               </div>
               <div class="form-group" style="display:flex; align-items:center; gap:10px;">
                  <input type="checkbox" id="popup-status" checked style="width:20px; height:20px;">
                  <label for="popup-status" style="margin:0;">Aktivdir (Sayta daxil olanda görünsün)</label>
               </div>
               <button type="submit" id="popup-submit-btn" class="btn-primary" style="width:100%; margin-top:15px; background:var(--success);">Yadda Saxla</button>
            </form>
         </div>

         <!-- List -->
         <div class="panel" style="padding: 0;">
            <div style="padding:20px 25px; border-bottom:1px solid rgba(255,255,255,0.05);">
               <h3 style="font-weight:800; font-size:1.1rem; margin:0;">Mövcud Pop Up-lar</h3>
            </div>
            <div style="overflow-x:auto;">
               <table class="data-table">
                  <thead>
                     <tr>
                        <th>Şəkil</th>
                        <th>Başlıq</th>
                        <th>Status</th>
                        <th>Link</th>
                        <th>Əməliyyatlar</th>
                     </tr>
                  </thead>
                  <tbody id="popup-tbody">
                     <!-- Popups loaded dynamically -->
                  </tbody>
               </table>
            </div>
         </div>
      </div>
    </div>
"""

if '<div id="view-popup"' not in content:
    content = content.replace('<div id="view-settings"', html_injection + '\n    <div id="view-settings"')

# 2. JS Injection
js_injection = """
    // --- POPUP LOGIC ---
    let popupData = [];
    window.loadPopups = async () => {
      try {
          const res = await fetch(`${API_URL}/popups?select=*&order=id.desc`, { headers: HEADERS });
          if(res.ok) {
              popupData = (await res.json()).map(r => ({ ...r.payload, _db_id_: r.id }));
              const tb = document.getElementById('popup-tbody'); 
              if(tb) tb.innerHTML = popupData.map((p, i) => `
                <tr>
                    <td><img src="${p.img}" style="width:50px;height:auto;border-radius:4px; max-height:40px; object-fit:cover;"></td>
                    <td>${p.title}</td>
                    <td>
                        <span style="padding:4px 8px; border-radius:4px; font-size:0.8rem; font-weight:700; ${p.status === 'active' ? 'background:rgba(16,185,129,0.2); color:#10B981;' : 'background:rgba(239,68,68,0.2); color:#EF4444;'}">
                            ${p.status === 'active' ? 'Aktiv' : 'Deaktiv'}
                        </span>
                    </td>
                    <td>${p.link ? `<a href="${p.link}" target="_blank" style="color:#3b82f6;"><i class="fas fa-external-link-alt"></i></a>` : '-'}</td>
                    <td>
                        <div style="display:flex; gap:8px;">
                            <button class="btn-view" style="padding:6px 10px; background:rgba(255,255,255,0.05);" onclick="editPopup(${i})"><i class="fas fa-edit"></i></button>
                            <button class="btn-danger" style="padding:6px 10px;" onclick="deletePopup('${p._db_id_}')"><i class="fas fa-trash"></i></button>
                        </div>
                    </td>
                </tr>
              `).join('');
          }
      } catch (err) {
          console.error('Popup load error:', err);
      }
    }

    window.editPopup = (idx) => {
        const p = popupData[idx];
        document.getElementById('popup-id').value = p._db_id_;
        document.getElementById('popup-title').value = p.title || '';
        document.getElementById('popup-link').value = p.link || '';
        document.getElementById('popup-img').value = p.img || '';
        document.getElementById('popup-status').checked = (p.status === 'active');
        document.getElementById('popup-form-title').innerText = "Pop Up-a Düzəliş Et";
        document.getElementById('popup-submit-btn').innerText = "Dəyişikliyi Saxla";
    };

    window.resetPopupForm = () => {
        document.getElementById('popup-form').reset();
        document.getElementById('popup-id').value = '';
        document.getElementById('popup-img').value = '';
        document.getElementById('popup-status').checked = true;
        document.getElementById('popup-form-title').innerText = "Yeni Pop Up Əlavə Et";
        document.getElementById('popup-submit-btn').innerText = "Yadda Saxla";
    };

    // Attach file uploader event listener globally safely
    document.addEventListener('change', function(e) {
        if(e.target && e.target.id === 'popup-img-file') {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(evt) { document.getElementById('popup-img').value = evt.target.result; };
                reader.readAsDataURL(file);
            }
        }
    });

    window.handlePopupSubmit = async (e) => {
        e.preventDefault();
        const id = document.getElementById('popup-id').value;
        const btn = document.getElementById('popup-submit-btn');
        const prevText = btn.innerHTML;
        btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Gözləyin...';
        btn.disabled = true;

        const payload = {
            title: document.getElementById('popup-title').value,
            img: document.getElementById('popup-img').value,
            link: document.getElementById('popup-link').value,
            status: document.getElementById('popup-status').checked ? 'active' : 'inactive'
        };

        const method = id ? 'PATCH' : 'POST';
        const url = id ? `${API_URL}/popups?id=eq.${id}` : `${API_URL}/popups`;
        
        try {
            const res = await fetch(url, {
                method,
                headers: HEADERS,
                body: JSON.stringify({ payload })
            });
            if(res.ok) {
                resetPopupForm();
                loadPopups();
                alert("Pop Up uğurla saxlanıldı!");
            } else {
                alert("Xəta baş verdi.");
            }
        } catch (err) {
            console.error(err);
            alert("Sistem xətası.");
        } finally {
            btn.innerHTML = prevText;
            btn.disabled = false;
        }
    };

    window.deletePopup = async (id) => {
        if(!confirm('Bu Pop Up-ı silmək istədiyinizə əminsiniz?')) return;
        try {
            const res = await fetch(`${API_URL}/popups?id=eq.${id}`, { method: 'DELETE', headers: HEADERS });
            if(res.ok) loadPopups();
        } catch(err) {
            console.error(err);
        }
    };
"""

if 'window.loadPopups =' not in content:
    content = content.replace('window.loadNews = async () => {', js_injection + '\n\n    window.loadNews = async () => {')
    
    # Make sure to call loadPopups() when needed
    if 'loadNews();' in content and 'loadPopups();' not in content:
        content = content.replace('loadNews();', 'loadNews(); loadPopups();')
    if "if(t==='news') loadNews();" in content and "if(t==='popup') loadPopups();" not in content:
        content = content.replace("if(t==='news') loadNews();", "if(t==='news') loadNews();\n      if(t==='popup') loadPopups();")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("POPUP Module HTML and JS injected.")
