import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Remove the display: none !important that I previously added for .hero-controls-container
content = re.sub(r'\.hero-controls-container\s*{\s*display:\s*none\s*!important;\s*}', '', content)

# But we STILL need to hide the play button and make the arrows small.
# Wait, let's look for @media (max-width: 768px) inside the style block of index.html 
# where hero-controls-container is defined.
# I'll just replace the whole style block from <style> .hero-controls-container to </style>
# to be clean.

# Let's find the original CSS block. It started with .hero-controls-container {
# We will inject a new robust CSS block.
