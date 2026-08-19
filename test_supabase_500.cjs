async function test() {
  const API_URL='https://gziuhrlvagflokivfgwt.supabase.co/rest/v1';
  const API_KEY='sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP';
  const HEADERS={ 'apikey':API_KEY, 'Authorization':'Bearer '+API_KEY, 'Content-Type':'application/json' };
  const res = await fetch(`${API_URL}/registrations?select=*&order=id.desc&limit=10000`, { headers: HEADERS, cache: 'no-store' });
  console.log(res.status);
  console.log(await res.text());
}
test();
