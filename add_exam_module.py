import re

with open('admin.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Sidebar Link
sidebar_insert = """
      <div class="sb-group-title" data-module="exam">İMTAHAN</div>
      <div class="sb-link" data-module="exam" onclick="switchTab('exam-results')"><i class="fas fa-file-signature"></i> <span>Nəticələr & Rəylər</span></div>
      
      <div class="sb-group-title">SİSTEM</div>"""
content = content.replace('<div class="sb-group-title">SİSTEM</div>', sidebar_insert)

# 2. Add Content Block
exam_html = """
    <!-- Exam Results & Reviews Panel -->
    <div id="view-exam-results" class="content" style="display: none;">
        <div class="stats-grid">
            <div class="ems-stat-card" style="--accent: var(--royal-blue);"><div class="ems-stat-icon"><i class="fas fa-user-graduate"></i></div><div class="stat-lab">İmtahan Verənlər</div><div class="stat-val">24</div></div>
            <div class="ems-stat-card" style="--accent: var(--warning);"><div class="ems-stat-icon"><i class="fas fa-clock"></i></div><div class="stat-lab">Rəy Gözləyən</div><div class="stat-val">8</div></div>
            <div class="ems-stat-card" style="--accent: var(--success);"><div class="ems-stat-icon"><i class="fas fa-check-double"></i></div><div class="stat-lab">Tamamlanmış</div><div class="stat-val">16</div></div>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1.5fr; gap: 30px;">
            <!-- Student List -->
            <div class="table-wrapper" style="height: 600px; overflow-y: auto;">
                <div style="padding:20px; border-bottom:1px solid var(--border); background:rgba(255,255,255,0.01);">
                    <h3 style="font-weight:800; font-size:1.1rem;"><i class="fas fa-list-ul" style="color:var(--burgundy); margin-right:10px;"></i> Şagirdlərin Siyahısı</h3>
                </div>
                <table>
                    <thead><tr><th>Şagird</th><th>Sinif</th><th>Status</th></tr></thead>
                    <tbody id="exam-students-list">
                        <tr onclick="loadExamStudent(1)" style="cursor:pointer;"><td>Əli Məmmədov</td><td>5-ci sinif</td><td><span style="color:var(--warning); font-weight:700;">Gözləyir</span></td></tr>
                        <tr onclick="loadExamStudent(2)" style="cursor:pointer;"><td>Aylin Quliyeva</td><td>6-cı sinif</td><td><span style="color:var(--success); font-weight:700;">Tamamlanıb</span></td></tr>
                        <tr onclick="loadExamStudent(3)" style="cursor:pointer;"><td>Nicat Səfərov</td><td>8-ci sinif</td><td><span style="color:var(--warning); font-weight:700;">Gözləyir</span></td></tr>
                    </tbody>
                </table>
            </div>

            <!-- Review Panel -->
            <div class="stat-card" id="exam-review-panel" style="display: flex; flex-direction: column; opacity: 0.5; pointer-events: none; transition: 0.3s;">
                <h3 style="margin-bottom: 25px; font-weight: 900; font-size: 1.4rem; border-bottom: 1px solid var(--border); padding-bottom: 15px;">
                    <i class="fas fa-user-edit" style="color:var(--burgundy); margin-right: 10px;"></i> 
                    <span id="exam-student-name">Şagird Seçin</span>
                </h3>

                <div style="flex:1; display:flex; flex-direction:column; gap:20px; overflow-y:auto; padding-right:10px;">
                    
                    <!-- Subject 1: Psixoloq -->
                    <div style="background: rgba(255,255,255,0.03); padding: 20px; border-radius: 16px; border: 1px solid var(--border);">
                        <div style="display:flex; justify-content:space-between; margin-bottom: 10px;">
                            <h4 style="color:var(--royal-blue); font-weight:800; font-size:0.9rem;"><i class="fas fa-brain"></i> Psixoloq Rəyi</h4>
                            <span id="status-psy" style="font-size:0.7rem; padding:3px 8px; border-radius:10px; background:var(--warning); color:white; font-weight:700;">Gözləyir</span>
                        </div>
                        <textarea class="admin-input exam-review-input" data-subject="psy" placeholder="Psixoloji dəyərləndirməni bura yazın..." style="height:80px; resize:vertical;"></textarea>
                    </div>

                    <!-- Subject 2: Riyaziyyat -->
                    <div style="background: rgba(255,255,255,0.03); padding: 20px; border-radius: 16px; border: 1px solid var(--border);">
                        <div style="display:flex; justify-content:space-between; margin-bottom: 10px;">
                            <h4 style="color:var(--royal-blue); font-weight:800; font-size:0.9rem;"><i class="fas fa-square-root-alt"></i> Riyaziyyat Rəyi</h4>
                            <span id="status-math" style="font-size:0.7rem; padding:3px 8px; border-radius:10px; background:var(--warning); color:white; font-weight:700;">Gözləyir</span>
                        </div>
                        <textarea class="admin-input exam-review-input" data-subject="math" placeholder="Riyazi biliklərin yoxlanması nəticələri..." style="height:80px; resize:vertical;"></textarea>
                    </div>

                    <!-- Subject 3: İngilis Dili -->
                    <div style="background: rgba(255,255,255,0.03); padding: 20px; border-radius: 16px; border: 1px solid var(--border);">
                        <div style="display:flex; justify-content:space-between; margin-bottom: 10px;">
                            <h4 style="color:var(--royal-blue); font-weight:800; font-size:0.9rem;"><i class="fas fa-language"></i> İngilis Dili Rəyi</h4>
                            <span id="status-eng" style="font-size:0.7rem; padding:3px 8px; border-radius:10px; background:var(--warning); color:white; font-weight:700;">Gözləyir</span>
                        </div>
                        <textarea class="admin-input exam-review-input" data-subject="eng" placeholder="İngilis dili səviyyəsi haqqında..." style="height:80px; resize:vertical;"></textarea>
                    </div>

                </div>

                <div style="margin-top: 25px; padding-top: 20px; border-top: 1px solid var(--border); display:flex; justify-content:space-between; align-items:center;">
                    <div style="font-size: 0.8rem; color: var(--text-muted);">
                        <i class="fas fa-info-circle"></i> Bütün müəllimlər rəy yazdıqdan sonra göndərmək aktivləşəcək.
                    </div>
                    <button id="exam-send-btn" class="btn-view" disabled style="background: var(--text-muted); color: rgba(255,255,255,0.5); border: none; padding: 15px 30px; font-size: 0.9rem; cursor: not-allowed;" onclick="sendExamResult()">
                        <i class="fas fa-paper-plane"></i> Nəticəni Valideynə Göndər (PDF)
                    </button>
                </div>
            </div>
        </div>
    </div>
"""
content = content.replace('<!-- Leadership / Management Panel -->', exam_html + '\n    <!-- Leadership / Management Panel -->')

# 3. Add Script logic for the new section
script_logic = """
<script>
    // Exam Review Logic
    function loadExamStudent(id) {
        const panel = document.getElementById('exam-review-panel');
        panel.style.opacity = '1';
        panel.style.pointerEvents = 'auto';
        
        const nameMap = {1: 'Əli Məmmədov', 2: 'Aylin Quliyeva', 3: 'Nicat Səfərov'};
        document.getElementById('exam-student-name').innerText = nameMap[id] + " (ID: " + id + ")";
        
        // Clear or load existing data (Simulation)
        document.querySelectorAll('.exam-review-input').forEach(input => {
            input.value = (id === 2) ? 'Simulyasiya edilmiş rəy mətni...' : '';
            checkReviewStatus(input);
        });
        checkAllReviews();
    }

    document.querySelectorAll('.exam-review-input').forEach(input => {
        input.addEventListener('input', function() {
            checkReviewStatus(this);
            checkAllReviews();
        });
    });

    function checkReviewStatus(input) {
        const subject = input.getAttribute('data-subject');
        const badge = document.getElementById('status-' + subject);
        if(input.value.trim().length > 5) {
            badge.innerText = 'Yazılıb';
            badge.style.background = 'var(--success)';
        } else {
            badge.innerText = 'Gözləyir';
            badge.style.background = 'var(--warning)';
        }
    }

    function checkAllReviews() {
        let allFilled = true;
        document.querySelectorAll('.exam-review-input').forEach(input => {
            if(input.value.trim().length <= 5) allFilled = false;
        });

        const btn = document.getElementById('exam-send-btn');
        if(allFilled) {
            btn.disabled = false;
            btn.style.background = 'var(--success)';
            btn.style.color = 'white';
            btn.style.cursor = 'pointer';
        } else {
            btn.disabled = true;
            btn.style.background = 'var(--text-muted)';
            btn.style.color = 'rgba(255,255,255,0.5)';
            btn.style.cursor = 'not-allowed';
        }
    }

    function sendExamResult() {
        const btn = document.getElementById('exam-send-btn');
        btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Göndərilir...';
        btn.disabled = true;
        
        // Simulate PDF generation & Email/WhatsApp sending
        setTimeout(() => {
            btn.innerHTML = '<i class="fas fa-check"></i> Göndərildi!';
            btn.style.background = '#3B82F6';
            alert('Nəticələr PDF formatında valideynin E-poçt və WhatsApp nömrəsinə uğurla göndərildi!');
            
            setTimeout(() => {
                btn.innerHTML = '<i class="fas fa-paper-plane"></i> Nəticəni Valideynə Göndər (PDF)';
                btn.disabled = false;
                btn.style.background = 'var(--success)';
            }, 3000);
        }, 2000);
    }
</script>
</body>
"""

content = content.replace('</body>', script_logic)

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added exam results module")
