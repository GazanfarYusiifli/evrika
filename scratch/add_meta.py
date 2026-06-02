import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

meta_tag = '<meta name="format-detection" content="telephone=no">'

for f_name in html_files:
    with open(f_name, "r", encoding="utf-8") as f:
        content = f.read()
    
    if meta_tag not in content:
        # Insert right after <head> or <meta charset="UTF-8">
        if '<meta charset="UTF-8" />' in content:
            content = content.replace('<meta charset="UTF-8" />', f'<meta charset="UTF-8" />\n  {meta_tag}')
        elif '<head>' in content:
            content = content.replace('<head>', f'<head>\n  {meta_tag}')
            
        with open(f_name, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {f_name}")

