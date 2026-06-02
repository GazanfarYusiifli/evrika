import re

filepath = 'index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add "Xəbərlər" to Haqqımızda Dropdown
# Let's find: <a href="achievements.html" class="dropdown-item">...</a>
news_dropdown_item = """
            <a href="news.html" class="dropdown-item">
              <div class="item-icon"><i class="fas fa-newspaper"></i></div>
              <div class="dropdown-item-text">
                <span class="dropdown-item-title">Xəbərlər</span>
                <span class="dropdown-item-desc">Ən son yeniliklər</span>
              </div>
            </a>"""

# Insert it after achievements dropdown item
# We can search for the end of the achievements block
achievements_pattern = r'(<a href="achievements\.html".*?</a>)'
match = re.search(achievements_pattern, content, re.DOTALL)
if match and "news.html" not in content[:match.end() + 500]:
    content = content[:match.end()] + news_dropdown_item + content[match.end():]


# 2. Insert the News section before "ƏMƏKDAŞLIQLARIMIZ"
news_section = """
  <!-- LATEST NEWS SECTION -->
  <section class="section section-light" id="news-section">
    <div class="container">
      <div class="sec-header text-center" style="margin-bottom: 60px;">
        <div class="premium-eyebrow" style="letter-spacing: 0.5em; color: var(--burgundy); font-weight: 800; font-size: 0.8rem; margin-bottom: 20px; text-transform: uppercase;">YENİLİKLƏR</div>
        <h2 class="titan-header" style="font-size: clamp(2.5rem, 5vw, 4rem); color: var(--navy); line-height: 1.1; font-weight: 900; letter-spacing: -0.02em;">Son Xəbərlər</h2>
      </div>
      <div class="news-grid" id="home-news-grid">
         <div style="text-align:center; width:100%; grid-column:1/-1; opacity:0.5; font-size:1.2rem;"><i class="fas fa-spinner fa-spin"></i> Xəbərlər yüklənir...</div>
      </div>
      <div style="text-align: center; margin-top: 50px;">
        <a href="news.html" class="btn btn-xl btn-primary" style="padding: 16px 40px; border-radius: 30px;">Daha Çoxu <i class="fas fa-arrow-right"></i></a>
      </div>
    </div>
  </section>
"""

# The partners section starts somewhere with `<!-- Partners Section -->` or `<div class="premium-eyebrow"...ƏMƏKDAŞLIQLARIMIZ`
# Let's search for `<section class="section section-dark"` just above `ƏMƏKDAŞLIQLARIMIZ`
# Wait, let's just find the section that contains ƏMƏKDAŞLIQLARIMIZ
partners_match = re.search(r'(<section[^>]*>[\s\S]*?ƏMƏKDAŞLIQLARIMIZ[\s\S]*?</section>)', content)
if partners_match and "LATEST NEWS SECTION" not in content:
    content = content.replace(partners_match.group(1), news_section + "\n" + partners_match.group(1))

# 3. Add fetching script at the end
fetch_script = """
  <script>
    document.addEventListener("DOMContentLoaded", async function() {
        const grid = document.getElementById('home-news-grid');
        if(!grid) return;
        try {
            const API_URL = 'https://miwvdhwrmxoetszkxlzy.supabase.co/rest/v1';
            const API_KEY = 'sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV';
            const res = await fetch(`${API_URL}/news?select=*&order=id.desc&limit=3`, {
                headers: { 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY }
            });
            if(res.ok) {
                const data = await res.json();
                if(!data.length) {
                    grid.innerHTML = '<div style="text-align:center; width:100%; grid-column:1/-1; opacity:0.5; font-size:1.2rem;">Hələ ki, heç bir xəbər yoxdur.</div>';
                    return;
                }
                grid.innerHTML = data.map(row => {
                    const n = row.payload;
                    const dateStr = n.date || "";
                    const parts = dateStr.split(/[-./]/);
                    const months = ["Yan", "Fev", "Mar", "Apr", "May", "İyn", "İyl", "Avq", "Sen", "Okt", "Noy", "Dek"];
                    
                    let day = "13", month = "Apr";
                    if(parts.length === 3) {
                        if(parts[0].length === 4) {
                            day = parts[2];
                            month = months[parseInt(parts[1]) - 1] || "Ay";
                        } else {
                            day = parts[0];
                            month = months[parseInt(parts[1]) - 1] || "Ay";
                        }
                    }
                    
                    return `
                        <a href="news-detail.html?id=${row.id}" class="news-card">
                            <div class="card-media">
                                <img src="${n.img}" alt="${n.title}" loading="lazy">
                                <div class="date-badge">
                                    <strong>${day}</strong>
                                    <span>${month}</span>
                                </div>
                            </div>
                            <div class="card-body">
                                <div class="card-cat">EVRİKA YENİLİK</div>
                                <h3 class="card-title">${n.title}</h3>
                                <p class="card-desc">${n.text}</p>
                                <div class="card-footer">TAM OXU <i class="fas fa-arrow-right"></i></div>
                            </div>
                        </a>
                    `;
                }).join('');
            }
        } catch(e) {}
    });
  </script>
"""

if "home-news-grid" not in content or fetch_script not in content:
    content = content.replace("</body>", fetch_script + "\n</body>")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html")
