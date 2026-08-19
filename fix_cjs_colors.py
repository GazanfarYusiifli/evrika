import re

file = 'generate_forms.cjs'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Make Qeydiyyat title red
content = re.sub(
    r'<h1 class="titan-header"(.*?)color: var\(--text-primary\);(.*?)>Qeydiyyat</h1>',
    r'<h1 class="titan-header"\g<1>color: var(--burgundy);\g<2>>Qeydiyyat</h1>',
    content
)

# Make form container slightly reddish
content = re.sub(
    r'\.form-container \{([\s\S]*?)background: rgba\(255, 255, 255, 0\.85\);',
    r'.form-container {\g<1>background: #fdf0f2;',
    content
)

# Fix labels
content = re.sub(
    r'<label>HAZIRDA TƏHSİL ALDIĞI TƏHSİL MÜƏSSİSƏSİ \( BAĞÇA VƏ MƏKTƏB\)</label>',
    r'<label>Hazırda təhsil aldığı təhsil müəssisəsi ( bağça və məktəb)</label>',
    content
)
content = re.sub(
    r'<label>MÜRACİƏT ETDİYİ SİNİF</label>',
    r'<label>Müraciət etdiyi sinif</label>',
    content
)
content = re.sub(
    r'<label>MÜRACİƏT ETDİYİ BÖLMƏ</label>',
    r'<label>Müraciət etdiyi bölmə</label>',
    content
)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("generate_forms.cjs updated")
