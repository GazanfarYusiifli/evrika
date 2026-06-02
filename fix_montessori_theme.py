import re

with open('montessori.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Root Colors
root_old = """    :root {
      --accent: #9ca476;
      --accent-light: #b0b985;
      --accent-glow: rgba(156,164,118,0.25);
      --navy: #0a0d0f;
      --navy-mid: #111418;
      --white: #ffffff;
      --text: #e8eaf2;
      --text-muted: #8892a4;
      --surface: rgba(255,255,255,0.04);
      --border: rgba(255,255,255,0.08);
    }"""
    
root_new = """    :root {
      --accent: #6c8a55;
      --accent-light: #8fae73;
      --accent-glow: rgba(108,138,85,0.25);
      --navy: #f9fbf7;
      --navy-mid: #ffffff;
      --white: #ffffff;
      --text: #1a2315;
      --text-muted: #5e6c53;
      --surface: rgba(0,0,0,0.02);
      --border: rgba(0,0,0,0.06);
    }"""
content = content.replace(root_old, root_new)

# 2. Update Hero Gradient
hero_bg_old = "background: linear-gradient(135deg, rgba(10,13,15,0.97) 0%, rgba(50,30,5,0.9) 50%, rgba(10,13,15,0.97) 100%),"
hero_bg_new = "background: linear-gradient(135deg, rgba(249,251,247,0.96) 0%, rgba(255,255,255,0.92) 50%, rgba(249,251,247,0.96) 100%),"
content = content.replace(hero_bg_old, hero_bg_new)

# 3. Replace text colors
content = re.sub(r'color:\s*#fff(;|(?="))', r'color:var(--text)\1', content)
content = re.sub(r'color:\s*rgba\(255,255,255,0\.\d+\)(;|(?="))', r'color:var(--text-muted)\1', content)

# Restore specific buttons
content = content.replace('.btn-primary { background:var(--accent); color:var(--text);', '.btn-primary { background:var(--accent); color:#fff;')
content = content.replace('.btn-glass { background:rgba(255,255,255,0.06); color:var(--text);', '.btn-glass { background:rgba(108,138,85,0.1); color:var(--accent);')
content = content.replace('.submit-btn { width:100%; padding:17px; border:none; background:linear-gradient(135deg, var(--accent), var(--accent-light)); color:var(--text);', '.submit-btn { width:100%; padding:17px; border:none; background:linear-gradient(135deg, var(--accent), var(--accent-light)); color:#fff;')
content = content.replace('.about-float { position:absolute; bottom:-20px; right:-20px; background:var(--accent); color:var(--text);', '.about-float { position:absolute; bottom:-20px; right:-20px; background:var(--accent); color:#fff;')
content = content.replace('.infra-top { position:absolute; top:20px; right:20px; width:42px; height:42px; border-radius:10px; background:var(--accent); display:flex; align-items:center; justify-content:center; color:var(--text);', '.infra-top { position:absolute; top:20px; right:20px; width:42px; height:42px; border-radius:10px; background:var(--accent); display:flex; align-items:center; justify-content:center; color:#fff;')
content = content.replace('.level-badge { position: absolute; top: 25px; right: 25px; font-size: 0.7rem; font-weight: 900; background: var(--accent); color: var(--text);', '.level-badge { position: absolute; top: 25px; right: 25px; font-size: 0.7rem; font-weight: 900; background: var(--accent); color: #fff;')

# 4. Backgrounds and borders
content = content.replace('background:rgba(255,255,255,0.04)', 'background:rgba(0,0,0,0.02)')
content = content.replace('background:rgba(255,255,255,0.05)', 'background:rgba(0,0,0,0.03)')
content = content.replace('background:rgba(255,255,255,0.06)', 'background:rgba(0,0,0,0.04)')
content = content.replace('background:rgba(255,255,255,0.12)', 'background:rgba(0,0,0,0.06)')
content = content.replace('background:rgba(255,255,255,0.1)', 'background:rgba(0,0,0,0.05)')
content = content.replace('border:1px solid rgba(255,255,255,0.1)', 'border:1px solid rgba(0,0,0,0.06)')
content = content.replace('border:1px solid rgba(255,255,255,0.07)', 'border:1px solid rgba(0,0,0,0.05)')
content = content.replace('border:1.5px solid rgba(255,255,255,0.15)', 'border:1.5px solid var(--accent)')
content = content.replace('border:1px solid rgba(255,255,255,0.2)', 'border:1px solid rgba(0,0,0,0.08)')
content = content.replace('border:1.5px solid rgba(255,255,255,0.12)', 'border:1.5px solid rgba(0,0,0,0.1)')
content = content.replace('color:rgba(255,255,255,0.04)', 'color:rgba(0,0,0,0.03)') # hero num big

# Shadows
content = content.replace('box-shadow:0 40px 100px rgba(0,0,0,0.5)', 'box-shadow:0 40px 100px rgba(0,0,0,0.08)')
content = content.replace('box-shadow:0 40px 120px rgba(0,0,0,0.6)', 'box-shadow:0 40px 120px rgba(0,0,0,0.1)')
content = content.replace('box-shadow:0 40px 120px rgba(0,0,0,0.4)', 'box-shadow:0 40px 120px rgba(0,0,0,0.1)')
content = content.replace('box-shadow: 0 40px 100px rgba(0,0,0,0.5)', 'box-shadow: 0 40px 100px rgba(0,0,0,0.08)')
content = content.replace('box-shadow: 0 32px 80px rgba(0,0,0,0.5)', 'box-shadow: 0 32px 80px rgba(0,0,0,0.1)')

# Specific fixes
reg_bg_old = "background:linear-gradient(135deg, var(--navy-mid) 0%, #1a1005 100%);"
reg_bg_new = "background:linear-gradient(135deg, var(--navy-mid) 0%, #f4f6f0 100%);"
content = content.replace(reg_bg_old, reg_bg_new)

content = content.replace('.fgroup select option { background:#111418; }', '.fgroup select option { background:#fff; }')

ft_old = ".ft { background:#04060a;"
ft_new = ".ft { background:var(--navy-mid);"
content = content.replace(ft_old, ft_new)

with open('montessori.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated montessori.html theme")
