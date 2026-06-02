import os
import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Change EVRIKA to EVRİKA in the footer logo
    content = re.sub(
        r'(<a[^>]*class="logo"[^>]*>)\s*EVRIKA\s*(</a>)',
        r'\1EVRİKA\2',
        content,
        flags=re.IGNORECASE
    )
    
    # 2. Add dot to the end of the footer description
    content = content.replace(
        'Evrika Təhsil Ekosistemi — Qlobal təhsil standartları, innovativ yanaşma və parlaq gələcəkdir<',
        'Evrika Təhsil Ekosistemi — Qlobal təhsil standartları, innovativ yanaşma və parlaq gələcəkdir.<'
    )
    
    # In index.html, delete the final-statement section
    if file == 'index.html':
        # Use regex to match from <!-- Final Institutional Message to </section>
        pattern = r'<!-- Final Institutional Message \(Clean Pattern Version\) -->.*?</section>'
        content = re.sub(pattern, '', content, flags=re.DOTALL)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(html_files)} files.")
