import re

with open('victory.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix hero facts (keep only the first 3)
old_hero_facts_6 = r'<div class="hero-facts" style="display: grid; grid-template-columns: repeat\(2, 1fr\); gap: 15px;">\s*<div class="hero-fact"><div class="hero-fact-icon"><i class="fas fa-calendar-alt"></i></div><div class="hero-fact-text"><strong>8\+</strong><span>İl</span></div></div>\s*<div class="hero-fact"><div class="hero-fact-icon"><i class="fas fa-users"></i></div><div class="hero-fact-text"><strong>2000\+</strong><span>Məmnun tələbə</span></div></div>\s*<div class="hero-fact"><div class="hero-fact-icon"><i class="fas fa-award"></i></div><div class="hero-fact-text"><strong>170\+</strong><span>Təqaüd Proqramı</span></div></div>\s*<div class="hero-fact"><div class="hero-fact-icon"><i class="fas fa-user-graduate"></i></div><div class="hero-fact-text"><strong>500\+ tələbə</strong><span>6 il təcrübə</span></div></div>\s*<div class="hero-fact"><div class="hero-fact-icon"><i class="fas fa-star"></i></div><div class="hero-fact-text"><strong>73% tələbəmiz</strong><span>1400\+ SAT əldə edib</span></div></div>\s*<div class="hero-fact"><div class="hero-fact-icon"><i class="fas fa-globe-americas"></i></div><div class="hero-fact-text"><strong>63 ölkədə</strong><span>tələbələrimiz var</span></div></div>\s*</div>'

new_hero_facts_3 = """<div class="hero-facts">
        <div class="hero-fact"><div class="hero-fact-icon"><i class="fas fa-calendar-alt"></i></div><div class="hero-fact-text"><strong>8+</strong><span>İl</span></div></div>
        <div class="hero-fact"><div class="hero-fact-icon"><i class="fas fa-users"></i></div><div class="hero-fact-text"><strong>2000+</strong><span>Məmnun tələbə</span></div></div>
        <div class="hero-fact"><div class="hero-fact-icon"><i class="fas fa-award"></i></div><div class="hero-fact-text"><strong>170+</strong><span>Təqaüd Proqramı</span></div></div>
      </div>"""

html = re.sub(old_hero_facts_6, new_hero_facts_3, html)


# 2. Fix image styles so they show full size (not 50% border radius)
# I replaced `.about-img-side img` earlier. Let's make sure there are no other border-radius 50% rules affecting it.
html = re.sub(r'border-radius:\s*50%;', 'border-radius: 24px;', html)

# 3. Fix Instagram embeds again! The embed URL requires a proper format.
# A standard instagram embed iframe URL is:
# https://www.instagram.com/p/CODE/embed
# But the blockquote format requires:
# data-instgrm-permalink="https://www.instagram.com/p/CODE/?utm_source=ig_embed&amp;utm_campaign=loading"
# Let's ensure the URLs are cleanly formatted without double query params
html = html.replace('DZVJSn4CINw/?utm_source=ig_embed&amp;utm_campaign=loading?utm_source=ig_embed&utm_campaign=loading', 'DZVJSn4CINw/?utm_source=ig_embed&amp;utm_campaign=loading')
html = html.replace('DYnHejPO-_3/?utm_source=ig_embed&amp;utm_campaign=loading?utm_source=ig_embed&utm_campaign=loading', 'DYnHejPO-_3/?utm_source=ig_embed&amp;utm_campaign=loading')
html = html.replace('DW81xBLiG3D/?utm_source=ig_embed&amp;utm_campaign=loading?utm_source=ig_embed&utm_campaign=loading', 'DW81xBLiG3D/?utm_source=ig_embed&amp;utm_campaign=loading')

# To be absolutely sure, let's just rewrite the instagram blockquotes using a clean iframe approach if the blockquote script doesn't run, or make sure the blockquote script is there.
# Let's check if the embed.js is included at the bottom:
if 'instagram.com/embed.js' not in html:
    html = html.replace('</body>', '<script async src="https://www.instagram.com/embed.js"></script>\n</body>')

with open('victory.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Victory HTML updated.")
