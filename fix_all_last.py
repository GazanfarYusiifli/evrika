import re

with open('victory.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Instagram updates
html = html.replace('@victory_az', '@victory.colleges')
html = html.replace('https://www.instagram.com/victory_az', 'https://www.instagram.com/victory.colleges')

old_ig_1 = 'DYke8I1MuNG'
old_ig_2 = 'DYg1dX1ssnb'
old_ig_3 = 'DYPVguhM6xS'

new_ig_1 = 'DZVJSn4CINw'
new_ig_2 = 'DYnHejPO-_3'
new_ig_3 = 'DW81xBLiG3D'

html = html.replace(old_ig_1, new_ig_1)
html = html.replace(old_ig_2, new_ig_2)
html = html.replace(old_ig_3, new_ig_3)


# 2. Images updates
# Replace hero bg
html = html.replace(
    "url('https://files.cdn-files-a.com/uploads/10086696/2000_695ef25fe482e.jpg')",
    "url('./assets/sekill1.jpeg')"
)

# Replace 1000720061.jpg with sekill2.jpeg
html = html.replace('./assets/1000720061.jpg', './assets/sekill2.jpeg')

# Replace 1000720090.jpg with sekill3.jpeg
html = html.replace('./assets/1000720090.jpg', './assets/sekill3.jpeg')


# 3. Move stats to Hero Card
# First, remove the stats from Haqqımızda
stats_in_about = r'<div style="margin-top: 30px; display: grid; grid-template-columns: repeat\(3, 1fr\); gap: 15px;">.*?</div>\s*</div>\s*</div>\s*</div>'
html = re.sub(stats_in_about, '</div></div>', html, flags=re.DOTALL)

# Then add them to hero-facts
old_hero_facts = r'<div class="hero-facts">\s*<div class="hero-fact"><div class="hero-fact-icon"><i class="fas fa-users"></i></div><div class="hero-fact-text"><strong>500\+ tələbə</strong><span>6 il təcrübə</span></div></div>\s*<div class="hero-fact"><div class="hero-fact-icon"><i class="fas fa-star"></i></div><div class="hero-fact-text"><strong>73% tələbəmiz</strong><span>1400\+ SAT əldə edib</span></div></div>\s*<div class="hero-fact"><div class="hero-fact-icon"><i class="fas fa-globe-americas"></i></div><div class="hero-fact-text"><strong>63 ölkədə</strong><span>tələbələrimiz var</span></div></div>\s*</div>'

new_hero_facts = """<div class="hero-facts" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px;">
        <div class="hero-fact"><div class="hero-fact-icon"><i class="fas fa-calendar-alt"></i></div><div class="hero-fact-text"><strong>8+</strong><span>İl</span></div></div>
        <div class="hero-fact"><div class="hero-fact-icon"><i class="fas fa-users"></i></div><div class="hero-fact-text"><strong>2000+</strong><span>Məmnun tələbə</span></div></div>
        <div class="hero-fact"><div class="hero-fact-icon"><i class="fas fa-award"></i></div><div class="hero-fact-text"><strong>170+</strong><span>Təqaüd Proqramı</span></div></div>
        <div class="hero-fact"><div class="hero-fact-icon"><i class="fas fa-user-graduate"></i></div><div class="hero-fact-text"><strong>500+ tələbə</strong><span>6 il təcrübə</span></div></div>
        <div class="hero-fact"><div class="hero-fact-icon"><i class="fas fa-star"></i></div><div class="hero-fact-text"><strong>73% tələbəmiz</strong><span>1400+ SAT əldə edib</span></div></div>
        <div class="hero-fact"><div class="hero-fact-icon"><i class="fas fa-globe-americas"></i></div><div class="hero-fact-text"><strong>63 ölkədə</strong><span>tələbələrimiz var</span></div></div>
      </div>"""

html = re.sub(old_hero_facts, new_hero_facts, html)

with open('victory.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updates applied successfully.")
