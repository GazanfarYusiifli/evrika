import re

file = 'index.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update initPartners logic to fetch from Supabase
old_init_partners = r'async function initPartners\(\) \{[\s\S]*?\}'
new_init_partners = """async function initPartners() {
          const API_URL = 'https://gziuhrlvagflokivfgwt.supabase.co/rest/v1';
          const API_KEY = 'sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP';
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
        }"""
content = re.sub(old_init_partners, new_init_partners, content)

# 2. Fix renderPartners to handle Supabase DB format (logo_url instead of logo)
old_render_partners = r'function renderPartners\(partners\) \{[\s\S]*?\}'
new_render_partners = """function renderPartners(partners) {
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
        }"""
content = re.sub(old_render_partners, new_render_partners, content)

# 3. Remove STATIC_PARTNERS logic block
static_logic_regex = r'const STATIC_PARTNERS = \[.*?\];[\s\n]*// Render partners immediately.*?\}'
content = re.sub(static_logic_regex, '', content, flags=re.DOTALL)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html updated for dynamic partners.")
