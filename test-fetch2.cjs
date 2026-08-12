const fs = require('fs');
fetch('https://gziuhrlvagflokivfgwt.supabase.co/rest/v1/registrations?select=*&order=id.desc&limit=50', {
    headers: {
        'apikey': 'sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP',
        'Authorization': 'Bearer sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP'
    }
}).then(res => res.json()).then(data => {
    const karyera = data.find(d => d.payload && d.payload.source === 'Karyera');
    if (karyera) {
        fs.writeFileSync('scratch/karyera.json', JSON.stringify(karyera.payload, null, 2));
    }
});
