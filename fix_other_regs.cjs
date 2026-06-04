const fs = require('fs');

const labels = [
    ["Övladınızın adı", "reg-child-name", "Child's First Name", "Имя ребенка"],
    ["Övladınızın soyadı", "reg-child-surname", "Child's Last Name", "Фамилия ребенка"],
    ["Müraciət etmək istədiyi bölmə", "reg-child-sector", "Sector Applied For", "Сектор"],
    ["Övladınızın yaşı", "reg-child-age", "Child's Age", "Возраст ребенка"],
    ["Valideyinin əlaqə nömrəsi", "reg-parent-contact", "Parent's Contact Number", "Контактный номер родителя"],
    ["Adınız", "reg-your-name", "Your First Name", "Ваше имя"],
    ["Soyadınız", "reg-your-surname", "Your Last Name", "Ваша фамилия"],
    ["Müraciət etdiyiniz proqram", "reg-your-program", "Program Applied For", "Программа"],
    ["Hal-hazırda oxuduğunuz sinif (və ya məzun)", "reg-current-class", "Current Grade (or Graduate)", "Текущий класс (или выпускник)"],
    ["Əlaqə nömrəsi", "reg-contact-num", "Contact Number", "Контактный номер"],
    ["İştirak etmək istədiyiniz xidmət", "reg-your-service", "Service Applied For", "Желаемая услуга"],
    ["Yaşınız", "reg-your-age", "Your Age", "Ваш возраст"]
];

const placeholders = [
    ["Məs: 4 və ya 4.5", "reg-pl-age-4", "e.g., 4 or 4.5", "Например: 4 или 4.5"],
    ["Məs: Zümrüd", "reg-pl-zumrud", "e.g., Zumrud", "Например: Зюмруд"],
    ["Məs: Əliyeva", "reg-pl-aliyeva", "e.g., Aliyeva", "Например: Алиева"],
    ["Məs: 10-cu sinif / Məzun", "reg-pl-grade10", "e.g., 10th Grade / Graduate", "Например: 10 класс / Выпускник"],
    ["Məs: 25", "reg-pl-age-25", "e.g., 25", "Например: 25"]
];

const options = [
    ["Türk bölməsi", "reg-opt-tr", "Turkish Sector", "Турецкий сектор"],
    ["Proqram seçin", "reg-opt-sel-prog", "Select Program", "Выберите программу"],
    ["SAT", "reg-opt-sat", "SAT", "SAT"],
    ["IELTS", "reg-opt-ielts", "IELTS", "IELTS"],
    ["TOEFL", "reg-opt-toefl", "TOEFL", "TOEFL"],
    ["DİM (Abituriyent)", "reg-opt-dim", "SEC (Abituriyent)", "ГЕЦ (Абитуриент)"],
    ["Xarici Dil Hazırlıqları", "reg-opt-lang", "Foreign Language Courses", "Курсы иностранных языков"],
    ["Xidmət seçin", "reg-opt-sel-serv", "Select Service", "Выберите услугу"],
    ["Üzgüçülük", "reg-opt-swim", "Swimming", "Плавание"],
    ["Fitness", "reg-opt-fit", "Fitness", "Фитнес"],
    ["Pilates", "reg-opt-pilates", "Pilates", "Пилатес"],
    ["Yoga", "reg-opt-yoga", "Yoga", "Йога"],
    ["Ana və uşaqlar", "reg-opt-mom", "Mother & Kids", "Мама и дети"]
];

const files = [
  'register-montessori.html',
  'register-eduhome.html',
  'register-zumrud.html'
];

function escapeRegex(str) {
  return str.split('(').join('\\(').split(')').join('\\)');
}

files.forEach(file => {
  let content = fs.readFileSync(file, 'utf8');

  labels.forEach(l => {
    const rx = new RegExp(`<label>${escapeRegex(l[0])}</label>`, "g");
    content = content.replace(rx, `<label data-i18n="${l[1]}">${l[0]}</label>`);
  });

  placeholders.forEach(p => {
    const rx = new RegExp(`placeholder="${escapeRegex(p[0])}"`, "g");
    content = content.replace(rx, `placeholder="${p[0]}" data-i18n-placeholder="${p[1]}"`);
  });

  options.forEach(o => {
    const rx = new RegExp(`>\\s*${escapeRegex(o[0])}\\s*<\\/option>`, "g");
    content = content.replace(rx, ` data-i18n="${o[1]}">${o[0]}</option>`);
  });

  fs.writeFileSync(file, content);
});

let mainjs = fs.readFileSync('src/main.js', 'utf8');

let az = "", en = "", ru = "";
[...labels, ...placeholders, ...options].forEach(item => {
    if (!mainjs.includes('"' + item[1] + '"')) {
        az += `\n        "${item[1]}": "${item[0]}",`;
        en += `\n        "${item[1]}": "${item[2]}",`;
        ru += `\n        "${item[1]}": "${item[3]}",`;
    }
});

mainjs = mainjs.replace(/(az:\s*\{)/, "$1" + az);
mainjs = mainjs.replace(/(en:\s*\{)/, "$1" + en);
mainjs = mainjs.replace(/(ru:\s*\{)/, "$1" + ru);
fs.writeFileSync('src/main.js', mainjs);
console.log("Updated main.js with missing forms!");
