import glob
import re

for filepath in glob.glob('*.html'):
    if filepath in ['admin.html', 'verify.html']:
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace all occurrences of "Evrika Məktəbli Jurnalı" with "Evrika Jurnalı"
    content = content.replace('Evrika Məktəbli Jurnalı', 'Evrika Jurnalı')

    # Add a class `desktop-lang-wrapper` to the nav-actions language dropdown
    # We only want to add it to the one inside <div class="nav-actions">
    # So we can match `<div class="nav-actions">` and the first `class="lang-dropdown-wrapper"` after it.
    
    parts = content.split('<div class="nav-actions">')
    if len(parts) > 1:
        new_parts = [parts[0]]
        for part in parts[1:]:
            # Replace the first lang-dropdown-wrapper in this part
            part = re.sub(r'<div class="lang-dropdown-wrapper"', r'<div class="lang-dropdown-wrapper desktop-lang-wrapper"', part, count=1)
            new_parts.append(part)
        content = '<div class="nav-actions">'.join(new_parts)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Update style.css
with open('src/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

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

print("Updates applied.")
