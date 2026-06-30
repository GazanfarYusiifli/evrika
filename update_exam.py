import re

with open('admin.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update UI Textareas
ui_old = """                    <!-- Subject 1: Psixoloq -->
                    <div style="background: rgba(255,255,255,0.03); padding: 20px; border-radius: 16px; border: 1px solid var(--border);">
                        <div style="display:flex; justify-content:space-between; margin-bottom: 10px;">
                            <h4 style="color:var(--royal-blue); font-weight:800; font-size:0.9rem;"><i class="fas fa-brain"></i> Psixoloq Rəyi</h4>
                            <span id="status-psy" style="font-size:0.7rem; padding:3px 8px; border-radius:10px; background:var(--warning); color:white; font-weight:700;">Gözləyir</span>
                        </div>
                        <textarea class="admin-input exam-review-input" id="review-psy" placeholder="Psixoloji dəyərləndirməni bura yazın..." style="height:80px; resize:vertical;" oninput="checkExamStatus()"></textarea>
                    </div>

                    <!-- Subject 2: Riyaziyyat -->
                    <div style="background: rgba(255,255,255,0.03); padding: 20px; border-radius: 16px; border: 1px solid var(--border);">
                        <div style="display:flex; justify-content:space-between; margin-bottom: 10px;">
                            <h4 style="color:var(--royal-blue); font-weight:800; font-size:0.9rem;"><i class="fas fa-square-root-alt"></i> Riyaziyyat Rəyi</h4>
                            <span id="status-math" style="font-size:0.7rem; padding:3px 8px; border-radius:10px; background:var(--warning); color:white; font-weight:700;">Gözləyir</span>
                        </div>
                        <textarea class="admin-input exam-review-input" id="review-math" placeholder="Riyazi biliklərin yoxlanması nəticələri..." style="height:80px; resize:vertical;" oninput="checkExamStatus()"></textarea>
                    </div>

                    <!-- Subject 3: İngilis Dili -->
                    <div style="background: rgba(255,255,255,0.03); padding: 20px; border-radius: 16px; border: 1px solid var(--border);">
                        <div style="display:flex; justify-content:space-between; margin-bottom: 10px;">
                            <h4 style="color:var(--royal-blue); font-weight:800; font-size:0.9rem;"><i class="fas fa-language"></i> İngilis Dili Rəyi</h4>
                            <span id="status-eng" style="font-size:0.7rem; padding:3px 8px; border-radius:10px; background:var(--warning); color:white; font-weight:700;">Gözləyir</span>
                        </div>
                        <textarea class="admin-input exam-review-input" id="review-eng" placeholder="İngilis dili səviyyəsi haqqında..." style="height:80px; resize:vertical;" oninput="checkExamStatus()"></textarea>
                    </div>"""

ui_new = """                    <!-- Section 1: Score -->
                    <div style="background: rgba(255,255,255,0.03); padding: 20px; border-radius: 16px; border: 1px solid var(--border);">
                        <div style="display:flex; justify-content:space-between; margin-bottom: 10px;">
                            <h4 style="color:var(--royal-blue); font-weight:800; font-size:0.9rem;"><i class="fas fa-poll"></i> Şagirdin İmtahan Balı</h4>
                            <span id="status-score" style="font-size:0.7rem; padding:3px 8px; border-radius:10px; background:var(--warning); color:white; font-weight:700;">Gözləyir</span>
                        </div>
                        <textarea class="admin-input exam-review-input" id="review-score" placeholder="Övladınız ... tarixində ... imtahanında ... bal toplayaraq uğur qazanmışdır." style="height:80px; resize:vertical;" oninput="checkExamStatus()"></textarea>
                    </div>

                    <!-- Section 2: Academic -->
                    <div style="background: rgba(255,255,255,0.03); padding: 20px; border-radius: 16px; border: 1px solid var(--border);">
                        <div style="display:flex; justify-content:space-between; margin-bottom: 10px;">
                            <h4 style="color:var(--royal-blue); font-weight:800; font-size:0.9rem;"><i class="fas fa-book-open"></i> Akademik Qiymətləndirmə</h4>
                            <span id="status-academic" style="font-size:0.7rem; padding:3px 8px; border-radius:10px; background:var(--warning); color:white; font-weight:700;">Gözləyir</span>
                        </div>
                        <textarea class="admin-input exam-review-input" id="review-academic" placeholder="* Rus dilində şifahi nitqi zəifdir&#10;* Oxu bacarıqları formalaşıb..." style="height:100px; resize:vertical;" oninput="checkExamStatus()"></textarea>
                    </div>

                    <!-- Section 3: Psycho -->
                    <div style="background: rgba(255,255,255,0.03); padding: 20px; border-radius: 16px; border: 1px solid var(--border);">
                        <div style="display:flex; justify-content:space-between; margin-bottom: 10px;">
                            <h4 style="color:var(--royal-blue); font-weight:800; font-size:0.9rem;"><i class="fas fa-brain"></i> Psixoloji Müayinə Protokolu</h4>
                            <span id="status-psycho" style="font-size:0.7rem; padding:3px 8px; border-radius:10px; background:var(--warning); color:white; font-weight:700;">Gözləyir</span>
                        </div>
                        <textarea class="admin-input exam-review-input" id="review-psycho" placeholder="Aparılan psixoloji müayinə zamanı idrak proseslərinin inkişaf göstəriciləri..." style="height:100px; resize:vertical;" oninput="checkExamStatus()"></textarea>
                    </div>"""

if ui_old in content:
    content = content.replace(ui_old, ui_new)
else:
    print("UI block not found!")

# 2. Update loadExamStudent
load_old = """        const rev = item.exam_reviews || {};
        document.getElementById('review-psy').value = rev.psy || '';
        document.getElementById('review-math').value = rev.math || '';
        document.getElementById('review-eng').value = rev.eng || '';"""
load_new = """        const rev = item.exam_reviews || {};
        document.getElementById('review-score').value = rev.score || '';
        document.getElementById('review-academic').value = rev.academic || '';
        document.getElementById('review-psycho').value = rev.psycho || '';"""
content = content.replace(load_old, load_new)

# 3. Update checkExamStatus
check_old = """        const p = document.getElementById('review-psy').value.trim();
        const m = document.getElementById('review-math').value.trim();
        const e = document.getElementById('review-eng').value.trim();
        
        document.getElementById('status-psy').innerText = p ? 'Yazılıb' : 'Gözləyir';
        document.getElementById('status-psy').style.background = p ? 'var(--success)' : 'var(--warning)';
        
        document.getElementById('status-math').innerText = m ? 'Yazılıb' : 'Gözləyir';
        document.getElementById('status-math').style.background = m ? 'var(--success)' : 'var(--warning)';
        
        document.getElementById('status-eng').innerText = e ? 'Yazılıb' : 'Gözləyir';
        document.getElementById('status-eng').style.background = e ? 'var(--success)' : 'var(--warning)';
        
        const btns = document.querySelectorAll('.exam-send-btn');
        if (p && m && e) {"""
check_new = """        const score = document.getElementById('review-score').value.trim();
        const academic = document.getElementById('review-academic').value.trim();
        const psycho = document.getElementById('review-psycho').value.trim();
        
        document.getElementById('status-score').innerText = score ? 'Yazılıb' : 'Gözləyir';
        document.getElementById('status-score').style.background = score ? 'var(--success)' : 'var(--warning)';
        
        document.getElementById('status-academic').innerText = academic ? 'Yazılıb' : 'Gözləyir';
        document.getElementById('status-academic').style.background = academic ? 'var(--success)' : 'var(--warning)';
        
        document.getElementById('status-psycho').innerText = psycho ? 'Yazılıb' : 'Gözləyir';
        document.getElementById('status-psycho').style.background = psycho ? 'var(--success)' : 'var(--warning)';
        
        const btns = document.querySelectorAll('.exam-send-btn');
        if (score && academic && psycho) {"""
content = content.replace(check_old, check_new)

# 4. Update saveExamReviews
save_old = """        const rev = {
            psy: document.getElementById('review-psy').value.trim(),
            math: document.getElementById('review-math').value.trim(),
            eng: document.getElementById('review-eng').value.trim()
        };"""
save_new = """        const rev = {
            score: document.getElementById('review-score').value.trim(),
            academic: document.getElementById('review-academic').value.trim(),
            psycho: document.getElementById('review-psycho').value.trim()
        };"""
content = content.replace(save_old, save_new)

# 5. Update sendExamResult PDF HTML
html_old = """                <div style="margin-bottom:25px;">
                    <h3 style="color:#0f172a; border-bottom:1px solid #e2e8f0; padding-bottom:8px; font-size:18px;">Psixoloq Rəyi</h3>
                    <p style="white-space:pre-wrap; font-size:15px; line-height:1.6; color:#334155;">${rev.psy || 'Rəy yoxdur'}</p>
                </div>
                
                <div style="margin-bottom:25px;">
                    <h3 style="color:#0f172a; border-bottom:1px solid #e2e8f0; padding-bottom:8px; font-size:18px;">Riyaziyyat Rəyi</h3>
                    <p style="white-space:pre-wrap; font-size:15px; line-height:1.6; color:#334155;">${rev.math || 'Rəy yoxdur'}</p>
                </div>
                
                <div style="margin-bottom:25px;">
                    <h3 style="color:#0f172a; border-bottom:1px solid #e2e8f0; padding-bottom:8px; font-size:18px;">İngilis Dili Rəyi</h3>
                    <p style="white-space:pre-wrap; font-size:15px; line-height:1.6; color:#334155;">${rev.eng || 'Rəy yoxdur'}</p>
                </div>"""
html_new = """                <div style="margin-bottom:25px;">
                    <h3 style="color:#0f172a; border-bottom:1px solid #e2e8f0; padding-bottom:8px; font-size:18px;">Şagirdin İmtahan Balı</h3>
                    <p style="white-space:pre-wrap; font-size:15px; line-height:1.6; color:#334155;">${rev.score || 'Rəy yoxdur'}</p>
                </div>
                
                <div style="margin-bottom:25px;">
                    <h3 style="color:#0f172a; border-bottom:1px solid #e2e8f0; padding-bottom:8px; font-size:18px;">Akademik Qiymətləndirmə</h3>
                    <p style="white-space:pre-wrap; font-size:15px; line-height:1.6; color:#334155;">${rev.academic || 'Rəy yoxdur'}</p>
                </div>
                
                <div style="margin-bottom:25px;">
                    <h3 style="color:#0f172a; border-bottom:1px solid #e2e8f0; padding-bottom:8px; font-size:18px;">Psixoloji Müayinə Protokolu</h3>
                    <p style="white-space:pre-wrap; font-size:15px; line-height:1.6; color:#334155;">${rev.psycho || 'Rəy yoxdur'}</p>
                </div>"""
content = content.replace(html_old, html_new)

# Also add 'Müraciət etdiyi müəssisə' to PDF
header_old = """                <div style="background:#f8fafc; padding:20px; border-radius:10px; margin-bottom:30px;">
                    <p style="margin:0 0 10px 0; font-size:16px;"><strong>Şagird:</strong> ${fullName}</p>
                    <p style="margin:0; font-size:16px;"><strong>Sinif:</strong> ${className}</p>
                </div>"""
header_new = """                <div style="background:#f8fafc; padding:20px; border-radius:10px; margin-bottom:30px;">
                    <p style="margin:0 0 10px 0; font-size:16px;"><strong>Şagird:</strong> ${fullName}</p>
                    <p style="margin:0 0 10px 0; font-size:16px;"><strong>Sinif:</strong> ${className}</p>
                    <p style="margin:0; font-size:16px;"><strong>Müraciət etdiyi müəssisə:</strong> ${getGranularSource(item)}</p>
                </div>"""
content = content.replace(header_old, header_new)

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated admin.html")
