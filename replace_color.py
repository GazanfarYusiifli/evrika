import re

filepath = 'montessori.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace any text color setting of #070d1f with #5c4033
# Using regex to match color: #070d1f with optional spaces and optional !important
# We want to match: color:\s*#070d1f
content = re.sub(r'color:\s*#070d1f', 'color: #5c4033', content, flags=re.IGNORECASE)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Replaced text colors in {filepath}")
