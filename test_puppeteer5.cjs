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
  
  const op = await page.evaluate(() => window.getComputedStyle(document.getElementById('view-hr-panel')).opacity);
  
  console.log("NEW OPACITY:", op);
  
  await browser.close();
})();
