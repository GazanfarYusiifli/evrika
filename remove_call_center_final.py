import re

file = 'admin.html'
with open(file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False

for i, line in enumerate(lines):
    # 1. Remove the sidebar link for call center
    if 'data-module="crm"' in line and 'Zəng Mərkəzi' in line:
        continue
    
    # 2. Skip the view-call-center block
    if '<div id="view-call-center" class="content"' in line or '<!-- CALL CENTER MODULE -->' in line:
        skip = True
        
    if skip and '<div id="view-apps"' in line:
        # Reached the next section, stop skipping
        skip = False

    if not skip:
        # 3. Remove 'call-center': 'Zəng Mərkəzi' from the titles dictionary
        if "'call-center': 'Zəng Mərkəzi'," in line:
            line = line.replace("'call-center': 'Zəng Mərkəzi',", "")
        new_lines.append(line)

with open(file, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Call center removed.")
