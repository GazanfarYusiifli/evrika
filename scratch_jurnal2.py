import os

filepath = "/Users/gazanfaryusifli/Downloads/Evrika/jurnal.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

import re

# Remove CV Modal
content = re.sub(r'<!-- CV Application Modal -->.*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)

# Update page title
content = re.sub(r'<title>Vakansiyalar \| Evrika Təhsil Ekosistemi</title>', '<title>Evrika Məktəbli Jurnalı | Evrika Təhsil Ekosistemi</title>', content)

# Replace the hero section text
content = re.sub(r'<div class="brand-eyebrow modern-glow"[^>]*>KARYERA VƏ İNKİŞAF</div>', '<div class="brand-eyebrow modern-glow" style="margin-bottom: 24px; color: rgba(255,255,255,0.7); letter-spacing: 0.6em; text-transform: uppercase;">NƏŞRLƏRİMİZ</div>', content)
content = re.sub(r'<h1 class="titan-header"[^>]*>Vakansiya və Təcrübə</h1>', '<h1 class="titan-header" style="font-size: clamp(3rem, 6vw, 5.5rem); color: #fff; margin-bottom: 30px; font-weight: 900;">Evrika Məktəbli Jurnalı</h1>', content)
content = re.sub(r'<p class="subtitle-pro"[^>]*>Evrika ailəsinə qoşulun.*?<br>.*?</p>', '<p class="subtitle-pro" style="max-width: 850px; margin: 0 auto; font-size: 1.6rem; color: #fff; line-height: 1.6;">Tezliklə...</p>', content)

# Remove the content sections
content = re.sub(r'<!-- Filter Section -->.*?(?=<!-- Modern Footer -->)', '<div class="container" style="min-height: 40vh; display: flex; align-items: center; justify-content: center;"><h2 style="color: white; font-size: 2rem; opacity: 0.6;">Səhifə hazırlanır...</h2></div>', content, flags=re.DOTALL)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
