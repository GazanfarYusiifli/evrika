const API_URL='https://osicmnagzeqkhwticiqp.supabase.co/rest/v1';
const API_KEY='sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE';
const HEADERS={ 'apikey':API_KEY, 'Authorization':'Bearer '+API_KEY, 'Content-Type':'application/json' };

fetch(`${API_URL}/mezunlar?limit=1`, { headers: HEADERS })
  .then(r => r.json())
  .then(console.log);
