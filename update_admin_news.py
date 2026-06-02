import re

filepath = 'admin.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Javascript functions for News management
news_js = """
// ----------------------------------------------------
// NEWS MANAGEMENT
// ----------------------------------------------------
let allNews = [];

async function fetchNews() {
    const tbody = document.getElementById('news-tbody');
    if (!tbody) return;
    try {
        const res = await fetch(`${API_URL}/news?select=*&order=id.desc`, {
            headers: { 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY }
        });
        if (res.ok) {
            allNews = await res.json();
            tbody.innerHTML = allNews.map(row => {
                const n = row.payload;
                return `<tr>
                    <td><img src="${n.img}" style="width:50px; height:50px; object-fit:cover; border-radius:8px;"></td>
                    <td><strong style="color:white;">${n.title}</strong></td>
                    <td style="color:var(--text-muted);">${n.date || '-'}</td>
                    <td>
                        <button class="btn-view" onclick="editNews('${row.id}')" style="padding:6px 12px; margin-right:5px; background:var(--royal-blue); border:none;"><i class="fas fa-edit"></i></button>
                        <button class="btn-view" onclick="deleteNews('${row.id}')" style="padding:6px 12px; background:var(--error); border:none;"><i class="fas fa-trash"></i></button>
                    </td>
                </tr>`;
            }).join('');
        }
    } catch (e) {
        console.error('Error fetching news:', e);
    }
}

async function handleNewsSubmit(e) {
    e.preventDefault();
    const id = document.getElementById('news-id').value;
    const title = document.getElementById('news-title').value;
    const img = document.getElementById('news-img').value;
    const text = document.getElementById('news-text').value;
    
    // Auto-generate date for new posts (e.g., "15.06.2026")
    const today = new Date();
    const dd = String(today.getDate()).padStart(2, '0');
    const mm = String(today.getMonth() + 1).padStart(2, '0');
    const yyyy = today.getFullYear();
    const dateStr = `${dd}.${mm}.${yyyy}`;

    const payloadData = { title, img, text, date: dateStr };
    
    const btn = document.getElementById('news-submit-btn');
    const originalText = btn.innerHTML;
    btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Gözləyin...';
    btn.disabled = true;

    try {
        let url = `${API_URL}/news`;
        let method = 'POST';
        
        if (id) {
            url += `?id=eq.${id}`;
            method = 'PATCH';
            // keep original date if editing? Actually easier to just overwrite or not fetch it. Let's let it overwrite or we can fetch original. 
            // For simplicity, we overwrite with today's date.
        }
        
        const res = await fetch(url, {
            method,
            headers: {
                'apikey': API_KEY,
                'Authorization': 'Bearer ' + API_KEY,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(id ? { payload: payloadData } : { payload: payloadData })
        });
        
        if (res.ok) {
            alert('Xəbər uğurla yadda saxlanıldı!');
            resetNewsForm();
            fetchNews();
        } else {
            alert('Xəta baş verdi!');
        }
    } catch (e) {
        alert('Xəta: ' + e.message);
    } finally {
        btn.innerHTML = originalText;
        btn.disabled = false;
    }
}

function editNews(id) {
    const item = allNews.find(x => String(x.id) === String(id));
    if (!item) return;
    const n = item.payload;
    
    document.getElementById('news-id').value = item.id;
    document.getElementById('news-title').value = n.title;
    document.getElementById('news-img').value = n.img;
    document.getElementById('news-text').value = n.text;
    
    document.getElementById('news-form-title').innerText = 'Xəbəri Redaktə Et';
    document.getElementById('news-submit-btn').innerHTML = 'Yenilə';
    document.getElementById('news-title').scrollIntoView({ behavior: 'smooth' });
}

function resetNewsForm() {
    document.getElementById('news-form').reset();
    document.getElementById('news-id').value = '';
    document.getElementById('news-form-title').innerText = 'Yeni Xəbər Paylaş';
    document.getElementById('news-submit-btn').innerHTML = 'Paylaş';
}

async function deleteNews(id) {
    if (!confirm('Silmək istədiyinizə əminsiniz?')) return;
    try {
        const res = await fetch(`${API_URL}/news?id=eq.${id}`, {
            method: 'DELETE',
            headers: { 'apikey': API_KEY, 'Authorization': 'Bearer ' + API_KEY }
        });
        if (res.ok) fetchNews();
    } catch (e) {
        alert('Xəta baş verdi: ' + e.message);
    }
}
"""

if "function handleNewsSubmit" not in content:
    # Let's insert it right before the last closing script tag
    last_script_close = content.rfind("</script>")
    if last_script_close != -1:
        content = content[:last_script_close] + news_js + content[last_script_close:]
    else:
        content += "\n<script>\n" + news_js + "\n</script>\n"
        
    # We also need to add `fetchNews()` to the `fetchData()` function if it exists, or just where switchTab('news') is triggered.
    # Let's add it to `switchTab`
    switch_tab_code = "if(tab === 'news') { fetchNews(); }"
    
    # Check if switchTab exists
    match = re.search(r'function switchTab\(tab\) \{([\s\S]*?)\}', content)
    if match and "fetchNews" not in match.group(1):
        content = content.replace(match.group(1), match.group(1) + f"\n    {switch_tab_code}\n")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Injected JS to admin.html")
else:
    print("JS already present in admin.html")

