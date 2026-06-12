const API_URL='https://miwvdhwrmxoetszkxlzy.supabase.co/rest/v1';
const API_KEY='sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV';
const HEADERS={ 'apikey':API_KEY, 'Authorization':'Bearer '+API_KEY, 'Content-Type':'application/json' };

fetch(`${API_URL}/mezunlar?limit=1`, { headers: HEADERS })
  .then(r => r.json())
  .then(console.log);
