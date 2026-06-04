const fs = require('fs');

const files = [
  'register-lisey1.html',
  'register-lisey2.html',
  'register-montessori.html',
  'register-eduhome.html',
  'register-zumrud.html'
];

files.forEach(file => {
  let content = fs.readFileSync(file, 'utf8');

  // Placeholders
  content = content.replace(/placeholder="Məs: Əli"/g, 'placeholder="Məs: Əli" data-i18n-placeholder="reg-pl-ali"');
  content = content.replace(/placeholder="Məs: Əliyev"/g, 'placeholder="Məs: Əliyev" data-i18n-placeholder="reg-pl-aliyev"');
  content = content.replace(/placeholder="Məs: 20 nömrəli məktəb"/g, 'placeholder="Məs: 20 nömrəli məktəb" data-i18n-placeholder="reg-pl-school"');
  content = content.replace(/placeholder="Məs: 551234567"/g, 'placeholder="Məs: 551234567" data-i18n-placeholder="reg-pl-phone"');
  content = content.replace(/placeholder="Məs: info@evrika\.az"/g, 'placeholder="Məs: info@evrika.az" data-i18n-placeholder="reg-pl-email"');

  // Sectors
  content = content.replace(/>Bölmə seçin<\/option>/g, ' data-i18n="reg-opt-select-sector">Bölmə seçin</option>');
  content = content.replace(/>Azərbaycan bölməsi<\/option>/g, ' data-i18n="reg-opt-az">Azərbaycan bölməsi</option>');
  content = content.replace(/>Rus bölməsi<\/option>/g, ' data-i18n="reg-opt-ru">Rus bölməsi</option>');
  content = content.replace(/>İngilis bölməsi<\/option>/g, ' data-i18n="reg-opt-en">İngilis bölməsi</option>');

  // Classes
  content = content.replace(/>Məktəbəqədər<\/option>/g, ' data-i18n="reg-opt-class-0">Məktəbəqədər</option>');
  content = content.replace(/>1-ci sinif<\/option>/g, ' data-i18n="reg-opt-class-1">1-ci sinif</option>');
  content = content.replace(/>2-ci sinif<\/option>/g, ' data-i18n="reg-opt-class-2">2-ci sinif</option>');
  content = content.replace(/>3-cü sinif<\/option>/g, ' data-i18n="reg-opt-class-3">3-cü sinif</option>');
  content = content.replace(/>4-cü sinif<\/option>/g, ' data-i18n="reg-opt-class-4">4-cü sinif</option>');
  content = content.replace(/>5-ci sinif<\/option>/g, ' data-i18n="reg-opt-class-5">5-ci sinif</option>');
  content = content.replace(/>6-cı sinif<\/option>/g, ' data-i18n="reg-opt-class-6">6-cı sinif</option>');
  content = content.replace(/>7-ci sinif<\/option>/g, ' data-i18n="reg-opt-class-7">7-ci sinif</option>');
  content = content.replace(/>8-ci sinif<\/option>/g, ' data-i18n="reg-opt-class-8">8-ci sinif</option>');
  content = content.replace(/>9-cu sinif<\/option>/g, ' data-i18n="reg-opt-class-9">9-cu sinif</option>');
  content = content.replace(/>10-cu sinif<\/option>/g, ' data-i18n="reg-opt-class-10">10-cu sinif</option>');
  content = content.replace(/>11-ci sinif<\/option>/g, ' data-i18n="reg-opt-class-11">11-ci sinif</option>');

  fs.writeFileSync(file, content);
});

let mainjs = fs.readFileSync('src/main.js', 'utf8');

if (!mainjs.includes('"reg-pl-ali"')) {
    const az = `
        "reg-pl-ali": "Məs: Əli",
        "reg-pl-aliyev": "Məs: Əliyev",
        "reg-pl-school": "Məs: 20 nömrəli məktəb",
        "reg-pl-phone": "Məs: 551234567",
        "reg-pl-email": "Məs: info@evrika.az",
        "reg-opt-select-sector": "Bölmə seçin",
        "reg-opt-az": "Azərbaycan bölməsi",
        "reg-opt-ru": "Rus bölməsi",
        "reg-opt-en": "İngilis bölməsi",
        "reg-opt-class-0": "Məktəbəqədər",
        "reg-opt-class-1": "1-ci sinif",
        "reg-opt-class-2": "2-ci sinif",
        "reg-opt-class-3": "3-cü sinif",
        "reg-opt-class-4": "4-cü sinif",
        "reg-opt-class-5": "5-ci sinif",
        "reg-opt-class-6": "6-cı sinif",
        "reg-opt-class-7": "7-ci sinif",
        "reg-opt-class-8": "8-ci sinif",
        "reg-opt-class-9": "9-cu sinif",
        "reg-opt-class-10": "10-cu sinif",
        "reg-opt-class-11": "11-ci sinif",
`;
    const en = `
        "reg-pl-ali": "e.g., Ali",
        "reg-pl-aliyev": "e.g., Aliyev",
        "reg-pl-school": "e.g., School No. 20",
        "reg-pl-phone": "e.g., 551234567",
        "reg-pl-email": "e.g., info@evrika.az",
        "reg-opt-select-sector": "Select Sector",
        "reg-opt-az": "Azerbaijani Sector",
        "reg-opt-ru": "Russian Sector",
        "reg-opt-en": "English Sector",
        "reg-opt-class-0": "Preschool",
        "reg-opt-class-1": "1st Grade",
        "reg-opt-class-2": "2nd Grade",
        "reg-opt-class-3": "3rd Grade",
        "reg-opt-class-4": "4th Grade",
        "reg-opt-class-5": "5th Grade",
        "reg-opt-class-6": "6th Grade",
        "reg-opt-class-7": "7th Grade",
        "reg-opt-class-8": "8th Grade",
        "reg-opt-class-9": "9th Grade",
        "reg-opt-class-10": "10th Grade",
        "reg-opt-class-11": "11th Grade",
`;
    const ru = `
        "reg-pl-ali": "Например: Али",
        "reg-pl-aliyev": "Например: Алиев",
        "reg-pl-school": "Например: Школа №20",
        "reg-pl-phone": "Например: 551234567",
        "reg-pl-email": "Например: info@evrika.az",
        "reg-opt-select-sector": "Выберите Сектор",
        "reg-opt-az": "Азербайджанский сектор",
        "reg-opt-ru": "Русский сектор",
        "reg-opt-en": "Английский сектор",
        "reg-opt-class-0": "Дошкольный",
        "reg-opt-class-1": "1 класс",
        "reg-opt-class-2": "2 класс",
        "reg-opt-class-3": "3 класс",
        "reg-opt-class-4": "4 класс",
        "reg-opt-class-5": "5 класс",
        "reg-opt-class-6": "6 класс",
        "reg-opt-class-7": "7 класс",
        "reg-opt-class-8": "8 класс",
        "reg-opt-class-9": "9 класс",
        "reg-opt-class-10": "10 класс",
        "reg-opt-class-11": "11 класс",
`;
    
    mainjs = mainjs.replace(/(az:\s*\{)/, "$1" + az);
    mainjs = mainjs.replace(/(en:\s*\{)/, "$1" + en);
    mainjs = mainjs.replace(/(ru:\s*\{)/, "$1" + ru);
    fs.writeFileSync('src/main.js', mainjs);
    console.log("Updated main.js");
}

