import os
import re

desktop_replacement = """
<a class="dropdown-item" href="montessori.html">
<div class="item-icon"><i class="fas fa-child"></i></div>
<div class="dropdown-item-text">
<span class="dropdown-item-title" data-i18n="nav-montessori">Montessori Kids Academy</span>
<span class="dropdown-item-desc" data-i18n="nav-montessori-desc">Bağça və Erkən İnkişaf</span>
</div>
</a>
<a class="dropdown-item" href="lisey2.html">
<div class="item-icon"><i class="fas fa-school"></i></div>
<div class="dropdown-item-text">
<span class="dropdown-item-title" data-i18n="nav-montessori-sinifleri">Montessorri Sinifləri</span>
<span class="dropdown-item-desc" data-i18n="nav-montessori-sinifleri-desc">I–XI Siniflər üzrə Montessori Təhsili</span>
</div>
</a>
<a class="dropdown-item" href="lisey.html">
<div class="item-icon"><i class="fas fa-microscope"></i></div>
<div class="dropdown-item-text">
<span class="dropdown-item-title" data-i18n="nav-lisey1">Evrika BETL Nərimanov</span>
<span class="dropdown-item-desc" data-i18n="nav-lisey1-desc">Elm və Texnologiya Mərkəzi</span>
</div>
</a>
<a class="dropdown-item" href="lisey2.html">
<div class="item-icon"><i class="fas fa-atom"></i></div>
<div class="dropdown-item-text">
<span class="dropdown-item-title" data-i18n="nav-lisey2">Evrika BETL Gənclik</span>
<span class="dropdown-item-desc" data-i18n="nav-lisey2-desc">Beynəlxalq Təhsil Müəssisəsi</span>
</div>
</a>
<a class="dropdown-item" href="victory.html">
<div class="item-icon"><i class="fas fa-graduation-cap"></i></div>
<div class="dropdown-item-text">
<span class="dropdown-item-title" data-i18n="nav-eduhome">Victory Colleges by Evrika</span>
<span class="dropdown-item-desc" data-i18n="nav-eduhome-desc">Xaricdə Təhsil və Hazırlıq</span>
</div>
</a>
<a class="dropdown-item" href="zumrud.html">
<div class="item-icon"><i class="fas fa-swimmer"></i></div>
<div class="dropdown-item-text">
<span class="dropdown-item-title" data-i18n="nav-zumrud">Zümrüd İdman Mərkəzi</span>
<span class="dropdown-item-desc" data-i18n="nav-zumrud-desc">Sağlam Həyat və Fəaliyyət</span>
</div>
</a>
"""

for root, dirs, files in os.walk("."):
    if "dist" in root or "node_modules" in root or ".git" in root:
        continue
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            # Desktop: from href="schools.html" to the end of the nav-dropdown block.
            # We match the anchor, the start of nav-dropdown, and then replace its content up to the closing tags.
            pattern_desktop = r'(<a[^>]*href="schools.html"[^>]*>.*?</a>\s*<div class="nav-dropdown">).*?(</div>\s*</div>\s*<div class="nav-item-has-dropdown">\s*<a[^>]*href="vacancy.html")'
            new_content = re.sub(pattern_desktop, r'\g<1>' + desktop_replacement + r'\g<2>', content, flags=re.DOTALL)
            
            if new_content != content:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Updated {file}")
