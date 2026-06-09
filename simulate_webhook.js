import crypto from 'crypto';

const PRIVATE_KEY = "HNIbtyFLu3PbxXlVykJEwOR1";

const resultObj = {
  order_id: 260,
  status: 'success',
  amount: 0.01,
  currency: 'AZN',
  card_number: '416973******0717',
  card_type: 'VISA',
  bank: 'Kapital Bank',
  transaction: 'TEST-WEBHOOK-123',
  rrn: 'RRN-999',
  date: '2026-06-07 20:30:00'
};

const dataStr = Buffer.from(JSON.stringify(resultObj)).toString('base64');
const shasum = crypto.createHash('sha1');
shasum.update(PRIVATE_KEY + dataStr + PRIVATE_KEY);
const signature = shasum.digest('base64');

console.log(JSON.stringify({ data: dataStr, signature: signature }));
