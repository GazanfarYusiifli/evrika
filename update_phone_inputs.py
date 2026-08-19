import os
import re

files = [
    'register-lisey1.html',
    'register-lisey2.html',
    'register-montessori.html',
    'register-eduhome.html',
    'register-zumrud.html'
]

for file in files:
    if not os.path.exists(file):
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # The original line:
    # <input type="tel" id="mf_phoneNum" placeholder="Məs: 551234567" data-i18n-placeholder="reg-pl-phone" required>
    
    # We want to replace it with an input group that looks like standard and also add validation.
    # To keep focus working easily, I'll wrap it but add focus-within to the wrapper inside the html via style attr or just rely on simple validation on the current input.
    # Actually, let's just add the attributes and an inline visual prefix using position absolute.
    
    search_input = r'<input type="tel" id="mf_phoneNum" placeholder="Məs: 551234567" data-i18n-placeholder="reg-pl-phone" required>'
    
    replace_input = r"""<div style="position: relative; display: flex; align-items: center;">
                <span style="position: absolute; left: 18px; color: rgba(255,255,255,0.7); font-weight: 600; font-size: 0.95rem; pointer-events: none;">+994</span>
                <input type="tel" id="mf_phoneNum" placeholder="551234567" data-i18n-placeholder="reg-pl-phone" required pattern="[0-9]{9}" maxlength="9" minlength="9" title="Nömrə yalnız 9 rəqəmdən ibarət olmalıdır (Məs: 551234567)" style="padding-left: 65px;" oninput="this.value = this.value.replace(/[^0-9]/g, '').slice(0, 9);">
              </div>"""
    
    content = re.sub(search_input, replace_input, content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Phone inputs updated")
