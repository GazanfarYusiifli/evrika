async function test() {
  const API_URL='https://gziuhrlvagflokivfgwt.supabase.co/rest/v1';
  const API_KEY='sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP';
  const HEADERS={ 'apikey':API_KEY, 'Authorization':'Bearer '+API_KEY, 'Content-Type':'application/json' };

  try {
    const res = await fetch(`${API_URL}/registrations?select=*&order=id.desc&limit=10000`, { headers: HEADERS });
    console.log("Status:", res.status);
    if (!res.ok) {
        console.log("Error:", await res.text());
    } else {
        const data = await res.json();
        console.log("Rows fetched:", data.length);
    }
  } catch(e) {
    console.error(e);
  }
}
test();
