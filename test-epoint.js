import crypto from 'crypto';
const PUB_KEY = "i000201608";
const PVT_KEY = "HNIbtyFLu3PbxXlVykJEwOR1";
const dataObj = { public_key: PUB_KEY, transaction: "159" }; // assuming 159 is an order_id
const dataJson = JSON.stringify(dataObj);
const dataB64 = Buffer.from(dataJson).toString('base64');
const shasum = crypto.createHash('sha1');
shasum.update(PVT_KEY + dataB64 + PVT_KEY);
const signatureStr = shasum.digest('base64');

fetch("https://epoint.az/api/1/get-status", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({ data: dataB64, signature: signatureStr }).toString()
}).then(res => res.json()).then(console.log).catch(console.error);
