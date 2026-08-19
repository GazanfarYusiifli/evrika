const SUPABASE_URL = "https://gziuhrlvagflokivfgwt.supabase.co";
const SUPABASE_KEY = "sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP";

async function run() {
    const res = await fetch(`${SUPABASE_URL}/rest/v1/registrations?select=*&order=id.desc&limit=1`, {
        headers: { 'apikey': SUPABASE_KEY, 'Authorization': `Bearer ${SUPABASE_KEY}` }
    });
    const data = await res.json();
    console.log(Object.keys(data[0] || {}));
}
run();
