import os
import glob

html_files = glob.glob("/Users/gazanfaryusifli/Downloads/Evrika/*.html")

for path in html_files:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # E-jurnal buttons
    content = content.replace("background: #1565C0;", "background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);")
    content = content.replace("onmouseover=\"this.style.background='#0d47a1';", "onmouseover=\"this.style.background='linear-gradient(135deg, #3b82f6 0%, #1e3a8a 100%)';")
    content = content.replace("onmouseout=\"this.style.background='#1565C0';", "onmouseout=\"this.style.background='linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%)';")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
print("done")
