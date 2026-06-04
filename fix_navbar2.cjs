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

  // Desktop Navbar translations
  content = content.replace(/<a href="index\.html">Ana Səhifə<\/a>/g, '<a href="index.html" data-i18n="nav-home">Ana Səhifə</a>');
  content = content.replace(/<a href="about\.html">Haqqımızda<\/a>/g, '<a href="about.html" data-i18n="nav-about">Haqqımızda</a>');
  content = content.replace(/<a href="schools\.html">Akademik İstiqamətlər<\/a>/g, '<a href="schools.html" data-i18n="nav-academic">Akademik İstiqamətlər</a>');
  content = content.replace(/<a href="vacancy\.html">Vakansiya &amp; Təcrübə<\/a>/g, '<a href="vacancy.html" data-i18n="nav-vacancy">Vakansiya &amp; Təcrübə</a>');
  content = content.replace(/<a href="jurnal\.html">Evrika Jurnalı<\/a>/g, '<a href="jurnal.html" data-i18n="nav-journal">Evrika Jurnalı</a>');
  content = content.replace(/<a href="contact\.html">Əlaqə<\/a>/g, '<a href="contact.html" data-i18n="nav-contact">Əlaqə</a>');

  // Desktop Dropdown Titles
  content = content.replace(/<span class="dropdown-item-title">Haqqımızda<\/span>/g, '<span class="dropdown-item-title" data-i18n="nav-about">Haqqımızda</span>');
  content = content.replace(/<span class="dropdown-item-desc">Bizim hekayəmiz<\/span>/g, '<span class="dropdown-item-desc" data-i18n="nav-about-desc">Bizim hekayəmiz</span>');

  content = content.replace(/<span class="dropdown-item-title">Məzunlar<\/span>/g, '<span class="dropdown-item-title" data-i18n="nav-alumni">Məzunlar</span>');
  content = content.replace(/<span class="dropdown-item-desc">Fəxrlərimiz<\/span>/g, '<span class="dropdown-item-desc" data-i18n="nav-alumni-desc">Fəxrlərimiz</span>');

  content = content.replace(/<span class="dropdown-item-title">Uğurlar<\/span>/g, '<span class="dropdown-item-title" data-i18n="nav-achievements">Uğurlar</span>');
  content = content.replace(/<span class="dropdown-item-desc">Nailiyyətlərimiz<\/span>/g, '<span class="dropdown-item-desc" data-i18n="nav-achievements-desc">Nailiyyətlərimiz</span>');

  content = content.replace(/<span class="dropdown-item-title">Xəbərlər<\/span>/g, '<span class="dropdown-item-title" data-i18n="nav-news">Xəbərlər</span>');
  content = content.replace(/<span class="dropdown-item-desc">Ən son xəbərlər<\/span>/g, '<span class="dropdown-item-desc" data-i18n="nav-news-desc">Ən son xəbərlər</span>');

  content = content.replace(/<span class="dropdown-item-title">Evrika BETL Nərimanov<\/span>/g, '<span class="dropdown-item-title" data-i18n="nav-lisey1">Evrika BETL Nərimanov</span>');
  content = content.replace(/<span class="dropdown-item-desc">Elm və Texnologiya Mərkəzi<\/span>/g, '<span class="dropdown-item-desc" data-i18n="nav-lisey1-desc">Elm və Texnologiya Mərkəzi</span>');

  content = content.replace(/<span class="dropdown-item-title">Evrika BETL Gənclik<\/span>/g, '<span class="dropdown-item-title" data-i18n="nav-lisey2">Evrika BETL Gənclik</span>');
  content = content.replace(/<span class="dropdown-item-desc">Beynəlxalq Təhsil Müəssisəsi<\/span>/g, '<span class="dropdown-item-desc" data-i18n="nav-lisey2-desc">Beynəlxalq Təhsil Müəssisəsi</span>');
  content = content.replace(/<span class="dropdown-item-desc">Beynəlxalq Təhsil Kampusu<\/span>/g, '<span class="dropdown-item-desc" data-i18n="nav-lisey2-desc">Beynəlxalq Təhsil Kampusu</span>');

  content = content.replace(/<span class="dropdown-item-title">Montessori Kids Academy<\/span>/g, '<span class="dropdown-item-title" data-i18n="nav-montessori">Montessori Kids Academy</span>');
  content = content.replace(/<span class="dropdown-item-desc">Bağça və Erkən İnkişaf<\/span>/g, '<span class="dropdown-item-desc" data-i18n="nav-montessori-desc">Bağça və Erkən İnkişaf</span>');

  content = content.replace(/<span class="dropdown-item-title">Eduhome Hazırlıq<\/span>/g, '<span class="dropdown-item-title" data-i18n="nav-eduhome">Eduhome Hazırlıq</span>');
  content = content.replace(/<span class="dropdown-item-desc">Xaricdə Təhsil və Hazırlıq<\/span>/g, '<span class="dropdown-item-desc" data-i18n="nav-eduhome-desc">Xaricdə Təhsil və Hazırlıq</span>');

  content = content.replace(/<span class="dropdown-item-title">Zümrüd İdman Mərkəzi<\/span>/g, '<span class="dropdown-item-title" data-i18n="nav-zumrud">Zümrüd İdman Mərkəzi</span>');
  content = content.replace(/<span class="dropdown-item-desc">Sağlam Həyat və Fəaliyyət<\/span>/g, '<span class="dropdown-item-desc" data-i18n="nav-zumrud-desc">Sağlam Həyat və Fəaliyyət</span>');

  content = content.replace(/<span class="dropdown-item-title">Karyera və Vakansiyalar<\/span>/g, '<span class="dropdown-item-title" data-i18n="nav-vac-title">Karyera və Vakansiyalar</span>');
  content = content.replace(/<span class="dropdown-item-desc">Açıq iş elanları<\/span>/g, '<span class="dropdown-item-desc" data-i18n="nav-vac-desc">Açıq iş elanları</span>');

  content = content.replace(/<span class="dropdown-item-title">Pedaqoji Təcrübə və İnkişaf Mərkəzi<\/span>/g, '<span class="dropdown-item-title" data-i18n="nav-ptim-title">Pedaqoji Təcrübə və İnkişaf Mərkəzi</span>');
  content = content.replace(/<span class="dropdown-item-desc">PTİM<\/span>/g, '<span class="dropdown-item-desc" data-i18n="nav-ptim-desc">PTİM</span>');

  // Mobile Accordion and Nav Links
  // Some of these use the same class names, so we just replace the innerHTML spans directly.
  content = content.replace(/<span class="acc-title">Haqqımızda<\/span>/g, '<span class="acc-title" data-i18n="nav-about">Haqqımızda</span>');
  content = content.replace(/<span class="acc-desc">Bizim hekayəmiz<\/span>/g, '<span class="acc-desc" data-i18n="nav-about-desc">Bizim hekayəmiz</span>');

  content = content.replace(/<span class="acc-title">Məzunlar<\/span>/g, '<span class="acc-title" data-i18n="nav-alumni">Məzunlar</span>');
  content = content.replace(/<span class="acc-desc">Fəxrlərimiz<\/span>/g, '<span class="acc-desc" data-i18n="nav-alumni-desc">Fəxrlərimiz</span>');

  content = content.replace(/<span class="acc-title">Uğurlar<\/span>/g, '<span class="acc-title" data-i18n="nav-achievements">Uğurlar</span>');
  content = content.replace(/<span class="acc-desc">Nailiyyətlərimiz<\/span>/g, '<span class="acc-desc" data-i18n="nav-achievements-desc">Nailiyyətlərimiz</span>');

  content = content.replace(/<span class="acc-title">Xəbərlər<\/span>/g, '<span class="acc-title" data-i18n="nav-news">Xəbərlər</span>');
  content = content.replace(/<span class="acc-desc">Ən son xəbərlər<\/span>/g, '<span class="acc-desc" data-i18n="nav-news-desc">Ən son xəbərlər</span>');

  content = content.replace(/<span class="acc-title">Evrika BETL Nərimanov<\/span>/g, '<span class="acc-title" data-i18n="nav-lisey1">Evrika BETL Nərimanov</span>');
  content = content.replace(/<span class="acc-desc">Elm və Texnologiya Mərkəzi<\/span>/g, '<span class="acc-desc" data-i18n="nav-lisey1-desc">Elm və Texnologiya Mərkəzi</span>');

  content = content.replace(/<span class="acc-title">Evrika BETL Gənclik<\/span>/g, '<span class="acc-title" data-i18n="nav-lisey2">Evrika BETL Gənclik</span>');
  content = content.replace(/<span class="acc-desc">Beynəlxalq Təhsil Kampusu<\/span>/g, '<span class="acc-desc" data-i18n="nav-lisey2-desc">Beynəlxalq Təhsil Kampusu</span>');

  content = content.replace(/<span class="acc-title">Montessori Kids Academy<\/span>/g, '<span class="acc-title" data-i18n="nav-montessori">Montessori Kids Academy</span>');
  content = content.replace(/<span class="acc-desc">Bağça və Erkən İnkişaf<\/span>/g, '<span class="acc-desc" data-i18n="nav-montessori-desc">Bağça və Erkən İnkişaf</span>');

  content = content.replace(/<span class="acc-title">Eduhome Hazırlıq<\/span>/g, '<span class="acc-title" data-i18n="nav-eduhome">Eduhome Hazırlıq</span>');
  content = content.replace(/<span class="acc-desc">Xaricdə Təhsil və Hazırlıq<\/span>/g, '<span class="acc-desc" data-i18n="nav-eduhome-desc">Xaricdə Təhsil və Hazırlıq</span>');

  content = content.replace(/<span class="acc-title">Zümrüd İdman Mərkəzi<\/span>/g, '<span class="acc-title" data-i18n="nav-zumrud">Zümrüd İdman Mərkəzi</span>');
  content = content.replace(/<span class="acc-desc">Sağlam Həyat və Fəaliyyət<\/span>/g, '<span class="acc-desc" data-i18n="nav-zumrud-desc">Sağlam Həyat və Fəaliyyət</span>');

  content = content.replace(/<span class="acc-title">Karyera və Vakansiyalar<\/span>/g, '<span class="acc-title" data-i18n="nav-vac-title">Karyera və Vakansiyalar</span>');
  content = content.replace(/<span class="acc-desc">Açıq iş elanları<\/span>/g, '<span class="acc-desc" data-i18n="nav-vac-desc">Açıq iş elanları</span>');

  content = content.replace(/<span class="acc-title">Pedaqoji Təcrübə və İnkişaf Mərkəzi<\/span>/g, '<span class="acc-title" data-i18n="nav-ptim-title">Pedaqoji Təcrübə və İnkişaf Mərkəzi</span>');
  content = content.replace(/<span class="acc-desc">PTİM<\/span>/g, '<span class="acc-desc" data-i18n="nav-ptim-desc">PTİM</span>');

  fs.writeFileSync(file, content);
});

console.log("Updated navbars in register HTMLs.");
