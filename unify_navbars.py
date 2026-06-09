import re

with open('lisey.html', 'r', encoding='utf-8') as f:
    lisey_content = f.read()

# Extract Block 1
block1_match = re.search(r'/\* --- NAVBAR STYLES \(eduhome-style\) --- \*/(.*?)/\* --- NEW CONTENT STYLES --- \*/', lisey_content, re.DOTALL)
if not block1_match:
    print("Failed to find Block 1 in lisey.html")
    exit(1)
block1 = block1_match.group(1).strip()

# Extract Block 2
block2_match = re.search(r'(@media \(max-width: 1024px\) \{\s*\.nav-glass-container.*?)(?=\n</style>)', lisey_content, re.DOTALL)
if not block2_match:
    print("Failed to find Block 2 in lisey.html")
    exit(1)
block2 = block2_match.group(1).strip()

# New CSS to inject
new_css = "/* --- NAVBAR STYLES (eduhome-style) --- */\n" + block1 + "\n\n" + block2 + "\n"

files = ['montessori.html', 'victory.html', 'zumrud.html']
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace from /* --- Modernized Neo-Glass Floating Navigation --- */ up to the first </style>
    # Note: montessori.html, victory.html, zumrud.html use /* --- Modernized Neo-Glass Floating Navigation --- */
    
    new_content = re.sub(
        r'/\* --- Modernized Neo-Glass Floating Navigation --- \*/.*?(?=\n</style>)',
        new_css.replace('\\', '\\\\'), # Escape backslashes for re.sub
        content,
        flags=re.DOTALL,
        count=1
    )
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated CSS in {file}")
    else:
        print(f"No match found in {file}")

