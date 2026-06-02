import glob
import re

files = glob.glob('*.html')

script_to_add = """
  <script>
    function toggleMobileAcc(id) {
      var el = document.getElementById(id);
      if (!el) return;
      el.classList.toggle('open');
    }
  </script>
"""

for filepath in files:
    # Skip admin or payment if they don't have mobile-accordion
    if filepath in ['admin.html', 'verify.html', 'payment.html', 'admin-login.html']:
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if "mobile-accordion-trigger" in content and "function toggleMobileAcc" not in content:
        content = content.replace("</body>", script_to_add + "</body>")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added toggleMobileAcc to {filepath}")
    elif "function toggleMobileAcc" in content:
        print(f"toggleMobileAcc already in {filepath}")
    else:
        print(f"No mobile accordion found in {filepath}")
