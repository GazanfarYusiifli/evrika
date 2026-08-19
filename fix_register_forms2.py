import re
import os

files = [
    'register-lisey1.html',
    'register-lisey2.html',
    'register-montessori.html',
    'register-victory.html',
    'register-zumrud.html'
]

# We need to reorder the dyn-input-groups and change their labels.
# Current order in file is: name, surname, sector, class, school, phone, email.
# Wait, let's verify current order! In register-lisey1 it is:
# 1. mf_firstName
# 2. mf_lastName
# 3. mf_sector
# 4. mf_class
# 5. mf_previousSchool
# 6. mf_phoneNum
# 7. mf_email

def extract_groups(html):
    # This regex assumes standard formatting: <div class="dyn-input-group">...</div> ending before next <div class="dyn-input-group" or </div>\s*</div>
    # Actually, we can split by '<div class="dyn-input-group'
    parts = html.split('<div class="dyn-input-group')
    pre_form = parts[0]
    
    groups = []
    # parts[1:] are the groups, but the last part contains the rest of the file
    for i, p in enumerate(parts[1:]):
        group_html = '<div class="dyn-input-group' + p
        if i == len(parts[1:]) - 1:
            # The last part has the rest of the file after its closing div
            # Find the closing boundary for the last dyn-input-group
            # It ends before `<div class="payment-info-alert">` or `<button type="submit"`
            end_match = re.search(r'(<div class="payment-info-alert"|<button type="submit")', group_html)
            if end_match:
                end_idx = end_match.start()
                # we also need to step back over the closing </div> of dyn-form-grid
                end_idx = group_html.rfind('</div>', 0, end_idx)
                groups.append(group_html[:end_idx])
                post_form = group_html[end_idx:]
            else:
                groups.append(group_html)
                post_form = ""
        else:
            groups.append(group_html)
            
    return pre_form, groups, post_form

for f in files:
    if not os.path.exists(f): continue
    with open(f, 'r', encoding='utf-8') as file:
        html = file.read()
        
    pre, groups, post = extract_groups(html)
    
    # Identify groups by id
    g_map = {}
    for g in groups:
        if 'id="mf_firstName"' in g: g_map['name'] = g
        elif 'id="mf_lastName"' in g: g_map['surname'] = g
        elif 'id="mf_sector"' in g: g_map['sector'] = g
        elif 'id="mf_class"' in g: g_map['class'] = g
        elif 'id="mf_previousSchool"' in g: g_map['school'] = g
        elif 'id="mf_phoneNum"' in g: g_map['phone'] = g
        elif 'id="mf_email"' in g: g_map['email'] = g
        else:
            print("Unknown group found in", f)
            g_map['unknown'] = g
            
    # Apply new labels
    def update_label(html_str, label_text):
        if not html_str: return ""
        return re.sub(r'(<label[^>]*>).*?(</label>)', r'\g<1>' + label_text + r'\g<2>', html_str)
        
    g_map['name'] = update_label(g_map.get('name', ''), 'ŞAGİRDİN ADI')
    g_map['surname'] = update_label(g_map.get('surname', ''), 'ŞAGİRDİN SOYADI')
    g_map['school'] = update_label(g_map.get('school', ''), 'Hazırda təhsil aldığı təhsil müəssisəsi  ( bağça və məktəb)')
    g_map['class'] = update_label(g_map.get('class', ''), 'Müraciət etdiyi sinif')
    g_map['sector'] = update_label(g_map.get('sector', ''), 'Müraciət etdiyi bölmə')
    g_map['phone'] = update_label(g_map.get('phone', ''), 'VALİDEYNİN ƏLAQƏ NÖMRƏSİ')
    g_map['email'] = update_label(g_map.get('email', ''), 'MAİL ÜNVANI')

    # Desired order: name, surname, school, class, sector, phone, email
    ordered = [
        g_map.get('name'),
        g_map.get('surname'),
        g_map.get('school'),
        g_map.get('class'),
        g_map.get('sector'),
        g_map.get('phone'),
        g_map.get('email')
    ]
    
    ordered_clean = [g for g in ordered if g]
    new_html = pre + "".join(ordered_clean) + post
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_html)

print("HTML reordering done.")
