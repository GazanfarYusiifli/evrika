import sys

html_content = """
            <!-- Item 1: Lisey 1 -->
            <div class="reveal" style="display: grid; grid-template-columns: 1.2fr 1fr; gap: 60px; align-items: center; background: var(--white); border-radius: var(--radius-xl); overflow: hidden; box-shadow: 0 40px 100px rgba(76, 96, 171,0.06);">
               <div style="height: 100%; min-height: 500px; background: url('/assets/images/lisey_building.png') no-repeat center center / cover;"></div>
               <div style="padding: 60px;">
                  <div style="color: var(--burgundy); font-weight: 800; text-transform: uppercase; letter-spacing: 0.2em; margin-bottom: 16px;">Elm və Texnologiya</div>
                  <h2 style="font-size: 2.5rem; color: var(--navy); margin-bottom: 24px; font-weight: 900; line-height: 1.1;">EVRİKA Beynəlxalq Elm və Texnologiya Liseyi 1</h2>
                  <div style="font-size: 1.1rem; color: var(--text-muted); line-height: 1.8; margin-bottom: 30px;">
                    AZ, RUS, ENG SEKTORU
                  </div>
                  <ul style="list-style: none; margin-bottom: 40px;">
                    <li style="margin-bottom: 15px; display: flex; align-items: center; color: var(--navy); font-weight: 600;"><i class="fas fa-map-marker-alt" style="color: var(--burgundy); margin-right: 12px;"></i> ÜNVAN: </li>
                    <li style="margin-bottom: 15px; display: flex; align-items: center; color: var(--navy); font-weight: 600;"><i class="fas fa-phone-alt" style="color: var(--burgundy); margin-right: 12px;"></i> ƏLAQƏ TELEFONU: </li>
                  </ul>
                  <a href="lisey.html" class="btn btn-primary btn-xl" style="width: 100%; justify-content: center;">Ətraflı Bax</a>
               </div>
            </div>

            <!-- Item 2: Lisey 2 -->
            <div class="reveal" style="display: grid; grid-template-columns: 1fr 1.2fr; gap: 60px; align-items: center; background: var(--white); border-radius: var(--radius-xl); overflow: hidden; box-shadow: 0 40px 100px rgba(76, 96, 171,0.06);">
               <div style="padding: 60px;">
                  <div style="color: var(--burgundy); font-weight: 800; text-transform: uppercase; letter-spacing: 0.2em; margin-bottom: 16px;">Elm və Texnologiya</div>
                  <h2 style="font-size: 2.5rem; color: var(--navy); margin-bottom: 24px; font-weight: 900; line-height: 1.1;">EVRİKA Beynəlxalq Elm və Texnologiya Liseyi 2</h2>
                  <div style="font-size: 1.1rem; color: var(--text-muted); line-height: 1.8; margin-bottom: 30px;">
                    AZ, TURK, RUS, ENG SEKTORU<br>Montessori məktəbi (ibtidai)
                  </div>
                  <ul style="list-style: none; margin-bottom: 40px;">
                    <li style="margin-bottom: 15px; display: flex; align-items: center; color: var(--navy); font-weight: 600;"><i class="fas fa-map-marker-alt" style="color: var(--burgundy); margin-right: 12px;"></i> ÜNVAN: </li>
                    <li style="margin-bottom: 15px; display: flex; align-items: center; color: var(--navy); font-weight: 600;"><i class="fas fa-phone-alt" style="color: var(--burgundy); margin-right: 12px;"></i> ƏLAQƏ TELEFONU: </li>
                  </ul>
                  <a href="lisey.html" class="btn btn-primary btn-xl" style="width: 100%; justify-content: center;">Ətraflı Bax</a>
               </div>
               <div style="height: 100%; min-height: 500px; background: url('https://files.cdn-files-a.com/uploads/10086696/2000_695e52c388a8e.jpg') no-repeat center center / cover;"></div>
            </div>

            <!-- Item 3: Montessori -->
            <div class="reveal" style="display: grid; grid-template-columns: 1.2fr 1fr; gap: 60px; align-items: center; background: var(--white); border-radius: var(--radius-xl); overflow: hidden; box-shadow: 0 40px 100px rgba(76, 96, 171,0.06);">
               <div style="height: 100%; min-height: 500px; background: url('https://images.unsplash.com/photo-1503454537195-1dcabb73ffb9?auto=format&fit=crop&q=80&w=1200') no-repeat center center / cover;"></div>
               <div style="padding: 60px;">
                  <div style="color: #d4850a; font-weight: 800; text-transform: uppercase; letter-spacing: 0.2em; margin-bottom: 16px;">Erkən İnkişaf</div>
                  <h2 style="font-size: 2.5rem; color: var(--navy); margin-bottom: 24px; font-weight: 900; line-height: 1.1;">Evrika Montessori Kids Academy</h2>
                  <div style="font-size: 1.1rem; color: var(--text-muted); line-height: 1.8; margin-bottom: 30px;">
                    AZ, TURK, RUS, ENG SEKTORU<br>1-3 yaş qruplar<br>3-6 yaş 
                  </div>
                  <ul style="list-style: none; margin-bottom: 40px;">
                    <li style="margin-bottom: 15px; display: flex; align-items: center; color: var(--navy); font-weight: 600;"><i class="fas fa-map-marker-alt" style="color: #d4850a; margin-right: 12px;"></i> ÜNVAN: </li>
                    <li style="margin-bottom: 15px; display: flex; align-items: center; color: var(--navy); font-weight: 600;"><i class="fas fa-phone-alt" style="color: #d4850a; margin-right: 12px;"></i> ƏLAQƏ TELEFONU: </li>
                  </ul>
                  <a href="montessori.html" class="btn btn-primary btn-xl" style="width: 100%; justify-content: center; background: #d4850a; border-color: #d4850a;">Ətraflı Bax</a>
               </div>
            </div>

            <!-- Item 4: Eduhome -->
            <div class="reveal" style="display: grid; grid-template-columns: 1fr 1.2fr; gap: 60px; align-items: center; background: var(--white); border-radius: var(--radius-xl); overflow: hidden; box-shadow: 0 40px 100px rgba(76, 96, 171,0.06);">
               <div style="padding: 60px;">
                  <div style="color: #0284c7; font-weight: 800; text-transform: uppercase; letter-spacing: 0.2em; margin-bottom: 16px;">Akademik Dəstək</div>
                  <h2 style="font-size: 2.5rem; color: var(--navy); margin-bottom: 24px; font-weight: 900; line-height: 1.1;">Eduhome Təhsil Mərkəzi</h2>
                  <div style="font-size: 1.1rem; color: var(--text-muted); line-height: 1.8; margin-bottom: 30px;">
                    SAT, IELTS, TOEFL, DIM, DİGƏR XARİCİ DİL HAZIRLIQLARI
                  </div>
                  <ul style="list-style: none; margin-bottom: 40px;">
                    <li style="margin-bottom: 15px; display: flex; align-items: center; color: var(--navy); font-weight: 600;"><i class="fas fa-map-marker-alt" style="color: #0284c7; margin-right: 12px;"></i> ÜNVAN: </li>
                    <li style="margin-bottom: 15px; display: flex; align-items: center; color: var(--navy); font-weight: 600;"><i class="fas fa-phone-alt" style="color: #0284c7; margin-right: 12px;"></i> ƏLAQƏ TELEFONU: </li>
                  </ul>
                  <a href="eduhome.html" class="btn btn-primary btn-xl" style="width: 100%; justify-content: center; background: #0284c7; border-color: #0284c7;">Ətraflı Bax</a>
               </div>
               <div style="height: 100%; min-height: 500px; background: url('https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&q=80&w=1200') no-repeat center center / cover;"></div>
            </div>

            <!-- Item 5: Zümrüd -->
            <div class="reveal" style="display: grid; grid-template-columns: 1.2fr 1fr; gap: 60px; align-items: center; background: var(--white); border-radius: var(--radius-xl); overflow: hidden; box-shadow: 0 40px 100px rgba(76, 96, 171,0.06);">
               <div style="height: 100%; min-height: 500px; background: url('https://files.cdn-files-a.com/uploads/10086696/800_67876d203dee6_filter_67876d35c2717.jpg') no-repeat center center / cover;"></div>
               <div style="padding: 60px;">
                  <div style="color: #16a34a; font-weight: 800; text-transform: uppercase; letter-spacing: 0.2em; margin-bottom: 16px;">Peşəkar İdman</div>
                  <h2 style="font-size: 2.5rem; color: var(--navy); margin-bottom: 24px; font-weight: 900; line-height: 1.1;">Zümrüd Women Club</h2>
                  <div style="font-size: 1.1rem; color: var(--text-muted); line-height: 1.8; margin-bottom: 30px;">
                    By Evrika Active Life<br>Ana və uşaqlar<br>üzgüçülük<br>fitness<br>pilates<br>yoga və s.
                  </div>
                  <ul style="list-style: none; margin-bottom: 40px;">
                    <li style="margin-bottom: 15px; display: flex; align-items: center; color: var(--navy); font-weight: 600;"><i class="fas fa-map-marker-alt" style="color: #16a34a; margin-right: 12px;"></i> ÜNVAN: </li>
                    <li style="margin-bottom: 15px; display: flex; align-items: center; color: var(--navy); font-weight: 600;"><i class="fas fa-phone-alt" style="color: #16a34a; margin-right: 12px;"></i> ƏLAQƏ TELEFONU: </li>
                  </ul>
                  <a href="zumrud.html" class="btn btn-primary btn-xl" style="width: 100%; justify-content: center; background: #16a34a; border-color: #16a34a;">Ətraflı Bax</a>
               </div>
            </div>
"""

content = open('schools.html').read()
start_marker = '<!-- Item 1: Lisey -->'
end_marker = '<!-- Footer Copy From Index -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + html_content + '          </div>\n        </div>\n      </section>\n    </main>\n\n    ' + content[end_idx:]
    open('schools.html', 'w').write(new_content)
    print("Success")
else:
    print("Markers not found")
