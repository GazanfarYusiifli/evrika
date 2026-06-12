import re

with open('victory.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove "Tələbələr aşağıdakı istiqamətlər üzrə hazırlıq keçə bilərlər:"
html = html.replace('<br><br>Tələbələr aşağıdakı istiqamətlər üzrə hazırlıq keçə bilərlər:', '')

# 2. Update icons for the 8 items
icons = [
    'fa-book-open',    # SAT
    'fa-award',        # SAT + Attestat
    'fa-language',     # IELTS
    'fa-comment-dots', # TOEFL
    'fa-university',   # Foundation
    'fa-chalkboard-teacher', # Academic English
    'fa-passport',     # Pearson/A-Level
    'fa-globe-asia'    # CSCA
]
# Find the 8 <i class="fas fa-check-circle"></i> and replace them
for icon in icons:
    html = html.replace('<i class="fas fa-check-circle"></i>', f'<i class="fas {icon}"></i>', 1)

# 3. Replace "Evrika Abituriyent Məktəbi" section with Foundation Proqramı
# The section starts with <div class="about-text-side"> and contains Evrika Abituriyent Məktəbi
# Let's write a regex that finds the about section that contains "Evrika Abituriyent Məktəbi"
about_abituriyent = r'<div class="about-text-side">.*?Evrika Abituriyent Məktəbi.*?</div>\s*</div>\s*</div>\s*</section>'

# Let's inspect the file first to make sure about the structure for this
