import re
import os

# 1. Fix src/main.js
try:
    with open('src/main.js', 'r', encoding='utf-8') as f:
        js = f.read()
    js = js.replace('Eduhome Hazırlıq', 'Victory Colleges by Evrika')
    js = js.replace('Eduhome', 'Victory Colleges')
    with open('src/main.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("Fixed src/main.js")
except FileNotFoundError:
    print("src/main.js not found!")

# 2. Fix victory.html
with open('victory.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix Instagram urls - replacing utm_source=ig_web_copy_link with ig_embed
# Wait, the user said the instagram embeds don't show pictures. Instagram blockquote needs correct URL.
html = html.replace('DZVJSn4CINw/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==', 'DZVJSn4CINw/?utm_source=ig_embed&utm_campaign=loading')
html = html.replace('DYnHejPO-_3/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==', 'DYnHejPO-_3/?utm_source=ig_embed&utm_campaign=loading')
html = html.replace('DW81xBLiG3D/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==', 'DW81xBLiG3D/?utm_source=ig_embed&utm_campaign=loading')

# Let's ensure the URLs are simply the post URL for the ahref, and the embed for the iframe blockquote
# Actually, the python script earlier blindly replaced the IDs inside the IG embed.
# Let's verify the IG embed URL format:
# data-instgrm-permalink="https://www.instagram.com/p/DZVJSn4CINw/?utm_source=ig_embed&amp;utm_campaign=loading"
html = html.replace('DZVJSn4CINw/?utm_source=ig_embed&amp;utm_campaign=loading', 'DZVJSn4CINw/?utm_source=ig_embed&amp;utm_campaign=loading')
# Since it might have just replaced the ID, the old query params (?utm_source=ig_embed) were KEPT!
# Wait, the ID `DYnHejPO-_3` is a reel, but the first one `DZVJSn4CINw` is a post (`/p/`).
# Let's make sure `/reel/DZVJSn4CINw` is changed to `/p/DZVJSn4CINw` if it's a post.
html = html.replace('/reel/DZVJSn4CINw', '/p/DZVJSn4CINw')


# 3. Fix images in About and Foundation to be full size
# Let's find the about-img-side images
# It might be styled with border-radius 50%
# Let's search for border-radius in the style section for about-img-side
html = html.replace('.about-img-side img{width:400px;height:400px;border-radius:50%;object-fit:cover;box-shadow:0 20px 50px rgba(0,0,0,0.15);position:relative;z-index:2;}',
                    '.about-img-side img{width:100%;height:100%;border-radius:24px;object-fit:cover;box-shadow:0 20px 50px rgba(0,0,0,0.15);position:relative;z-index:2; aspect-ratio: 1/1;}')

# And maybe another occurrence if it's not exactly that string. Let's just use regex
html = re.sub(r'\.about-img-side img\s*\{[^\}]*?\}', '.about-img-side img{width:100%;max-width:500px;border-radius:24px;object-fit:cover;box-shadow:0 20px 50px rgba(0,0,0,0.15);position:relative;z-index:2;}', html)

# Also check for inline styles on the img tags
html = re.sub(r'<img src="\./assets/sekill2\.jpeg" alt="Victory Colleges" style="[^"]*?">', r'<img src="./assets/sekill2.jpeg" alt="Victory Colleges" style="width: 100%; border-radius: 24px;">', html)
html = re.sub(r'<img src="\./assets/sekill3\.jpeg" alt="Victory Colleges" style="[^"]*?">', r'<img src="./assets/sekill3.jpeg" alt="Victory Colleges" style="width: 100%; border-radius: 24px;">', html)

with open('victory.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updates to HTML and JS applied.")
