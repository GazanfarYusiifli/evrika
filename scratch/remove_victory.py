import glob, re, os, json

def clean_file(path, func):
    if not os.path.exists(path):
        return
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = func(content)
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {path}")

# 1. Clean dropdowns and mobile accordions across ALL html files
html_files = [f for f in glob.glob('*.html') if f not in ['victory.html', 'register-victory.html']]

dropdown_pattern = re.compile(
    r'\s*<a\s+[^>]*href=[\"\']victory\.html[\"\'][^>]*class=[\"\']dropdown-item[\"\'][^>]*>.*?</a>',
    re.DOTALL
)

dropdown_pattern_alt = re.compile(
    r'\s*<a\s+class=[\"\']dropdown-item[\"\'][^>]*href=[\"\']victory\.html[\"\'][^>]*>.*?</a>',
    re.DOTALL
)

acc_pattern = re.compile(
    r'\s*<a\s+[^>]*href=[\"\']victory\.html[\"\'][^>]*>\s*<div\s+class=[\"\']acc-icon[\"\']><i\s+class=[\"\']fas fa-graduation-cap[\"\']></i></div>\s*<div\s+class=[\"\']acc-text[\"\']>.*?</div>\s*</a>',
    re.DOTALL
)

for hf in html_files:
    def remove_nav_items(text):
        t1 = dropdown_pattern.sub('', text)
        t2 = dropdown_pattern_alt.sub('', t1)
        t3 = acc_pattern.sub('', t2)
        return t3
    clean_file(hf, remove_nav_items)

# 2. Specific page cleanups:
# --- index.html ---
def clean_index(text):
    # Slide 5
    text = re.sub(r'\s*<!-- Slide 5: Victory Colleges by Evrika -->.*?(?=\s*<!-- Slide 6: Zümrüd Women Club -->)', '', text, flags=re.DOTALL)
    # Entity 4
    text = re.sub(r'\s*<!-- Entity 4: Victory Colleges by Evrika -->.*?(?=\s*<!-- Entity 5: Zumrud -->)', '', text, flags=re.DOTALL)
    # Renumber Entity 5 to Entity 4
    text = text.replace('<!-- Entity 5: Zumrud -->', '<!-- Entity 4: Zumrud -->')
    text = text.replace('data-id="5"', 'data-id="4"')
    text = text.replace('05</div>', '04</div>')
    # Select option eduhome
    text = re.sub(r'\s*<option\s+value=[\"\']eduhome[\"\'][^>]*>.*?</option>', '', text)
    # Sector branch === 'eduhome'
    text = re.sub(r'\}\s*else\s+if\s*\(\s*branch\s*===\s*[\'\"]eduhome[\'\"].*?\}(?=\s*if\s*\(window\.updateContent\))', '', text, flags=re.DOTALL)
    # schoolRegistry eduhome
    text = re.sub(r'\s*eduhome:\s*\{[^}]*\},?', '', text)
    return text

clean_file('index.html', clean_index)

# --- live_index_vercel.html ---
def clean_live_index(text):
    text = re.sub(r'\s*<!-- Slide 5: Victory Colleges by Evrika -->.*?(?=\s*<!-- Slide 6: Zümrüd Women Club -->)', '', text, flags=re.DOTALL)
    text = re.sub(r'\s*<!-- Entity 4: Eduhome -->.*?(?=\s*<!-- Entity 5: Zumrud -->)', '', text, flags=re.DOTALL)
    text = text.replace('<!-- Entity 5: Zumrud -->', '<!-- Entity 4: Zumrud -->')
    text = text.replace('data-id="5"', 'data-id="4"')
    text = text.replace('05</div>', '04</div>')
    text = re.sub(r'\s*<option\s+value=[\"\']eduhome[\"\'][^>]*>.*?</option>', '', text)
    text = re.sub(r'\}\s*else\s+if\s*\(\s*branch\s*===\s*[\'\"]eduhome[\'\"].*?\}(?=\s*if\s*\(window\.updateContent\))', '', text, flags=re.DOTALL)
    text = re.sub(r'\s*eduhome:\s*\{[^}]*\},?', '', text)
    return text

clean_file('live_index_vercel.html', clean_live_index)

# --- schools.html ---
def clean_schools(text):
    # Remove Item 4
    text = re.sub(r'\s*<!-- Item 4: Victory Colleges by Evrika -->.*?(?=\s*<!-- Item 5: Zumrud -->)', '', text, flags=re.DOTALL)
    # Renumber Item 5 to Item 4
    text = text.replace('<!-- Item 5: Zumrud -->', '<!-- Item 4: Zumrud -->')
    text = text.replace('hub-card-5', 'hub-card-4')
    return text

clean_file('schools.html', clean_schools)

# --- branches.html ---
def clean_branches(text):
    text = re.sub(r'\s*<!-- Eduhome -->.*?(?=\s*<!-- Zumrud -->)', '', text, flags=re.DOTALL)
    return text

clean_file('branches.html', clean_branches)

# --- contact.html ---
def clean_contact(text):
    text = re.sub(r'\{\s*name:\s*\"Victory Colleges by Evrika\".*?\},\s*', '', text, flags=re.DOTALL)
    return text

clean_file('contact.html', clean_contact)

# --- news.html ---
def clean_news(text):
    # Remove news card with id=3 (Victory Colleges partnership)
    text = re.sub(r'\s*<a\s+href=[\"\']news-detail\.html\?id=3[\"\']\s+class=[\"\']news-card[\"\']>.*?</a>', '', text, flags=re.DOTALL)
    return text

clean_file('news.html', clean_news)

# --- src/main.js ---
def clean_main_js(text):
    # Remove 4: from schools registry object
    text = re.sub(r'\s*4:\s*\{\s*badge:\s*\"Akademik Dəstək\",\s*name:\s*\"Victory Colleges by Evrika Mərkəzi\".*?cta:\s*\"Konsultasiya Rezerv Et\"\s*\},?', '', text, flags=re.DOTALL)
    # In school-modal links, remove eduhome logic
    text = text.replace("id === '4' ? 'eduhome' : ", "")
    return text

clean_file('src/main.js', clean_main_js)

# --- vercel.json ---
def clean_vercel_json(text):
    data = json.loads(text)
    new_rewrites = []
    for r in data.get('rewrites', []):
        src = r.get('source', '')
        dest = r.get('destination', '')
        if src in ['/eduhome', '/register-eduhome', '/victory', '/register-victory'] or dest in ['/victory.html', '/register-victory.html']:
            continue
        new_rewrites.append(r)
    data['rewrites'] = new_rewrites
    return json.dumps(data, indent=2)

clean_file('vercel.json', clean_vercel_json)

# 3. Remove victory.html and register-victory.html files
for f_del in ['victory.html', 'register-victory.html']:
    if os.path.exists(f_del):
        os.remove(f_del)
        print(f"Deleted file {f_del}")

print("Cleanup complete!")
