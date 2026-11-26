export default async function handler(req, res) {
  const branch = String(req.query.branch || req.query.b || '').toUpperCase();
  const isGenclik = branch === 'LIS2' || branch === 'LISEY2' || branch.includes('GENCLIK');
  const target = isGenclik
    ? 'https://evrikaliseyi.edu.az/valideyn-sesi-genclik'
    : 'https://evrikaliseyi.edu.az/valideyn-sesi-nerimanov';

  try {
    const upstream = await fetch(target);
    const html = await upstream.text();
    res.setHeader('Content-Type', 'text/html; charset=utf-8');
    res.setHeader('Cache-Control', 'public, max-age=0, must-revalidate');
    res.status(upstream.status).send(html);
  } catch (err) {
    res.status(500).send('Error loading survey page');
  }
}
