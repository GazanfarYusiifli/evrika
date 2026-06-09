import re

with open('register-victory.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace texts
html = html.replace('Eduhome Hazırlıq Mərkəzi', 'Victory Colleges by Evrika')
html = html.replace('Eduhome Hazırlıq', 'Victory Colleges')
html = html.replace('Eduhome', 'Victory Colleges')
html = html.replace('<title>Victory Colleges Qeydiyyat', '<title>Victory Colleges by Evrika Qeydiyyat')

# Theme colors (Yellow -> Blue)
old_css = '/* Dynamic Colorful Mesh Background - Eduhome (Gold/Yellow Theme) */'
new_css = '/* Dynamic Colorful Mesh Background - Victory (Blue Theme) */'
html = html.replace(old_css, new_css)
html = html.replace('radial-gradient(circle at 15% 50%, rgba(234, 179, 8, 0.4)', 'radial-gradient(circle at 15% 50%, rgba(59, 130, 246, 0.4)')
html = html.replace('radial-gradient(circle at 85% 30%, rgba(202, 138, 4, 0.4)', 'radial-gradient(circle at 85% 30%, rgba(37, 99, 235, 0.4)')
html = html.replace('rgba(250, 204, 21, 0.3)', 'rgba(59, 130, 246, 0.3)')

html = html.replace('--primary-color: #eab308;', '--primary-color: #3B82F6;')
html = html.replace('--primary-hover: #ca8a04;', '--primary-hover: #2563EB;')
html = html.replace('--accent-color: #facc15;', '--accent-color: #93C5FD;')

# Phone
html = html.replace('+994 50 254 53 53', '+994 55 519 99 32')
html = html.replace('+994 51 254 53 53', '+994 55 519 99 32')

# Tracking Source
html = html.replace('source: "Qeydiyyat - Victory Colleges"', 'source: "Qeydiyyat - Victory"')

with open('register-victory.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated register-victory.html")
