import glob
import re

files = glob.glob('register-*.html')

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
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if "function toggleMobileAcc" not in content:
        content = content.replace("</body>", script_to_add + "</body>")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added toggleMobileAcc to {filepath}")
    else:
        print(f"toggleMobileAcc already in {filepath}")
