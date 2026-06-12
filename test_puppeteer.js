const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('file:///Users/gazanfaryusifli/Downloads/EvrikaProje/admin.html');
  await page.evaluate(() => {
    document.getElementById('login-icon').className = 'fas fa-user-tie';
    unlockModule('hr');
  });
  await page.waitForTimeout(500);
  await page.type('#hub-pass-input', 'hr123');
  await page.keyboard.press('Enter');
  await page.waitForTimeout(1000);
  await page.screenshot({path: 'admin_hr_test.png'});
  await browser.close();
})();
