import re
import json

def update_main_js():
    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/src/main.js', 'r', encoding='utf-8') as f:
        js = f.read()

    en_names = {
        "Xudaqulu Rzayev": "Khudaqulu Rzayev",
        "Ofeliya Muradova": "Ofeliya Muradova",
        "Elvin Bədirov": "Elvin Badirov",
        "Bahar İsgəndərova": "Bahar Isgandarova",
        "Könül Mustafayeva": "Konul Mustafayeva",
        "Lalə Mürsalzadə": "Lala Mursalzada",
        "Günel Qafarova": "Gunel Qafarova",
        "Elnarə Əmiraslanova": "Elnara Amiraslanova",
        "Sevda İbrahimova": "Sevda Ibrahimova",
        "Kəmalə Cavadova": "Kamala Javadova",
        "Nazan Akkoyun": "Nazan Akkoyun",
        "Gülnar Piroğlanova": "Gulnar Piroghlanova",
        "Aygün Həmzəyeva": "Aygun Hamzayeva",
        "Orxan Əsgərov": "Orkhan Asgarov",
        "Aygül Mirzəyeva": "Aygul Mirzayeva",
        "Vəfa Xıdırova": "Vafa Khidirova",
        "Afaq Alıyeva": "Afaq Aliyeva",
        "Elməddin Musayev": "Elmaddin Musayev",

        "EVRİKA TƏHSİL EKOSİSTEMİ ÜZRƏ TƏSİSÇİ": "FOUNDER OF EVRIKA EDUCATION ECOSYSTEM",
        "EVRIKA TƏHSIL EKOSISTEMI ÜZRƏ TƏSISÇI": "FOUNDER OF EVRIKA EDUCATION ECOSYSTEM",
        
        "EVRİKA BEYNƏLXALQ ELM VƏ TEXNOLOGİYA LİSEYİ ( NƏRİMANOV FİLİALI ÜZRƏ) DİREKTOR": "DIRECTOR OF EVRIKA ISTE (NARIMANOV BRANCH)",
        "EVRIKA BEYNƏLXALQ ELM VƏ TEXNOLOGIYA LISEYI ( NƏRIMANOV FILIALI ÜZRƏ) DIREKTOR": "DIRECTOR OF EVRIKA ISTE (NARIMANOV BRANCH)",
        
        "EVRİKA BEYNƏLXALQ ELM VƏ TEXNOLOGİYA LİSEYİ ( GƏNCLİK FİLİALI ÜZRƏ ) DİREKTOR": "DIRECTOR OF EVRIKA ISTE (GANJLIK BRANCH)",
        "EVRIKA BEYNƏLXALQ ELM VƏ TEXNOLOGIYA LISEYI ( GƏNCLIK FILIALI ÜZRƏ ) DIREKTOR": "DIRECTOR OF EVRIKA ISTE (GANJLIK BRANCH)",

        "TƏMAYÜL İŞLƏRİ ÜZRƏ DİREKTOR MÜAVİNİ": "DEPUTY DIRECTOR FOR SPECIALIZED AFFAIRS",
        "TƏMAYÜL IŞLƏRI ÜZRƏ DIREKTOR MÜAVINI": "DEPUTY DIRECTOR FOR SPECIALIZED AFFAIRS",

        "MALİYYƏ DİREKTORU": "FINANCE DIRECTOR",
        "MALIYYƏ DIREKTORU": "FINANCE DIRECTOR",

        "İNSAN RESURSLARI ÜZRƏ DEPARTAMENT RƏHBƏRİ": "HEAD OF HUMAN RESOURCES",
        "İNSAN RESURSLARI ÜZRƏ DEPARTAMENT RƏHBƏRI": "HEAD OF HUMAN RESOURCES",

        "VALİDEYNLƏRLƏ İŞ ÜZRƏ DİREKTOR MÜAVİNİ": "DEPUTY DIRECTOR FOR PARENT AFFAIRS",
        "VALIDEYNLƏRLƏ İŞ ÜZRƏ DIREKTOR MÜAVINI": "DEPUTY DIRECTOR FOR PARENT AFFAIRS",

        "İBTİDAİ TƏHSİL ÜZRƏ DİREKTOR MÜAVİNİ": "DEPUTY DIRECTOR FOR PRIMARY EDUCATION",
        "İBTIDAI TƏHSIL ÜZRƏ DIREKTOR MÜAVINI": "DEPUTY DIRECTOR FOR PRIMARY EDUCATION",

        "ÜMUMİ ORTA TƏHSİL ÜZRƏ DİREKTOR MÜAVİNİ": "DEPUTY DIRECTOR FOR GENERAL SECONDARY EDUCATION",
        "ÜMUMI ORTA TƏHSIL ÜZRƏ DIREKTOR MÜAVINI": "DEPUTY DIRECTOR FOR GENERAL SECONDARY EDUCATION",

        "İNGİLİS BÖLMƏSİ RƏHBƏRİ": "HEAD OF ENGLISH DEPARTMENT",
        "İNGILIS BÖLMƏSI RƏHBƏRI": "HEAD OF ENGLISH DEPARTMENT",

        "TÜRK BÖLMƏSİ ÜZRƏ DİR. MÜAVİNİ": "DEPUTY DIRECTOR FOR TURKISH DEPARTMENT",
        "TÜRK BÖLMƏSI ÜZRƏ DIR. MÜAVINI": "DEPUTY DIRECTOR FOR TURKISH DEPARTMENT",

        "İBTİDAİ TƏRBİYƏ İŞLƏRİ MÜAVİNİ": "DEPUTY DIRECTOR FOR PRIMARY UPBRINGING",
        "İBTIDAI TƏRBIYƏ IŞLƏRI MÜAVINI": "DEPUTY DIRECTOR FOR PRIMARY UPBRINGING",

        "YUXARI SİNİF TƏRBİYƏ İŞLƏRİ MÜAVİNİ": "DEPUTY DIRECTOR FOR HIGH SCHOOL UPBRINGING",
        "YUXARI SINIF TƏRBIYƏ IŞLƏRI MÜAVINI": "DEPUTY DIRECTOR FOR HIGH SCHOOL UPBRINGING",

        "İDMAN VƏ DƏRNƏKLƏR MÜAVİNİ": "DEPUTY DIRECTOR FOR SPORTS AND CLUBS",
        "İDMAN VƏ DƏRNƏKLƏR MÜAVINI": "DEPUTY DIRECTOR FOR SPORTS AND CLUBS",

        "TƏHSİL NAZİRLİYİ ÜZRƏ KOORDİNATOR": "COORDINATOR FOR MINISTRY OF EDUCATION",
        "TƏHSIL NAZIRLIYI ÜZRƏ KOORDINATOR": "COORDINATOR FOR MINISTRY OF EDUCATION",

        "HƏKİM": "DOCTOR",
        "HƏKIM": "DOCTOR",

        "PSİXOLOQ": "PSYCHOLOGIST",
        "PSIXOLOQ": "PSYCHOLOGIST",

        "STEAM RƏHBƏRİ": "STEAM LEADER",
        "STEAM RƏHBƏRI": "STEAM LEADER"
    }

    ru_names = {
        "Xudaqulu Rzayev": "Худагулу Рзаев",
        "Ofeliya Muradova": "Офелия Мурадова",
        "Elvin Bədirov": "Эльвин Бадиров",
        "Bahar İsgəndərova": "Бахар Искендерова",
        "Könül Mustafayeva": "Кенюль Мустафаева",
        "Lalə Mürsalzadə": "Лала Мурсалзаде",
        "Günel Qafarova": "Гюнель Гафарова",
        "Elnarə Əmiraslanova": "Эльнара Амирасланова",
        "Sevda İbrahimova": "Севда Ибрагимова",
        "Kəmalə Cavadova": "Кямаля Джавадова",
        "Nazan Akkoyun": "Назан Аккоюн",
        "Gülnar Piroğlanova": "Гюльнар Пирогланова",
        "Aygün Həmzəyeva": "Айгюн Гамзаева",
        "Orxan Əsgərov": "Орхан Аскеров",
        "Aygül Mirzəyeva": "Айгюль Мирзаева",
        "Vəfa Xıdırova": "Вафа Хидирова",
        "Afaq Alıyeva": "Афаг Алыева",
        "Elməddin Musayev": "Эльмаддин Мусаев",

        "EVRİKA TƏHSİL EKOSİSTEMİ ÜZRƏ TƏSİSÇİ": "УЧРЕДИТЕЛЬ ОБРАЗОВАТЕЛЬНОЙ ЭКОСИСТЕМЫ",
        "EVRIKA TƏHSIL EKOSISTEMI ÜZRƏ TƏSISÇI": "УЧРЕДИТЕЛЬ ОБРАЗОВАТЕЛЬНОЙ ЭКОСИСТЕМЫ",

        "EVRİKA BEYNƏLXALQ ELM VƏ TEXNOLOGİYA LİSEYİ ( NƏRİMANOV FİLİALI ÜZRƏ) DİREKTOR": "ДИРЕКТОР ЭВРИКА МЛНТ (ФИЛИАЛ НАРИМАНОВ)",
        "EVRIKA BEYNƏLXALQ ELM VƏ TEXNOLOGIYA LISEYI ( NƏRIMANOV FILIALI ÜZRƏ) DIREKTOR": "ДИРЕКТОР ЭВРИКА МЛНТ (ФИЛИАЛ НАРИМАНОВ)",

        "EVRİKA BEYNƏLXALQ ELM VƏ TEXNOLOGİYA LİSEYİ ( GƏNCLİK FİLİALI ÜZRƏ ) DİREKTOR": "ДИРЕКТОР ЭВРИКА МЛНТ (ФИЛИАЛ ГЯНДЖЛИК)",
        "EVRIKA BEYNƏLXALQ ELM VƏ TEXNOLOGIYA LISEYI ( GƏNCLIK FILIALI ÜZRƏ ) DIREKTOR": "ДИРЕКТОР ЭВРИКА МЛНТ (ФИЛИАЛ ГЯНДЖЛИК)",

        "TƏMAYÜL İŞLƏRİ ÜZRƏ DİREKTOR MÜAVİNİ": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО ПРОФИЛЬНЫМ ДЕЛАМ",
        "TƏMAYÜL IŞLƏRI ÜZRƏ DIREKTOR MÜAVINI": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО ПРОФИЛЬНЫМ ДЕЛАМ",

        "MALİYYƏ DİREKTORU": "ФИНАНСОВЫЙ ДИРЕКТОР",
        "MALIYYƏ DIREKTORU": "ФИНАНСОВЫЙ ДИРЕКТОР",

        "İNSAN RESURSLARI ÜZRƏ DEPARTAMENT RƏHBƏRİ": "РУКОВОДИТЕЛЬ ОТДЕЛА КАДРОВ",
        "İNSAN RESURSLARI ÜZRƏ DEPARTAMENT RƏHBƏRI": "РУКОВОДИТЕЛЬ ОТДЕЛА КАДРОВ",

        "VALİDEYNLƏRLƏ İŞ ÜZRƏ DİREKTOR MÜAVİNİ": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО РАБОТЕ С РОДИТЕЛЯМИ",
        "VALIDEYNLƏRLƏ İŞ ÜZRƏ DIREKTOR MÜAVINI": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО РАБОТЕ С РОДИТЕЛЯМИ",

        "İBTİDAİ TƏHSİL ÜZRƏ DİREKTOR MÜAVİNİ": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО НАЧАЛЬНОМУ ОБРАЗОВАНИЮ",
        "İBTIDAI TƏHSIL ÜZRƏ DIREKTOR MÜAVINI": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО НАЧАЛЬНОМУ ОБРАЗОВАНИЮ",

        "ÜMUMİ ORTA TƏHSİL ÜZRƏ DİREKTOR MÜAVİNİ": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО ОБЩЕМУ СРЕДНЕМУ ОБРАЗОВАНИЮ",
        "ÜMUMI ORTA TƏHSIL ÜZRƏ DIREKTOR MÜAVINI": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО ОБЩЕМУ СРЕДНЕМУ ОБРАЗОВАНИЮ",

        "İNGİLİS BÖLMƏSİ RƏHBƏRİ": "ЗАВЕДУЮЩИЙ АНГЛИЙСКИМ ОТДЕЛЕНИЕМ",
        "İNGILIS BÖLMƏSI RƏHBƏRI": "ЗАВЕДУЮЩИЙ АНГЛИЙСКИМ ОТДЕЛЕНИЕМ",

        "TÜRK BÖLMƏSİ ÜZRƏ DİR. MÜAVİNİ": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО ТУРЕЦКОМУ ОТДЕЛЕНИЮ",
        "TÜRK BÖLMƏSI ÜZRƏ DIR. MÜAVINI": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО ТУРЕЦКОМУ ОТДЕЛЕНИЮ",

        "İBTİDAİ TƏRBİYƏ İŞLƏRİ MÜAVİNİ": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО ВОСПИТАТЕЛЬНОЙ РАБОТЕ (НАЧАЛЬНАЯ ШКОЛА)",
        "İBTIDAI TƏRBIYƏ IŞLƏRI MÜAVINI": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО ВОСПИТАТЕЛЬНОЙ РАБОТЕ (НАЧАЛЬНАЯ ШКОЛА)",

        "YUXARI SİNİF TƏRBİYƏ İŞLƏRİ MÜAVİNİ": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО ВОСПИТАТЕЛЬНОЙ РАБОТЕ (СТАРШИЕ КЛАССЫ)",
        "YUXARI SINIF TƏRBIYƏ IŞLƏRI MÜAVINI": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО ВОСПИТАТЕЛЬНОЙ РАБОТЕ (СТАРШИЕ КЛАССЫ)",

        "İDMAN VƏ DƏRNƏKLƏR MÜAVİNİ": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО СПОРТУ И КРУЖКАМ",
        "İDMAN VƏ DƏRNƏKLƏR MÜAVINI": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО СПОРТУ И КРУЖКАМ",

        "TƏHSİL NAZİRLİYİ ÜZRƏ KOORDİNATOR": "КООРДИНАТОР ПО ЛИНИИ МИНИСТЕРСТВА ОБРАЗОВАНИЯ",
        "TƏHSIL NAZIRLIYI ÜZRƏ KOORDINATOR": "КООРДИНАТОР ПО ЛИНИИ МИНИСТЕРСТВА ОБРАЗОВАНИЯ",

        "HƏKİM": "ВРАЧ",
        "HƏKIM": "ВРАЧ",

        "PSİXOLOQ": "ПСИХОЛОГ",
        "PSIXOLOQ": "ПСИХОЛОГ",

        "STEAM RƏHBƏRİ": "РУКОВОДИТЕЛЬ STEAM",
        "STEAM RƏHBƏRI": "РУКОВОДИТЕЛЬ STEAM"
    }

    # Append to EN
    en_str = ',\\n    '.join([f'"{k}": "{v}"' for k,v in en_names.items()])
    js = re.sub(r'("nav-home": "Home",)', r'\1\n    ' + en_str + ',', js)

    # Append to RU
    ru_str = ',\\n    '.join([f'"{k}": "{v}"' for k,v in ru_names.items()])
    js = re.sub(r'("nav-home": "Главная",)', r'\1\n    ' + ru_str + ',', js)

    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/src/main.js', 'w', encoding='utf-8') as f:
        f.write(js)

def fix_about_html_team_render():
    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/about.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Modify renderMembers inside about.html
    replacement = """
        function renderMembers(members) {
          const leadCont = document.getElementById('leadership-container');
          const boardCont = document.getElementById('board-container');
          if (!leadCont || !boardCont) return;
          leadCont.innerHTML = ''; boardCont.innerHTML = '';
          
          let currentLang = localStorage.getItem('evrika-lang') || 'az';
          let dict = window.langData ? window.langData[currentLang] : {};

          members.forEach(m => {
            const translatedName = dict[m.name] || m.name;
            const translatedRole = dict[m.role] || m.role;
            const html = `
              <div class="team-card" style="${m.category === 'leadership' ? 'aspect-ratio: 1/1.2;' : ''}">
                <div class="team-card-img"><img src="${m.img}" alt="${m.name}"></div>
                <div class="team-overlay" style="${m.category === 'leadership' ? 'padding: 15px 8px 12px;' : ''}">
                  <div class="team-name" style="${m.category === 'leadership' ? 'font-size: 0.9rem; margin-bottom: 2px;' : ''}">${translatedName}</div>
                  <div class="team-role" style="${m.category === 'leadership' ? 'font-size: 0.65rem;' : ''}">${translatedRole}</div>
                  ${m.category === 'leadership' && m.quote ? `<div class="team-quote" style="font-size: 0.6rem; margin-top: 5px;">${m.quote}</div>` : ''}
                </div>
              </div>`;
            if (m.category === 'leadership') leadCont.innerHTML += html;
            else boardCont.innerHTML += html;
          });
        }
"""
    html = re.sub(r'function renderMembers\(members\).*?\}\s*document.addEventListener', 
                  replacement.strip() + "\n        document.addEventListener", html, flags=re.DOTALL)
    
    # We also need to re-render members on language change!
    # By default, language changes in about.html do window.updateContent(lang) 
    # Let's add a small script to override window.updateContent to also fetch or just re-render if we cache members
    # Since we can't easily cache members without changing a lot, we will just call fetchManagement() inside updateContent event listener
    # Actually, we can just hook into localstorage change, but it's simpler to listen to a custom event or just poll
    # I'll just append `fetchManagement();` to the onmousedown in the language dropdown!
    html = html.replace("window.updateContent('az');", "window.updateContent('az'); setTimeout(fetchManagement, 50);")
    html = html.replace("window.updateContent('en');", "window.updateContent('en'); setTimeout(fetchManagement, 50);")
    html = html.replace("window.updateContent('ru');", "window.updateContent('ru'); setTimeout(fetchManagement, 50);")

    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/about.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    update_main_js()
    fix_about_html_team_render()
    print("Done")
