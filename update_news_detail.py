import re

news_file = 'news.html'
detail_file = 'news-detail.html'

with open(news_file, 'r', encoding='utf-8') as f:
    news_content = f.read()

with open(detail_file, 'r', encoding='utf-8') as f:
    detail_content = f.read()

# Extract the header (from <!DOCTYPE html> to </header>...</div> representing mobile nav)
header_match = re.search(r'([\s\S]*?<main>)', news_content)
if not header_match:
    print("Could not find header in news.html")
    exit()

head_and_nav = header_match.group(1)
# Modify title
head_and_nav = head_and_nav.replace('<title>Xəbərlərimiz | Evrika Təhsil Ekosistemi</title>', '<title>Xəbər Təfərrüatı | Evrika Təhsil Ekosistemi</title>')

# We also need to add the specific CSS for news-detail.html that we extracted
detail_styles = """
<style>
.article-hero { margin-top: 40px; border-radius: 20px; overflow: hidden; height: 450px; box-shadow: 0 20px 40px rgba(0,0,0,0.1); }
.article-hero img { width: 100%; height: 100%; object-fit: cover; }

.article-content { background: white; margin-top: -60px; position: relative; z-index: 10; border-radius: 20px; padding: 50px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
.article-date { color: var(--burgundy); font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 20px; display: block; }
.article-title { font-size: 2.5rem; font-weight: 800; color: var(--navy); line-height: 1.2; margin-bottom: 30px; }
.article-text { font-size: 1.15rem; line-height: 1.8; color: #444; white-space: pre-wrap; }

.other-news-section { margin-top: 80px; padding-bottom: 80px; }
.other-news-title { font-size: 1.5rem; font-weight: 800; color: var(--navy); margin-bottom: 30px; display: flex; align-items: center; gap: 15px; }
.other-news-title::after { content:""; flex: 1; height: 2px; background: #eee; }

.small-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; }
.small-card { background: white; border-radius: 12px; overflow: hidden; text-decoration: none; color: inherit; box-shadow: 0 5px 15px rgba(0,0,0,0.05); transition: 0.3s; }
.small-card:hover { transform: translateY(-5px); }
.small-card img { width: 100%; height: 160px; object-fit: cover; }
.small-card-body { padding: 15px; }
.small-card-title { font-size: 0.95rem; font-weight: 700; line-height: 1.4; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; color: var(--navy); }
</style>
"""

head_and_nav = head_and_nav.replace('</head>', detail_styles + '</head>')

# Extract the content of news-detail.html
content_match = re.search(r'(<div class="container">\s*<div id="article-view">[\s\S]*?</section>\s*</div>)', detail_content)
if not content_match:
    print("Could not find article content in news-detail.html")
    exit()

article_content = content_match.group(1)
article_content = article_content.replace('<div class="container">', '<div class="container" style="padding-top: 100px;">')

# Extract footer and scripts from news.html
footer_match = re.search(r'(<footer[\s\S]*)', news_content)
if not footer_match:
    print("Could not find footer in news.html")
    exit()

footer = footer_match.group(1)

# Extract detail scripts
detail_js_match = re.search(r'(<script>\s*const API_URL = \'https://miwvdhwrmxoetszkxlzy\.supabase\.co[\s\S]*?loadDetail\(\);\s*</script>)', detail_content)
if detail_js_match:
    detail_js = detail_js_match.group(1)
else:
    detail_js = ""

# Merge footer and replace news.html's fetch script with news-detail.html's loadDetail script
# Remove the old script
footer = re.sub(r'<script>\s*document\.addEventListener\("DOMContentLoaded", async function\(\) {[\s\S]*?</script>', '', footer)

final_content = head_and_nav + '\n' + article_content + '\n</main>\n' + footer.replace('</body>', detail_js + '\n</body>')

with open(detail_file, 'w', encoding='utf-8') as f:
    f.write(final_content)

print("Updated news-detail.html successfully")
