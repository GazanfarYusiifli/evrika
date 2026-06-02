with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("height: 240px !important;", "height: auto !important;\n              min-height: 460px !important;")
content = content.replace(".exp-card .expanded-info > div:nth-child(3) {\n              display: none !important;\n            }", ".exp-card .expanded-info > div:nth-child(3) {\n              display: block !important;\n              font-size: 0.95rem !important;\n            }")
content = content.replace("background: linear-gradient(to top, rgba(10, 20, 60, 0.82) 0%, rgba(10, 20, 60, 0.4) 60%, rgba(10, 20, 60, 0.15) 100%) !important;", "background: linear-gradient(to top, rgba(10, 20, 60, 0.95) 0%, rgba(10, 20, 60, 0.8) 50%, rgba(10, 20, 60, 0.4) 100%) !important;")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
