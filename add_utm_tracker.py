import glob

html_files = glob.glob('*.html')

utm_script = """
<!-- UTM Tracker -->
<script>
(function() {
    var params = new URLSearchParams(window.location.search);
    var utms = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'];
    utms.forEach(function(utm) {
        if (params.has(utm)) {
            sessionStorage.setItem(utm, params.get(utm));
        }
    });
})();
</script>
<!-- End UTM Tracker -->
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    if "UTM Tracker" in content:
        continue

    content = content.replace('</head>', utm_script + '\n</head>')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Added UTM tracker to {file}")

