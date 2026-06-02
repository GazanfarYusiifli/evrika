import re

def update_alert_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update static HTML alert
    old_static = '<strong>Diqqət:</strong> Qəbul imtahanında iştirak etmək və buraxılış kuponunu əldə etmək üçün <strong>25 AZN</strong> onlayn ödəniş tələb olunur.'
    new_static = """<strong>Diqqət:</strong> Qəbul imtahanında iştirak etmək və buraxılış kuponunu əldə etmək üçün onlayn ödəniş tələb olunur:<br>
              &bull; Məktəbəqədər - 25 AZN<br>
              &bull; 1-11 siniflər - 35 AZN"""
    content = content.replace(old_static, new_static)

    # We must also update the dynamic JS that overrides it, so it overrides with the same list!
    # Otherwise it will just show the single amount.
    old_dynamic = "'<strong>Diqqət:</strong> Qəbul imtahanında iştirak etmək və buraxılış kuponunu əldə etmək üçün <strong>' + amountText + '</strong> onlayn ödəniş tələb olunur.'"
    new_dynamic = "'<strong>Diqqət:</strong> Qəbul imtahanında iştirak etmək və buraxılış kuponunu əldə etmək üçün onlayn ödəniş tələb olunur:<br>&bull; Məktəbəqədər - 25 AZN<br>&bull; 1-11 siniflər - 35 AZN'"
    
    content = content.replace(old_dynamic, new_dynamic)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated list text in {filepath}")

for fp in ['register-lisey1.html', 'register-lisey2.html']:
    update_alert_text(fp)
