async function test() {
  const API_URL='https://osicmnagzeqkhwticiqp.supabase.co/rest/v1';
  const API_KEY='sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE';
  const HEADERS={ 'apikey':API_KEY, 'Authorization':'Bearer '+API_KEY, 'Content-Type':'application/json' };

  try {
    const res = await fetch(`${API_URL}/registrations?select=*&order=id.desc&limit=10000`, { headers: HEADERS });
    const data = await res.json();
    let fetchedData = data.map(r => ({ ...r.payload, _db_id_: r.id, created_at: r.created_at })); 

    let dropped = fetchedData.filter(r => {
        if (r.source === 'Karyera' || r.position) return false;
        
        let shouldDrop = false;
        if ((r.amount || r.epoint_amount || r.epoint_transaction) && r.payment_status !== 'Ödənilib') shouldDrop = true;
        if (r.is_scan_log) shouldDrop = true;
        
        return shouldDrop;
    });

    console.log("Dropped records:", dropped.map(d => ({ name: d.fullName || d['Ad Soyad'] || 'Unknown', amount: d.amount, epoint_amount: d.epoint_amount, is_scan_log: d.is_scan_log, source: d.source })));
  } catch(e) {
    console.error(e);
  }
}
test();
