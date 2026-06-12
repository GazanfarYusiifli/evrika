import re

with open('victory.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix hero background gradient (remove yellow)
html = html.replace(
    'linear-gradient(135deg,rgba(40,35,0,0.92) 0%,rgba(90,80,0,0.8) 50%,rgba(20,18,0,0.95) 100%)',
    'linear-gradient(135deg,rgba(14,27,65,0.95) 0%,rgba(20,40,100,0.8) 50%,rgba(2,6,23,0.98) 100%)'
)

# 2. Fix reg-section background gradient (remove yellow)
html = html.replace(
    '#292500',
    'rgba(14,27,65,0.8)'
)

# 3. Replace hero-facts items
old_facts = r'<div class="hero-facts">.*?<div class="hero-fact"><div class="hero-fact-icon"><i class="fas fa-language"></i></div><div class="hero-fact-text"><strong>IELTS / TOEFL / SAT</strong><span>İntensiv dil və test hazırlığı</span></div></div>.*?</div>'
new_facts = """<div class="hero-facts">
        <div class="hero-fact"><div class="hero-fact-icon"><i class="fas fa-users"></i></div><div class="hero-fact-text"><strong>500+ tələbə</strong><span>6 il təcrübə</span></div></div>
        <div class="hero-fact"><div class="hero-fact-icon"><i class="fas fa-star"></i></div><div class="hero-fact-text"><strong>73% tələbəmiz</strong><span>1400+ SAT əldə edib</span></div></div>
        <div class="hero-fact"><div class="hero-fact-icon"><i class="fas fa-globe-americas"></i></div><div class="hero-fact-text"><strong>63 ölkədə</strong><span>tələbələrimiz var</span></div></div>
      </div>"""
# Since old_facts might have multiple newlines, let's just find and replace the block
html = re.sub(r'<div class="hero-facts">.*?Tam proses boyunca yanınızda</span></div></div>\s*</div>', new_facts, html, flags=re.DOTALL)

with open('victory.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updates applied")
