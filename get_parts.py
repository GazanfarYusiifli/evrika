with open('victory.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("--- Niyə məhz section ---")
idx = html.find('Niyə məhz')
print(html[max(0, idx-200):idx+500])

print("\n--- Gələcəyi hədəfləyən ---")
idx2 = html.find('Gələcəyi hədəfləyən')
print(html[max(0, idx2-200):idx2+500])

print("\n--- Dünya Universitetlərinə Açılan Qapı ---")
idx3 = html.find('Dünya')
print(html[max(0, idx3-200):idx3+500])

