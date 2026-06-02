import re

with open('montessori.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the final-cta section
old_cta = """  <!-- ── FINAL CTA ── -->
  <section id="final-cta" class="section">
    <div class="container">
      <div class="reveal" style="padding:100px 40px; background: var(--accent); border-radius:60px; box-shadow: 0 40px 100px var(--accent-glow); text-align: center; position: relative; overflow: hidden;">
        <div style="position: absolute; top: -100px; right: -100px; width: 400px; height: 400px; background: radial-gradient(circle, rgba(255,255,255,0.15) 0%, transparent 70%);"></div>
        <div style="position: absolute; bottom: -50px; left: -50px; width: 200px; height: 200px; background: radial-gradient(circle, rgba(0,0,0,0.1) 0%, transparent 70%);"></div>
        <h3 style="font-size:2.8rem; font-weight:900; color:var(--text); margin-bottom:30px; letter-spacing: -1px;">“Övladınız üçün doğru başlanğıcı seçin.”</h3>
        <p style="color:var(--text-muted); font-size:1.25rem; max-width:800px; margin:0 auto 40px; line-height:1.6; font-weight: 500;">
          <i class="fas fa-map-marker-alt" style="margin-right: 10px; opacity: 0.8;"></i> Qafur Rəşad 16, Bakı, Azərbaycan <br>
          <i class="fas fa-phone-alt" style="margin-right: 10px; opacity: 0.8; margin-top: 15px;"></i> (+994) 10 300 50 50
        </p>
        <a href="register-montessori.html" class="btn-primary" style="background:#fff; color:var(--navy); font-weight:900; padding:22px 60px; font-size:1.25rem; border: none; border-radius: 16px; box-shadow: 0 20px 40px rgba(0,0,0,0.15); transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);">Qeydiyyatdan keçin <i class="fas fa-arrow-right"></i></a>
      </div>
    </div>
  </section>"""

new_cta = """  <!-- ── FINAL CTA ── -->
  <section id="final-cta" class="section" style="background: #9ba278;">
    <div class="container">
      <div class="reveal" style="padding:100px 40px; background: #ffffff; border-radius:60px; box-shadow: 0 40px 100px rgba(0,0,0,0.1); text-align: center; position: relative; overflow: hidden;">
        <div style="position: absolute; top: -100px; right: -100px; width: 400px; height: 400px; background: radial-gradient(circle, rgba(155,162,120,0.05) 0%, transparent 70%);"></div>
        <div style="position: absolute; bottom: -50px; left: -50px; width: 200px; height: 200px; background: radial-gradient(circle, rgba(155,162,120,0.1) 0%, transparent 70%);"></div>
        <h3 style="font-size:2.8rem; font-weight:900; color:#070d1f; margin-bottom:30px; letter-spacing: -1px;">“Övladınız üçün doğru başlanğıcı seçin.”</h3>
        <p style="color:#070d1f; font-size:1.25rem; max-width:800px; margin:0 auto 40px; line-height:1.6; font-weight: 700;">
          <i class="fas fa-map-marker-alt" style="margin-right: 10px; color: #9ba278;"></i> Qafur Rəşad 16, Bakı, Azərbaycan <br>
          <i class="fas fa-phone-alt" style="margin-right: 10px; color: #9ba278; margin-top: 15px;"></i> (+994) 10 300 50 50
        </p>
        <a href="register-montessori.html" class="btn-primary" style="background:#9ba278; color:#fff; font-weight:900; padding:22px 60px; font-size:1.25rem; border: none; border-radius: 16px; box-shadow: 0 20px 40px rgba(155,162,120,0.3); transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);">Qeydiyyatdan keçin <i class="fas fa-arrow-right"></i></a>
      </div>
    </div>
  </section>"""

content = content.replace(old_cta, new_cta)

with open('montessori.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated CTA section")
