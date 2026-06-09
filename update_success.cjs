const fs = require('fs');
let code = fs.readFileSync('success.html', 'utf8');

code = code.replace(
    /const emailParam = urlParams\.get\('email'\);/,
    "const emailParam = urlParams.get('email') || localStorage.getItem('last_email');"
);

code = code.replace(
    /const regName = urlParams\.get\('name'\);/,
    "const regName = urlParams.get('name') || localStorage.getItem('last_name');"
);

code = code.replace(
    /const finalEmail = emailParam \|\| currentPayload\.email \|\| currentPayload\['E-mail'\] \|\| 'qeyd etdiyiniz';/,
    `let extractedEmail = '';
                if (currentPayload && currentPayload.note) {
                    const match = currentPayload.note.match(/E-mail:\\s*([^\\s|]+)/);
                    if (match && match[1]) extractedEmail = match[1].trim();
                }
                const finalEmail = emailParam || extractedEmail || currentPayload.email || currentPayload['E-mail'] || 'qeyd etdiyiniz';`
);

fs.writeFileSync('success.html', code);
