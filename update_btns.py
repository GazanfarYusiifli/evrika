import sys

def update_cards():
    with open('schools.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Update Lisey 2 Address
    content = content.replace(
        '<div>6 Əhməd Rəcəbli, Baku, Azerbaijan</div>',
        '<div>68 Fəxrəddin Musayev, Baku, Azerbaijan</div>'
    )

    # 1. Lisey 1 Add Qeydiyyat Button
    content = content.replace(
        '<div class="hub-action">\n                  <a href="lisey.html" class="btn btn-primary btn-xl" style="padding: 16px 40px; box-shadow: 0 10px 30px rgba(139, 26, 43, 0.2);">Ətraflı Kəşf Et</a>\n                </div>',
        '<div class="hub-action" style="gap: 16px;">\n                  <a href="lisey.html" class="btn btn-primary btn-xl" style="padding: 16px 40px; box-shadow: 0 10px 30px rgba(139, 26, 43, 0.2);">Ətraflı Kəşf Et</a>\n                  <a href="register.html" class="btn btn-primary btn-xl" style="padding: 16px 40px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05); background: #ffffff; color: var(--navy); border: 2px solid rgba(0,0,0,0.1);">Qeydiyyat <i class="fas fa-arrow-right" style="margin-left: 8px;"></i></a>\n                </div>'
    )

    # 3. Montessori Add Qeydiyyat Button
    content = content.replace(
        '<div class="hub-action">\n                  <a href="montessori.html" class="btn btn-primary btn-xl" style="background: #d4850a; border-color: #d4850a; box-shadow: 0 10px 30px rgba(212, 133, 10, 0.2); padding: 16px 40px;">Ətraflı Kəşf Et</a>\n                </div>',
        '<div class="hub-action" style="gap: 16px;">\n                  <a href="montessori.html" class="btn btn-primary btn-xl" style="background: #d4850a; border-color: #d4850a; box-shadow: 0 10px 30px rgba(212, 133, 10, 0.2); padding: 16px 40px;">Ətraflı Kəşf Et</a>\n                  <a href="register.html" class="btn btn-primary btn-xl" style="padding: 16px 40px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05); background: #ffffff; color: var(--navy); border: 2px solid rgba(0,0,0,0.1);">Qeydiyyat <i class="fas fa-arrow-right" style="margin-left: 8px;"></i></a>\n                </div>'
    )

    # 4. Eduhome Add Qeydiyyat Button
    content = content.replace(
        '<div class="hub-action">\n                  <a href="victory.html" class="btn btn-primary btn-xl" style="background: #0284c7; border-color: #0284c7; box-shadow: 0 10px 30px rgba(2, 132, 199, 0.2); padding: 16px 40px;">Ətraflı Kəşf Et</a>\n                </div>',
        '<div class="hub-action" style="gap: 16px;">\n                  <a href="victory.html" class="btn btn-primary btn-xl" style="background: #0284c7; border-color: #0284c7; box-shadow: 0 10px 30px rgba(2, 132, 199, 0.2); padding: 16px 40px;">Ətraflı Kəşf Et</a>\n                  <a href="register.html" class="btn btn-primary btn-xl" style="padding: 16px 40px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05); background: #ffffff; color: var(--navy); border: 2px solid rgba(0,0,0,0.1);">Qeydiyyat <i class="fas fa-arrow-right" style="margin-left: 8px;"></i></a>\n                </div>'
    )

    # 5. Zumrud Add Qeydiyyat Button
    content = content.replace(
        '<div class="hub-action">\n                  <a href="zumrud.html" class="btn btn-primary btn-xl" style="background: #16a34a; border-color: #16a34a; box-shadow: 0 10px 30px rgba(22, 163, 74, 0.2); padding: 16px 40px;">Ətraflı Kəşf Et</a>\n                </div>',
        '<div class="hub-action" style="gap: 16px;">\n                  <a href="zumrud.html" class="btn btn-primary btn-xl" style="background: #16a34a; border-color: #16a34a; box-shadow: 0 10px 30px rgba(22, 163, 74, 0.2); padding: 16px 40px;">Ətraflı Kəşf Et</a>\n                  <a href="register.html" class="btn btn-primary btn-xl" style="padding: 16px 40px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05); background: #ffffff; color: var(--navy); border: 2px solid rgba(0,0,0,0.1);">Qeydiyyat <i class="fas fa-arrow-right" style="margin-left: 8px;"></i></a>\n                </div>'
    )

    with open('schools.html', 'w', encoding='utf-8') as f:
        f.write(content)
        print("Updated buttons and address")

update_cards()
