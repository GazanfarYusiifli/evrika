import os
import re

desktop_new = """<a class="dropdown-item" href="montessori.html">
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
</a>"""

mobile_new = """<a href="montessori.html">
<div class="acc-icon"><i class="fas fa-child"></i></div>
<div class="acc-text"><span class="acc-title" data-i18n="nav-montessori">Montessori Kids Academy</span><span class="acc-desc" data-i18n="nav-montessori-desc">Bağça və Erkən İnkişaf</span></div>
</a>
<a href="lisey2.html">
<div class="acc-icon"><i class="fas fa-school"></i></div>
<div class="acc-text"><span class="acc-title" data-i18n="nav-montessori-sinifleri">Montessorri Sinifləri</span><span class="acc-desc" data-i18n="nav-montessori-sinifleri-desc">I–XI Siniflər üzrə Montessori Təhsili</span></div>
</a>
<a href="lisey.html">
<div class="acc-icon"><i class="fas fa-microscope"></i></div>
<div class="acc-text"><span class="acc-title" data-i18n="nav-lisey1">Evrika BETL Nərimanov</span><span class="acc-desc" data-i18n="nav-lisey1-desc">Elm və Texnologiya Mərkəzi</span></div>
</a>
<a href="lisey2.html">
<div class="acc-icon"><i class="fas fa-atom"></i></div>
<div class="acc-text"><span class="acc-title" data-i18n="nav-lisey2">Evrika BETL Gənclik</span><span class="acc-desc" data-i18n="nav-lisey2-desc">Beynəlxalq Təhsil Müəssisəsi</span></div>
</a>
<a href="victory.html">
<div class="acc-icon"><i class="fas fa-graduation-cap"></i></div>
<div class="acc-text"><span class="acc-title" data-i18n="nav-eduhome">Victory Colleges by Evrika</span><span class="acc-desc" data-i18n="nav-eduhome-desc">Xaricdə Təhsil və Hazırlıq</span></div>
</a>
<a href="zumrud.html">
<div class="acc-icon"><i class="fas fa-swimmer"></i></div>
<div class="acc-text"><span class="acc-title" data-i18n="nav-zumrud">Zümrüd İdman Mərkəzi</span><span class="acc-desc" data-i18n="nav-zumrud-desc">Sağlam Həyat və Fəaliyyət</span></div>
</a>"""

import glob

for path in glob.glob("*.html") + glob.glob("live_vercel_code/*.html"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # Desktop
        # We find the start of the 'schools.html' dropdown list.
        # We match <a ... href="lisey.html"> up to </a> of zumrud.html
        # Since it's exactly 5 items, let's use regex that starts with lisey.html and ends with zumrud.html</a>
        
        desktop_pattern = r'<a class="dropdown-item" href="lisey\.html">.*?<a class="dropdown-item" href="zumrud\.html">.*?</a>'
        new_content = re.sub(desktop_pattern, desktop_new, content, flags=re.DOTALL)
        
        # Mobile
        # Starts with <a href="lisey.html"> inside acc-icon, ends with <a href="zumrud.html">...</a>
        mobile_pattern = r'<a href="lisey\.html">\s*<div class="acc-icon">.*?<a href="zumrud\.html">\s*<div class="acc-icon">.*?</a>'
        new_content = re.sub(mobile_pattern, mobile_new, new_content, flags=re.DOTALL)

        if new_content != content:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated {path}")
            
    except Exception as e:
        print(f"Error on {path}: {e}")
