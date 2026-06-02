import os
import re

mobile_css = """
@media (max-width: 1024px) {
  .nav-glass-container {
    display: flex !important;
    align-items: center !important;
    flex-direction: row !important;
    width: 100% !important;
    box-sizing: border-box !important;
    padding: 8px 15px !important;
    margin: 0 !important;
    border-radius: 0 !important;
  }

  .modern-floating-nav.scrolled .nav-glass-container {
    padding: 8px 15px !important;
    border-radius: 0 !important;
  }

  .nav-glass-container .logo {
    flex-shrink: 0 !important;
  }

  .nav-links {
    display: none !important;
  }

  .nav-actions,
  .modern-floating-nav.scrolled .nav-actions,
  .modern-floating-nav.nav-hidden .nav-actions {
    display: flex !important;
    align-items: center !important;
    margin-left: auto !important;
    margin-right: 0 !important;
    flex-shrink: 0 !important;
  }
  
  .nav-actions > a:not(.nav-btn) {
    display: none !important;
  }
  
  .nav-actions > a.nav-btn {
    padding: 8px 16px !important;
    font-size: 0.82rem !important;
    margin: 0 !important;
    border-radius: 10px !important;
    white-space: nowrap !important;
  }
  
  .nav-actions > a.nav-btn:hover {
    transform: none !important;
  }

  .mobile-menu-btn,
  .modern-floating-nav.scrolled .mobile-menu-btn,
  .modern-floating-nav.nav-hidden .mobile-menu-btn {
    margin-left: 8px !important;
    margin-right: 10px !important;
    flex-shrink: 0 !important;
    position: relative !important;
    right: auto !important;
    top: auto !important;
    transform: none !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    width: 44px !important;
    height: 44px !important;
    background: #f8f9fa !important;
    border: 1px solid rgba(0,0,0,0.1) !important;
    color: #070d1f !important;
    border-radius: 50% !important;
  }

  .modern-floating-nav {
    position: fixed !important;
    top: 0 !important;
    width: 100% !important;
    left: 0 !important;
    right: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
    border-bottom: 1px solid rgba(0,0,0,0.05) !important;
    box-shadow: 0 4px 20px rgba(0,0,0,0.03) !important;
    pointer-events: auto !important;
  }

  .modern-floating-nav.nav-hidden {
    transform: translateY(-100%) !important;
  }

  .modern-floating-nav.scrolled {
    transform: translateY(0) !important;
    top: 0 !important;
  }
}
"""

files_to_check = [f for f in os.listdir('.') if f.endswith('.html')]

for file in files_to_check:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # If it uses style.css or main.js, it gets the global styles anyway, 
    # but we deleted the inline block in all files.
    # Actually, we should just inject this right before the closing </style> tag 
    # in ANY file that has a <style> tag, just to be absolutely sure.
    
    # Wait, if we inject it into index.html, it's redundant but safe because of !important.
    # But better only inject if the file does NOT have main.js or style.css.
    
    if 'style.css' not in content and 'main.js' not in content:
        # Find the last </style>
        if '</style>' in content:
            new_content = content.replace('</style>', mobile_css + '\n</style>', 1)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Injected mobile nav styles into {file}")

