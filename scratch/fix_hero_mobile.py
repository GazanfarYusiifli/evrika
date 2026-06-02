import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Hide #heroControls on mobile in index.html
# Find @media (max-width: 768px) inside the hero controls style block
pattern = r'(@media\s*\(max-width:\s*768px\)\s*{)(\s*\.hero-controls-container\s*{[^}]*})'
replacement = r'\1\n          .hero-controls-container { display: none !important; }'
new_content = re.sub(pattern, replacement, content)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_content)

# 2. Update style.css for .hero-video-slider on mobile
with open("src/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Add height fix to the mobile media query
mobile_hero_css = """
  .hero-video-slider {
    min-height: unset !important;
    height: 100vh !important;
    height: 100svh !important;
  }
"""

# Find @media (max-width: 768px) { in style.css and inject
if "@media (max-width: 768px) {" in css:
    css = css.replace("@media (max-width: 768px) {", "@media (max-width: 768px) {\n" + mobile_hero_css)
else:
    css += "\n@media (max-width: 768px) {" + mobile_hero_css + "\n}\n"

with open("src/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Updated index.html and style.css")
