import re

def fix_about_html_again():
    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/about.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix Evrika Konsepsiyası
    html = re.sub(
        r'(<h2 class="titan-header".*?>)\s*Evrika Konsepsiyası\s*</h2>',
        r'\1<span data-i18n="about-concept-title">Evrika Konsepsiyası</span></h2>',
        html
    )

    # Fix İdarə Heyəti duplicate data-i18n
    html = html.replace('data-i18n="team-board" ', '')

    # Hardcode the role/name dictionary directly into renderMembers to avoid any window/module scope timing issues!
    replacement = """
        function renderMembers(members) {
          const leadCont = document.getElementById('leadership-container');
          const boardCont = document.getElementById('board-container');
          if (!leadCont || !boardCont) return;
          leadCont.innerHTML = ''; boardCont.innerHTML = '';
          
          let currentLang = localStorage.getItem('evrika-lang') || 'az';
          
          const dicts = {
            en: {
                "Təmayül işləri üzrə direktor müavini": "DEPUTY DIRECTOR FOR SPECIALIZED AFFAIRS",
                "Maliyyə Direktoru": "FINANCE DIRECTOR",
                "İnsan Resursları üzrə departament rəhbəri": "HEAD OF HUMAN RESOURCES",
                "Valideynlərlə İş üzrə direktor müavini": "DEPUTY DIRECTOR FOR PARENT AFFAIRS",
                "İbtidai təhsil üzrə direktor müavini": "DEPUTY DIRECTOR FOR PRIMARY EDUCATION",
                "Ümumi Orta Təhsil üzrə direktor müavini": "DEPUTY DIRECTOR FOR GENERAL SECONDARY EDUCATION",
                "İngilis bölməsi rəhbəri": "HEAD OF ENGLISH DEPARTMENT",
                "Türk bölməsi üzrə dir. müavini": "DEPUTY DIRECTOR FOR TURKISH DEPARTMENT",
                "İbtidai tərbiyə işləri müavini": "DEPUTY DIRECTOR FOR PRIMARY UPBRINGING",
                "Yuxarı sinif tərbiyə işləri müavini": "DEPUTY DIRECTOR FOR UPPER GRADES UPBRINGING",
                "İdman və Dərnəklər müavini": "DEPUTY DIRECTOR FOR SPORTS AND CLUBS",
                "Təhsil Nazirliyi üzrə koordinator": "COORDINATOR FOR THE MINISTRY OF EDUCATION",
                "Həkim": "DOCTOR",
                "Psixoloq": "PSYCHOLOGIST",
                "STEAM rəhbəri": "STEAM LEADER",
                "Evrika Təhsil Ekosistemi Üzrə Təsisçi": "FOUNDER OF EVRIKA EDUCATION ECOSYSTEM",
                "Evrika Beynəlxalq Elm və Texnologiya Liseyi ( Nərimanov filialı üzrə) Direktor": "DIRECTOR OF EVRIKA INT. LYCEUM OF SCIENCE AND TECHNOLOGY (NARIMANOV)",
                "Evrika Beynəlxalq Elm və Texnologiya Liseyi ( Gənclik filialı üzrə ) Direktor": "DIRECTOR OF EVRIKA INT. LYCEUM OF SCIENCE AND TECHNOLOGY (GANJLIK)",
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
                "Elməddin Musayev": "Elmaddin Musayev"
            },
            ru: {
                "Təmayül işləri üzrə direktor müavini": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО ПРОФИЛЬНЫМ ДЕЛАМ",
                "Maliyyə Direktoru": "ФИНАНСОВЫЙ ДИРЕКТОР",
                "İnsan Resursları üzrə departament rəhbəri": "РУКОВОДИТЕЛЬ ОТДЕЛА КАДРОВ",
                "Valideynlərlə İş üzrə direktor müavini": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО РАБОТЕ С РОДИТЕЛЯМИ",
                "İbtidai təhsil üzrə direktor müavini": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО НАЧАЛЬНОМУ ОБРАЗОВАНИЮ",
                "Ümumi Orta Təhsil üzrə direktor müavini": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО ОБЩЕМУ СРЕДНЕМУ ОБРАЗОВАНИЮ",
                "İngilis bölməsi rəhbəri": "ЗАВЕДУЮЩИЙ АНГЛИЙСКИМ ОТДЕЛЕНИЕМ",
                "Türk bölməsi üzrə dir. müavini": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО ТУРЕЦКОМУ ОТДЕЛЕНИЮ",
                "İbtidai tərbiyə işləri müavini": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО ВОСПИТАТЕЛЬНОЙ РАБОТЕ",
                "Yuxarı sinif tərbiyə işləri müavini": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО ВОСПИТАТЕЛЬНОЙ РАБОТЕ (СТАРШИЕ КЛАССЫ)",
                "İdman və Dərnəklər müavini": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО СПОРТУ И КРУЖКАМ",
                "Təhsil Nazirliyi üzrə koordinator": "КООРДИНАТОР ПО ЛИНИИ МИНИСТЕРСТВА ОБРАЗОВАНИЯ",
                "Həkim": "ВРАЧ",
                "Psixoloq": "ПСИХОЛОГ",
                "STEAM rəhbəri": "РУКОВОДИТЕЛЬ STEAM",
                "Evrika Təhsil Ekosistemi Üzrə Təsisçi": "УЧРЕДИТЕЛЬ ОБРАЗОВАТЕЛЬНОЙ ЭКОСИСТЕМЫ ЭВРИКА",
                "Evrika Beynəlxalq Elm və Texnologiya Liseyi ( Nərimanov filialı üzrə) Direktor": "ДИРЕКТОР МЕЖДУНАРОДНОГО ЛИЦЕЯ (НАРИМАНОВ)",
                "Evrika Beynəlxalq Elm və Texnologiya Liseyi ( Gənclik filialı üzrə ) Direktor": "ДИРЕКТОР МЕЖДУНАРОДНОГО ЛИЦЕЯ (ГЯНДЖЛИК)",
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
                "Elməddin Musayev": "Эльмаддин Мусаев"
            }
          };
          
          let dict = dicts[currentLang] || {};

          members.forEach(m => {
            const translatedName = dict[m.name] || window.translations?.[currentLang]?.[m.name] || m.name;
            const translatedRole = dict[m.role] || window.translations?.[currentLang]?.[m.role] || m.role;
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
    # Replace the renderMembers function
    html = re.sub(
        r'function renderMembers\(members\).*?\}\s*document\.addEventListener',
        replacement.strip() + "\n        document.addEventListener",
        html,
        flags=re.DOTALL
    )

    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/about.html', 'w', encoding='utf-8') as f:
        f.write(html)

    # We also need to add "about-concept-title" to main.js!
    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/src/main.js', 'r', encoding='utf-8') as f:
        js = f.read()
    
    js = js.replace('"nav-home": "Ana Səhifə",', '"nav-home": "Ana Səhifə",\n    "about-concept-title": "Evrika Konsepsiyası",')
    js = js.replace('"nav-home": "Home",', '"nav-home": "Home",\n    "about-concept-title": "Evrika Concept",')
    js = js.replace('"nav-home": "Главная",', '"nav-home": "Главная",\n    "about-concept-title": "Концепция Эврики",')

    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/src/main.js', 'w', encoding='utf-8') as f:
        f.write(js)

if __name__ == "__main__":
    fix_about_html_again()
    print("Fixed about.html final bugs!")
