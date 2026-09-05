async function check() {
  const SUPABASE_URL = "https://osicmnagzeqkhwticiqp.supabase.co";
  const SUPABASE_KEY = "sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE";
  const res = await fetch(`${SUPABASE_URL}/rest/v1/registrations?select=id,created_at,payload&order=id.desc&limit=5`, {
    headers: { 'apikey': SUPABASE_KEY, 'Authorization': `Bearer ${SUPABASE_KEY}` }
  });
  if(res.ok) {
     const data = await res.json();
     data.forEach(r => {
        console.log(`ID: ${r.id}, Name: ${r.payload.fullName || r.payload['[2.Şagird] Adı']}, Payment Status: ${r.payload.payment_status}, Epoint Status: ${r.payload.epoint_amount ? 'Yes' : 'No'}`);
     });
  } else {
     console.log("Error fetching", await res.text());
  }
}
check();
