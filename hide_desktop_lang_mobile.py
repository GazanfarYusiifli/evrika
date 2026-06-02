import glob
import re

for filepath in glob.glob('*.html'):
    if filepath in ['admin.html', 'verify.html']:
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The desktop lang button wrapper needs a class like 'desktop-lang' to hide it on mobile via inline style, 
    # or we can just append a style tag inside <head> if we don't want to edit style.css, but we have style.css.
    # Actually, we can add a class `desktop-lang-wrapper` to the desktop button and hide it with inline style or `<style>` block.
    # But wait! I can just do this inline in the HTML:
    content = re.sub(r'(<div class="lang-dropdown-wrapper"[^>]*?)(\s*style=")', r'\1 class="desktop-lang-wrapper"\2', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

with open('src/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add a rule to hide desktop-lang-wrapper on mobile
if '.desktop-lang-wrapper' not in css:
    css_to_add = """
@media (max-width: 992px) {
  .nav-actions .desktop-lang-wrapper {
    display: none !important;
  }
}
"""
    css += css_to_add
    with open('src/style.css', 'w', encoding='utf-8') as f:
        f.write(css)

print("Hidden desktop lang on mobile.")
