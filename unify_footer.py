import glob
import re

new_footer_body = """<footer class="site-footer" style="background: #070d1f; color: white; padding: 80px 0 40px; border-top: 1px solid rgba(255,255,255,0.05);">
  <div class="container" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 40px; justify-items: start; margin-bottom: 50px;">
    
    <!-- Column 1 -->
    <div class="footer-brand">
      <a class="logo" data-i18n="join-title1" href="index.html" style="color: var(--accent, #8B1A2B); font-size: 1.8rem; font-weight: 900; text-decoration: none; display: block; margin-bottom: 25px;">EVRİKA</a>
      <p style="color: rgba(255,255,255,0.6); line-height: 1.7; margin-bottom: 30px; font-size: 0.95rem; max-width: 320px;" data-i18n="footer-desc">Innovativ təhsil, qlobal gələcək. Biz şagirdlərimizin uğuru üçün hər gün çalışırıq.</p>
    </div>

    <!-- Column 2 -->
    <div class="footer-links">
      <h4 style="text-transform: uppercase; letter-spacing: 0.15em; margin-bottom: 30px; font-size: 0.9rem; font-weight: 800; color: var(--accent, #8B1A2B);" data-i18n="footer-nav">NAVİQASİYA</h4>
      <div style="display: flex; flex-direction: column; gap: 15px;">
        <a data-i18n="nav-home" href="index.html" style="color: rgba(255,255,255,0.6); text-decoration: none; font-size: 0.95rem; transition: 0.3s;" onmouseover="this.style.color='white'" onmouseout="this.style.color='rgba(255,255,255,0.6)'">Ana Səhifə</a>
        <a data-i18n="nav-about" href="about.html" style="color: rgba(255,255,255,0.6); text-decoration: none; font-size: 0.95rem; transition: 0.3s;" onmouseover="this.style.color='white'" onmouseout="this.style.color='rgba(255,255,255,0.6)'">Haqqımızda</a>
        <a data-i18n="nav-academic" href="schools.html" style="color: rgba(255,255,255,0.6); text-decoration: none; font-size: 0.95rem; transition: 0.3s;" onmouseover="this.style.color='white'" onmouseout="this.style.color='rgba(255,255,255,0.6)'">Akademik İstiqamətlər</a>
        <a data-i18n="nav-contact" href="contact.html" style="color: rgba(255,255,255,0.6); text-decoration: none; font-size: 0.95rem; transition: 0.3s;" onmouseover="this.style.color='white'" onmouseout="this.style.color='rgba(255,255,255,0.6)'">Əlaqə</a>
      </div>
    </div>

    <!-- Column 3 -->
    <div class="footer-contact">
      <h4 style="text-transform: uppercase; letter-spacing: 0.15em; margin-bottom: 30px; font-size: 0.9rem; font-weight: 800; color: var(--accent, #8B1A2B);" data-i18n="footer-contact">ƏLAQƏ</h4>
      <div style="display: flex; flex-direction: column; gap: 20px;">
        <div style="display: flex; gap: 15px; align-items: center;">
          <i class="fas fa-phone-alt" style="color: var(--accent, #8B1A2B);"></i>
          <span style="color: rgba(255,255,255,0.7); font-weight: 800; font-size: 1.1rem; letter-spacing: 0.05em;">(+994) 12 525 10 10</span>
        </div>
      </div>
    </div>

    <!-- Column 4 -->
    <div class="footer-apps">
      <h4 style="text-transform: uppercase; letter-spacing: 0.15em; margin-bottom: 30px; font-size: 0.9rem; font-weight: 800; color: var(--accent, #8B1A2B);">E- JURNAL</h4>
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
  </div>\n  <div class="footer-bottom\""""
# Note: we replaced up to `<div class="footer-bottom"`, so we must put it back exactly like that so the rest of the HTML connects.

counter = 0

for file_path in glob.glob("*.html"):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # The regex matches `<footer...>` up to `<div class="footer-bottom"` (including it)
    pattern = re.compile(r'<footer\s+class="site-footer".*?<div\s+class="footer-bottom"', re.DOTALL)
    
    match = pattern.search(content)
    if match:
        new_content = content[:match.start()] + new_footer_body + content[match.end():]
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Replaced perfectly in {file_path}")
        counter += 1
    else:
        # Fallback if footer doesn't have "site-footer"
        pattern2 = re.compile(r'<footer.*?<div\s+class="footer-bottom"', re.DOTALL)
        match2 = pattern2.search(content)
        if match2:
            new_content = content[:match2.start()] + new_footer_body + content[match2.end():]
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Replaced generic footer in {file_path}")
            counter += 1

print(f"Total HTML files updated with unified footer: {counter}")
