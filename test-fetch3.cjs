fetch('https://osicmnagzeqkhwticiqp.supabase.co/rest/v1/registrations?select=id,payload', {
    headers: {
        'apikey': 'sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE',
        'Authorization': 'Bearer sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE'
    }
}).then(res => res.json()).then(data => {
    const withStorage = data.filter(d => JSON.stringify(d.payload).includes('supabase.co/storage'));
    console.log("Registrations with storage URL:", withStorage.length);
    if(withStorage.length > 0) {
        console.log(JSON.stringify(withStorage[0], null, 2));
    }
});
