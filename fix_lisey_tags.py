import os

css_to_add = """
    /* --- HERO TAG FIX --- */
    @media (min-width: 1025px) {
      .hero {
        position: relative;
      }
      .hero-tag {
        position: absolute;
        bottom: 120px;
        right: 60px;
        margin-bottom: 0;
        z-index: 50;
        background: rgba(139, 26, 43, 0.9);
        color: #ffffff;
        border-color: rgba(255,255,255,0.3);
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        font-size: 1rem;
        padding: 12px 28px;
        letter-spacing: 2px;
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

