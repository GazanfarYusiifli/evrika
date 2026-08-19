const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

const html = fs.readFileSync('admin.html', 'utf8');
const dom = new JSDOM(html, { runScripts: "dangerously", pretendToBeVisual: true, url: "http://localhost" });

dom.window.onerror = function(msg, source, lineno, colno, error) {
    console.error("PAGE ERROR:", msg, "Line:", lineno);
};

// Wait a bit to let async scripts execute
setTimeout(() => {
    console.log("Done testing HTML execution.");
}, 2000);
