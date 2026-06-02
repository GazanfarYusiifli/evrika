with open("src/style.css", "r", encoding="utf-8") as f:
    content = f.read()

old_block = """/* Mobile Nav Actions - show Qeydiyyat next to hamburger */
@media (max-width: 1024px) {
  .nav-actions {
    display: flex !important;
    align-items: center;
    margin-left: auto;
    margin-right: 15px;
  }
  
  /* Hide non-primary buttons like E-jurnal in header on mobile */
  .nav-actions > a:not(.nav-btn) {
    display: none !important;
  }
  
  /* Style Qeydiyyat button for mobile */
  .nav-actions > a.nav-btn {
    padding: 8px 18px !important;
    font-size: 0.85rem !important;
    margin: 0 !important;
  }
  
  .mobile-menu-btn {
    margin-left: 0 !important;
  }
}"""

new_block = """/* Mobile Nav Actions - show Qeydiyyat next to hamburger */
@media (max-width: 1024px) {
  .nav-actions {
    display: flex !important;
    align-items: center !important;
    margin-left: auto !important;
    margin-right: 15px !important;
  }
  
  /* Hide non-primary buttons like E-jurnal in header on mobile */
  .nav-actions > a:not(.nav-btn) {
    display: none !important;
  }
  
  /* Style Qeydiyyat button for mobile */
  .nav-actions > a.nav-btn {
    padding: 8px 18px !important;
    font-size: 0.85rem !important;
    margin: 0 !important;
    border-radius: 10px !important;
  }
  
  .mobile-menu-btn {
    margin-left: 0 !important;
  }
}"""

if old_block in content:
    content = content.replace(old_block, new_block)
    with open("src/style.css", "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated style.css successfully!")
else:
    print("Could not find the block in style.css")
