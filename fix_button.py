import re

def fix_update_content():
    main_js_path = '/Users/gazanfaryusifli/Downloads/EvrikaProje/src/main.js'
    with open(main_js_path, 'r', encoding='utf-8') as f:
        js = f.read()

    # Find window.updateContent definition and append the button text update
    # The existing function looks like:
    # window.updateContent = function(lang) {
    #   document.querySelectorAll('[data-i18n]').forEach(el => {
    #     const key = el.getAttribute('data-i18n');
    #     if (translations[lang] && translations[lang][key]) {
    #       el.innerHTML = translations[lang][key];
    #     }
    #   });
    #   localStorage.setItem('evrika-lang', lang);
    #   document.documentElement.lang = lang;
    # };

    pattern = r"(window\.updateContent = function\(lang\) \{.*?(?=localStorage\.setItem))"
    # Actually, let's just do a simple replacement:
    
    old_code = """  localStorage.setItem('evrika-lang', lang);
  document.documentElement.lang = lang;
};"""

    new_code = """  localStorage.setItem('evrika-lang', lang);
  document.documentElement.lang = lang;
  
  // Update all language toggle buttons to show the correct selected language
  document.querySelectorAll('.lang-text').forEach(e => {
    e.innerText = lang.toUpperCase();
  });
};"""

    if old_code in js:
        js = js.replace(old_code, new_code)
    else:
        # Fallback if the code formatting is slightly different
        js = re.sub(
            r"localStorage\.setItem\('evrika-lang',\s*lang\);\s*document\.documentElement\.lang\s*=\s*lang;\s*\}",
            r"localStorage.setItem('evrika-lang', lang);\n  document.documentElement.lang = lang;\n  document.querySelectorAll('.lang-text').forEach(e => e.innerText = lang.toUpperCase());\n}",
            js
        )

    with open(main_js_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print("Fixed updateContent in main.js")

if __name__ == "__main__":
    fix_update_content()
