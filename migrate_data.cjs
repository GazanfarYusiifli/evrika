const fs = require('fs');
const OLD_URL = 'https://gziuhrlvagflokivfgwt.supabase.co/rest/v1';
const OLD_KEY = 'sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP';

const NEW_URL = 'https://gziuhrlvagflokivfgwt.supabase.co/rest/v1';
const NEW_KEY = 'sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP';

const TABLES = ['registrations', 'news', 'ugurlar', 'partners', 'vacancies'];

async function fetchWithRetry(url, options, retries = 3) {
    for (let i = 0; i < retries; i++) {
        try {
            const res = await fetch(url, options);
            if (!res.ok) {
                const text = await res.text();
                throw new Error(`HTTP ${res.status}: ${text}`);
            }
            return res;
        } catch (e) {
            if (i === retries - 1) throw e;
            console.log(`Retry ${i+1} for ${url}...`);
            await new Promise(r => setTimeout(r, 1000));
        }
    }
}

async function migrateTable(tableName) {
    console.log(`Migrating table: ${tableName}`);
    // Fetch all old data
    const res = await fetchWithRetry(`${OLD_URL}/${tableName}?select=*`, {
        headers: { 'apikey': OLD_KEY, 'Authorization': 'Bearer ' + OLD_KEY }
    });
    const oldData = await res.json();
    console.log(`Found ${oldData.length} rows in ${tableName}`);
    if (oldData.length === 0) return;

    // Batch insert to new DB
    const batchSize = 100;
    for (let i = 0; i < oldData.length; i += batchSize) {
        const batch = oldData.slice(i, i + batchSize);
        await fetchWithRetry(`${NEW_URL}/${tableName}`, {
            method: 'POST',
            headers: { 
                'apikey': NEW_KEY, 
                'Authorization': 'Bearer ' + NEW_KEY, 
                'Content-Type': 'application/json',
                'Prefer': 'return=minimal' 
            },
            body: JSON.stringify(batch)
        });
        console.log(`Inserted ${i + batch.length}/${oldData.length} into ${tableName}`);
    }
}

async function run() {
    for (const t of TABLES) {
        await migrateTable(t);
    }
    console.log("MIGRATION COMPLETE!");
}

run().catch(console.error);
