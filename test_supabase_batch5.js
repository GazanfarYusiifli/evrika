async function check() {
  const API_URL="https://gziuhrlvagflokivfgwt.supabase.co/rest/v1";
  const API_KEY="sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP";
  const HEADERS={ "apikey":API_KEY, "Authorization":"Bearer "+API_KEY, "Content-Type":"application/json" };
  const res = await fetch(`${API_URL}/registrations?select=id&order=id.desc`, { headers: HEADERS });
  const ids = await res.json();
  
  let allData = [];
  for (let i = 0; i < ids.length; i += 5) {
      const batchIds = ids.slice(i, i + 5).map(x => x.id).join(',');
      const bRes = await fetch(`${API_URL}/registrations?id=in.(${batchIds})&select=*`, { headers: HEADERS });
      if(!bRes.ok) {
          console.log("FAILED BATCH", i, await bRes.text());
      } else {
          allData.push(...await bRes.json());
      }
  }
  console.log("Total Fetched Data length:", allData.length);
}
check();
