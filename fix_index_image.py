with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Line 662 is 661 in 0-indexed. Let's do it safely by searching for "Entity 4" and replacing the next background-image.
for i in range(len(lines)):
    if '<!-- Entity 4: Victory Colleges' in lines[i]:
        # find the next line with exp-bg
        for j in range(i, i+5):
            if 'exp-bg' in lines[j] and 'sekill3.jpeg' in lines[j]:
                lines[j] = lines[j].replace('sekill3.jpeg', 'sekill2.jpeg')
                break
        break

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Updated Entity 4 image to sekill2.jpeg in index.html")
