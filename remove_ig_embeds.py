import re
import os

files = ['lisey.html', 'lisey2.html', 'montessori.html', 'victory.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the post container:
    # <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 30px;">
    # ...
    # </div>
    # <script async src="//www.instagram.com/embed.js"></script>
    
    start_str = '<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 30px;">'
    start_idx = content.find(start_str)
    
    if start_idx != -1:
        # Find the closing div of this flex container
        script_idx = content.find('<script async src="//www.instagram.com/embed.js"></script>', start_idx)
        if script_idx != -1:
            # We remove everything from start_str to just before script_idx
            new_content = content[:start_idx] + content[script_idx:]
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Removed embedded posts from {file}")
        else:
            print(f"Could not find script tag in {file}")
    else:
        print(f"Could not find post container in {file}")
