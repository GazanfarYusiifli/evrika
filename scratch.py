import os

def update_file(filename, old_subtitle, new_subtitle_html, main_color_hex, bright_color_hex, hover_color_hex, bg_gradient_rgb_str, nav_color):
    path = os.path.join("/Users/gazanfaryusifli/Downloads/Evrika", filename)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Update subtitle
    import re
    # We replace the text inside the <p class="subtitle-pro"...>...</p>
    content = re.sub(r'(<p class="subtitle-pro"[^>]*>\s*)' + old_subtitle + r'(\s*</p>)', r'\1' + new_subtitle_html + r'\2', content)

    # Update CSS colors
    content = content.replace("--burgundy: #8B1A2B;", f"--burgundy: {main_color_hex};")
    content = content.replace("--burgundy-bright: #b32a3e;", f"--burgundy-bright: {bright_color_hex};")
    
    # Update RGBA in vibrant-bg
    content = content.replace("rgba(139, 26, 43, 0.3)", f"rgba({bg_gradient_rgb_str}, 0.3)")
    content = content.replace("rgba(139, 26, 43, 0.2)", f"rgba({bg_gradient_rgb_str}, 0.2)")
    content = content.replace("rgba(139, 26, 43, 0.05)", f"rgba({bg_gradient_rgb_str}, 0.05)")
    content = content.replace("rgba(139, 26, 43, 0.5)", f"rgba({bg_gradient_rgb_str}, 0.5)")

    # Update button gradient end color #63121f (which is darker burgundy)
    content = content.replace("#63121f", hover_color_hex)
    
    # Background color #050a18 to something matching the navy of each
    content = content.replace("#050a18", nav_color)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# eduhome: yellow/gold 
# --accent:#eab308; rgb(234, 179, 8)
update_file("register-victory.html", "Eduhome Center", "Eduhome<br>Təhsil<br>Mərkəzi", "#eab308", "#fef08a", "#a17902", "234, 179, 8", "#0a0a05")

# zumrud: green
# --accent:#16a34a; rgb(22, 163, 74)
update_file("register-zumrud.html", "Zümrüd Bağçası", "Zümrüd<br>Women<br>Club", "#16a34a", "#4ade80", "#0e6b30", "22, 163, 74", "#050c08")

# montessori: soft green/olive
# --accent: #9ca476; rgb(156, 164, 118)
update_file("register-montessori.html", "Montessori Kids", "Evrika Montessori Kids Academy", "#9ca476", "#b0b985", "#6c734e", "156, 164, 118", "#0a0d0f")

print("Done")
