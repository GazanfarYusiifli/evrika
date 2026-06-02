import sys

css_file = "src/style.css"

with open(css_file, "r") as f:
    css_content = f.read()

if "/* === GLOBAL MOBILE RESPONSIVENESS FIXES === */" not in css_content:
    mobile_css = """

/* === GLOBAL MOBILE RESPONSIVENESS FIXES === */
@media (max-width: 768px) {
  /* Prevent horizontal scrolling globally */
  html, body {
    overflow-x: hidden !important;
    width: 100% !important;
    max-width: 100vw !important;
  }

  /* Optimize section spacing for small screens */
  section, .section, .modern-section, .parents-modern-section, footer {
    padding-top: 60px !important;
    padding-bottom: 60px !important;
  }
  
  /* Container adjustments */
  .container {
    padding-left: 20px !important;
    padding-right: 20px !important;
    width: 100% !important;
    max-width: 100vw !important;
    box-sizing: border-box !important;
  }

  /* Typography scale-down */
  h1 { font-size: 2.2rem !important; line-height: 1.1 !important; }
  h2 { font-size: 1.8rem !important; line-height: 1.2 !important; margin-bottom: 15px !important; }
  h3 { font-size: 1.5rem !important; line-height: 1.3 !important; }
  p { font-size: 1rem !important; line-height: 1.5 !important; }

  /* Ensure grid and flex containers wrap properly */
  .grid, .grid-2, .grid-3, .grid-4, 
  .infra-grid, .prog-grid, .team-grid, .values-grid,
  .footer-top, .footer-grid {
    grid-template-columns: 1fr !important;
    gap: 20px !important;
  }

  .flex-row, .d-flex {
    flex-direction: column !important;
  }

  /* Images should never overflow */
  img, video {
    max-width: 100% !important;
    height: auto;
  }

  /* Buttons and CTAs */
  .btn, .modern-btn, .primary-btn {
    width: 100% !important;
    text-align: center !important;
    justify-content: center !important;
    margin-bottom: 10px !important;
  }

  /* Hero Section adjustments */
  .hero-content {
    margin-top: 80px !important;
    padding: 20px !important;
    text-align: center !important;
  }
  .hero-buttons {
    flex-direction: column !important;
    width: 100% !important;
  }

  /* Hide decorative elements that overlap */
  .decorative-blob, .bg-shape {
    display: none !important;
  }

  /* Improve Card padding */
  .parent-testimonial-card, .value-card, .prog-item, .infra-card {
    padding: 20px !important;
    flex-direction: column !important;
    gap: 15px !important;
  }

  /* Navigation adjustments */
  .mobile-nav-trigger {
    display: flex !important;
  }
}
"""
    with open(css_file, "a") as f:
        f.write(mobile_css)
    print("Mobile fixes appended successfully.")
else:
    print("Mobile fixes already exist.")

