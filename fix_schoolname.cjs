const fs = require('fs');

// School name texts per file and their translation keys
const fileSchoolNames = {
  'register-lisey1.html': {
    az_name: 'EVRİKA Beynəlxalq Elm və Texnologiya Liseyi (Nərimanov filialı)',
    key: 'reg-school-name',
    en: 'EVRIKA International Science and Technology Lyceum (Narimanov Branch)',
    ru: 'ЭВРИКА Международный Лицей Науки и Технологий (Нариманов филиал)'
  },
  'register-lisey2.html': {
    az_name: 'EVRİKA Beynəlxalq Elm və Texnologiya Liseyi (Gənclik filialı)',
    key: 'reg-school-name',
    en: 'EVRIKA International Science and Technology Lyceum (Ganjlik Branch)',
    ru: 'ЭВРИКА Международный Лицей Науки и Технологий (Гянджлик филиал)'
  },
  'register-montessori.html': {
    az_name: 'Evrika Montessori Kids Academy',
    key: 'reg-school-name',
    en: 'Evrika Montessori Kids Academy',
    ru: 'Эврика Монтессори Академия'
  },
  'register-eduhome.html': {
    az_name: 'Eduhome Hazırlıq Mərkəzi',
    key: 'reg-school-name',
    en: 'Eduhome Preparation Center',
    ru: 'Eduhome Учебный Центр'
  },
  'register-zumrud.html': {
    az_name: 'Zümrüd<br>Women<br>Club',
    key: 'reg-school-name',
    en: 'Zumrud<br>Women<br>Club',
    ru: 'Зюмруд<br>Женский<br>Клуб'
  }
};

const files = Object.keys(fileSchoolNames);

// Add data-i18n to school name and button in each file
files.forEach(file => {
  const info = fileSchoolNames[file];
  let content = fs.readFileSync(file, 'utf8');
  
  // Replace school name with tagged version
  const searchName = info.az_name;
  // Wrap the text with a span that has data-i18n
  if (!content.includes(`data-i18n="${info.key}"`)) {
    content = content.replace(
      new RegExp(`(>\\s*)${searchName.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}(\\s*<)`,'g'),
      `$1<span data-i18n="${info.key}">${searchName}</span>$2`
    );
  }

  // Fix "MÜRACİƏTİ TAMAMLA" button (for montessori/eduhome/zumrud)
  content = content.replace(
    /\n\s*MÜRACİƏTİ TAMAMLA\s*(<i)/g,
    `\n            <span data-i18n="reg-submit">MÜRACİƏTİ TAMAMLA</span> $1`
  );

  fs.writeFileSync(file, content);
});

// Now update main.js with translations per file key
let mainjs = fs.readFileSync('src/main.js', 'utf8');

// The school name is per-page, so we use the same key but different values won't work for a shared key.
// Instead, let's check which unique names exist across all pages.
// Actually, per-page names differ, so we need unique keys per page.
// Let's redo: use unique keys per page.
const uniqueKeys = {
  'reg-school-lisey1': {
    az: 'EVRİKA Beynəlxalq Elm və Texnologiya Liseyi (Nərimanov filialı)',
    en: 'EVRIKA International Science and Technology Lyceum (Narimanov Branch)',
    ru: 'ЭВРИКА Международный Лицей Науки и Технологий (Нариманов филиал)'
  },
  'reg-school-lisey2': {
    az: 'EVRİKA Beynəlxalq Elm və Texnologiya Liseyi (Gənclik filialı)',
    en: 'EVRIKA International Science and Technology Lyceum (Ganjlik Branch)',
    ru: 'ЭВРИКА Международный Лицей Науки и Технологий (Гянджлик филиал)'
  },
  'reg-school-montessori': {
    az: 'Evrika Montessori Kids Academy',
    en: 'Evrika Montessori Kids Academy',
    ru: 'Эврика Монтессори Академия'
  },
  'reg-school-eduhome': {
    az: 'Eduhome Hazırlıq Mərkəzi',
    en: 'Eduhome Preparation Center',
    ru: 'Eduhome Учебный Центр'
  },
  'reg-school-zumrud': {
    az: 'Zümrüd<br>Women<br>Club',
    en: 'Zumrud<br>Women<br>Club',
    ru: 'Зюмруд<br>Женский<br>Клуб'
  },
  'reg-submit': {
    az: 'MÜRACİƏTİ TAMAMLA',
    en: 'SUBMIT APPLICATION',
    ru: 'ПОДАТЬ ЗАЯВКУ'
  }
};

// Fix the HTML files to use the correct unique keys
const keyMap = {
  'register-lisey1.html': 'reg-school-lisey1',
  'register-lisey2.html': 'reg-school-lisey2',
  'register-montessori.html': 'reg-school-montessori',
  'register-eduhome.html': 'reg-school-eduhome',
  'register-zumrud.html': 'reg-school-zumrud'
};

files.forEach(file => {
  let content = fs.readFileSync(file, 'utf8');
  const correctKey = keyMap[file];
  // Replace the generic key with the correct per-page key
  content = content.replace(/data-i18n="reg-school-name"/g, `data-i18n="${correctKey}"`);
  fs.writeFileSync(file, content);
});

// Inject translations
let azAdd = '', enAdd = '', ruAdd = '';
Object.entries(uniqueKeys).forEach(([key, vals]) => {
  if (!mainjs.includes(`"${key}"`)) {
    azAdd += `\n        "${key}": "${vals.az}",`;
    enAdd += `\n        "${key}": "${vals.en}",`;
    ruAdd += `\n        "${key}": "${vals.ru}",`;
  }
});

mainjs = mainjs.replace(/(az:\s*\{)/, "$1" + azAdd);
mainjs = mainjs.replace(/(en:\s*\{)/, "$1" + enAdd);
mainjs = mainjs.replace(/(ru:\s*\{)/, "$1" + ruAdd);
fs.writeFileSync('src/main.js', mainjs);
console.log("Done! School names and submit button tagged.");
