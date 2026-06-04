import re

def update_main_js_with_api_roles():
    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/src/main.js', 'r', encoding='utf-8') as f:
        js = f.read()

    en_names = {
        "Təmayül işləri üzrə direktor müavini": "DEPUTY DIRECTOR FOR SPECIALIZED AFFAIRS",
        "Maliyyə Direktoru": "FINANCE DIRECTOR",
        "İnsan Resursları üzrə departament rəhbəri": "HEAD OF HUMAN RESOURCES DEPARTMENT",
        "Valideynlərlə İş üzrə direktor müavini": "DEPUTY DIRECTOR FOR PARENT AFFAIRS",
        "İbtidai təhsil üzrə direktor müavini": "DEPUTY DIRECTOR FOR PRIMARY EDUCATION",
        "Ümumi Orta Təhsil üzrə direktor müavini": "DEPUTY DIRECTOR FOR GENERAL SECONDARY EDUCATION",
        "İngilis bölməsi rəhbəri": "HEAD OF ENGLISH DEPARTMENT",
        "Türk bölməsi üzrə dir. müavini": "DEPUTY DIRECTOR FOR TURKISH DEPARTMENT",
        "İbtidai tərbiyə işləri müavini": "DEPUTY DIRECTOR FOR PRIMARY UPBRINGING AFFAIRS",
        "Yuxarı sinif tərbiyə işləri müavini": "DEPUTY DIRECTOR FOR UPPER GRADES UPBRINGING AFFAIRS",
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
    }

    ru_names = {
        "Təmayül işləri üzrə direktor müavini": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО ПРОФИЛЬНЫМ ДЕЛАМ",
        "Maliyyə Direktoru": "ФИНАНСОВЫЙ ДИРЕКТОР",
        "İnsan Resursları üzrə departament rəhbəri": "РУКОВОДИТЕЛЬ ОТДЕЛА КАДРОВ",
        "Valideynlərlə İş üzrə direktor müavini": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО РАБОТЕ С РОДИТЕЛЯМИ",
        "İbtidai təhsil üzrə direktor müavini": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО НАЧАЛЬНОМУ ОБРАЗОВАНИЮ",
        "Ümumi Orta Təhsil üzrə direktor müavini": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО ОБЩЕМУ СРЕДНЕМУ ОБРАЗОВАНИЮ",
        "İngilis bölməsi rəhbəri": "ЗАВЕДУЮЩИЙ АНГЛИЙСКИМ ОТДЕЛЕНИЕМ",
        "Türk bölməsi üzrə dir. müavini": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО ТУРЕЦКОМУ ОТДЕЛЕНИЮ",
        "İbtidai tərbiyə işləri müavini": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО ВОСПИТАТЕЛЬНОЙ РАБОТЕ (НАЧАЛЬНАЯ ШКОЛА)",
        "Yuxarı sinif tərbiyə işləri müavini": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО ВОСПИТАТЕЛЬНОЙ РАБОТЕ (СТАРШИЕ КЛАССЫ)",
        "İdman və Dərnəklər müavini": "ЗАМЕСТИТЕЛЬ ДИРЕКТОРА ПО СПОРТУ И КРУЖКАМ",
        "Təhsil Nazirliyi üzrə koordinator": "КООРДИНАТОР ПО ЛИНИИ МИНИСТЕРСТВА ОБРАЗОВАНИЯ",
        "Həkim": "ВРАЧ",
        "Psixoloq": "ПСИХОЛОГ",
        "STEAM rəhbəri": "РУКОВОДИТЕЛЬ STEAM",
        "Evrika Təhsil Ekosistemi Üzrə Təsisçi": "УЧРЕДИТЕЛЬ ОБРАЗОВАТЕЛЬНОЙ ЭКОСИСТЕМЫ ЭВРИКА",
        "Evrika Beynəlxalq Elm və Texnologiya Liseyi ( Nərimanov filialı üzrə) Direktor": "ДИРЕКТОР МЕЖДУНАРОДНОГО ЛИЦЕЯ НАУКИ И ТЕХНОЛОГИЙ ЭВРИКА (ФИЛИАЛ НАРИМАНОВ)",
        "Evrika Beynəlxalq Elm və Texnologiya Liseyi ( Gənclik filialı üzrə ) Direktor": "ДИРЕКТОР МЕЖДУНАРОДНОГО ЛИЦЕЯ НАУКИ И ТЕХНОЛОГИЙ ЭВРИКА (ФИЛИАЛ ГЯНДЖЛИК)",
        
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

    en_str = ',\\n    '.join([f'"{k}": "{v}"' for k,v in en_names.items()])
    js = re.sub(r'("nav-home": "Home",)', r'\1\n    ' + en_str + ',', js)

    ru_str = ',\\n    '.join([f'"{k}": "{v}"' for k,v in ru_names.items()])
    js = re.sub(r'("nav-home": "Главная",)', r'\1\n    ' + ru_str + ',', js)

    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/src/main.js', 'w', encoding='utf-8') as f:
        f.write(js)

if __name__ == "__main__":
    update_main_js_with_api_roles()
    print("Exact API roles appended to main.js!")
