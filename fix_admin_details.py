import re

file = 'admin.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the Ad/Soyad split logic
split_logic = r"""      // Split name into Ad and Soyad
      if \(item\.name\) \{
          let parts = item\.name\.split\(' '\);
          if \(parts\.length > 1\) \{
              item\['Soyad'\] = parts\.pop\(\);
              item\['Ad'\] = parts\.join\(' '\);
          \} else \{
              item\['Ad'\] = item\.name;
          \}
          delete item\.name;
      \}"""
content = re.sub(split_logic, """      // Do not split name, keep as AD SOYAD
      if (item.name) {
          item['Ad Soyad'] = item.name;
          delete item.name;
      }""", content, count=1)

# 2. Map all 'DİGƏR / SİSTEM' items to 'ÖDƏNİŞ DETALLARI'
# Look for the final else block:
# } else {
#   groups['DİGƏR / SİSTEM'].push(dataPair);
# }
content = content.replace("groups['DİGƏR / SİSTEM'].push(dataPair);", "groups['ÖDƏNİŞ DETALLARI'].push(dataPair);")

# Remove the empty group 'DİGƏR / SİSTEM' from initialization
content = content.replace("'DİGƏR / SİSTEM': [],\n", "")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updates applied")
