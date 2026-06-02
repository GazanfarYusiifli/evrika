import glob
import re

files = glob.glob('*.html')

news_mobile_item = """
          <a href="news.html">
            <div class="acc-icon"><i class="fas fa-newspaper"></i></div>
            <div class="acc-text"><span class="acc-title">Xəbərlər</span><span class="acc-desc">Ən son yeniliklər</span></div>
          </a>"""

# We look for the end of the achievements block in the mobile accordion
achievements_mob_pattern = r'(<a href="achievements\.html"[^>]*>[\s\S]*?</a>)'

for filepath in files:
    if filepath in ['admin.html', 'verify.html', 'payment.html', 'admin-login.html']:
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The achievements link occurs twice: once in nav-dropdown, once in mobile-accordion
    # We want to replace the SECOND occurrence (or all occurrences)
    # Actually, let's just find all matches and replace them
    
    matches = list(re.finditer(achievements_mob_pattern, content))
    if len(matches) >= 2:
        # The second match is usually the mobile accordion one
        match = matches[1]
        if "news.html" not in content[match.end():match.end() + 500]:
            content = content[:match.end()] + news_mobile_item + content[match.end():]
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added news.html to mobile accordion in {filepath}")
        else:
            print(f"news.html already in mobile accordion of {filepath}")

