import re

file = 'lisey2.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the HAQQIMIZDA section
content = content.replace(
    '<h2 class="sec-h2">Milli Kurikulum, Cambridge və <em>STEAM/iSTEM</em></h2>',
    '<h2 class="sec-h2">Milli Kurikulum və <em>STEAM/iSTEM</em></h2>'
)
content = content.replace(
    'Məktəbəqədər hazırlıq və I–XI siniflər üzrə təşkil olunan tədris prosesi Milli kurikulum, Beynəlxalq Cambridge proqramı və STEAM/iSTEM modeli əsasında qurulur.',
    'Məktəbəqədər hazırlıq və I–XI siniflər üzrə təşkil olunan tədris prosesi Milli kurikulum və STEAM/iSTEM modeli əsasında qurulur.'
)

# 2. Fix the layout of the HAQQIMIZDA section and remove the image
# We need to add grid-template-columns: 1fr to the about-wrap specifically for this section
content = re.sub(
    r'(<div class="about-wrap">)(\s*<div class="about-text-side reveal-left">\s*<div class="sec-eyebrow">Haqqımızda</div>)',
    r'<div class="about-wrap" style="grid-template-columns: 1fr;">\g<2>',
    content
)

# Remove the img-side block
content = re.sub(
    r'<div class="about-img-side reveal-right" style="position:relative;">\s*<div class="img-placeholder"[^>]*>\s*<img src="\./assets/cambridge-logo\.png"[^>]*>\s*</div>\s*</div>',
    '',
    content
)

# 3. Other references in lisey2.html
content = content.replace(
    'Bu yanaşma Cambridge proqramı ilə inteqrasiya olunaraq',
    'Bu yanaşma beynəlxalq təhsil standartları ilə inteqrasiya olunaraq'
)

content = content.replace(
    '<li><i class="fas fa-check"></i> Cambridge tədris materiallarından istifadə</li>',
    '<li><i class="fas fa-check"></i> Beynəlxalq tədris materiallarından istifadə</li>'
)

content = content.replace(
    '<li><i class="fas fa-check"></i> Cambridge Exam Preparation</li>\n',
    ''
)

content = content.replace(
    'Proqram Cambridge beynəlxalq kurikulumu və Montessori yanaşmasının inteqrasiyası ilə qurulmuşdur.',
    'Proqram müasir beynəlxalq kurikulum və Montessori yanaşmasının inteqrasiyası ilə qurulmuşdur.'
)

content = content.replace(
    'Cambridge və beynəlxalq akademik sertifikatlar',
    'Beynəlxalq akademik sertifikatlar'
)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Cambridge references removed from lisey2.html")
