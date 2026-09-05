fetch('https://osicmnagzeqkhwticiqp.supabase.co/rest/v1/registrations?select=*&order=id.desc&limit=10', {
    headers: {
        'apikey': 'sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE',
        'Authorization': 'Bearer sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE'
    }
}).then(res => res.json()).then(data => {
    const karyera = data.filter(d => d.payload && d.payload.source === 'Karyera');
    if (karyera.length > 0) {
        console.log(JSON.stringify(karyera[0].payload, null, 2));
    } else {
        console.log("No Karyera found in top 10, fetching specifically...");
        fetch('https://osicmnagzeqkhwticiqp.supabase.co/rest/v1/registrations?select=*&order=id.desc&limit=5', {
            headers: {
                'apikey': 'sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE',
                'Authorization': 'Bearer sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE'
            }
        }).then(res => res.json()).then(d2 => {
            const k2 = d2.find(x => x.payload.source === 'Karyera' || x.payload.cv_file);
            console.log(k2 ? JSON.stringify(k2, null, 2) : "Still none.");
        });
    }
});
