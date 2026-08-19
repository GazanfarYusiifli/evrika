import re

file = 'generate_forms.cjs'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace inputs in generate_forms.cjs
search_fields = r"""            <div class="dyn-input-group">
              <label>Şagirdin Adı</label>
              <input type="text" id="mf_firstName" placeholder="Məs: Əli" required>
            </div>
            <div class="dyn-input-group">
              <label>Şagirdin Soyadı</label>
              <input type="text" id="mf_lastName" placeholder="Məs: Əliyev" required>
            </div>
            <div class="dyn-input-group full-width">
              <label>Bölmə \(Sektor\)</label>
              <div style="position: relative;">
                <select id="mf_sector" required>
                  <option value="" disabled selected>Bölmə seçin</option>
                  \$\{sectorOptions\}
                </select>
                <i class="fas fa-chevron-down select-arrow"></i>
              </div>
            </div>
            <div class="dyn-input-group">
              <label>\$\{classLabel\}</label>
              <div style="position: relative;">
                <select id="mf_class" required>
                  \$\{classOptions\}
                </select>
                <i class="fas fa-chevron-down select-arrow"></i>
              </div>
            </div>
            <div class="dyn-input-group">
              <label>Nömrə \(55 123 45 67\)</label>
              <input type="tel" id="mf_phoneNum" placeholder="Məs: 551234567" required>
            </div>
            <div class="dyn-input-group full-width">
              <label>E-mail ünvanı</label>
              <input type="email" id="mf_email" placeholder="Məs: info@evrika.az" required>
            </div>"""

replace_fields = r"""            <div class="dyn-input-group">
              <label>ŞAGİRDİN ADI</label>
              <input type="text" id="mf_firstName" placeholder="Məs: Əli" required>
            </div>
            <div class="dyn-input-group">
              <label>ŞAGİRDİN SOYADI</label>
              <input type="text" id="mf_lastName" placeholder="Məs: Əliyev" required>
            </div>
            <div class="dyn-input-group full-width">
              <label>HAZIRDA TƏHSİL ALDIĞI TƏHSİL MÜƏSSİSƏSİ ( BAĞÇA VƏ MƏKTƏB)</label>
              <input type="text" id="mf_previousSchool" placeholder="Məs: 20 nömrəli məktəb" required>
            </div>
            <div class="dyn-input-group">
              <label>HAZIRDA TƏHSİL ALDIĞI TƏHSİL SİNİF</label>
              <input type="text" id="mf_currentClass" placeholder="Məs: 9-cu sinif" required>
            </div>
            <div class="dyn-input-group">
              <label>HAZIRDA TƏHSİL ALDIĞI TƏHSİL BÖLMƏ</label>
              <input type="text" id="mf_currentSector" placeholder="Məs: Azərbaycan bölməsi" required>
            </div>
            <div class="dyn-input-group">
              <label>MÜRACİƏT ETDİYİ SİNİF</label>
              <div style="position: relative;">
                <select id="mf_class" required>
                  ${classOptions}
                </select>
                <i class="fas fa-chevron-down select-arrow"></i>
              </div>
            </div>
            <div class="dyn-input-group">
              <label>MÜRACİƏT ETDİYİ BÖLMƏ</label>
              <div style="position: relative;">
                <select id="mf_sector" required>
                  <option value="" disabled selected>Bölmə seçin</option>
                  ${sectorOptions}
                </select>
                <i class="fas fa-chevron-down select-arrow"></i>
              </div>
            </div>
            <div class="dyn-input-group">
              <label>VALİDEYNİN ƏLAQƏ NÖMRƏSİ</label>
              <div style="position: relative; display: flex; align-items: center;">
                <span style="position: absolute; left: 18px; color: rgba(255,255,255,0.7); font-weight: 600; font-size: 0.95rem; pointer-events: none;">+994</span>
                <input type="tel" id="mf_phoneNum" placeholder="551234567" required pattern="[0-9]{9}" maxlength="9" minlength="9" title="Nömrə yalnız 9 rəqəmdən ibarət olmalıdır (Məs: 551234567)" style="padding-left: 65px;" oninput="this.value = this.value.replace(/[^0-9]/g, '').slice(0, 9);">
              </div>
            </div>
            <div class="dyn-input-group full-width">
              <label>MAİL ÜNVANI</label>
              <input type="email" id="mf_email" placeholder="Məs: info@evrika.az" required>
            </div>"""

content = re.sub(search_fields, replace_fields, content)

search_js = r"""              var firstName = document.getElementById\('mf_firstName'\).value;
              var lastName = document.getElementById\('mf_lastName'\).value;
              var sectorText = document.getElementById\('mf_sector'\).value;
              var grade = document.getElementById\('mf_class'\).value;
              var phoneNum = document.getElementById\('mf_phoneNum'\).value;
              var email = document.getElementById\('mf_email'\).value;

              var note = "Filial: \$\{branchTitle\} \| Bölmə: " \+ sectorText \+ " \| Sinif: " \+ grade \+ " \| E-mail: " \+ email;"""

replace_js = r"""              var firstName = document.getElementById('mf_firstName').value;
              var lastName = document.getElementById('mf_lastName').value;
              var sectorText = document.getElementById('mf_sector').value;
              var grade = document.getElementById('mf_class').value;
              var phoneNum = document.getElementById('mf_phoneNum').value;
              var email = document.getElementById('mf_email').value;
              var previousSchool = document.getElementById('mf_previousSchool') ? document.getElementById('mf_previousSchool').value : '';
              var currentClass = document.getElementById('mf_currentClass') ? document.getElementById('mf_currentClass').value : '';
              var currentSector = document.getElementById('mf_currentSector') ? document.getElementById('mf_currentSector').value : '';

              var note = "Filial: ${branchTitle} | Bölmə: " + sectorText + " | Sinif: " + grade + " | E-mail: " + email + " | Əvvəlki müəssisə: " + previousSchool + " | Hazırda oxuduğu sinif: " + currentClass + " | Hazırda oxuduğu bölmə: " + currentSector;"""

content = re.sub(search_js, replace_js, content)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("generate_forms.cjs updated")
