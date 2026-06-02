import re

def clean_and_update(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove the HERO TAG FIX blocks
    content = re.sub(r'/\* --- HERO TAG FIX --- \*/\s*@media \(min-width: 1025px\) \{[\s\S]*?\}\s*\}', '', content)
    
    # Just in case there are nested or malformed blocks left over
    content = re.sub(r'/\* --- HERO TAG FIX --- \*/.*?\}[\s\n]*\}', '', content, flags=re.DOTALL)
    
    # 2. Update the base .hero-tag to look like montessori but with a readable bright red color
    # Original lisey.html line:
    # .hero-tag { display:inline-flex; align-items:center; gap:8px; background:rgba(139,26,43,0.2); border:1px solid var(--accent); color:var(--accent-light); padding:8px 20px; border-radius:100px; font-size:.8rem; font-weight:800; text-transform:uppercase; margin-bottom:30px; }
    
    old_tag_regex = r'\.hero-tag\s*\{[^\}]+\}'
    
    new_tag = ".hero-tag { display:inline-flex; align-items:center; gap:8px; background:rgba(139,26,43,0.4); border:1px solid rgba(255,80,80,0.5); color:#ff6b6b; padding:8px 20px; border-radius:100px; font-size:.85rem; font-weight:800; text-transform:uppercase; letter-spacing:1px; margin-bottom:30px; box-shadow: 0 4px 15px rgba(139,26,43,0.3); }"
    
    # We'll just replace the first occurrence in the <style> block, usually around line 464
    content = re.sub(r'\.hero-tag\s*\{[^}]+\}', new_tag, content, count=1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
for fp in ['lisey.html', 'lisey2.html']:
    clean_and_update(fp)
    print(f"Updated {fp}")

