import crypto from 'crypto';
const Z_KEY = '46c1136999a0003106d4';
const Z_SECRET = '698e98b07e9c2c4e5cf0';

async function fetchZadarma(apiPath) {
    const paramsStr = '';
    const md5Str = crypto.createHash('md5').update(paramsStr).digest('hex');
    const dataToSign = apiPath + paramsStr + md5Str;
    const signature = crypto.createHmac('sha1', Z_SECRET).update(dataToSign).digest('base64');
    
    const res = await fetch(`https://api.zadarma.com${apiPath}`, {
        headers: { 'Authorization': `${Z_KEY}:${signature}` }
    });
    return await res.json();
}

async function run() {
    console.log("Sip:", await fetchZadarma('/v1/sip/'));
    console.log("Direct numbers:", await fetchZadarma('/v1/direct_numbers/'));
}
run();
