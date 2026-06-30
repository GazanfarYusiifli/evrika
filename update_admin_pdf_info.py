import re

with open('admin.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_html_block = """                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:40px; border-bottom:2px solid #9c1c31; padding-bottom:20px;">
                    <h1 style="color:#9c1c31; margin:0; font-size:28px;">EVRİKA LİSEYİ</h1>
                    <img src="assets/loqoYeni.PNG" style="height:60px;" alt="Evrika Loqo">
                </div>

                <p style="font-size:16px; margin-bottom:20px;">Hörmətli valideyn,</p>

                <p style="font-size:16px; line-height:1.6; margin-bottom:30px;">"""

new_html_block = """                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:40px; border-bottom:2px solid #9c1c31; padding-bottom:20px;">
                    <h1 style="color:#9c1c31; margin:0; font-size:28px;">EVRİKA LİSEYİ</h1>
                    <img src="assets/loqoYeni.PNG" style="height:60px;" alt="Evrika Loqo">
                </div>
                
                <div style="background-color: #f8fafc; padding: 15px 20px; border-radius: 8px; margin-bottom: 30px; border: 1px solid #e2e8f0;">
                    <table style="width:100%; font-size:15px; color:#334155; border-collapse: collapse;">
                        <tr>
                            <td style="padding-bottom:8px; width:45%;"><strong>Şagirdin Adı və Soyadı:</strong></td>
                            <td style="padding-bottom:8px;">${fullName}</td>
                        </tr>
                        <tr>
                            <td style="padding-bottom:8px;"><strong>Müraciət Etdiyi Müəssisə:</strong></td>
                            <td style="padding-bottom:8px;">${getGranularSource(item)}</td>
                        </tr>
                        <tr>
                            <td style="padding-bottom:8px;"><strong>Bölmə (Sektor):</strong></td>
                            <td style="padding-bottom:8px;">${item.sector_name || item['Bölmə'] || item.Bölmə || (item.note && item.note.match(/Bölmə:\\s*([^|]+)/) ? item.note.match(/Bölmə:\\s*([^|]+)/)[1].trim() : 'Qeyd edilməyib')}</td>
                        </tr>
                        <tr>
                            <td style="padding-bottom:0;"><strong>Müraciət Etdiyi Sinif:</strong></td>
                            <td style="padding-bottom:0;">${className}</td>
                        </tr>
                    </table>
                </div>

                <p style="font-size:16px; margin-bottom:20px;">Hörmətli valideyn,</p>

                <p style="font-size:16px; line-height:1.6; margin-bottom:30px;">"""

if old_html_block in content:
    content = content.replace(old_html_block, new_html_block)
    with open('admin.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("PDF Info block added successfully.")
else:
    print("Warning: old_html_block not found in admin.html!")
