const fs = require('fs');
const html = fs.readFileSync('admin.html', 'utf8');
const filterLogic = html.match(/rawData = fetchedData\.filter\([^]+?\}\);/);
console.log(filterLogic ? filterLogic[0] : "Not found");
