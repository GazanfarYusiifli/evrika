import re

file = 'achievements.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the sort logic in JS after fetching
search_fetch = r"""            if \(res.ok\) \{
              const data = await res.json\(\);
              data.forEach\(item => \{"""
replace_fetch = """            if (res.ok) {
              let data = await res.json();
              data.sort((a,b) => (parseInt(a.payload.seq)||0) - (parseInt(b.payload.seq)||0));
              data.forEach(item => {"""
content = re.sub(search_fetch, replace_fetch, content, count=1)

# 2. Update the card HTML to remove the text block
search_card = r"""                  card.innerHTML = `
                    <div class="ug-img-box-modern">
                      <img src="\$\{u.img\}" alt="\$\{u.name\}">
                      <div class="ug-overlay-modern"></div>
                    </div>
                    <div class="ug-content-modern">
                      <h3>\$\{u.name\}</h3>
                      <p>\$\{u.uni \|\| ''\}</p>
                    </div>
                  `;"""
replace_card = """                  card.innerHTML = `
                    <div class="ug-img-box-modern">
                      <img src="${u.img}" alt="Uğur">
                      <div class="ug-overlay-modern"></div>
                    </div>
                  `;"""
content = re.sub(search_card, replace_card, content, count=1)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("achievements.html updated successfully")
