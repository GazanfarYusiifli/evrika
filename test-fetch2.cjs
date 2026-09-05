const fs = require('fs');
fetch('https://osicmnagzeqkhwticiqp.supabase.co/rest/v1/registrations?select=*&order=id.desc&limit=50', {
    headers: {
        'apikey': 'sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE',
        'Authorization': 'Bearer sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE'
    }
}).then(res => res.json()).then(data => {
    const karyera = data.find(d => d.payload && d.payload.source === 'Karyera');
    if (karyera) {
        fs.writeFileSync('scratch/karyera.json', JSON.stringify(karyera.payload, null, 2));
    }
});
