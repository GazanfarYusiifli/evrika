import re

with open('victory.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's add the subtitle below the h2
old_header = r'<h2 class="sec-h2" style="text-align:center">Akademik <em>Hazırlıq Proqramları</em></h2>'
new_header = """<h2 class="sec-h2" style="text-align:center">Akademik <em>Hazırlıq Proqramları</em></h2>
      <p style="color: #555; max-width: 600px; margin: 10px auto 30px; font-size: 1.05rem;">Victory Colleges by Evrika tələbələrə beynəlxalq universitetlərə qəbul olmaq üçün müxtəlif akademik hazırlıq proqramları təqdim edir. Tədris proqramlarımız dünyanın aparıcı universitetlərinin qəbul tələblərinə uyğun şəkildə hazırlanıb.<br><br>Tələbələr aşağıdakı istiqamətlər üzrə hazırlıq keçə bilərlər:</p>"""

html = html.replace(old_header, new_header)

with open('victory.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Subtitle replaced")
