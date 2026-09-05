file = 'index.html'
with open(file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_content = """        function renderPartners(partners) {
          const grid = document.getElementById('partners-grid-content');
          if (!grid) return;
          const repeated = [...partners, ...partners, ...partners, ...partners, ...partners];
          grid.innerHTML = repeated.map(p => {
            const logo = p.logo_url || p.logo;
            let imgStyle = '';
            if (p.name === 'APEIA' || (p.logo_url && p.logo_url.includes('aotmalogo'))) imgStyle = 'transform: scale(1.6);';
            return `
            <div class="partner-item">
              <img src="${logo}" alt="${p.name}" ${imgStyle ? `style="${imgStyle}"` : ''}>
              <span class="partner-name">${p.name}</span>
              ${p.description ? `
                <div class="partner-overlay">
                  <div style="font-weight: 800; color: white; font-size: 0.85rem; text-transform: uppercase; margin-bottom: 5px;">${p.name}</div>
                  <div class="partner-info-text">${p.description}</div>
                </div>
              ` : ''}
            </div>
            `;
          }).join('');
        }

        async function initPartners() {
          const API_URL = 'https://osicmnagzeqkhwticiqp.supabase.co/rest/v1';
          const API_KEY = 'sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE';
          const HEADERS = { 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY };
          try {
            const res = await fetch(`${API_URL}/partners?select=*&order=sort_order.asc`, { headers: HEADERS });
            if (res.ok) {
              const data = await res.json();
              renderPartners(data);
            }
          } catch (e) {
            console.error('Failed to load partners from Supabase:', e);
          }
        }
"""

# Replace lines 3722 to 3785 (0-indexed 3721 to 3785)
lines = lines[:3722] + [new_content] + lines[3785:]

with open(file, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Syntax error fixed.")
