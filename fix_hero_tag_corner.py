import re

css_to_add = """
    /* --- HERO TAG FIX --- */
    @media (min-width: 1025px) {
      .hero {
        position: relative;
      }
      .hero-tag {
        position: absolute !important;
        bottom: 120px !important;
        right: 60px !important;
        margin-bottom: 0 !important;
        z-index: 50 !important;
      }
    }
"""

for filepath in ['lisey.html', 'lisey2.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the closing </style> tag and insert before it
    if '/* --- HERO TAG FIX --- */' not in content:
        content = content.replace('</style>', css_to_add + '\n</style>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"Already updated {filepath}")
