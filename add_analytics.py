import re

with open('admin.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the sidebar link
old_link = r'<a href="https://vercel.com/evrikaproject/evrika/analytics" target="_blank" class="sb-link" data-module="crm" style="text-decoration:none;"><i class="fas fa-chart-line"></i> <span>Analitika</span></a>'
new_link = r'<a href="#" class="sb-link" data-module="crm" onclick="switchView(\'analytics\')" style="text-decoration:none;"><i class="fas fa-chart-line"></i> <span>Analitika</span></a>'
content = content.replace(old_link, new_link)

# 2. Add the view-analytics HTML right before view-speed
html_to_add = """
    <div id="view-analytics" class="content" style="display: none;">
      <h2 style="color: white; margin-bottom: 20px;">Marketinq Analitikası (UTM)</h2>
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">
        <div class="stat-card" style="background: rgba(255,255,255,0.03); padding: 20px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05);">
          <h3 style="color: white; margin-bottom: 20px; font-size: 1.1rem; text-align: center;">Mənbələr üzrə (utm_source)</h3>
          <canvas id="utmSourceChart"></canvas>
        </div>
        <div class="stat-card" style="background: rgba(255,255,255,0.03); padding: 20px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05);">
          <h3 style="color: white; margin-bottom: 20px; font-size: 1.1rem; text-align: center;">Kampaniyalar üzrə (utm_campaign)</h3>
          <canvas id="utmCampaignChart"></canvas>
        </div>
      </div>
    </div>
"""
content = content.replace('<div id="view-speed"', html_to_add + '\n    <div id="view-speed"')

# 3. Add window.utmSourceChart and window.utmCampaignChart variables
# Right before function renderDashboard()
js_to_add = """
    window.utmSourceChartObj = null;
    window.utmCampaignChartObj = null;

    function renderAnalytics() {
      const sourceCounts = {};
      const campaignCounts = {};

      rawData.forEach(item => {
        let source = item.utm_source || item.utm_medium || '';
        let campaign = item.utm_campaign || '';
        
        if (source) {
            source = source.toLowerCase().trim();
            if (source.includes('face') || source.includes('fb')) source = 'Facebook';
            else if (source.includes('insta') || source.includes('ig')) source = 'Instagram';
            else if (source.includes('goog') || source.includes('gl')) source = 'Google';
            sourceCounts[source] = (sourceCounts[source] || 0) + 1;
        }

        if (campaign) {
            campaign = campaign.trim();
            campaignCounts[campaign] = (campaignCounts[campaign] || 0) + 1;
        }
      });

      const sLabels = Object.keys(sourceCounts).length > 0 ? Object.keys(sourceCounts) : ['Məlumat yoxdur'];
      const sData = Object.keys(sourceCounts).length > 0 ? Object.values(sourceCounts) : [1];
      
      const cLabels = Object.keys(campaignCounts).length > 0 ? Object.keys(campaignCounts) : ['Məlumat yoxdur'];
      const cData = Object.keys(campaignCounts).length > 0 ? Object.values(campaignCounts) : [1];

      // Colors
      const colors = ['#E11D48', '#2563EB', '#10B981', '#F59E0B', '#8B5CF6'];

      // Source Chart
      const ctxS = document.getElementById('utmSourceChart');
      if (ctxS) {
          if (window.utmSourceChartObj) window.utmSourceChartObj.destroy();
          window.utmSourceChartObj = new Chart(ctxS.getContext('2d'), {
              type: 'doughnut',
              data: {
                  labels: sLabels,
                  datasets: [{
                      data: sData,
                      backgroundColor: colors,
                      borderWidth: 0
                  }]
              },
              options: {
                  plugins: { legend: { labels: { color: 'white' }, position: 'bottom' } },
                  cutout: '65%'
              }
          });
      }

      // Campaign Chart
      const ctxC = document.getElementById('utmCampaignChart');
      if (ctxC) {
          if (window.utmCampaignChartObj) window.utmCampaignChartObj.destroy();
          window.utmCampaignChartObj = new Chart(ctxC.getContext('2d'), {
              type: 'bar',
              data: {
                  labels: cLabels,
                  datasets: [{
                      label: 'Müraciət sayı',
                      data: cData,
                      backgroundColor: 'rgba(225, 29, 72, 0.8)',
                      borderRadius: 6
                  }]
              },
              options: {
                  plugins: { legend: { display: false } },
                  scales: {
                      y: { ticks: { color: 'rgba(255,255,255,0.7)', stepSize: 1 }, grid: { color: 'rgba(255,255,255,0.1)' } },
                      x: { ticks: { color: 'rgba(255,255,255,0.7)' }, grid: { display: false } }
                  }
              }
          });
      }
    }

"""
content = content.replace('    function renderDashboard() {', js_to_add + '    function renderDashboard() {')

# 4. Trigger renderAnalytics on load/switch
content = content.replace('renderDashboard(); renderApps();', 'renderDashboard(); renderApps(); renderAnalytics();')
content = content.replace("if(t==='dashboard') renderDashboard();", "if(t==='dashboard') renderDashboard();\n      if(t==='analytics') renderAnalytics();")


with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Analytics script added successfully.")
