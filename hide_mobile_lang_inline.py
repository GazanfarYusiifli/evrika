import glob
import re

files = ['lisey.html', 'lisey2.html', 'montessori.html', 'victory.html', 'zumrud.html']

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to add an inline <style> to hide desktop-lang-wrapper explicitly in each file
    # just in case style.css is cached by the user.
    inline_style = """
<style>
@media (max-width: 1024px) {
  .nav-actions .desktop-lang-wrapper, 
  .nav-actions .lang-dropdown-wrapper {
    display: none !important;
  }
}
</style>
"""
    if "/* mobile-lang-hide */" not in content:
        # insert before </head>
        content = content.replace("</head>", "/* mobile-lang-hide */" + inline_style + "\n</head>")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
