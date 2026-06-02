import re

filepath = '/Users/gazanfaryusifli/Downloads/Evrika/lisey2.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

style_block = """
<style>
/* 1. Haqqımızda - Ağ fon, tünd yazılar */
#about { background-color: #fff !important; color: #000 !important; }
#about .sec-eyebrow { color: #8b1a2b !important; }
#about .sec-h2, #about .sec-h2 em { color: #070d1f !important; }
#about p { color: #333 !important; }
#about .img-placeholder { background: rgba(0,0,0,0.02) !important; border-color: rgba(0,0,0,0.1) !important; }

/* 2. Xidmətlərimiz və İnfrastruktur - Qırmızı fon */
#xidmetler-sec { background-color: #8b1a2b !important; color: #fff !important; }
#xidmetler-sec .sec-h2, #xidmetler-sec .sec-h2 em { color: #fff !important; }
</style>
"""

# Insert style block before </head> if not already there
if "/* 1. Haqqımızda - Ağ fon, tünd yazılar */" not in content:
    content = content.replace("</head>", style_block + "\n</head>")

# Xidmətlərimiz
# Search for: <section class="section" style="position: relative; z-index: 20; background: #070d1f; color: #fff;">
content = content.replace('<section class="section" style="position: relative; z-index: 20; background: #070d1f; color: #fff;">', 
                          '<section class="section" id="xidmetler-sec" style="position: relative; z-index: 20; background: #8b1a2b; color: #fff;">')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
