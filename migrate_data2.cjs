const https = require('https');

const OLD_HOST = 'gziuhrlvagflokivfgwt.supabase.co';
const OLD_KEY = 'sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP';

const NEW_HOST = 'gziuhrlvagflokivfgwt.supabase.co';
const NEW_KEY = 'sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP';

const TABLES = ['registrations', 'news', 'ugurlar', 'partners', 'vacancies'];

function makeRequest(host, path, method, key, body = null) {
    return new Promise((resolve, reject) => {
        const options = {
            hostname: host,
            port: 443,
            path: path,
            method: method,
            family: 4, // FORCE IPv4 TO PREVENT HANGS
            headers: {
                'apikey': key,
                'Authorization': 'Bearer ' + key,
                'Content-Type': 'application/json',
                'Prefer': 'return=minimal'
            }
        };

        const req = https.request(options, (res) => {
            let data = '';
            res.on('data', chunk => data += chunk);
            res.on('end', () => {
                if (res.statusCode >= 200 && res.statusCode < 300) {
                    resolve(data ? JSON.parse(data) : null);
                } else {
                    reject(new Error(`HTTP ${res.statusCode}: ${data}`));
                }
            });
        });

        req.on('error', reject);
        
        if (body) {
            req.write(JSON.stringify(body));
        }
        req.end();
    });
}

async function run() {
    for (const t of TABLES) {
        console.log(`Fetching ${t}...`);
        try {
            const data = await makeRequest(OLD_HOST, `/rest/v1/${t}?select=*`, 'GET', OLD_KEY);
            console.log(`Fetched ${data.length} rows for ${t}.`);
            
            if (data.length > 0) {
                // To avoid duplicate ID issues on multiple runs, we can use UPSERT
                // But REST POST without resolution just fails on duplicate.
                // We'll just POST them.
                console.log(`Inserting into ${t}...`);
                await makeRequest(NEW_HOST, `/rest/v1/${t}`, 'POST', NEW_KEY, data).catch(e => {
                    console.log("Insert warning (might be duplicates):", e.message);
                });
                console.log(`Finished ${t}.`);
            }
        } catch(e) {
            console.log(`Error on ${t}:`, e.message);
        }
    }
    console.log("DONE");
}
run();
