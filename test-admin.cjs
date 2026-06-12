const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

const html = fs.readFileSync('admin.html', 'utf8');

const dom = new JSDOM(html, { runScripts: "dangerously", resources: "usable" });
dom.window.document.addEventListener("DOMContentLoaded", () => {
    console.log("DOM loaded");
    try {
        dom.window.switchTab('ugurlar');
        console.log("Switch tab ugurlar succeeded");
        console.log("ugurlarData:", dom.window.ugurlarData);
        
        // Mock a submit
        dom.window.document.getElementById('ug-name').value = "Test";
        dom.window.document.getElementById('ug-img').value = "Test";
        dom.window.document.getElementById('ug-form').dispatchEvent(new dom.window.Event('submit', { bubbles: true, cancelable: true }));
        console.log("Submit dispatched");
    } catch (e) {
        console.error("Error during execution:", e);
    }
});
setTimeout(() => { console.log("Done"); }, 3000);
