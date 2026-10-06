export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, PATCH, DELETE, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization, apikey');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  const SUPABASE_URL = "https://osicmnagzeqkhwticiqp.supabase.co/rest/v1";
  const KEY = "sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE";
  const HEADERS = {
    "apikey": KEY,
    "Authorization": `Bearer ${KEY}`,
    "Content-Type": "application/json",
    "Prefer": "return=representation"
  };

  try {
    // 1. GET /api/vacancies
    if (req.method === 'GET') {
      const getRes = await fetch(`${SUPABASE_URL}/vacancies?select=*&order=id.desc`, {
        headers: HEADERS
      });
      if (!getRes.ok) {
        throw new Error(`Supabase GET error: ${getRes.statusText}`);
      }
      const rawList = await getRes.json();
      const list = rawList.map(r => {
        const p = r.payload || {};
        return {
          ...p,
          ...r,
          id: r.id,
          _db_id_: r.id,
          title: p.title || r.title || 'Vakansiya',
          location: p.location || r.location || '',
          time: p.time || r.time || '',
          desc: p.desc || r.desc || '',
          responsibilities: p.responsibilities || r.responsibilities || '',
          requirements: p.requirements || r.requirements || '',
          status: p.status || r.status || 'Aktiv'
        };
      });
      return res.status(200).json(list);
    }

    // 2. POST /api/vacancies (Yeni vakansiya)
    if (req.method === 'POST') {
      const body = typeof req.body === 'string' ? JSON.parse(req.body) : req.body;
      const payload = body.payload ? body.payload : body;

      const postRes = await fetch(`${SUPABASE_URL}/vacancies`, {
        method: 'POST',
        headers: HEADERS,
        body: JSON.stringify({ payload })
      });
      if (!postRes.ok) {
        const errText = await postRes.text();
        throw new Error(`Supabase POST error: ${errText}`);
      }
      const data = await postRes.json();
      return res.status(201).json({ success: true, id: data[0]?.id, data: data[0] });
    }

    // 3. PUT / PATCH /api/vacancies?id=X
    if (req.method === 'PUT' || req.method === 'PATCH') {
      const id = req.query.id || req.body?.id;
      if (!id) return res.status(400).json({ error: "Missing id" });

      const cleanId = String(id).replace(/[^0-9]/g, '');
      const body = typeof req.body === 'string' ? JSON.parse(req.body) : req.body;
      const payload = body.payload ? body.payload : body;

      const patchRes = await fetch(`${SUPABASE_URL}/vacancies?id=eq.${cleanId}`, {
        method: 'PATCH',
        headers: HEADERS,
        body: JSON.stringify({ payload })
      });
      if (!patchRes.ok) {
        const errText = await patchRes.text();
        throw new Error(`Supabase PATCH error: ${errText}`);
      }
      return res.status(200).json({ success: true });
    }

    // 4. DELETE /api/vacancies?id=X
    if (req.method === 'DELETE') {
      const id = req.query.id || req.body?.id;
      if (!id) return res.status(400).json({ error: "Missing id" });

      const cleanId = String(id).replace(/[^0-9]/g, '');
      const delRes = await fetch(`${SUPABASE_URL}/vacancies?id=eq.${cleanId}`, {
        method: 'DELETE',
        headers: HEADERS
      });
      if (!delRes.ok) {
        const errText = await delRes.text();
        throw new Error(`Supabase DELETE error: ${errText}`);
      }
      return res.status(200).json({ success: true });
    }

    return res.status(405).json({ error: "Method not allowed" });
  } catch (err) {
    console.error("Vacancies API error:", err);
    return res.status(500).json({ error: err.message });
  }
}
