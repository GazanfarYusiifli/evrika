import re

with open('victory.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove stats-band
start_stats = content.find('<div class="stats-band">')
end_stats = content.find('</div>\n</div>\n\n<section class="section" id="about">')
if start_stats != -1 and end_stats != -1:
    content = content[:start_stats] + content[end_stats + 14:]
    print("Removed stats-band.")
else:
    print("Could not find stats-band bounds.")

# Remove 10+ İL TƏCRÜBƏ
about_float_str = '<div class="about-float"><span class="num">10+</span><span class="lbl">İl Təcrübə</span></div>'
if about_float_str in content:
    content = content.replace(about_float_str, '')
    print("Removed 10+ İl Təcrübə.")
else:
    print("Could not find 10+ İl Təcrübə.")

with open('victory.html', 'w', encoding='utf-8') as f:
    f.write(content)

