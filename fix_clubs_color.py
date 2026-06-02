import re

with open('montessori.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the section background
old_section = '<section class="section stack-wrapper" style="background: #070d1f; padding: 120px 0;">'
new_section = """<style>
  .clubs-white-bg { background: #ffffff !important; }
  .clubs-white-bg .category-title { color: #9ba278 !important; }
  .clubs-white-bg .category-title em { color: #9ba278 !important; }
  .clubs-white-bg p { color: #9ba278 !important; opacity: 0.8; }
  .clubs-white-bg .club-name { color: #9ba278 !important; }
  .clubs-white-bg .club-icon { color: #9ba278 !important; }
  .clubs-white-bg .club-card {
    background: rgba(155, 162, 120, 0.05);
    border-color: rgba(155, 162, 120, 0.2);
  }
  .clubs-white-bg .club-card:hover {
    background: rgba(155, 162, 120, 0.1);
  }
</style>
<section class="section stack-wrapper clubs-white-bg" style="background: #ffffff; padding: 120px 0;">"""

content = content.replace(old_section, new_section)

with open('montessori.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Clubs section updated")
