import re

filepath = '/Users/gazanfaryusifli/Downloads/Evrika/eduhome.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# I will replace the previous style block with a new one.
# First, I'll extract the old block and replace it.

old_style_block = """<style>
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
</style>"""

new_style_block = """<style>
/* For About Section */
#about { background-color: #facc15 !important; color: #000 !important; }
#about .sec-eyebrow { color: #000 !important; background: rgba(0,0,0,0.05) !important; padding: 5px 15px; border-radius: 20px; }
#about .sec-h2, #about .sec-h2 em { color: #000 !important; }
#about p { color: #333 !important; }
#about h4 { color: #000 !important; }
#about .pill { background: #fff !important; color: #000 !important; border: none !important; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }
#about .pills .pill i { color: #000 !important; }

/* For Akademik Hazırlıq (Xidmətlərimiz) */
#xidmetler { background-color: #fff !important; }
#xidmetler .sec-eyebrow { color: #000 !important; background: rgba(0,0,0,0.05) !important; padding: 5px 15px; border-radius: 20px; }
#xidmetler .sec-h2, #xidmetler .sec-h2 em { color: #000 !important; }
#xidmetler .prog-item { background: #f8f9fa !important; border: 1px solid #eee !important; box-shadow: 0 5px 15px rgba(0,0,0,0.05) !important; }
#xidmetler .prog-ico { background: #eab308 !important; color: #000 !important; border: none !important; }
#xidmetler .prog-n { color: #000 !important; font-weight: bold; }
#xidmetler .prog-title { color: #000 !important; }
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

/* Mobile Menu red color fix */
.mobile-nav-links a[style*="var(--accent, #8b1a2b)"] { color: #eab308 !important; }
</style>"""

content = content.replace(old_style_block, new_style_block)

# Also fix any inline styles with #8b1a2b
content = content.replace('#8b1a2b', '#eab308')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
