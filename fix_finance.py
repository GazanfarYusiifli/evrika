import re

with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace the #view-finance block
finance_html_new = """    <div id="view-finance" class="content" style="display: none;">
        <div style="display: flex; gap: 15px; margin-bottom: 25px;">
            <button id="btn-tab-report" class="btn-view" onclick="switchFinanceTab('report')" style="background: var(--accent); color: white; border: none; padding: 12px 25px; border-radius: 8px; font-weight: 700; cursor: pointer; transition: 0.3s;"><i class="fas fa-chart-pie" style="margin-right: 8px;"></i> Hesabatlıq</button>
            <button id="btn-tab-history" class="btn-view" onclick="switchFinanceTab('history')" style="background: rgba(255,255,255,0.05); color: white; border: 1px solid rgba(255,255,255,0.1); padding: 12px 25px; border-radius: 8px; font-weight: 700; cursor: pointer; transition: 0.3s;"><i class="fas fa-list-ul" style="margin-right: 8px;"></i> Ödəniş Tarixçəsi</button>
        </div>

        <div id="finance-view-report">
            <div class="stats-grid">
                <div class="ems-stat-card" style="--accent: var(--success);"><div class="ems-stat-icon"><i class="fas fa-arrow-up"></i></div><div class="stat-lab">Ümumi Epoint Gəliri</div><div class="stat-val" id="finance-monthly-income">0 <small style="font-size:1.2rem; opacity:0.4;">AZN</small></div></div>
                <div class="ems-stat-card" style="--accent: var(--warning);"><div class="ems-stat-icon"><i class="fas fa-percent"></i></div><div class="stat-lab">Ümumi Komissiya</div><div class="stat-val" id="finance-commission">0 <small style="font-size:1.2rem; opacity:0.4;">AZN</small></div></div>
                <div class="ems-stat-card" style="--accent: var(--royal-blue);"><div class="ems-stat-icon"><i class="fas fa-credit-card"></i></div><div class="stat-lab">Uğurlu Tranzaksiya</div><div class="stat-val" id="finance-tx-count">0</div></div>
            </div>
            <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 30px;">
                <div class="table-wrapper">
                    <div style="padding:25px; border-bottom:1px solid var(--border); display:flex; justify-content:space-between; align-items:center;">
                        <h3 style="font-weight:800;">Son Uğurlu Ödənişlər</h3>
                    </div>
                    <table>
                        <thead>
                          <tr>
                            <th>Müştəri</th>
                            <th>Məbləğ</th>
                            <th>Tarix</th>
                          </tr>
                        </thead>
                        <tbody id="finance-short-tbody">
                        </tbody>
                    </table>
                </div>
                <div class="stat-card">
                    <h3 style="margin-bottom:20px; font-weight:800;">Epoint Gəlir Dinamikası</h3>
                    <canvas id="financeChart" style="max-height: 250px;"></canvas>
                </div>
            </div>
        </div>

        <div id="finance-view-history" style="display: none;">
            <div class="table-wrapper">
                <div style="padding:25px; border-bottom:1px solid var(--border); display:flex; justify-content:space-between; align-items:center;">
                    <h3 style="font-weight:800;">Epoint Ödəniş Tarixçəsi</h3>
                    <button class="btn-view" style="font-size:0.75rem; background: var(--success); color: white; border: none;" onclick="alert('Excel export funksiyası hazırlanır')"><i class="fas fa-file-excel" style="margin-right:5px;"></i> Excel Yüklə</button>
                </div>
                <table>
                    <thead>
                      <tr>
                        <th>Kart Sahibi / Təsvir</th>
                        <th>Kart Nömrəsi / Növü</th>
                        <th>Məbləğ / Komissiya</th>
                        <th>RRN / Tarix</th>
                        <th>Sistem İcrası</th>
                      </tr>
                    </thead>
                    <tbody id="finance-history-tbody">
                    </tbody>
                </table>
            </div>
        </div>
    </div>"""

# regex to replace from <div id="view-finance" class="content" style="display: none;"> up to <!-- Exam Results & Reviews Panel -->
html = re.sub(r'<div id="view-finance" class="content" style="display: none;">.*?<!-- Exam Results & Reviews Panel -->',
              finance_html_new + '\n\n    <!-- Exam Results & Reviews Panel -->',
              html, flags=re.DOTALL)


# 2. Add switchFinanceTab to JS script
js_script = """
    window.switchFinanceTab = (tab) => {
        document.getElementById('finance-view-report').style.display = tab === 'report' ? 'block' : 'none';
        document.getElementById('finance-view-history').style.display = tab === 'history' ? 'block' : 'none';
        
        document.getElementById('btn-tab-report').style.background = tab === 'report' ? 'var(--accent)' : 'rgba(255,255,255,0.05)';
        document.getElementById('btn-tab-report').style.border = tab === 'report' ? 'none' : '1px solid rgba(255,255,255,0.1)';
        
        document.getElementById('btn-tab-history').style.background = tab === 'history' ? 'var(--accent)' : 'rgba(255,255,255,0.05)';
        document.getElementById('btn-tab-history').style.border = tab === 'history' ? 'none' : '1px solid rgba(255,255,255,0.1)';
    };
"""

# inject right before `window.renderFinance = () => {`
html = html.replace("window.renderFinance = () => {", js_script + "\n    window.renderFinance = () => {")

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(html)
