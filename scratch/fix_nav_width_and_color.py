import os
import re

files = ["lisey.html", "lisey2.html", "montessori.html", "eduhome.html", "zumrud.html"]

for fname in files:
    if not os.path.exists(fname):
        continue
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Fix mobile-nav-overlay padding
    # Look for: padding: 100px 40px; or similar inside .mobile-nav-overlay { ... }
    content = re.sub(r'(\.mobile-nav-overlay\s*{[^}]*?padding:\s*)100px\s+40px(;|[\s}])', r'\g<1>80px 0 40px 0\2', content)

    # 2. Fix Qeydiyyat color
    content = content.replace('style="color: var(--burgundy);"', 'style="color: var(--accent, #8b1a2b);"')
    content = content.replace('style="color: var(--accent);"', 'style="color: var(--accent, #8b1a2b);"')

    # Optional: ensure E-jurnal div has proper padding (index.html has padding: 20px; border-bottom: 1px solid rgba(255,255,255,0.1); margin-bottom: 20px;)
    # Currently lisey.html has it. We don't need to change if padding is fixed.
    
    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)
        print(f"Updated {fname}")
