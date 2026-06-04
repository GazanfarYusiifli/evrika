import re

def add_placeholders():
    paths = [
        '/Users/gazanfaryusifli/Downloads/EvrikaProje/contact.html',
        '/Users/gazanfaryusifli/Downloads/EvrikaProje/live_vercel_code/contact.html'
    ]
    for path in paths:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                html = f.read()

            html = html.replace('placeholder="Adınız"', 'placeholder="Adınız" data-i18n-placeholder="form-name-ph"')
            html = html.replace('placeholder="+994"', 'placeholder="+994" data-i18n-placeholder="form-phone-ph"')
            html = html.replace('placeholder="example@mail.com"', 'placeholder="example@mail.com" data-i18n-placeholder="form-email-ph"')
            html = html.replace('placeholder="Müraciətiniz və ya sualınız..."', 'placeholder="Müraciətiniz və ya sualınız..." data-i18n-placeholder="form-message-ph"')

            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)
        except FileNotFoundError:
            pass

    main_js_path = '/Users/gazanfaryusifli/Downloads/EvrikaProje/src/main.js'
    with open(main_js_path, 'r', encoding='utf-8') as f:
        js = f.read()

    new_az = r""",
    "form-name-ph": "Adınız",
    "form-phone-ph": "+994",
    "form-email-ph": "example@mail.com",
    "form-message-ph": "Müraciətiniz və ya sualınız..."
"""
    new_en = r""",
    "form-name-ph": "Your Name",
    "form-phone-ph": "+123",
    "form-email-ph": "example@mail.com",
    "form-message-ph": "Your request or question..."
"""
    new_ru = r""",
    "form-name-ph": "Ваше имя",
    "form-phone-ph": "+7",
    "form-email-ph": "example@mail.com",
    "form-message-ph": "Ваш запрос или вопрос..."
"""

    js = re.sub(r'("form-message-label": "Mesaj"\s*,\s*"form-submit-btn": "Müraciəti Göndər.*?</i>"\s*)', r'\1' + new_az, js, count=1)
    js = re.sub(r'("form-message-label": "Message"\s*,\s*"form-submit-btn": "Submit Request.*?</i>"\s*)', r'\1' + new_en, js, count=1)
    js = re.sub(r'("form-message-label": "Сообщение"\s*,\s*"form-submit-btn": "Отправить запрос.*?</i>"\s*)', r'\1' + new_ru, js, count=1)

    with open(main_js_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print("Updated placeholders in contact.html and main.js")

if __name__ == "__main__":
    add_placeholders()
