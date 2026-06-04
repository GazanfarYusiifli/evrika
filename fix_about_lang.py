import re

def fix_about():
    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/about.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # AZ
    html = html.replace(
        "e.innerText='AZ'); this.parentElement",
        "e.innerText='AZ'); window.updateContent('az'); this.parentElement"
    )
    # EN
    html = html.replace(
        "e.innerText='EN'); this.parentElement",
        "e.innerText='EN'); window.updateContent('en'); this.parentElement"
    )
    # RU
    html = html.replace(
        "e.innerText='RU'); this.parentElement",
        "e.innerText='RU'); window.updateContent('ru'); this.parentElement"
    )

    with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/about.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    fix_about()
    print("Fixed about.html language switcher")
