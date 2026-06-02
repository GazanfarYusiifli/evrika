import re

with open('lisey2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's replace the inline styles in lisey2.html
old_block = """      <div class="prog-grid" style="display: flex; flex-wrap: wrap; justify-content: center; gap: 30px; margin-top: 60px;">
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
      </div>"""

new_block = """      <style>
        .prog-card-flex { width: 250px; }
        @media (max-width: 768px) {
          .prog-card-flex { width: 100% !important; }
        }
      </style>
      <div class="prog-grid" style="display: flex; flex-wrap: wrap; justify-content: center; gap: 30px; margin-top: 60px;">
        <div class="prog-card reveal prog-card-flex">
          <img src="https://flagcdn.com/w160/az.png" alt="Azərbaycan" class="prog-flag">
          <h3 class="prog-h">Azərbaycan <br>Bölməsi</h3>
        </div>
        <div class="prog-card reveal prog-card-flex">
          <img src="https://flagcdn.com/w160/tr.png" alt="Türkiyə" class="prog-flag">
          <h3 class="prog-h">Türk <br>Bölməsi</h3>
        </div>
        <div class="prog-card reveal prog-card-flex">
          <img src="https://flagcdn.com/w160/ru.png" alt="Rusiya" class="prog-flag">
          <h3 class="prog-h">Rus <br>Bölməsi</h3>
        </div>
        <div class="prog-card reveal prog-card-flex">
          <img src="https://flagcdn.com/w160/gb.png" alt="İngiltərə" class="prog-flag">
          <h3 class="prog-h">İngilis <br>Bölməsi</h3>
        </div>
        <div class="prog-card reveal prog-card-flex">
          <div style="font-size: 3rem; margin-bottom: 20px;">🧩</div>
          <h3 class="prog-h">Montessori <br>Sinifləri</h3>
        </div>
      </div>"""

content = content.replace(old_block, new_block)

with open('lisey2.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated lisey2.html")
