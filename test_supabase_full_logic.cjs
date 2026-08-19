async function test() {
  const API_URL='https://gziuhrlvagflokivfgwt.supabase.co/rest/v1';
  const API_KEY='sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP';
  const HEADERS={ 'apikey':API_KEY, 'Authorization':'Bearer '+API_KEY, 'Content-Type':'application/json' };
  try {
      const res = await fetch(`${API_URL}/registrations?select=*&order=id.desc&limit=10000`, { headers: HEADERS, cache: 'no-store' });
      console.log(res.status);
      const json = await res.json();
      
      let fetchedData = json.map(r => ({ ...r.payload, _db_id_: r.id, created_at: r.created_at })); 
      let rawData = fetchedData.filter(r => {
          if (r.is_scan_log) return false;
          return true;
      });
      console.log("Raw Data Length:", rawData.length);
  } catch (e) {
      console.error("ERROR:", e.message);
  }
}
test();
