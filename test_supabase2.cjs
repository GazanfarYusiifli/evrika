async function test() {
  const API_URL='https://osicmnagzeqkhwticiqp.supabase.co/rest/v1';
  const API_KEY='sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE';
  const HEADERS={ 'apikey':API_KEY, 'Authorization':'Bearer '+API_KEY, 'Content-Type':'application/json' };

  try {
    const res = await fetch(`${API_URL}/registrations?select=*&order=id.desc&limit=10000`, { headers: HEADERS });
    const data = await res.json();
    let fetchedData = data.map(r => ({ ...r.payload, _db_id_: r.id, created_at: r.created_at })); 

    let hrData = fetchedData.filter(r => r.source === 'Karyera' || r.position);

    let rawData = fetchedData.filter(r => {
        if (r.source === 'Karyera' || r.position) return false;
        
        if ((r.amount || r.epoint_amount || r.epoint_transaction) && r.payment_status !== 'Ödənilib') return false;
        if (r.is_scan_log) return false;
        return true;
    });

    console.log("Total Fetched:", fetchedData.length);
    console.log("HR Data:", hrData.length);
    console.log("CRM Raw Data:", rawData.length);
    console.log("Dropped by payment/scan:", fetchedData.length - hrData.length - rawData.length);
  } catch(e) {
    console.error(e);
  }
}
test();
