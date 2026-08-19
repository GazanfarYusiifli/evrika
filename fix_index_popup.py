import re

file = 'index.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the inner part of initPopups()
old_init_popups_regex = r'const modal = document\.createElement\(\'div\'\);.*?sessionStorage\.setItem\(\'evrika_popup_seen\', \'true\'\);\s*};'

new_init_popups = """
                const modal = document.createElement('div');
                modal.className = "welcome-modal-overlay";
                modal.id = "welcomeModal";
                
                let linkHTML = p.link ? `<a class="welcome-modal-btn" href="${p.link}">Ətraflı</a>` : '';
                
                modal.innerHTML = `
                  <div class="welcome-modal-content">
                    <div class="welcome-modal-close" id="close-campaign-popup">
                      <i class="fas fa-times"></i>
                    </div>
                    ${p.img ? `<img alt="${p.title}" class="welcome-modal-image" src="${p.img}"/>` : ''}
                    <div class="welcome-modal-body">
                      <h2 class="welcome-modal-title">${p.title}</h2>
                      ${linkHTML}
                    </div>
                  </div>
                `;
                document.body.appendChild(modal);
                
                // Show modal with animation
                setTimeout(() => {
                  modal.classList.add('active');
                }, 1000);
                
                document.getElementById('close-campaign-popup').onclick = () => {
                   modal.classList.remove('active');
                   setTimeout(() => modal.remove(), 600);
                   sessionStorage.setItem('evrika_popup_seen', 'true');
                };
"""

if re.search(old_init_popups_regex, content, flags=re.DOTALL):
    content = re.sub(old_init_popups_regex, new_init_popups, content, flags=re.DOTALL)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Reverted to old light popup style in index.html.")
else:
    print("Pattern not found. Trying a manual fallback.")
