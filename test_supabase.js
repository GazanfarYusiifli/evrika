async function check() {
  const API_URL='https://osicmnagzeqkhwticiqp.supabase.co/rest/v1';
  const API_KEY='sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE';
  const HEADERS={ 'apikey':API_KEY, 'Authorization':'Bearer '+API_KEY, 'Content-Type':'application/json' };
  
  try {
     const res = await fetch(`${API_URL}/registrations?select=*`, { headers: HEADERS });
     console.log("Status:", res.status);
     const text = await res.text();
     console.log("Length:", text.length);
     console.log("Is JSON:", text.startsWith("["));
  } catch(e) {
     console.log("Error:", e);
  }
}
check();
