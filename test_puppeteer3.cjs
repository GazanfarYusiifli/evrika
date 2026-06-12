const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('file:///Users/gazanfaryusifli/Downloads/EvrikaProje/admin.html');
  await page.evaluate(() => {
    document.getElementById('login-icon').className = 'fas fa-user-tie';
    unlockModule('hr');
  });
  await new Promise(r => setTimeout(r, 500));
  await page.type('#hub-pass-input', 'hr123');
  await page.keyboard.press('Enter');
  await new Promise(r => setTimeout(r, 1000));
  
  const visibilityInfo = await page.evaluate(() => {
     let el = document.getElementById('view-hr-panel');
     let path = [];
     while(el) {
         path.push({
            id: el.id,
            tag: el.tagName,
            display: window.getComputedStyle(el).display,
            visibility: window.getComputedStyle(el).visibility,
            opacity: window.getComputedStyle(el).opacity,
            height: window.getComputedStyle(el).height
         });
         el = el.parentElement;
     }
     return path;
  });
  
  console.log(JSON.stringify(visibilityInfo, null, 2));
  
  await browser.close();
})();
