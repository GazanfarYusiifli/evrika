import re

file = 'admin.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the HTML part of view-popup
old_popup_html_pattern = r'<!-- POPUP MODULE -->\s*<div id="view-popup" class="content" style="display: none;">.*?</div>\s*</div>\s*</div>\s*</div>'

new_popup_html = """<!-- POPUP MODULE -->
    <div id="view-popup" class="content" style="display: none;">
        <div style="display: grid; grid-template-columns: 1fr 1.5fr; gap: 40px;">
          <div class="stat-card" style="background: rgba(255,255,255,0.02); height: fit-content; border-top: 4px solid var(--accent);">
            <h3 style="margin-bottom: 25px; font-weight: 900;" id="popup-form-title">Yeni Pop Up Əlavə Et</h3>
            <form onsubmit="handlePopupSubmit(event)" id="popup-form" style="display: flex; flex-direction: column; gap: 15px;">
              <input type="hidden" id="popup-id">
              <input type="text" id="popup-title" placeholder="Başlıq (Məs: Qəbul Kampaniyası 2026)" required class="admin-input">
              <input type="text" id="popup-link" placeholder="Keçid Linki (istəyə bağlı)" class="admin-input">
              <div style="font-size:0.65rem; color:var(--text-muted); margin-bottom:5px;"><i class="fas fa-info-circle"></i> Daha gözəl görünüş üçün uyğun ölçülü (Landscape) şəkillərə üstünlük verin</div>
              <div style="display:flex; gap:10px; align-items:center;">
                <input type="text" id="popup-img" placeholder="Şəkil URL" required class="admin-input" style="flex:1;">
                <label class="btn-view" style="cursor:pointer; padding:18px;"><i class="fas fa-upload"></i><input type="file" hidden accept="image/jpeg,image/png,image/webp" id="popup-img-file"></label>
                <img id="popup-img-preview" style="width:40px; height:40px; border-radius:5px; object-fit:cover; display:none;">
              </div>
              <div style="display:flex; align-items:center; gap:10px; margin-top:5px; margin-bottom:10px;">
                 <input type="checkbox" id="popup-status" checked style="width:18px; height:18px; accent-color:var(--success);">
                 <label for="popup-status" style="margin:0; font-size:0.85rem; font-weight:600; cursor:pointer;">Aktivdir (Sayta daxil olanda görünsün)</label>
              </div>
              <div style="display: flex; gap: 10px;">
                <button type="submit" id="popup-submit-btn" class="btn-view" style="flex:2; justify-content: center; background: var(--success); border: none; padding: 15px;">Yadda Saxla</button>
                <button type="button" onclick="resetPopupForm()" class="btn-view" style="flex:1; justify-content: center; background: rgba(255,255,255,0.05);"><i class="fas fa-undo"></i></button>
              </div>
            </form>
          </div>
          <div class="table-wrapper">
            <table><thead><tr><th>Şəkil</th><th>Başlıq</th><th>Status</th><th>Link</th><th>Əməliyyat</th></tr></thead><tbody id="popup-tbody"></tbody></table>
          </div>
        </div>
    </div>"""

if re.search(old_popup_html_pattern, content, flags=re.DOTALL):
    content = re.sub(old_popup_html_pattern, new_popup_html, content, flags=re.DOTALL)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("POPUP Module HTML updated to match Mezunlar style.")
else:
    print("Pattern not found!")
