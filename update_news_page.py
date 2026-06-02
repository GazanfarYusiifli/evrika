import re

ach_file = 'achievements.html'
news_file = 'news.html'

with open(ach_file, 'r', encoding='utf-8') as f:
    ach_content = f.read()

with open(news_file, 'r', encoding='utf-8') as f:
    news_content = f.read()

# Extract from achievements.html up to the end of the Hero Section (</section>)
match = re.search(r'([\s\S]*?</section>)', ach_content)
if not match:
    print("Could not find hero section in achievements.html")
    exit()

top_part = match.group(1)

# Modify the top part for news.html
top_part = top_part.replace('<title>Uğurlarımız | Evrika Təhsil Ekosistemi</title>', '<title>Xəbərlərimiz | Evrika Təhsil Ekosistemi</title>')
top_part = top_part.replace('REKORD NƏTİCƏLƏR', 'YENİLİKLƏR')
top_part = top_part.replace('Uğurlarımız', 'Xəbərlərimiz')
top_part = top_part.replace('15 illik təcrübəmiz və minlərlə uğurlu məzunumuzla fəxr edirik. Akademik zəfərimiz şagirdlərimizin gələcəyidir.', 'Ən son yeniliklər, layihələr və xəbərlərimizlə tanış olun. Akademik nailiyyətlər və məktəb həyatı haqqında ən aktual məlumatlar.')

# Now, we extract the news grid from news.html
news_grid_match = re.search(r'(<div class="news-grid" id="news-grid">[\s\S]*?<footer)', news_content)
if not news_grid_match:
    print("Could not find news grid in news.html")
    exit()

news_grid_and_rest = news_grid_match.group(1)

# Extract the rest (footer and script) from achievements.html to keep consistency
footer_match = re.search(r'(<footer[\s\S]*)', ach_content)
if not footer_match:
    print("Could not find footer in achievements.html")
    exit()

footer_and_scripts = footer_match.group(1)

# We need the JS for fetching news from the original news.html!
js_match = re.search(r'(<script>\s*document\.addEventListener\(\'DOMContentLoaded\', \(\) => {[\s\S]*?</script>)', news_content)
if js_match:
    news_js = js_match.group(1)
else:
    # Let's try another regex
    js_match = re.search(r'(<script>[\s\S]*?fetchNews[\s\S]*?</script>)', news_content)
    if js_match:
        news_js = js_match.group(1)
    else:
        # Just grab the last script tag if nothing else
        all_scripts = re.findall(r'<script>[\s\S]*?</script>', news_content)
        news_js = all_scripts[-1] if all_scripts else ''

# Replace the ugurlar JS in the footer_and_scripts with the news JS
# In achievements, there's a script tag starting with `document.addEventListener('DOMContentLoaded', () => {` containing `ug-grid`
# Let's just append the news JS right before </body>
footer_and_scripts = re.sub(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', \(\) => {\s*const gallery = document\.getElementById\(\'ug-grid\'\);[\s\S]*?fetchMore\(\);\s*}\);\s*</script>', '', footer_and_scripts)

new_content = top_part + '\n<div class="container" style="padding-top: 50px;">\n' + news_grid_and_rest.replace('<footer', '</div>\n<footer') + footer_and_scripts.replace('</body>', news_js + '\n</body>')

with open(news_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated news.html successfully")
