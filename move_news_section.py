import re

filepath = 'index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

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

# Insert it before `<!-- Partnerships Section -->`
content = content.replace("<!-- Partnerships Section -->", news_section + "\n    <!-- Partnerships Section -->")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Moved news section before Partnerships Section")
