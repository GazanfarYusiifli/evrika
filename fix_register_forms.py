import os
import re

files_to_process = [
    'register-lisey1.html',
    'register-lisey2.html',
    'register-montessori.html',
    'register-victory.html',
    'register-zumrud.html'
]

def extract_group(content, label_i18n):
    # Regex to find the entire div.dyn-input-group containing a specific data-i18n label
    pattern = r'<div class="dyn-input-group(?: full-width)?">\s*<label data-i18n="' + label_i18n + r'".*?</div>\s*</div>'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(0), match.start(), match.end()
    
    # Try simpler matching if no closing </div>\s*</div> is perfectly matched (due to select vs input)
    # Actually, let's just use string parsing to extract the div.
    idx = content.find(f'data-i18n="{label_i18n}"')
    if idx == -1: return None, -1, -1
    
    # find the preceding <div class="dyn-input-group
    start_idx = content.rfind('<div class="dyn-input-group', 0, idx)
    
    # find the balancing closing </div>
    # we know it's a simple structure, so we can just look for the second </div> if there is a select, or first if input.
    # Actually, input group has label + input -> 1 closing div.
    # input group with select has label + div + select + i + /div -> 2 closing divs.
    
    # Let's write a simple parser to find the matching closing div for start_idx
    div_count = 0
    i = start_idx
    while i < len(content):
        if content[i:i+4] == '<div':
            div_count += 1
            i += 4
        elif content[i:i+6] == '</div>':
            div_count -= 1
            if div_count == 0:
                end_idx = i + 6
                return content[start_idx:end_idx], start_idx, end_idx
            i += 6
        else:
            i += 1
            
    return None, -1, -1

for file in files_to_process:
    if not os.path.exists(file): continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    name_str, ns, ne = extract_group(content, 'reg-student-name')
    surname_str, sus, sue = extract_group(content, 'reg-student-surname')
    sector_str, secs, sece = extract_group(content, 'reg-sector')
    class_str, cls, cle = extract_group(content, 'reg-class')
    school_str, schs, sche = extract_group(content, 'reg-prev-school')
    phone_str, phs, phe = extract_group(content, 'reg-parent-phone')
    email_str, ems, eme = extract_group(content, 'reg-email')
    
    # We want to replace the whole block of fields with the newly ordered block
    # Find the boundary of all these fields
    starts = [x for x in [ns, sus, secs, cls, schs, phs, ems] if x != -1]
    ends = [x for x in [ne, sue, sece, cle, sche, phe, eme] if x != -1]
    if not starts: continue
    
    min_start = min(starts)
    max_end = max(ends)
    
    # Also update the inner text of labels
    def update_label(html_str, label_text):
        if not html_str: return ""
        return re.sub(r'(<label[^>]*>).*?(</label>)', r'\g<1>' + label_text + r'\g<2>', html_str)
        
    name_str = update_label(name_str, "ŞAGİRDİN ADI")
    surname_str = update_label(surname_str, "ŞAGİRDİN SOYADI")
    school_str = update_label(school_str, "Hazırda təhsil aldığı təhsil müəssisəsi  ( bağça və məktəb)")
    class_str = update_label(class_str, "Müraciət etdiyi sinif")
    sector_str = update_label(sector_str, "Müraciət etdiyi bölmə")
    phone_str = update_label(phone_str, "VALİDEYNİN ƏLAQƏ NÖMRƏSİ")
    email_str = update_label(email_str, "MAİL ÜNVANI")
    
    new_fields = [name_str, surname_str, school_str, class_str, sector_str, phone_str, email_str]
    new_fields_str = '\n            '.join([f for f in new_fields if f])
    
    content = content[:min_start] + new_fields_str + content[max_end:]
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("HTML files updated")
