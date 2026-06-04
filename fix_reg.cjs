const fs = require('fs');

const files = [
  'register-lisey1.html',
  'register-lisey2.html',
  'register-montessori.html',
  'register-eduhome.html',
  'register-zumrud.html'
];

const desktopLangSwitcher = `
        <div class="lang-dropdown-wrapper desktop-lang-wrapper" style="position: relative; display: inline-flex; margin-right: 12px; height: 100%;">
            <button class="lang-toggle-btn" onclick="let menu = this.nextElementSibling; menu.style.display = menu.style.display === 'flex' ? 'none' : 'flex';" onblur="let menu = this.nextElementSibling; setTimeout(() => menu.style.display = 'none', 200);" style="background: #1e3a8a; border: none; color: white; padding: 12px 22px; border-radius: 100px; font-weight: 800; font-size: 0.95rem; cursor: pointer; transition: 0.3s; display: inline-flex; align-items: center; justify-content: center; min-width: 80px;" onmouseover="this.style.background='#284baf'" onmouseout="this.style.background='#1e3a8a'">
               <span class="lang-text">AZ</span> <i class="fas fa-chevron-down" style="margin-left: 10px; font-size: 0.8rem; opacity: 0.9;"></i>
            </button>
            <div class="lang-menu" style="position: absolute; top: 115%; left: 50%; transform: translateX(-50%); background: white; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); display: none; flex-direction: column; overflow: hidden; min-width: 80px; z-index: 100;">
                <a href="#" onmousedown="event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='AZ'); this.parentElement.style.display='none'; if(window.updateContent) window.updateContent('az');" style="padding: 10px 20px; color: #333; text-decoration: none; font-weight: 700; font-size: 0.9rem; text-align: center; border-bottom: 1px solid #eee;" onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background='white'">AZ</a>
                <a href="#" onmousedown="event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='EN'); this.parentElement.style.display='none'; if(window.updateContent) window.updateContent('en');" style="padding: 10px 20px; color: #333; text-decoration: none; font-weight: 700; font-size: 0.9rem; text-align: center; border-bottom: 1px solid #eee;" onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background='white'">EN</a>
                <a href="#" onmousedown="event.preventDefault(); document.querySelectorAll('.lang-text').forEach(e=>e.innerText='RU'); this.parentElement.style.display='none'; if(window.updateContent) window.updateContent('ru');" style="padding: 10px 20px; color: #333; text-decoration: none; font-weight: 700; font-size: 0.9rem; text-align: center;" onmouseover="this.style.background='#f5f5f5'" onmouseout="this.style.background='white'">RU</a>
            </div>
        </div>
`;

files.forEach(file => {
  let content = fs.readFileSync(file, 'utf8');

  // Fix mobile lang switcher
  content = content.replace(/this\.parentElement\.style\.display='none';"/g, "this.parentElement.style.display='none'; if(window.updateContent) window.updateContent(this.innerText.toLowerCase());\"");

  // Inject desktop lang switcher
  content = content.replace(/<div class="nav-actions">\s*<\/div>/, `<div class="nav-actions">\n${desktopLangSwitcher}      </div>`);

  // Add data-i18n attributes
  content = content.replace(/<label>Şagirdin adı<\/label>/g, '<label data-i18n="reg-student-name">Şagirdin adı</label>');
  content = content.replace(/<label>Şagirdin soyadı<\/label>/g, '<label data-i18n="reg-student-surname">Şagirdin soyadı</label>');
  content = content.replace(/<label>Bölmə<\/label>/g, '<label data-i18n="reg-sector">Bölmə</label>');
  content = content.replace(/<label>Sinif<\/label>/g, '<label data-i18n="reg-class">Sinif</label>');
  content = content.replace(/<label>Əvvəl oxuduğu məktəb \(və ya bağça\)<\/label>/g, '<label data-i18n="reg-prev-school">Əvvəl oxuduğu məktəb (və ya bağça)</label>');
  content = content.replace(/<label>Valideynin əlaqə nömrəsi<\/label>/g, '<label data-i18n="reg-parent-phone">Valideynin əlaqə nömrəsi</label>');
  content = content.replace(/<label>Mail ünvanı<\/label>/g, '<label data-i18n="reg-email">Mail ünvanı</label>');
  
  content = content.replace(/<h2>Müraciət Forması<\/h2>/g, '<h2 data-i18n="reg-form-title">Müraciət Forması</h2>');
  content = content.replace(/<h1 class="titan-header"([^>]*)>\s*Qeydiyyat\s*<\/h1>/g, '<h1 class="titan-header"$1 data-i18n="reg-title">Qeydiyyat</h1>');
  content = content.replace(/Məlumatlarınızı daxil edərək onlayn müraciətinizi tamamlayın\./g, '<span data-i18n="reg-desc">Məlumatlarınızı daxil edərək onlayn müraciətinizi tamamlayın.</span>');

  content = content.replace(/DAVAM ET <i/g, '<span data-i18n="reg-continue">DAVAM ET</span> <i');
  
  // also handle some placeholders in the js part, or select options
  
  fs.writeFileSync(file, content);
});

console.log("Updated HTML files.");

let mainjs = fs.readFileSync('src/main.js', 'utf8');
if (!mainjs.includes('"reg-student-name"')) {
    const translationAdditions = `
        "reg-student-name": "Şagirdin adı",
        "reg-student-surname": "Şagirdin soyadı",
        "reg-sector": "Bölmə",
        "reg-class": "Sinif",
        "reg-prev-school": "Əvvəl oxuduğu məktəb (və ya bağça)",
        "reg-parent-phone": "Valideynin əlaqə nömrəsi",
        "reg-email": "Mail ünvanı",
        "reg-form-title": "Müraciət Forması",
        "reg-title": "Qeydiyyat",
        "reg-desc": "Məlumatlarınızı daxil edərək onlayn müraciətinizi tamamlayın.",
        "reg-continue": "DAVAM ET",
    `;
    const translationAdditionsEn = `
        "reg-student-name": "Student's First Name",
        "reg-student-surname": "Student's Last Name",
        "reg-sector": "Sector",
        "reg-class": "Grade/Class",
        "reg-prev-school": "Previous School (or Kindergarten)",
        "reg-parent-phone": "Parent's Contact Number",
        "reg-email": "Email Address",
        "reg-form-title": "Application Form",
        "reg-title": "Registration",
        "reg-desc": "Fill in your details to complete your online application.",
        "reg-continue": "CONTINUE",
    `;
    const translationAdditionsRu = `
        "reg-student-name": "Имя ученика",
        "reg-student-surname": "Фамилия ученика",
        "reg-sector": "Сектор",
        "reg-class": "Класс",
        "reg-prev-school": "Предыдущая школа (или детский сад)",
        "reg-parent-phone": "Контактный номер родителя",
        "reg-email": "Электронная почта",
        "reg-form-title": "Форма Заявки",
        "reg-title": "Регистрация",
        "reg-desc": "Введите свои данные, чтобы завершить онлайн-заявку.",
        "reg-continue": "ПРОДОЛЖИТЬ",
    `;
    
    // Naively inject them into translations object
    mainjs = mainjs.replace(/(az:\s*\{)/, "$1" + translationAdditions);
    mainjs = mainjs.replace(/(en:\s*\{)/, "$1" + translationAdditionsEn);
    mainjs = mainjs.replace(/(ru:\s*\{)/, "$1" + translationAdditionsRu);
    fs.writeFileSync('src/main.js', mainjs);
    console.log("Updated main.js");
}
