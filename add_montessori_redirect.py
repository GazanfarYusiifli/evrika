import re

new_html = """
      <div class="levels-grid" style="grid-template-columns: repeat(3, 1fr); gap: 30px;">
        <div class="level-card reveal">
          
          <i class="fas fa-baby level-icon"></i>
          <h4 style="color: #070d1f !important;">Toddler</h4>
          <span class="level-age">1–3 Yaş</span>
          <p>Uşağın müstəqil hərəkət, dil və özünə xidmət bacarıqlarının formalaşdığı erkən inkişaf mərhələsi.</p>
        </div>

        <div class="level-card reveal" style="transition-delay: 0.1s;">
          
          <i class="fas fa-child level-icon"></i>
          <h4 style="color: #070d1f !important;">Primary</h4>
          <span class="level-age">3–6 Yaş</span>
          <p>Sosiallaşma, akademik hazırlıq və dünyanı elmi şəkildə kəşf etmə dövrü (Məktəbə hazırlıq).</p>
        </div>

        <div class="level-card reveal" style="transition-delay: 0.2s; cursor: pointer; border-color: rgba(139, 26, 43, 0.4); box-shadow: 0 10px 30px rgba(139,26,43,0.15);" onclick="window.location.href='lisey2.html';">
          <div style="position: absolute; top: 15px; right: 20px; color: #8b1a2b; font-size: 1.2rem;"><i class="fas fa-external-link-alt"></i></div>
          <i class="fas fa-school level-icon" style="color: #8b1a2b;"></i>
          <h4 style="color: #070d1f !important;">Montessori Sinifləri</h4>
          <span class="level-age" style="color: #8b1a2b; font-weight: 800;">I-XI Siniflər</span>
          <p>Böyük uşaqlar üçün Montessori varmı? Bəli! Evrika BETL Gənclik filialında böyük yaş qrupları üçün xüsusi Montessori sinifləri fəaliyyət göstərir.</p>
        </div>
      </div>
"""

filepath = 'montessori.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the original levels-grid block
pattern = r'<div class="levels-grid" style="grid-template-columns: repeat\(2, 1fr\); gap: 30px;">.*?</div>\s*</div>'
if 'Montessori Sinifləri' not in content[content.find('<div class="levels-grid"'):content.find('<!-- ── DƏRNƏKLƏR ── -->')]:
    content = re.sub(pattern, new_html + '\n    </div>', content, flags=re.DOTALL)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated montessori.html.")
else:
    print("Already updated.")
