import csv
import json
import base64
import os

csv_path = os.path.expanduser('~/Desktop/registrations_rows.csv')
output_dir = os.path.expanduser('~/Desktop/Karyera_CVler/')

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

import sys
csv.field_size_limit(sys.maxsize)

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
            b64_data = payload.get('cv_file_base64')
            filename = payload.get('cv_file_name')
            fullName = payload.get('fullName', 'Adsiz')
            position = payload.get('position', 'Vezife_yoxdur')
            
            if b64_data and filename:
                if ',' in b64_data:
                    b64_data = b64_data.split(',', 1)[1]
                
                ext = os.path.splitext(filename)[1]
                if not ext:
                    ext = '.pdf'
                
                safe_name = f"{fullName} - {position}".replace('/', '_').replace('\\', '_')
                out_name = f"{safe_name}{ext}"
                out_path = os.path.join(output_dir, out_name)
                
                try:
                    file_bytes = base64.b64decode(b64_data)
                    with open(out_path, 'wb') as out_f:
                        out_f.write(file_bytes)
                    extracted_count += 1
                except Exception as e:
                    print(f"Error decoding {fullName}: {e}")

print(f"Successfully extracted {extracted_count} CVs.")
