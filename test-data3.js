const SUPABASE_URL = "https://osicmnagzeqkhwticiqp.supabase.co";
const SUPABASE_KEY = "sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE";

async function run() {
    const res = await fetch(`${SUPABASE_URL}/rest/v1/registrations?select=*&order=id.desc&limit=1`, {
        headers: { 'apikey': SUPABASE_KEY, 'Authorization': `Bearer ${SUPABASE_KEY}` }
    });
    const data = await res.json();
    console.log(Object.keys(data[0] || {}));
}
run();
