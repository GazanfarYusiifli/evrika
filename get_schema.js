const API_URL='https://gziuhrlvagflokivfgwt.supabase.co/rest/v1';
const API_KEY='sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP';
const HEADERS={ 'apikey':API_KEY, 'Authorization':'Bearer '+API_KEY, 'Content-Type':'application/json' };

fetch(`${API_URL}/mezunlar?limit=1`, { headers: HEADERS })
  .then(r => r.json())
  .then(console.log);
