async function test() {
  const API_URL='https://osicmnagzeqkhwticiqp.supabase.co/rest/v1';
  const API_KEY='sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE';
  const HEADERS={ 'apikey':API_KEY, 'Authorization':'Bearer '+API_KEY, 'Content-Type':'application/json' };
  const res = await fetch(`${API_URL}/registrations?select=*&order=id.desc&limit=100`, { headers: HEADERS, cache: 'no-store' });
  console.log("Status:", res.status);
  const text = await res.text();
  if (res.ok) {
     console.log("Length:", JSON.parse(text).length);
  } else {
     console.log("Error:", text);
  }
}
test();
