const fs = require('fs');
const path = require('path');
const API_URL='https://miwvdhwrmxoetszkxlzy.supabase.co/rest/v1';
const API_KEY='sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV';
const HEADERS={ 'apikey':API_KEY, 'Authorization':'Bearer '+API_KEY, 'Content-Type':'application/json' };

async function run() {
  const existingRes = await fetch(`${API_URL}/mezunlar`, { headers: HEADERS });
  const existing = await existingRes.json();
  const existingImgs = existing.map(r => r.payload.img);

  const files = fs.readdirSync('./assets/mezunlar');
  for (const file of files) {
    if (file.startsWith('mezun_') && (file.endsWith('.png') || file.endsWith('.jpeg') || file.endsWith('.jpg'))) {
      const imgPath = `assets/mezunlar/${file}`;
      if (!existingImgs.includes(imgPath)) {
        console.log(`Inserting ${imgPath}...`);
        await fetch(`${API_URL}/mezunlar`, {
          method: 'POST',
          headers: HEADERS,
          body: JSON.stringify({ payload: { img: imgPath, uni: '', name: 'Evrika Məzunu' } })
        });
      }
    }
  }
  console.log('Done.');
}
run();
