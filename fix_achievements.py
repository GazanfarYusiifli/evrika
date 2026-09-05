import re

file = 'achievements.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the hardcoded cards inside <div class="ugurlar-masonry" id="ug-grid"> with empty
masonry_regex = r'<div class="ugurlar-masonry" id="ug-grid">[\s\S]*?<!-- Dinamik məlumatlar admin paneldən yüklənəcək -->'
empty_masonry = '<div class="ugurlar-masonry" id="ug-grid">\n            <!-- Dinamik məlumatlar admin paneldən yüklənəcək -->'
content = re.sub(masonry_regex, empty_masonry, content)

# 2. Add the JS fetch logic before the closing </body> tag
fetch_script = """
<script>
document.addEventListener('DOMContentLoaded', async () => {
    const API_URL = 'https://osicmnagzeqkhwticiqp.supabase.co/rest/v1';
    const API_KEY = 'sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE';
    const HEADERS = { 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY };

    const grid = document.getElementById('ug-grid');
    if (!grid) return;

    try {
        const res = await fetch(`${API_URL}/ugurlar?select=*&order=id.desc`, { headers: HEADERS });
        if (res.ok) {
            const data = await res.json();
            grid.innerHTML = data.map(item => {
                const p = item.payload;
                return `
                <div class="ug-card-modern" data-name="${p.name || ''}" data-uni="${p.uni || ''}" data-img="${p.img || ''}">
                  <img src="${p.img || ''}" alt="${p.name || ''}" loading="lazy">
                  <div class="overlay-text">
                    <h3 data-i18n="ach-card-title">${p.name || ''}</h3>
                    <p>${p.uni || ''}</p>
                  </div>
                </div>`;
            }).join('');
        }
    } catch (e) {
        console.error('Failed to load ugurlar:', e);
    }
});
</script>
"""

# Insert before Whelp script to ensure it runs
content = content.replace('<!-- Whelp Widget Code -->', fetch_script + '\n<!-- Whelp Widget Code -->')

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("achievements.html updated to load ugurlar dynamically.")
