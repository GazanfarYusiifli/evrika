import csv
import json
import os
import sys
import shutil

csv.field_size_limit(sys.maxsize)

csv_path = os.path.expanduser('~/Desktop/registrations_rows.csv')
output_dir = os.path.expanduser('./Karyera_CVler')
html_path = os.path.expanduser('./BUTUN_MURACIETLER.html')

# Clean out the existing directory
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir)

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

import base64

extracted_count = 0

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
            extracted_count += 1
            safe_name = f"cv_{extracted_count}"
            local_cv_file = f"{safe_name}{ext}"
            out_path = os.path.join(output_dir, local_cv_file)
            
            # Write file
            b64_data = payload.get('cv_file_base64', '')
            if b64_data:
                if ',' in b64_data:
                    b64_data = b64_data.split(',', 1)[1]
                try:
                    file_bytes = base64.b64decode(b64_data)
                    with open(out_path, 'wb') as out_f:
                        out_f.write(file_bytes)
                except Exception as e:
                    print(f"Error decoding {fullName}: {e}")
            
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
                    <a href="./Karyera_CVler/{local_cv_file}" target="_blank" class="btn">CV Sənədini Aç</a>
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

print(f"Regenerated HTML and {extracted_count} safe CV filenames.")
