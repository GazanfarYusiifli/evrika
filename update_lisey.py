import re

filepath = '/Users/gazanfaryusifli/Downloads/Evrika/lisey.html'
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

/* 2. Klublar - Ağ fon, tünd yazılar */
#klublar { background-color: #fff !important; }
#klublar .category-title { color: #070d1f !important; }
#klublar .category-title em { color: #8b1a2b !important; }
#klublar .club-card { background: #f8f9fa !important; border: 1px solid #ddd !important; box-shadow: 0 5px 15px rgba(0,0,0,0.05) !important; }
#klublar .club-name { color: #000 !important; font-weight: 700; }
#klublar .club-icon { color: #8b1a2b !important; }

/* 3. Dəstək və Təhlükəsizlik - Qırmızı fon, ağ yazılar */
#destek { background-color: #8b1a2b !important; color: #fff !important; }
#destek .sec-eyebrow { color: rgba(255,255,255,0.8) !important; }
#destek .sec-h2, #destek .sec-h2 em { color: #fff !important; }
</style>
"""

# Insert style block
content = content.replace("</head>", style_block + "\n</head>")

# 1. Haqqımızda is already <section id="about" class="section">
# Just remove inline style if any. (It doesn't seem to have one).

# 2. Klublar
# Search for: <section class="section section-normal prog-bg">
content = content.replace('<section class="section section-normal prog-bg">', 
                          '<section class="section section-normal" id="klublar">')

# 3. Dəstək
# Search for:
#   <!-- ── İNFRASTRUKTUR & XİDMƏTLƏR ── -->
#   <section class="section">
content = content.replace('<!-- ── İNFRASTRUKTUR & XİDMƏTLƏR ── -->\n  <section class="section">', 
                          '<!-- ── İNFRASTRUKTUR & XİDMƏTLƏR ── -->\n  <section class="section" id="destek">')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
