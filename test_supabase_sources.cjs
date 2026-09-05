async function test() {
  const API_URL='https://osicmnagzeqkhwticiqp.supabase.co/rest/v1';
  const API_KEY='sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE';
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
