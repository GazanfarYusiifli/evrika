import re

with open('lisey2.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_pattern = r'<!-- Single Paper Sheet \(Dynamic\) -->'
end_pattern = r'</section>\s*<!-- 2\. The Folder Section'

start_match = re.search(start_pattern, content)
end_match = re.search(end_pattern, content)

if start_match and end_match:
    start_idx = start_match.start()
    
    # We want to keep </section> at the end, so we replace up to end_match.start() but we need to close the container and stack-wrapper.
    # Wait, the structure in lisey2 is:
    # <div class="stack-wrapper">
    #   <section class="section stack-base" ...>
    #     <div class="container">
    #       <!-- Single Paper Sheet (Dynamic) -->
    #       ...
    #       </style>
    #     </div>
    #   </section>
    
    # We will replace from <!-- Single Paper Sheet (Dynamic) --> up to but not including </div>\n    </section>
    
    end_pattern_inner = r'</div>\s*</section>\s*<!-- 2\. The Folder Section'
    end_match_inner = re.search(end_pattern_inner, content)
    
    if end_match_inner:
        end_idx = end_match_inner.start()
        
        new_html = """
      <div class="sec-header reveal" style="text-align:center;">
        <span class="sec-tag" style="margin: 0 auto 20px;">AKADEMİK</span>
        <h2 class="sec-h2-modern">Tədris <em>Bölmələri</em></h2>
      </div>
      
      <div class="prog-grid" style="display: flex; flex-wrap: wrap; justify-content: center; gap: 30px; margin-top: 60px;">
        <div class="prog-card reveal" style="width: 250px;">
          <img src="https://flagcdn.com/w160/az.png" alt="Azərbaycan" class="prog-flag">
          <h3 class="prog-h">Azərbaycan <br>Bölməsi</h3>
        </div>
        <div class="prog-card reveal" style="width: 250px;">
          <img src="https://flagcdn.com/w160/tr.png" alt="Türkiyə" class="prog-flag">
          <h3 class="prog-h">Türk <br>Bölməsi</h3>
        </div>
        <div class="prog-card reveal" style="width: 250px;">
          <img src="https://flagcdn.com/w160/ru.png" alt="Rusiya" class="prog-flag">
          <h3 class="prog-h">Rus <br>Bölməsi</h3>
        </div>
        <div class="prog-card reveal" style="width: 250px;">
          <img src="https://flagcdn.com/w160/gb.png" alt="İngiltərə" class="prog-flag">
          <h3 class="prog-h">İngilis <br>Bölməsi</h3>
        </div>
        <div class="prog-card reveal" style="width: 250px;">
          <div style="font-size: 3rem; margin-bottom: 20px;">🧩</div>
          <h3 class="prog-h">Montessori <br>Sinifləri</h3>
        </div>
      </div>
"""
        
        new_content = content[:start_idx] + new_html + content[end_idx:]
        
        with open('lisey2.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Replaced successfully")
    else:
        print("Could not find end inner")
else:
    print("Could not find start/end")
