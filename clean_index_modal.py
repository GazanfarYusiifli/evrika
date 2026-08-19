import re

file = 'index.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the HTML block for welcomeModal
content = re.sub(r'<!-- Admission Welcome Modal -->.*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)

# Remove the JS logic for welcomeModal
content = re.sub(r'const welcomeModal = document\.getElementById\(\'welcomeModal\'\);.*?setTimeout\(\(\) => welcomeModal\.classList\.add\(\'active\'\), 10\);', '', content, flags=re.DOTALL)
content = re.sub(r'function closeWelcomeModal\(\) \{.*?\}', '', content, flags=re.DOTALL)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Hardcoded welcomeModal removed from index.html.")
