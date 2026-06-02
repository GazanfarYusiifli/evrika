import re

with open('lisey2.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('<!-- ── STATS / ACHIEVEMENTS ── -->')
end_idx = content.find('  <div class="stack-wrapper">')

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + content[end_idx:]
    with open('lisey2.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully removed the stats section.")
else:
    print("Could not find boundaries.")
