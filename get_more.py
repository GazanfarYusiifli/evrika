with open('victory.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("--- Hero BG ---")
idx = html.find('.hero-bg{')
print(html[max(0, idx-100):idx+300])

print("\n--- Reg Section ---")
idx2 = html.find('.reg-section{')
print(html[max(0, idx2-100):idx2+300])

print("\n--- About Glow ---")
idx3 = html.find('.about-glow{')
print(html[max(0, idx3-100):idx3+300])

