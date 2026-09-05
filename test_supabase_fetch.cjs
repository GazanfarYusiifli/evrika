async function test() {
  const API_URL='https://osicmnagzeqkhwticiqp.supabase.co/rest/v1';
  const API_KEY='sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE';
  const HEADERS={ 'apikey':API_KEY, 'Authorization':'Bearer '+API_KEY, 'Content-Type':'application/json' };
  try {
      const res = await fetch(`${API_URL}/registrations?select=*&order=id.desc&limit=10000`, { headers: HEADERS, cache: 'no-store' });
      console.log(res.status);
      const j = await res.json();
      console.log(j.length);
  } catch (e) {
      console.error(e.message);
  }
}
test();
