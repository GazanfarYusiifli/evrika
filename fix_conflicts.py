import glob
import re

for file_path in glob.glob("*.html"):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(r'<<<<<<< Updated upstream(.*?)(=======.*?>>>>>>> Stashed changes\n?)', re.DOTALL)
    
    if pattern.search(content):
        new_content = pattern.sub(r'\1', content)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Fixed {file_path}")
