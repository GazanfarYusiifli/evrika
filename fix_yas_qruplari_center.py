import re

with open('montessori.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I added this previously:
# @media (max-width: 768px) {
#   #bolmeler {
#     padding-bottom: 100px !important;
#   }
#   .section-red {
#     padding-top: 80px !important;
#     margin-top: 40px !important;
#   }
# }

# We will modify that block to also center .sec-header inside .section-red
old_css = """.section-red {
    padding-top: 80px !important;
    margin-top: 40px !important;
  }"""
new_css = """.section-red {
    padding-top: 80px !important;
    margin-top: 40px !important;
  }
  .section-red .sec-header {
    text-align: center !important;
  }"""

content = content.replace(old_css, new_css)

with open('montessori.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Centered Yas Qruplari on mobile")
