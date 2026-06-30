import re

with open('admin.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_html_block = """        const html = `
            <div style="padding:40px; font-family:sans-serif; color:#1e293b; max-width:800px; margin:auto;">
                <div style="text-align:center; margin-bottom:30px; border-bottom:3px solid #9c1c31; padding-bottom:20px; position:relative;">
                    <img src="assets/loqoYeni.PNG" style="position:absolute; top:0; left:0; height:60px;" alt="Evrika Loqo">
                    <h1 style="color:#9c1c31; margin:0; font-size:28px;">EVRİKA LİSEYİ</h1>
                    <p style="margin:5px 0 0 0; font-size:14px; color:#64748b;">Mükəmməl təhsilin ünvanı</p>
                </div>
                <h2 style="text-align:center; margin-bottom:40px; font-size:22px;">Qəbul İmtahanı - Nəticə və Rəylər</h2>
                <div style="background:#f8fafc; padding:20px; border-radius:10px; margin-bottom:30px;">
                    <p style="margin:0 0 10px 0; font-size:16px;"><strong>Şagird:</strong> ${fullName}</p>
                    <p style="margin:0 0 10px 0; font-size:16px;"><strong>Sinif:</strong> ${className}</p>
                    <p style="margin:0; font-size:16px;"><strong>Müraciət etdiyi müəssisə:</strong> ${getGranularSource(item)}</p>
                </div>
                
                <div style="margin-bottom:25px;">
                    <h3 style="color:#0f172a; border-bottom:1px solid #e2e8f0; padding-bottom:8px; font-size:18px;">Şagirdin İmtahan Balı</h3>
                    <p style="white-space:pre-wrap; font-size:15px; line-height:1.6; color:#334155;">${rev.score ? `Övladınız ${fullName} Evrika Liseyində keçirilən ${className} üzrə qəbul imtahanında (maksimum 90 bal, keçid balı 45) ${rev.score} bal toplayaraq uğur qazanmışdır.` : 'Rəy yoxdur'}</p>
                </div>
                
                <div style="margin-bottom:25px;">
                    <h3 style="color:#0f172a; border-bottom:1px solid #e2e8f0; padding-bottom:8px; font-size:18px;">Akademik Qiymətləndirmə</h3>
                    <p style="white-space:pre-wrap; font-size:15px; line-height:1.6; color:#334155;">${rev.academic || 'Rəy yoxdur'}</p>
                </div>
                
                <div style="margin-bottom:25px;">
                    <h3 style="color:#0f172a; border-bottom:1px solid #e2e8f0; padding-bottom:8px; font-size:18px;">Psixoloji Müayinə Protokolu</h3>
                    <p style="white-space:pre-wrap; font-size:15px; line-height:1.6; color:#334155;">${rev.psycho || 'Rəy yoxdur'}</p>
                </div>
                
                <div style="margin-top:50px; padding-top:20px; border-top:1px dashed #cbd5e1; text-align:center; font-size:12px; color:#94a3b8;">
                    Bu sənəd sistem tərəfindən avtomatik generasiya olunmuşdur.
                </div>
            </div>
        `;"""

new_html_block = """        const html = `
            <div style="padding:40px; font-family:sans-serif; color:#1e293b; max-width:800px; margin:auto;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:40px; border-bottom:2px solid #9c1c31; padding-bottom:20px;">
                    <h1 style="color:#9c1c31; margin:0; font-size:28px;">EVRİKA LİSEYİ</h1>
                    <img src="assets/loqoYeni.PNG" style="height:60px;" alt="Evrika Loqo">
                </div>

                <p style="font-size:16px; margin-bottom:20px;">Hörmətli valideyn,</p>

                <p style="font-size:16px; line-height:1.6; margin-bottom:30px;">
                    Övladınız <strong>${fullName}</strong> Evrika Liseyində keçirilən qəbul imtahanında iştirak etmiş və <strong>90 mümkün baldan ${rev.score || 0} bal</strong> toplamışdır. Qəbul üçün müəyyən edilmiş keçid göstəricisi <strong>45 bal</strong> təşkil edir.
                </p>

                <p style="font-size:16px; line-height:1.6; margin-bottom:30px;">Şagirdin nəticələri akademik və psixoloji qiymətləndirmə çərçivəsində təhlil edilmişdir.</p>

                <div style="margin-bottom:25px;">
                    <h3 style="color:#0f172a; font-size:18px; margin-bottom:10px;"><strong>Akademik Qiymətləndirmə:</strong></h3>
                    <p style="white-space:pre-wrap; font-size:15px; line-height:1.6; color:#334155; margin:0;">${rev.academic || 'Rəy yoxdur'}</p>
                </div>
                
                <div style="margin-bottom:30px;">
                    <h3 style="color:#0f172a; font-size:18px; margin-bottom:10px;"><strong>Psixoloji Müayinə Protokolu:</strong></h3>
                    <p style="white-space:pre-wrap; font-size:15px; line-height:1.6; color:#334155; margin:0;">${rev.psycho || 'Rəy yoxdur'}</p>
                </div>

                <p style="font-size:16px; line-height:1.6; margin-bottom:40px;">Ətraflı məlumat üçün təqdim olunan fərdi hesabatla tanış ola bilərsiniz.</p>

                <div style="font-size:16px; line-height:1.6; margin-bottom:40px;">
                    Hörmətlə,<br>
                    <strong>Evrika Liseyi – Qəbul Komissiyası</strong>
                </div>

                <div style="margin-top:50px; padding-top:20px; border-top:1px dashed #cbd5e1; font-size:12px; color:#94a3b8;">
                    <em>*Bu məlumat Evrika Liseyinin qiymətləndirmə sistemi tərəfindən avtomatik olaraq yaradılmışdır.</em>
                </div>
            </div>
        `;"""

if old_html_block in content:
    content = content.replace(old_html_block, new_html_block)
    with open('admin.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Template updated successfully.")
else:
    print("Warning: old_html_block not found in admin.html!")
