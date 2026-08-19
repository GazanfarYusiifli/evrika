import re

# Update lisey2.html
file1 = 'lisey2.html'
with open(file1, 'r', encoding='utf-8') as f:
    content1 = f.read()
content1 = content1.replace('(+994) 12 525 10 10', '(+994) 10 300 10 30')
with open(file1, 'w', encoding='utf-8') as f:
    f.write(content1)

# Update victory.html
file2 = 'victory.html'
with open(file2, 'r', encoding='utf-8') as f:
    content2 = f.read()
content2 = content2.replace('+994 55 519 99 32', '(+994) 10 233 75 55')
with open(file2, 'w', encoding='utf-8') as f:
    f.write(content2)

print("Footer phones updated.")
