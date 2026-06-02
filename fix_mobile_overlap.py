import re

with open('montessori.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add a style fix for mobile overlap
fix_style = """
@media (max-width: 768px) {
  #bolmeler {
    padding-bottom: 100px !important;
  }
  .section-red {
    padding-top: 80px !important;
    margin-top: 40px !important;
  }
}
"""

# Insert before </style> at the bottom of the file
content = content.replace('</style>\n</head>', fix_style + '\n</style>\n</head>')
# Wait, the global styles are at the bottom just before </style> or inside body?
# Let's insert it before the closing </style> of the last style block.
content = re.sub(r'</style>\s*(<link|</head>|<body>)', fix_style + r'\n</style>\n\1', content, count=1)

with open('montessori.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added mobile spacing")
