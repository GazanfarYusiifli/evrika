const SUPABASE_URL = "https://gziuhrlvagflokivfgwt.supabase.co";
const SUPABASE_KEY = "sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP";

async function run() {
    const res = await fetch(`${SUPABASE_URL}/rest/v1/applications?select=id,created_at,epoint_date,submissionDate,payment_status,epoint_amount&order=created_at.desc&limit=10`, {
        headers: { 'apikey': SUPABASE_KEY, 'Authorization': `Bearer ${SUPABASE_KEY}` }
    });
    const data = await res.json();
    console.log(data);
}
run();
