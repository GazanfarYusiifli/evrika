import re

with open('jurnal.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the inline style of h1
content = content.replace('<h1 class="titan-header reveal" style="font-size: 5rem; line-height: 1.1; margin-bottom: 30px;">', '<h1 class="titan-header reveal" style="line-height: 1.1; margin-bottom: 30px;">')

# 2. Add media queries for mobile to the style block
old_style = """.magazine-card:hover .magazine-btn {
          background: #1e3a8a;
          color: white;
        }
      </style>"""

new_style = """.magazine-card:hover .magazine-btn {
          background: #1e3a8a;
          color: white;
        }
        .titan-header { font-size: 5rem; }
        @media (max-width: 768px) {
          .jurnal-hero { padding: 150px 20px 80px !important; }
          .titan-header { font-size: 2.5rem !important; }
        }
      </style>"""

content = content.replace(old_style, new_style)

with open('jurnal.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed mobile header for jurnal")
