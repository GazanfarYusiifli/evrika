import os
import re

files = ["lisey.html", "lisey2.html", "montessori.html", "eduhome.html", "zumrud.html"]

css_new = """
.mobile-nav-links {
  display: flex;
  flex-direction: column;
  width: 100%;
  flex: 1;
}

.mobile-nav-links a {
  color: #070d1f;
  text-decoration: none;
  font-size: 1.5rem !important;
  font-weight: 700 !important;
  padding: 22px 30px !important;
  border-bottom: 1px solid rgba(0,0,0,0.05);
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  transition: all 0.3s ease;
  background: transparent;
  opacity: 1 !important;
  transform: none !important;
  letter-spacing: 0 !important;
}

.mobile-nav-links a::after {
  content: '\\f105';
  font-family: 'Font Awesome 5 Free';
  font-weight: 900;
  opacity: 0.3;
  font-size: 1.1rem;
}

.mobile-nav-links a:hover {
  background: rgba(0,0,0,0.02);
  color: var(--accent, var(--burgundy));
  padding-left: 35px !important;
}

/* ── Mobile Accordion Styles ── */
.mobile-accordion {
  border-bottom: 1px solid rgba(0,0,0,0.05);
}

.mobile-accordion-trigger {
  color: #070d1f;
  font-size: 1.5rem !important;
  font-weight: 700 !important;
  padding: 22px 30px !important;
  display: flex;
  align-items: center;
  justify-content: space-between;
  cursor: pointer;
  background: transparent;
  border: none;
  width: 100%;
  text-align: left;
  letter-spacing: 0;
  transition: all 0.3s ease;
}

.mobile-nav-links .mobile-accordion-trigger:hover {
  background: rgba(0,0,0,0.02);
  color: var(--accent, var(--burgundy));
  padding-left: 35px !important;
}

.mobile-nav-links .mobile-accordion.open .mobile-accordion-trigger {
  color: var(--accent, var(--burgundy));
}

.acc-arrow {
  color: rgba(0,0,0,0.3);
  font-size: 1.2rem;
  transition: transform 0.3s ease;
}

.mobile-accordion.open .acc-arrow {
  color: var(--accent, var(--burgundy));
  transform: rotate(90deg);
}

.mobile-accordion-body {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  background: rgba(0,0,0,0.02);
  border-radius: 0 0 12px 12px;
  padding: 0 16px;
  margin-bottom: 10px;
}

.mobile-accordion.open .mobile-accordion-body {
  max-height: 700px;
  padding: 10px 16px;
}

.mobile-accordion-body a {
  display: flex !important;
  align-items: center !important;
  gap: 12px !important;
  font-size: 0.9rem !important;
  padding: 12px 14px !important;
  border-bottom: none !important;
  border-radius: 10px !important;
  margin-bottom: 4px;
  background: rgba(0,0,0,0.03) !important;
  color: #070d1f !important;
  letter-spacing: 0 !important;
  transition: all 0.25s !important;
}

.mobile-accordion-body a::after {
  display: none !important;
}

.mobile-accordion-body a:hover {
  background: rgba(139,26,43,0.06) !important;
  color: var(--accent, var(--burgundy)) !important;
  padding-left: 14px !important;
}

.acc-icon {
  width: 36px;
  height: 36px;
  border-radius: 10px;
  background: rgba(139,26,43,0.08);
  color: var(--accent, var(--burgundy));
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.9rem;
  flex-shrink: 0;
}

.acc-text {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.acc-title {
  color: #070d1f;
  font-weight: 700;
  font-size: 0.88rem;
  line-height: 1.3;
}

.acc-desc {
  color: rgba(0,0,0,0.5);
  font-size: 0.72rem;
}
"""

for fname in files:
    if not os.path.exists(fname):
        print(f"Skipping {fname}")
        continue
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()

    # Find where .mobile-nav-links { starts, and where .acc-desc { ... } ends
    # Note that in lisey.html and lisey2.html, we already have .mobile-accordion styles.
    # In montessori, eduhome, zumrud, we might only have .mobile-nav-links.
    
    start_pattern = re.search(r'\.mobile-nav-links\s*{', content)
    
    if not start_pattern:
        print(f"Could not find .mobile-nav-links in {fname}")
        continue
        
    start_idx = start_pattern.start()
    
    # Let's find the end. Look for `@media(max-width:1024px) {` which comes after it.
    end_pattern = re.search(r'@media\s*\(max-width:\s*1024px\)\s*{', content[start_idx:])
    if end_pattern:
        end_idx = start_idx + end_pattern.start()
        
        # Replace everything between start_idx and end_idx with css_new
        new_content = content[:start_idx] + css_new + "\n" + content[end_idx:]
        with open(fname, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {fname}")
    else:
        print(f"Could not find @media(max-width:1024px) after mobile-nav in {fname}")

