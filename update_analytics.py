import re

with open('admin.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the view-analytics block
new_html = """    <div id="view-analytics" class="content" style="display: none;">
      <div class="section-header" style="display:flex; justify-content:space-between; align-items:center;">
        <div>
          <h2 style="font-size:1.8rem; font-weight:900; color:var(--white);">Sayt Analitikası <span style="font-size:0.9rem; font-weight:600; color:var(--text-muted); background:rgba(255,255,255,0.05); padding:4px 8px; border-radius:6px; margin-left:10px;">Vercel API</span></h2>
          <p style="color:var(--text-muted); margin-top:5px;">Real vaxt rejimində istifadəçi və trafik statistikaları (Son 30 gün)</p>
        </div>
        <div>
          <button onclick="loadVercelAnalytics()" class="btn btn-primary" style="background:#3B82F6; color:white; border:none; padding:10px 20px; border-radius:8px; font-weight:700; cursor:pointer;"><i class="fas fa-sync-alt" id="analytics-refresh-icon"></i> Məlumatları Yenilə</button>
        </div>
      </div>
      
      <!-- Loading Skeleton -->
      <div id="analytics-loading" style="display:none; text-align:center; padding:50px;">
          <i class="fas fa-circle-notch fa-spin" style="font-size:3rem; color:#3B82F6;"></i>
          <p style="color:rgba(255,255,255,0.6); margin-top:15px; font-weight:600;">Məlumatlar Vercel-dən çəkilir...</p>
      </div>

      <!-- Error State -->
      <div id="analytics-error" style="display:none; background:rgba(239,68,68,0.1); border:1px solid rgba(239,68,68,0.3); border-radius:16px; padding:20px; margin-top:20px; color:#EF4444;">
          <h3 style="font-weight:700;"><i class="fas fa-exclamation-triangle"></i> Xəta Baş Verdi</h3>
          <p id="analytics-error-text" style="font-size:0.9rem; margin-top:10px;"></p>
          <p style="font-size:0.8rem; margin-top:10px; opacity:0.8;">Qeyd: Əmin olun ki, VERCEL_TOKEN, VERCEL_PROJECT_ID və VERCEL_TEAM_ID Vercel layihənizin Environment Variables bölməsinə əlavə edilib.</p>
      </div>

      <!-- Analytics Dashboard -->
      <div id="analytics-dashboard" style="display:none; margin-top:30px;">
          <!-- 4 Stats Cards -->
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:20px; margin-bottom:30px;">
              <div style="background:rgba(255,255,255,0.03); border:1px solid var(--glass-border); border-radius:16px; padding:20px;">
                  <p style="color:var(--text-muted); font-size:0.9rem; font-weight:600; text-transform:uppercase;">Visitors</p>
                  <h3 id="stat-visitors" style="font-size:2rem; font-weight:800; color:white; margin-top:10px;">-</h3>
              </div>
              <div style="background:rgba(255,255,255,0.03); border:1px solid var(--glass-border); border-radius:16px; padding:20px;">
                  <p style="color:var(--text-muted); font-size:0.9rem; font-weight:600; text-transform:uppercase;">Pageviews</p>
                  <h3 id="stat-pageviews" style="font-size:2rem; font-weight:800; color:white; margin-top:10px;">-</h3>
              </div>
              <div style="background:rgba(255,255,255,0.03); border:1px solid var(--glass-border); border-radius:16px; padding:20px;">
                  <p style="color:var(--text-muted); font-size:0.9rem; font-weight:600; text-transform:uppercase;">Countries</p>
                  <h3 id="stat-countries" style="font-size:2rem; font-weight:800; color:white; margin-top:10px;">-</h3>
              </div>
              <div style="background:rgba(255,255,255,0.03); border:1px solid var(--glass-border); border-radius:16px; padding:20px;">
                  <p style="color:var(--text-muted); font-size:0.9rem; font-weight:600; text-transform:uppercase;">Events</p>
                  <h3 id="stat-events" style="font-size:2rem; font-weight:800; color:white; margin-top:10px;">-</h3>
              </div>
          </div>

          <!-- Main Chart -->
          <div style="background:rgba(255,255,255,0.03); border:1px solid var(--glass-border); border-radius:16px; padding:25px; margin-bottom:30px;">
              <h3 style="color:white; font-weight:700; font-size:1.2rem; margin-bottom:20px;">Traffic Overview (Son 30 gün)</h3>
              <div style="height:350px; width:100%;">
                  <canvas id="analytics-traffic-chart"></canvas>
              </div>
          </div>

          <!-- 2 Columns: Top Pages & Countries -->
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(400px, 1fr)); gap:30px; margin-bottom:30px;">
              <div style="background:rgba(255,255,255,0.03); border:1px solid var(--glass-border); border-radius:16px; padding:25px;">
                  <h3 style="color:white; font-weight:700; font-size:1.1rem; margin-bottom:15px;">Top Pages</h3>
                  <div style="overflow-x:auto;">
                      <table style="width:100%; text-align:left; color:white; font-size:0.9rem;" id="analytics-pages-table">
                          <thead>
                              <tr style="color:var(--text-muted); border-bottom:1px solid rgba(255,255,255,0.1);">
                                  <th style="padding:10px 0;">Səhifə (Path)</th>
                                  <th style="padding:10px 0; text-align:right;">Baxış</th>
                              </tr>
                          </thead>
                          <tbody></tbody>
                      </table>
                  </div>
              </div>
              <div style="background:rgba(255,255,255,0.03); border:1px solid var(--glass-border); border-radius:16px; padding:25px;">
                  <h3 style="color:white; font-weight:700; font-size:1.1rem; margin-bottom:15px;">Top Countries</h3>
                  <div style="overflow-x:auto;">
                      <table style="width:100%; text-align:left; color:white; font-size:0.9rem;" id="analytics-countries-table">
                          <thead>
                              <tr style="color:var(--text-muted); border-bottom:1px solid rgba(255,255,255,0.1);">
                                  <th style="padding:10px 0;">Ölkə</th>
                                  <th style="padding:10px 0; text-align:right;">Ziyarətçi</th>
                              </tr>
                          </thead>
                          <tbody></tbody>
                      </table>
                  </div>
              </div>
          </div>

          <!-- 3 Columns: Browsers, Devices, Referrers -->
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(300px, 1fr)); gap:30px;">
              <div style="background:rgba(255,255,255,0.03); border:1px solid var(--glass-border); border-radius:16px; padding:25px;">
                  <h3 style="color:white; font-weight:700; font-size:1.1rem; margin-bottom:20px;">Browsers</h3>
                  <div style="height:250px; width:100%; position:relative;">
                      <canvas id="analytics-browser-chart"></canvas>
                  </div>
              </div>
              <div style="background:rgba(255,255,255,0.03); border:1px solid var(--glass-border); border-radius:16px; padding:25px;">
                  <h3 style="color:white; font-weight:700; font-size:1.1rem; margin-bottom:20px;">Devices</h3>
                  <div style="height:250px; width:100%; position:relative;">
                      <canvas id="analytics-device-chart"></canvas>
                  </div>
              </div>
              <div style="background:rgba(255,255,255,0.03); border:1px solid var(--glass-border); border-radius:16px; padding:25px; overflow-y:auto; max-height:350px;">
                  <h3 style="color:white; font-weight:700; font-size:1.1rem; margin-bottom:15px;">Referrers</h3>
                  <table style="width:100%; text-align:left; color:white; font-size:0.9rem;" id="analytics-referrers-table">
                      <thead>
                          <tr style="color:var(--text-muted); border-bottom:1px solid rgba(255,255,255,0.1);">
                              <th style="padding:10px 0;">Mənbə</th>
                              <th style="padding:10px 0; text-align:right;">Ziyarət</th>
                          </tr>
                      </thead>
                      <tbody></tbody>
                  </table>
              </div>
          </div>
      </div>
    </div>"""

# Find the old view-analytics block
pattern_view = r'<div id="view-analytics".*?</div>\n    </div>'
content = re.sub(r'<div id="view-analytics".*?Vercel Dashboard-a Keç\s*</a>\n\s*</div>\n\s*</div>', new_html, content, flags=re.DOTALL)


# 2. Add the JS logic for Vercel Analytics at the end of the script tag in admin.html
js_logic = """
    // --- Vercel Analytics Dashboard Logic ---
    let analyticsCharts = {};

    window.loadVercelAnalytics = async () => {
        const loading = document.getElementById('analytics-loading');
        const dashboard = document.getElementById('analytics-dashboard');
        const errorDiv = document.getElementById('analytics-error');
        const errorText = document.getElementById('analytics-error-text');
        const icon = document.getElementById('analytics-refresh-icon');

        loading.style.display = 'block';
        dashboard.style.display = 'none';
        errorDiv.style.display = 'none';
        if (icon) icon.classList.add('fa-spin');

        try {
            // We use from/to for the last 30 days
            const to = new Date();
            const from = new Date();
            from.setDate(from.getDate() - 30);
            const fromISO = from.toISOString();
            const toISO = to.toISOString();
            const timeParams = `from=${fromISO}&to=${toISO}`;

            // 1. Fetch Overall Stats (Visitors, Pageviews)
            const countRes = await fetch(`/api/vercel-analytics?queryType=visits-count&${timeParams}&groupBy=page`);
            if (!countRes.ok) {
                const err = await countRes.json();
                throw new Error(err.details || 'Failed to fetch visits count');
            }
            const countData = await countRes.json();
            
            // Note: The structure of Vercel Analytics API response might vary. 
            // We will attempt to parse it based on typical telemetry structures.
            // aggregate data for charts
            const aggViewsRes = await fetch(`/api/vercel-analytics?queryType=visits-aggregate&${timeParams}&groupBy=day`);
            const aggViewsData = await aggViewsRes.json();

            // aggregate for top pages
            const topPagesRes = await fetch(`/api/vercel-analytics?queryType=visits-aggregate&${timeParams}&groupBy=page&limit=10`);
            const topPagesData = await topPagesRes.json();

            // aggregate for countries
            const countriesRes = await fetch(`/api/vercel-analytics?queryType=visits-aggregate&${timeParams}&groupBy=country&limit=10`);
            const countriesData = await countriesRes.json();

            // aggregate for browsers
            const browsersRes = await fetch(`/api/vercel-analytics?queryType=visits-aggregate&${timeParams}&groupBy=browser&limit=5`);
            const browsersData = await browsersRes.json();

            // aggregate for devices
            const devicesRes = await fetch(`/api/vercel-analytics?queryType=visits-aggregate&${timeParams}&groupBy=device&limit=5`);
            const devicesData = await devicesRes.json();

            // aggregate for referrers
            const referrersRes = await fetch(`/api/vercel-analytics?queryType=visits-aggregate&${timeParams}&groupBy=referrer&limit=10`);
            const referrersData = await referrersRes.json();

            // events count
            const eventsRes = await fetch(`/api/vercel-analytics?queryType=events-count&${timeParams}`);
            const eventsData = await eventsRes.json();

            // === Update DOM ===
            
            // We assume data structure from Vercel is { data: [ { key: '...', visits: 100 } ] } or similar
            // If it's just raw arrays, we adapt. Let's write a safe getter.
            const getSum = (dataArr, field = 'visits') => Array.isArray(dataArr) ? dataArr.reduce((acc, curr) => acc + (curr[field] || curr.count || 0), 0) : 0;
            const getDataArray = (res) => Array.isArray(res) ? res : (res.data || []);

            const totalVisitors = getSum(getDataArray(countData), 'visitors');
            const totalPageviews = getSum(getDataArray(countData), 'visits') || getSum(getDataArray(aggViewsData), 'visits');
            const totalCountries = getDataArray(countriesData).length;
            const totalEvents = getSum(getDataArray(eventsData), 'events') || getSum(getDataArray(eventsData), 'count');

            document.getElementById('stat-visitors').innerText = totalVisitors > 0 ? totalVisitors.toLocaleString() : '-';
            document.getElementById('stat-pageviews').innerText = totalPageviews > 0 ? totalPageviews.toLocaleString() : '-';
            document.getElementById('stat-countries').innerText = totalCountries > 0 ? totalCountries.toLocaleString() : '-';
            document.getElementById('stat-events').innerText = totalEvents > 0 ? totalEvents.toLocaleString() : '-';

            // --- Tables ---
            const populateTable = (tableId, data, keyName, valName) => {
                const tbody = document.querySelector(`#${tableId} tbody`);
                tbody.innerHTML = '';
                const arr = getDataArray(data);
                if (arr.length === 0) {
                    tbody.innerHTML = `<tr><td colspan="2" style="text-align:center; padding:15px; color:rgba(255,255,255,0.4);">Məlumat yoxdur</td></tr>`;
                    return;
                }
                arr.forEach(item => {
                    const k = item[keyName] || item.key || 'Naməlum';
                    const v = item[valName] || item.visits || item.count || 0;
                    tbody.innerHTML += `
                        <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
                            <td style="padding:12px 0;">${k}</td>
                            <td style="padding:12px 0; text-align:right; font-weight:700;">${v.toLocaleString()}</td>
                        </tr>
                    `;
                });
            };

            populateTable('analytics-pages-table', topPagesData, 'page', 'visits');
            populateTable('analytics-countries-table', countriesData, 'country', 'visits');
            populateTable('analytics-referrers-table', referrersData, 'referrer', 'visits');

            // --- Charts ---
            const destroyChart = (name) => {
                if (analyticsCharts[name]) { analyticsCharts[name].destroy(); }
            };

            // Main Traffic Chart
            destroyChart('traffic');
            const ctxTraffic = document.getElementById('analytics-traffic-chart').getContext('2d');
            const trafficArr = getDataArray(aggViewsData);
            
            // Format labels for chart
            const labels = trafficArr.map(i => {
                const d = new Date(i.key || i.day || i.date);
                return isNaN(d) ? (i.key || '') : `${d.getDate()}/${d.getMonth()+1}`;
            });
            const visits = trafficArr.map(i => i.visits || i.count || 0);

            analyticsCharts['traffic'] = new Chart(ctxTraffic, {
                type: 'line',
                data: {
                    labels: labels.length > 0 ? labels : ['No Data'],
                    datasets: [{
                        label: 'Səhifə baxışları',
                        data: visits.length > 0 ? visits : [0],
                        borderColor: '#3B82F6',
                        backgroundColor: 'rgba(59, 130, 246, 0.1)',
                        borderWidth: 3,
                        pointBackgroundColor: '#3B82F6',
                        pointBorderColor: '#fff',
                        pointHoverBackgroundColor: '#fff',
                        pointHoverBorderColor: '#3B82F6',
                        fill: true,
                        tension: 0.4
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        y: { beginAtZero: true, grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: 'rgba(255,255,255,0.5)' } },
                        x: { grid: { display: false }, ticks: { color: 'rgba(255,255,255,0.5)' } }
                    },
                    plugins: {
                        legend: { display: false },
                        tooltip: { backgroundColor: 'rgba(0,0,0,0.8)', titleFont: { size: 13 }, bodyFont: { size: 14, weight: 'bold' }, padding: 12, cornerRadius: 8, displayColors: false }
                    }
                }
            });

            // Browser Pie Chart
            destroyChart('browser');
            const ctxBrowser = document.getElementById('analytics-browser-chart').getContext('2d');
            const browserArr = getDataArray(browsersData);
            analyticsCharts['browser'] = new Chart(ctxBrowser, {
                type: 'doughnut',
                data: {
                    labels: browserArr.length > 0 ? browserArr.map(i => i.browser || i.key || 'Naməlum') : ['No Data'],
                    datasets: [{
                        data: browserArr.length > 0 ? browserArr.map(i => i.visits || i.count || 0) : [1],
                        backgroundColor: ['#3B82F6', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6'],
                        borderWidth: 0,
                        hoverOffset: 4
                    }]
                },
                options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { position: 'right', labels: { color: 'white', boxWidth: 12 } }, tooltip: { backgroundColor: 'rgba(0,0,0,0.8)' } }, cutout: '70%' }
            });

            // Device Pie Chart
            destroyChart('device');
            const ctxDevice = document.getElementById('analytics-device-chart').getContext('2d');
            const deviceArr = getDataArray(devicesData);
            analyticsCharts['device'] = new Chart(ctxDevice, {
                type: 'doughnut',
                data: {
                    labels: deviceArr.length > 0 ? deviceArr.map(i => i.device || i.key || 'Naməlum') : ['No Data'],
                    datasets: [{
                        data: deviceArr.length > 0 ? deviceArr.map(i => i.visits || i.count || 0) : [1],
                        backgroundColor: ['#EC4899', '#6366F1', '#14B8A6', '#F97316', '#06B6D4'],
                        borderWidth: 0,
                        hoverOffset: 4
                    }]
                },
                options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { position: 'right', labels: { color: 'white', boxWidth: 12 } }, tooltip: { backgroundColor: 'rgba(0,0,0,0.8)' } }, cutout: '70%' }
            });

            loading.style.display = 'none';
            dashboard.style.display = 'block';
        } catch (error) {
            console.error('Analytics Error:', error);
            errorText.innerText = error.message;
            loading.style.display = 'none';
            errorDiv.style.display = 'block';
        } finally {
            if (icon) icon.classList.remove('fa-spin');
        }
    };
    
    // Inject load call into switchTab if analytics is clicked
    const oldSwitchTab = window.switchTab;
    window.switchTab = (t) => {
        oldSwitchTab(t);
        if (t === 'analytics') {
            loadVercelAnalytics();
        }
    };
</script>
"""

content = content.replace("</script>\n</body>", js_logic + "\n</body>")

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(content)
