async function check() {
  const API_URL="https://osicmnagzeqkhwticiqp.supabase.co/rest/v1";
  const API_KEY="sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE";
  const HEADERS={ "apikey":API_KEY, "Authorization":"Bearer "+API_KEY, "Content-Type":"application/json" };
  const res = await fetch(`${API_URL}/registrations?select=id&order=id.desc`, { headers: HEADERS });
  const ids = await res.json();
  
  for(const r of ids) {
     const rowRes = await fetch(`${API_URL}/registrations?id=eq.${r.id}&select=*`, { headers: HEADERS });
     if(rowRes.ok) {
         const t = await rowRes.text();
         if(t.length > 50000) {
             console.log(`Row ${r.id} is HUGE! Length: ${t.length}`);
         } else {
             // console.log(`Row ${r.id} OK, length: ${t.length}`);
         }
     } else {
         console.log(`Row ${r.id} FAILED:`, rowRes.status);
     }
  }
}
check();
