import re

with open('/tmp/old_index.html', 'r', encoding='utf-8') as f:
    old_content = f.read()

# Extract Parents HTML
parents_html_match = re.search(r'<!-- Premium Dynamic Parent Testimonials -->.*?(?=<!-- Founder/Message Section)', old_content, re.DOTALL)
if parents_html_match:
    with open('scratch/parents_html.txt', 'w', encoding='utf-8') as f:
        f.write(parents_html_match.group(0))

# Extract News HTML
news_html_match = re.search(r'<!-- LATEST NEWS SECTION -->.*?(?=<!-- Partnerships Section -->)', old_content, re.DOTALL)
if news_html_match:
    with open('scratch/news_html.txt', 'w', encoding='utf-8') as f:
        f.write(news_html_match.group(0))

# Extract Parents JS
# It starts with "async function initParentTestimonials()"
parents_js_match = re.search(r'async function initParentTestimonials\(\).*?}\n', old_content, re.DOTALL)
if parents_js_match:
    with open('scratch/parents_js.txt', 'w', encoding='utf-8') as f:
        f.write(parents_js_match.group(0))

# Extract News JS
# It starts around "const grid = document.getElementById('home-news-grid');"
# Let's search for the block that fetches news in index.html
news_js_match = re.search(r'try \{\s+const res = await fetch\(`\$\{NEWS_API_URL\}.*?\}\n', old_content, re.DOTALL)
# Actually, the news fetching is probably inside a DOMContentLoaded block in index.html.
# Let's find exactly the fetch logic for home-news-grid.
grid_match = re.search(r'const grid = document.getElementById\(\'home-news-grid\'\);.*?catch\(e\).*?\}', old_content, re.DOTALL)
if grid_match:
    with open('scratch/news_js.txt', 'w', encoding='utf-8') as f:
        f.write(grid_match.group(0))

print("Extraction complete.")
