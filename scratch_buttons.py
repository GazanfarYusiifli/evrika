import os
import re

files = [
    "register-lisey1.html",
    "register-lisey2.html",
    "register-montessori.html",
    "register-victory.html",
    "register-zumrud.html"
]

base_dir = "/Users/gazanfaryusifli/Downloads/Evrika"

for filename in files:
    path = os.path.join(base_dir, filename)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the .submit-btn block and replace it
    # We will use a more vibrant gradient. The user wants them to be clearly "gradient"
    # We can use a linear gradient from the bright color to the main color and then a darker color.
    
    # Let's replace the background line in .submit-btn
    content = re.sub(
        r'background: linear-gradient\(135deg, [^\)]+\);',
        r'background: linear-gradient(135deg, var(--burgundy-bright) 0%, var(--burgundy) 100%);',
        content
    )
    
    # In :hover as well
    content = re.sub(
        r'\.submit-btn:hover \{.*?background: linear-gradient.*?\}',
        r'.submit-btn:hover { transform: translateY(-5px) scale(1.02); box-shadow: 0 30px 60px rgba(255,255,255,0.2); background: linear-gradient(135deg, var(--burgundy) 0%, var(--burgundy-bright) 100%); }',
        content,
        flags=re.DOTALL
    )

    # Let's make E-jurnal buttons also gradient just in case
    content = content.replace("background: #1565C0;", "background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);")
    content = content.replace("onmouseover=\"this.style.background='#0d47a1';", "onmouseover=\"this.style.background='linear-gradient(135deg, #3b82f6 0%, #1e3a8a 100%)';")
    content = content.replace("onmouseout=\"this.style.background='#1565C0';", "onmouseout=\"this.style.background='linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%)';")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Buttons updated")
