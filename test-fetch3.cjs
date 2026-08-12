fetch('https://gziuhrlvagflokivfgwt.supabase.co/rest/v1/registrations?select=id,payload', {
    headers: {
        'apikey': 'sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP',
        'Authorization': 'Bearer sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP'
    }
}).then(res => res.json()).then(data => {
    const withStorage = data.filter(d => JSON.stringify(d.payload).includes('supabase.co/storage'));
    console.log("Registrations with storage URL:", withStorage.length);
    if(withStorage.length > 0) {
        console.log(JSON.stringify(withStorage[0], null, 2));
    }
});
