import glob
import re

files = glob.glob('*.html')

news_dropdown_item = """
            <a href="news.html" class="dropdown-item">
              <div class="item-icon"><i class="fas fa-newspaper"></i></div>
              <div class="dropdown-item-text">
                <span class="dropdown-item-title">Xəbərlər</span>
                <span class="dropdown-item-desc">Ən son yeniliklər</span>
              </div>
            </a>"""

achievements_pattern = r'(<a href="achievements\.html"[^>]*>[\s\S]*?</a>)'

for filepath in files:
    if filepath in ['admin.html', 'verify.html', 'payment.html', 'admin-login.html']:
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(achievements_pattern, content)
    if match and "news.html" not in content[match.end():match.end() + 500]:
        content = content[:match.end()] + news_dropdown_item + content[match.end():]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added news.html to dropdown in {filepath}")
    elif match:
        print(f"news.html already in {filepath}")

