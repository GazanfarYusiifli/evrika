import os
import glob
import re

footer_apps_html = """
<div class="footer-apps" style="margin-left: auto;">
<h4 style="text-transform: uppercase; letter-spacing: 0.15em; margin-bottom: 30px; font-size: 0.9rem; font-weight: 800; color: var(--accent, #8B1A2B);">E- Jurnal</h4>
<div style="display: flex; gap: 15px;">
  <div style="text-align: center;">
    <a href="https://play.google.com/store/apps/details?id=com.ibp.evrika&pcampaignid=web_share" target="_blank">
      <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASwAAAEsAQMAAABDsxw2AAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAACK0lEQVRoge2ava3DMAyEaaRwmRE8ikezR9MoHiFlisB84p8UAwkQM3ndsQgM6XMjEscTHaLPYmELonk7rvBKkz9twLJYka2B6+525QcRc5lu40PfmG72IrA8Vo/6MUgWmO/C17gy7yRZuI2SIGDfY5KFux76LOkY2NIB7DcY6ZnvpCv3y9tkATuHhYbUM6eLCHJdsd3ySmqAncKiAy6qzMPxoXdAYCnsEKMrcy1yZnobwD7GNAsqyMx2+LUVusGoWu1iAiyLFTv8Z3vsRm5V/zZw2GNg57EaV7Ntc9uViHRY2QNLYrXItc3xOnd7rB3wqeyBZTEVirjciT2Wmn7Ki9Y/sCzWdlctaQ5fsYeGyIsbsCxWaklb49tI7fHq0qEro6sKsDxG4iLs0rHHivPkqgIsh+mVuds2NXKmIfrQeyKwLCZZ6LFwRLEt82/AcphpSD9zWXUNkdVm84BlsLjBVQ3x2i5ELS8H/wbsPOaDCDnqcBob0QsNAZbAlpiaLW3GHhJiI6A9bB6wDFZs/mC8p8OLXB1dTH6AZTGdPxz8m00k9HLH3HMELIW9mFsOUery4gYsibVYfATkvkIv0d4BgaWxhWNRfh/eAcf+v4iB23Ae2HmsyMH7GE392+rfkfunTwKWxyb/O0ShNrdsZW95MYMB7CtM73SHaidvhcB+g7l/C0cX1u5Q5MDOYa4hC8c0mEI6ZG55YWDfYGxhmPa7dneuCbLbNLB/xj6LPzkebqk2nc3qAAAAAElFTkSuQmCC" alt="Google Play QR" style="width: 100px; height: 100px; background: white; padding: 5px; border-radius: 8px;">
    </a>
    <div style="font-size: 0.75rem; color: rgba(255,255,255,0.6); margin-top: 8px;">Google Play</div>
  </div>
  <div style="text-align: center;">
    <a href="https://apps.apple.com/az/app/e-evrika/id6743225913" target="_blank">
      <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASwAAAEsAQMAAABDsxw2AAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAAB0UlEQVRoge2au43DMAyGaVyRUiNkFI8mj+ZRPILLFEF04kuy7xAgDR0VPytF/JLmB58K0WeWixnR7VU///CBPz+J7u7bgAVjm4hRvffyopl59i5y81ClgMVjLM3uGu31sjz8i49JVAN2HSZi1UO9nMqSOGSAjYpR9a7s5USXJcSAXYbRIY5WPnNay/vbNAgsACtmiiWWhsXSIDIDFoz9McHkwD3YWwP2FUw15eLCtiZvzE7iAgvHWik5DilL4m9V10KW34BFYtxfWXusQ4p4Ww/mIQNsBKy0TkBCjCygWOXGAwvGtAc+i2W89clPAhaOsc2qkVUZ3XGZLUTkjRmwKCwfdimmyb17tQARARsDEymJLJtJWuPiou3xpJtJYMGYnIuutlQ17cf6msXzG7A4zLYr1Gt990rspOOOC1ggNrtYs4dMPi1+CdggmPRjbaIUcXW0VKylQWCRGHuSdmG2nDevmAz4G7BYrJvkt+KbRrJHEzFgY2DZ1OyvVxJZ+XRDwIKxLg3nt3TENMQI2AUYT/H+erX68+L/NAjsWoy86PtTO7AxMX3P8vymsrbxH1gc5vmNd1yzXN58SPFfABaNFVdE/w5RvNF60mlUBDYA9pn9AhnrKTqMZrz6AAAAAElFTkSuQmCC" alt="App Store QR" style="width: 100px; height: 100px; background: white; padding: 5px; border-radius: 8px;">
    </a>
    <div style="font-size: 0.75rem; color: rgba(255,255,255,0.6); margin-top: 8px;">App Store</div>
  </div>
</div>
</div>
"""

# Update style.css
with open("src/style.css", "a", encoding="utf-8") as f:
    f.write("\n\n/* Mobile responsive override for E-Jurnal in footer */\n")
    f.write("@media (max-width: 768px) {\n")
    f.write("  .footer-apps {\n")
    f.write("    margin-left: 0 !important;\n")
    f.write("    width: 100%;\n")
    f.write("    display: flex;\n")
    f.write("    flex-direction: column;\n")
    f.write("    align-items: center;\n")
    f.write("    text-align: center;\n")
    f.write("    margin-top: 20px;\n")
    f.write("  }\n")
    f.write("}\n")

for file_path in glob.glob("*.html"):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Clear old footer-apps that might be existing from manually adding
    content = re.sub(r'<div class="footer-apps".*?App Store</div>\s*</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
    
    # We find the container closure.
    # The structure: </div>\n<div class="footer-bottom"
    pattern = re.compile(r'(</div>\s*)(<div class="footer-bottom")')
    match = pattern.search(content)
    if match:
        content = content[:match.start()] + "\n" + footer_apps_html + "\n" + match.group(1) + match.group(2) + content[match.end():]
        print(f"Updated {file_path}")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
    else:
        print(f"Skipped {file_path}")
