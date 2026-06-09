import re

filepath = '/Users/gazanfaryusifli/Downloads/Evrika/victory.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

style_block = """
<style>
/* For About Section */
#about { background-color: #fff !important; color: #333 !important; }
#about .sec-eyebrow { color: #8b1a2b !important; }
#about .sec-h2, #about .sec-h2 em { color: #070d1f !important; }
#about p { color: #555 !important; }
#about h4 { color: #8b1a2b !important; }
#about .pill { background: #f8f9fa !important; color: #333 !important; border: 1px solid #ddd !important; }
#about .pills .pill i { color: #8b1a2b !important; }

/* For Akademik Hazırlıq (Xidmətlərimiz) */
#xidmetler { background-color: #fff !important; }
#xidmetler .sec-eyebrow { color: #8b1a2b !important; }
#xidmetler .sec-h2, #xidmetler .sec-h2 em { color: #070d1f !important; }
#xidmetler .prog-item { background: #f8f9fa !important; border: 1px solid #eee !important; box-shadow: 0 5px 15px rgba(0,0,0,0.05) !important; }
#xidmetler .prog-n { color: #8b1a2b !important; font-weight: bold; }
#xidmetler .prog-title { color: #070d1f !important; }
#xidmetler .prog-desc { color: #555 !important; }
#xidmetler .chip { background: #fff !important; color: #333 !important; border: 1px solid #ddd !important; }

/* For Sistemin Üstünlükləri */
#ustunlukler { background-color: #facc15 !important; }
#ustunlukler .sec-eyebrow { color: #000 !important; background: rgba(0,0,0,0.05) !important; padding: 5px 15px; border-radius: 20px; }
#ustunlukler .sec-h2, #ustunlukler .sec-h2 em { color: #000 !important; }
#ustunlukler .prog-item { background: #fff !important; border: none !important; box-shadow: 0 5px 15px rgba(0,0,0,0.1) !important; }
#ustunlukler .prog-title { color: #000 !important; }
#ustunlukler .prog-desc { color: #333 !important; }
#ustunlukler .prog-ico { background: #facc15 !important; color: #000 !important; border: none !important; }

/* For Sosial Media */
#sosial-media { background: #facc15 !important; }
#sosial-media .sec-eyebrow { color: #000 !important; background: rgba(0,0,0,0.05) !important; padding: 5px 15px; border-radius: 20px; }
#sosial-media .sec-h2, #sosial-media .sec-h2 em { color: #000 !important; }
#sosial-media a { color: #333 !important; }
#sosial-media .btn-primary { background: #000 !important; color: #fff !important; }
</style>
"""

# Inject the style block right before </head>
content = content.replace("</head>", style_block + "\n</head>")

# 2. Xidmətlərimiz section
content = content.replace('<section class="section prog-bg">\n  <div class="container">\n    <div style="text-align:center" class="reveal"><span class="sec-eyebrow">Xidmətlərimiz</span>', 
                          '<section class="section prog-bg" id="xidmetler">\n  <div class="container">\n    <div style="text-align:center" class="reveal"><span class="sec-eyebrow">Xidmətlərimiz</span>')

# 3. Sistemin Üstünlükləri section
content = content.replace('<section class="section prog-bg">\n  <div class="container">\n    <div style="text-align:center" class="reveal"><span class="sec-eyebrow">Sistemin Üstünlükləri</span>', 
                          '<section class="section prog-bg" id="ustunlukler">\n  <div class="container">\n    <div style="text-align:center" class="reveal"><span class="sec-eyebrow">Sistemin Üstünlükləri</span>')

# 4. Sosial media section
content = content.replace('<section class="section" style="background: var(--navy-mid); padding-bottom: 80px;">', 
                          '<section class="section" id="sosial-media" style="padding-bottom: 80px;">')


with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
