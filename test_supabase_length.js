async function check() {
  const API_URL="https://osicmnagzeqkhwticiqp.supabase.co/rest/v1";
  const API_KEY="sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE";
  const HEADERS={ "apikey":API_KEY, "Authorization":"Bearer "+API_KEY, "Content-Type":"application/json" };
  // Fetch only the ID and the first 100 chars of the payload to avoid timeout?
  // Supabase postgrest doesn't have length() easily available without rpc.
  // We can fetch just the payload for one row at a time.
  const res = await fetch(`${API_URL}/registrations?select=id`, { headers: HEADERS });
  const ids = await res.json();
  for(const r of ids.slice(0, 10)) {
     const rowRes = await fetch(`${API_URL}/registrations?id=eq.${r.id}&select=id`, { headers: HEADERS });
     console.log(r.id, "exists");
  }
}
check();
