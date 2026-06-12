const fs = require('fs');
fetch('https://miwvdhwrmxoetszkxlzy.supabase.co/rest/v1/registrations?select=*&order=id.desc&limit=10', {
    headers: {
        'apikey': 'sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV',
        'Authorization': 'Bearer sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV'
    }
}).then(res => res.json()).then(data => {
    console.log(JSON.stringify(data, null, 2));
});
