import re

with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

# I need to pass the correct index to viewDetails.
# Since payments is filtered from rawData, we can just find the index of the item in filteredData!
# Wait, filteredData might be different depending on search. It's better to find it dynamically.
# Let's add a global helper function:
helper_fn = """
    window.openFinanceDetails = (order_id) => {
        // find index in filteredData
        const idx = filteredData.findIndex(i => (i.id == order_id || i.order_id == order_id || (i.epoint_transaction && i.epoint_transaction == order_id)));
        if(idx >= 0) {
            viewDetails(idx);
        } else {
            // fallback to rawData
            const rIdx = rawData.findIndex(i => (i.id == order_id || i.order_id == order_id || (i.epoint_transaction && i.epoint_transaction == order_id)));
            if(rIdx >= 0) {
                // temporarily put it in filteredData to view
                filteredData.push(rawData[rIdx]);
                viewDetails(filteredData.length - 1);
            } else {
                alert('Detallar tapılmadı');
            }
        }
    };
"""

html = html.replace("window.viewDetails = (idx) => {", helper_fn + "\n    window.viewDetails = (idx) => {")

# Add the button to the Finance table
btn_html = """             <td>
                <div style="font-size:0.75rem; font-weight:800; color:white; text-transform:uppercase;">EPOINT MÜHƏRRİKİ</div>
                <div style="font-size:0.65rem; color:var(--success); margin-top:3px;"><i class="fas fa-check-circle"></i> Uğurlu</div>
              </td>
              <td>
                <button class="btn-view" style="padding:10px 15px; font-size:0.7rem; background:rgba(59,130,246,0.1); color:var(--royal-blue); border-color:rgba(59,130,246,0.2);" onclick="openFinanceDetails('${p.id || p.order_id || p.epoint_transaction}')"><i class="fas fa-eye" style="margin-right:5px;"></i> Detallar</button>
              </td>"""

html = re.sub(r'<td>\s*<div style="font-size:0\.75rem; font-weight:800; color:white; text-transform:uppercase;">EPOINT MÜHƏRRİKİ</div>\s*<div style="font-size:0\.65rem; color:var\(--success\); margin-top:3px;"><i class="fas fa-check-circle"></i> Uğurlu</div>\s*</td>\s*</tr>', btn_html + '\n            </tr>', html, flags=re.DOTALL)


# Also we need to add the <th>Detallar</th> in the header!
html = html.replace('<th>Sistem İcrası</th>', '<th>Sistem İcrası</th>\n                        <th>Əməliyyatlar</th>')


with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(html)
