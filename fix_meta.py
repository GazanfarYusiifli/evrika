import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # If it's index.html, replace the title
    if filepath == 'index.html':
        content = re.sub(
            r'<title>Evrika Təhsil Ekosistemi \| Gələcəyin Liderləri Üçün Premium Platforma</title>',
            r'<title>Evrika – gələcəyin liderlərini yetişdirən müasir təhsil ekosistemi.</title>',
            content
        )
        content = re.sub(
            r'<title>Evrika Təhsil Ekosistemi \| Gələcəyin Liderləri Üçün Premium Platforma</title>',
            r'<title>Evrika – gələcəyin liderlərini yetişdirən müasir təhsil ekosistemi.</title>',
            content,
            flags=re.IGNORECASE
        )

    # Function to replace the content of the meta tag
    def g_replace_meta(match):
        return match.group(1) + "Evrika – gələcəyin liderlərini yetişdirən müasir təhsil ekosistemi." + match.group(3)

    # Replace meta description if it exists
    if re.search(r'<meta[^>]*name=["\']description["\'][^>]*>', content, flags=re.IGNORECASE):
        # We also need to handle the case where content is before name
        content = re.sub(
            r'(<meta[^>]*content=["\'])([^"\']*)(["\'][^>]*name=["\']description["\'][^>]*>)',
            g_replace_meta,
            content,
            flags=re.IGNORECASE
        )
        content = re.sub(
            r'(<meta[^>]*name=["\']description["\'][^>]*content=["\'])([^"\']*)(["\'][^>]*>)',
            g_replace_meta,
            content,
            flags=re.IGNORECASE
        )
    else:
        # insert after <title>
        meta_tag = '\n    <meta name="description" content="Evrika – gələcəyin liderlərini yetişdirən müasir təhsil ekosistemi.">'
        if '<title>' in content:
            content = re.sub(r'(<title>.*?</title>)', r'\1' + meta_tag, content)
        elif '<head>' in content:
            content = re.sub(r'(<head>)', r'\1' + meta_tag, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
