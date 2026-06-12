const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();

  page.on('console', msg => console.log('PAGE LOG:', msg.text()));
  page.on('pageerror', err => console.log('PAGE ERROR:', err.toString()));

  await page.setViewport({width: 1440, height: 900});
  await page.goto('file://' + __dirname + '/admin.html', { waitUntil: 'networkidle2' });
  
  await page.evaluate(() => {
    window.currentModuleKey = 'site';
    document.getElementById('hub-pass-input').value = 'EvrikaSite2026'; // Wait, let's just bypass it via the function.
    window.overlaySuccessfulLogin();
  });
  
  await new Promise(r => setTimeout(r, 1000));
  
  await page.evaluate(() => {
    window.switchTab('news');
  });

  await new Promise(r => setTimeout(r, 2000));
  await page.screenshot({path: 'admin_test.png', fullPage: true});
  
  const newsBox = await page.evaluate(() => {
    const el = document.getElementById('view-news');
    const r = el.getBoundingClientRect();
    return { 
      x: r.x, y: r.y, width: r.width, height: r.height,
      parentTag: el.parentElement.tagName,
      parentClass: el.parentElement.className,
      parentId: el.parentElement.id
    };
  });
  console.log('NEWS BOX:', newsBox);
  
  await browser.close();
})();
