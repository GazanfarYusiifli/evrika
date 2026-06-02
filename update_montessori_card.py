import re

filepath = 'montessori.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Update the text and add the full-width-mobile class
old_card_pattern = r'<p>Böyük uşaqlar üçün Montessori varmı\? Bəli! Evrika BETL Gənclik filialında böyük yaş qrupları üçün xüsusi Montessori sinifləri fəaliyyət göstərir\.</p>'
new_text = '<p>Evrika BETL Gənclik filialında böyük yaş qrupları üçün xüsusi Montessori sinifləri fəaliyyət göstərir.</p>'

content = content.replace(old_card_pattern, new_text)

# Add the full-width-mobile class to the 3rd card
content = content.replace('<div class="level-card reveal" style="transition-delay: 0.2s; cursor: pointer; border-color: rgba(139, 26, 43, 0.4); box-shadow: 0 10px 30px rgba(139,26,43,0.15);" onclick="window.location.href=\'lisey2.html\';">', 
                          '<div class="level-card reveal full-width-mobile" style="transition-delay: 0.2s; cursor: pointer; border-color: rgba(139, 26, 43, 0.4); box-shadow: 0 10px 30px rgba(139,26,43,0.15);" onclick="window.location.href=\'lisey2.html\';">')

# Inject the CSS rule for full-width-mobile
css_to_add = """
    /* Mobile full width for 3rd card */
    @media (max-width: 768px) {
      .full-width-mobile { grid-column: 1 / -1; }
    }
</style>
"""
if '.full-width-mobile { grid-column: 1 / -1; }' not in content:
    content = content.replace('</style>', css_to_add, 1)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated montessori.html text and mobile width.")
