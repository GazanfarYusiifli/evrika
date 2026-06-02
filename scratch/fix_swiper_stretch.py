with open("src/style.css", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace('.heroSwiper {\n  width: 100%;\n  height: 100%;\n}', '.heroSwiper {\n  position: absolute;\n  inset: 0;\n  width: 100%;\n  height: 100%;\n}')

with open("src/style.css", "w", encoding="utf-8") as f:
    f.write(content)
