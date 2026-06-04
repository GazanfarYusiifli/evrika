const fs = require('fs');

const index = fs.readFileSync('index.html', 'utf8');

const navStart = index.indexOf('<nav class="nav-links">');
const navEnd = index.indexOf('</nav>', navStart) + 6;
const desktopNav = index.substring(navStart, navEnd);

const mobNavStart = index.indexOf('<div class="mobile-nav-links">');
const mobNavEnd = index.indexOf('</div>\n  </div>\n\n  <!-- Video Popup Modal -->', mobNavStart);
// Wait, the end of mobile nav is a bit tricky. Let's find the closing tag.
let mobNavStr = index.substring(mobNavStart, mobNavStart + 10000);
// Instead of indexof, we can just regex replace the specific translations in the files themselves, it's safer.

