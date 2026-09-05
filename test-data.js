const SUPABASE_URL = "https://osicmnagzeqkhwticiqp.supabase.co";
const SUPABASE_KEY = "sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE";

async function run() {
    const res = await fetch(`${SUPABASE_URL}/rest/v1/applications?select=id,created_at,epoint_date,submissionDate,payment_status,epoint_amount&order=created_at.desc&limit=10`, {
        headers: { 'apikey': SUPABASE_KEY, 'Authorization': `Bearer ${SUPABASE_KEY}` }
    });
    const data = await res.json();
    console.log(data);
}
run();
