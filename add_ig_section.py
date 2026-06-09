import os

# Extract the Instagram section from zumrud.html
with open('zumrud.html', 'r', encoding='utf-8') as f:
    content_zumrud = f.read()

start_marker = '<!-- ── INSTAGRAM POSTS SECTION ── -->'
end_marker = '</section>\n\n                                              <!-- Footer -->'
if end_marker not in content_zumrud:
    end_marker = '</section>\n\n<footer'

start_idx = content_zumrud.find(start_marker)
# Let's just find </section> after start_marker
temp = content_zumrud[start_idx:]
end_section_idx = temp.find('</section>') + len('</section>')
ig_section = temp[:end_section_idx]

targets = {
    'lisey.html': {
        'url': 'https://www.instagram.com/evrikaliseyi?utm_source=qr',
        'handle': '@evrikaliseyi',
        'posts': [
            'https://www.instagram.com/reel/DWEyNg1CChT/', # we can just keep the same posts or empty them?
            # Wait, the posts are specific to zumrud. The user didn't give posts.
            # I will leave the posts as they are, or I can remove the blockquotes and let the user add them later. 
            # The user said "SOSİAL MEDİA Bizi İnstagramda İzləyin sectionunu ... bu seyfeler ucun de elave ele"
            # So I will copy the section but just update the main link and handle.
        ]
    },
    'lisey2.html': {
        'url': 'https://www.instagram.com/evrika.betl?utm_source=qr',
        'handle': '@evrika.betl'
    },
    'montessori.html': {
        'url': 'https://www.instagram.com/evrikamontessorikids?igsh=d3hmdjQxdzJlM3g5&utm_source=qr',
        'handle': '@evrikamontessorikids'
    },
    'victory.html': {
        'url': 'https://www.instagram.com/eduhome_az?utm_source=qr',
        'handle': '@eduhome_az'
    }
}

for file, data in targets.items():
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if section already exists
    if start_marker in content:
        print(f"Skipping {file}, already has the section.")
        continue
    
    # Custom section for this file
    custom_ig = ig_section.replace('https://www.instagram.com/zumrud_womens_club/', data['url'])
    custom_ig = custom_ig.replace('@zumrud_womens_club', data['handle'])
    
    # Replace the second instagram link (the button) which might have been missed if it was exactly the same string
    # Actually, the replace above will replace all occurrences of 'https://www.instagram.com/zumrud_womens_club/' 
    # Let's ensure the button link is correct. The original link was 'https://www.instagram.com/zumrud_womens_club/'
    
    # Find footer
    footer_idx = content.find('<footer')
    if footer_idx != -1:
        # Insert before footer
        new_content = content[:footer_idx] + custom_ig + '\n\n' + content[footer_idx:]
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
    else:
        print(f"Could not find footer in {file}")

