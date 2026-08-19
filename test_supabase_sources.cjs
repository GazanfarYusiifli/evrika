async function test() {
  const API_URL='https://gziuhrlvagflokivfgwt.supabase.co/rest/v1';
  const API_KEY='sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP';
  const HEADERS={ 'apikey':API_KEY, 'Authorization':'Bearer '+API_KEY, 'Content-Type':'application/json' };
  const res = await fetch(`${API_URL}/registrations?select=*&order=id.desc&limit=10000`, { headers: HEADERS });
  const data = await res.json();
  const sources = {};
  data.forEach(r => {
    let s = r.payload ? r.payload.source : r.source;
    if (r.payload && r.payload.is_scan_log) s = 'scan_log';
    if (r.payload && r.payload.position) s = 'Karyera';
    sources[s] = (sources[s] || 0) + 1;
  });
  console.log(sources);
}
test();
