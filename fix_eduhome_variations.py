import re

with open('eduhome.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <h1 class="hero-h1">Eduhome<br>Təhsil<br><span class="accent">Mərkəzi</span></h1>
content = content.replace('Eduhome<br>Təhsil<br><span class="accent">Mərkəzi</span>', 'Eduhome<br>Hazırlıq<br><span class="accent">Mərkəzi</span>')

# Replace <h2 class="sec-h2">Eduhome <em>Təhsil Mərkəzi</em></h2>
content = content.replace('Eduhome <em>Təhsil Mərkəzi</em>', 'Eduhome <em>Hazırlıq Mərkəzi</em>')

with open('eduhome.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed variations in eduhome.html")
