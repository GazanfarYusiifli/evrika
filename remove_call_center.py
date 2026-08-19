import re

file = 'admin.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the sidebar link
content = re.sub(
    r'<div class="sb-link"\s+data-module="crm"\s+onclick="switchTab\(\'call-center\'\)".*?Zəng Mərkəzi</span></div>\n?',
    '',
    content
)

# 2. Remove the 'call-center' key from the JS titles dictionary
content = re.sub(r"'call-center': 'Zəng Mərkəzi',\s*", '', content)

# 3. Find and remove the view-call-center div
# Since regex for balanced HTML is tricky, we can do it by finding the start and end string
start_str = '<!-- CALL CENTER MODULE -->'
# Find where this section ends. Let's see what the next module is.
