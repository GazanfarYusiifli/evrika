async function test() {
  const API_URL='https://gziuhrlvagflokivfgwt.supabase.co/rest/v1';
  const API_KEY='sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP';
  const HEADERS={ 'apikey':API_KEY, 'Authorization':'Bearer '+API_KEY, 'Content-Type':'application/json' };
  try {
      const res = await fetch(`${API_URL}/registrations?select=*&limit=10000`, { headers: HEADERS, cache: 'no-store' });
      const text = await res.text();
      console.log("Status:", res.status);
      if (!res.ok) {
         console.log("Error body:", text);
         return;
      }
      let json = JSON.parse(text);
      let fetchedData = json
          .map(r => ({ ...r.payload, _db_id_: r.id, created_at: r.created_at }))
          .sort((a, b) => b._db_id_ - a._db_id_);
      let rawData = fetchedData.filter(r => {
          if (r.is_scan_log) return false;
          return true;
      });
      console.log("Raw Data Length:", rawData.length);
      console.log("First item:", rawData[0]);
  } catch (e) {
      console.error("ERROR:", e.message);
  }
}
test();
