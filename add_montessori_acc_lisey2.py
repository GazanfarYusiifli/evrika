import re

new_accordion = """
  <!-- ACCORDION 0: BAĞÇA VƏ MƏKTƏBƏQƏDƏR -->
  <div class="m-acc-item" onclick="window.location.href='montessori.html';" style="cursor: pointer; border-color: rgba(108, 138, 85, 0.4); box-shadow: 0 10px 30px rgba(108,138,85,0.15);">
    <div class="m-acc-header">
      <div class="m-acc-icon" style="background: linear-gradient(135deg, #8fae73, #6c8a55); box-shadow: 0 10px 20px rgba(108, 138, 85, 0.3);"><i class="fas fa-child"></i></div>
      <div class="m-acc-title-group">
        <h3 class="m-acc-title" style="color: #8fae73;">MƏKTƏBƏQƏDƏR VƏ BAĞÇA</h3>
        <p class="m-acc-subtitle">Montessori Kids Academy</p>
      </div>
      <div style="color: #8fae73; font-size: 1.2rem;"><i class="fas fa-external-link-alt"></i></div>
    </div>
    <div class="m-acc-body m-bento-content">
       <p style="padding-top:10px;">Valideynlərimiz tez-tez məktəbəqədər uşaqlar üçün Montessori proqramını soruşurlar. <strong>Montessori Kids Academy</strong> bölməmizdə 2-6 yaşlı uşaqlar üçün xüsusi inkişaf proqramımız fəaliyyət göstərir!</p>
    </div>
  </div>
"""

filepath = 'lisey2.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

if 'ACCORDION 0: BAĞÇA' not in content:
    content = content.replace('<!-- ACCORDION 1: İBTİDAİ TƏHSİL -->', new_accordion + '\n  <!-- ACCORDION 1: İBTİDAİ TƏHSİL -->')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added new accordion.")
else:
    print("Already added.")
