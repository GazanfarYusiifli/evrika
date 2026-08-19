import csv
import json
import os
import sys

csv.field_size_limit(sys.maxsize)

csv_path = os.path.expanduser('~/Desktop/registrations_rows.csv')
html_path = os.path.expanduser('~/Desktop/BUTUN_MURACIETLER.html')

html_content = """
<!DOCTYPE html>
<html lang="az">
<head>
    <meta charset="UTF-8">
    <title>Karyera Müraciətləri</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f3f4f6; margin: 0; padding: 20px; color: #333; }
        .header { text-align: center; margin-bottom: 40px; }
        .header h1 { color: #8b1a2b; font-size: 2.5rem; margin-bottom: 10px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(400px, 1fr)); gap: 20px; }
        .card { background: white; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); overflow: hidden; display: flex; flex-direction: column; border-top: 5px solid #8b1a2b; }
        .card-header { padding: 20px; background: #fafafa; border-bottom: 1px solid #eee; }
        .card-header h2 { margin: 0; font-size: 1.4rem; color: #111; }
        .card-header .position { color: #8b1a2b; font-weight: bold; font-size: 1.1rem; margin-top: 5px; }
        .card-body { padding: 20px; flex: 1; }
        .info-row { margin-bottom: 10px; font-size: 0.95rem; }
        .info-label { font-weight: bold; color: #555; }
        .card-footer { padding: 15px 20px; background: #f9fafb; border-top: 1px solid #eee; text-align: right; }
        .btn { background: #8b1a2b; color: white; text-decoration: none; padding: 10px 20px; border-radius: 6px; font-weight: bold; display: inline-block; transition: 0.2s; }
        .btn:hover { background: #6b1421; }
    </style>
</head>
<body>
    <div class="header">
        <h1>Evrika Liseyi - Karyera Müraciətləri</h1>
        <p>Aşağıdakı siyahıdan hər bir namizədin anket məlumatlarına baxa və birbaşa CV faylını aça bilərsiniz.</p>
    </div>
    <div class="grid">
"""

with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        payload_str = row.get('payload', '{}')
        if not payload_str: continue
        try:
            payload = json.loads(payload_str)
        except json.JSONDecodeError:
            continue
            
        if payload.get('source') == 'Karyera':
            fullName = payload.get('fullName', 'Adsız')
            position = payload.get('position', 'Vəzifə yoxdur')
            filename = payload.get('cv_file_name', '')
            
            ext = os.path.splitext(filename)[1] if filename else '.pdf'
            safe_name = f"{fullName} - {position}".replace('/', '_').replace('\\', '_')
            local_cv_file = f"Karyera_CVler/{safe_name}{ext}"
            
            keys_to_skip = ['cv_file_base64', 'cv_file_name', 'source', 'status', 'submissionDate']
            
            html_content += f"""
            <div class="card">
                <div class="card-header">
                    <h2>{fullName}</h2>
                    <div class="position">{position}</div>
                </div>
                <div class="card-body">
            """
            
            for key, val in payload.items():
                if key not in keys_to_skip and val:
                    html_content += f"""<div class="info-row"><span class="info-label">{key}:</span> {val}</div>"""
                    
            html_content += f"""
                </div>
                <div class="card-footer">
                    <a href="./{local_cv_file}" target="_blank" class="btn">CV Sənədini Aç</a>
                </div>
            </div>
            """

html_content += """
    </div>
</body>
</html>
"""

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated BUTUN_MURACIETLER.html on Desktop")
