import os
import glob
import re

widget_html = """
<!-- FLOATING E-JURNAL WIDGET -->
<style>
.floating-ejurnal {
    position: fixed;
    right: 0;
    top: 50%;
    transform: translateY(-50%);
    background: #1e3a8a;
    color: white;
    z-index: 9999;
    border-radius: 12px 0 0 12px;
    padding: 15px 12px;
    display: flex;
    flex-direction: column;
    gap: 15px;
    box-shadow: -4px 0 20px rgba(0,0,0,0.15);
    transition: all 0.3s ease;
    align-items: center;
    border: 1px solid rgba(255,255,255,0.1);
    border-right: none;
}
.floating-ejurnal-title {
    writing-mode: vertical-rl;
    text-orientation: mixed;
    transform: rotate(180deg);
    font-weight: 800;
    font-size: 0.95rem;
    letter-spacing: 2px;
    margin: 0;
    padding: 10px 0;
    color: #ffffff;
}
.floating-app-btn {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 45px;
    height: 45px;
    background: rgba(255,255,255,0.15);
    border-radius: 8px;
    color: white;
    text-decoration: none;
    font-size: 1.6rem;
    transition: all 0.3s ease;
}
.floating-app-btn:hover {
    background: white;
    color: #8B1A2B;
}
.floating-app-btn .qr-tooltip {
    position: absolute;
    right: 60px;
    top: 50%;
    transform: translateY(-50%) translateX(20px);
    background: white;
    padding: 12px;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    opacity: 0;
    visibility: hidden;
    transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
    border: 1px solid rgba(0,0,0,0.08);
}
.floating-app-btn .qr-tooltip::after {
    content: '';
    position: absolute;
    right: -8px;
    top: 50%;
    transform: translateY(-50%);
    border-width: 8px 0 8px 8px;
    border-style: solid;
    border-color: transparent transparent transparent white;
}
.floating-app-btn:hover .qr-tooltip {
    opacity: 1;
    visibility: visible;
    transform: translateY(-50%) translateX(0);
}
.floating-app-btn .qr-tooltip img {
    width: 100px;
    height: 100px;
    border-radius: 8px;
    object-fit: cover;
}
.floating-app-btn .qr-tooltip span {
    color: #333;
    font-size: 0.85rem;
    font-weight: 800;
    white-space: nowrap;
}

@media (max-width: 768px) {
    .floating-ejurnal {
        top: auto;
        bottom: 25px;
        right: 50%;
        transform: translateX(50%);
        flex-direction: row;
        border-radius: 50px;
        padding: 8px 15px;
        align-items: center;
        width: auto;
        border: 1px solid rgba(255,255,255,0.15);
        box-shadow: 0 10px 25px rgba(0,0,0,0.25);
    }
    .floating-ejurnal-title {
        writing-mode: horizontal-tb;
        transform: none;
        padding: 0;
        margin-right: 5px;
        font-size: 0.95rem;
    }
    .floating-app-btn {
        width: 40px;
        height: 40px;
        font-size: 1.3rem;
    }
    .floating-app-btn .qr-tooltip {
        display: none !important;
    }
}
</style>

<div class="floating-ejurnal">
    <div class="floating-ejurnal-title">E-JURNAL</div>
    <a href="#" class="floating-app-btn" title="Google Play">
        <i class="fab fa-google-play"></i>
        <div class="qr-tooltip">
            <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASwAAAEsAQMAAABDsxw2AAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAACK0lEQVRoge2ava3DMAyEaaRwmRE8ikezR9MoHiFlisB84p8UAwkQM3ndsQgM6XMjEscTHaLPYmELonk7rvBKkz9twLJYka2B6+525QcRc5lu40PfmG72IrA8Vo/6MUgWmO/C17gy7yRZuI2SIGDfY5KFux76LOkY2NIB7DcY6ZnvpCv3y9tkATuHhYbUM6eLCHJdsd3ySmqAncKiAy6qzMPxoXdAYCnsEKMrcy1yZnobwD7GNAsqyMx2+LUVusGoWu1iAiyLFTv8Z3vsRm5V/zZw2GNg57EaV7Ntc9uViHRY2QNLYrXItc3xOnd7rB3wqeyBZTEVirjciT2Wmn7Ki9Y/sCzWdlctaQ5fsYeGyIsbsCxWaklb49tI7fHq0qEro6sKsDxG4iLs0rHHivPkqgIsh+mVuds2NXKmIfrQeyKwLCZZ6LFwRLEt82/AcphpSD9zWXUNkdVm84BlsLjBVQ3x2i5ELS8H/wbsPOaDCDnqcBob0QsNAZbAlpiaLW3GHhJiI6A9bB6wDFZs/mC8p8OLXB1dTH6AZTGdPxz8m00k9HLH3HMELIW9mFsOUery4gYsibVYfATkvkIv0d4BgaWxhWNRfh/eAcf+v4iB23Ae2HmsyMH7GE392+rfkfunTwKWxyb/O0ShNrdsZW95MYMB7CtM73SHaidvhcB+g7l/C0cX1u5Q5MDOYa4hC8c0mEI6ZG55YWDfYGxhmPa7dneuCbLbNLB/xj6LPzkebqk2nc3qAAAAAElFTkSuQmCC" alt="Google Play QR">
            <span>Google Play</span>
        </div>
    </a>
    <a href="#" class="floating-app-btn" title="App Store">
        <i class="fab fa-apple"></i>
        <div class="qr-tooltip">
            <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASwAAAEsAQMAAABDsxw2AAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAAB0UlEQVRoge2au43DMAyGaVyRUiNkFI8mj+ZRPILLFEF04kuy7xAgDR0VPytF/JLmB58K0WeWixnR7VU///CBPz+J7u7bgAVjm4hRvffyopl59i5y81ClgMVjLM3uGu31sjz8i49JVAN2HSZi1UO9nMqSOGSAjYpR9a7s5USXJcSAXYbRIY5WPnNay/vbNAgsACtmiiWWhsXSIDIDFoz9McHkwD3YWwP2FUw15eLCtiZvzE7iAgvHWik5DilL4m9V10KW34BFYtxfWXusQ4p4Ww/mIQNsBKy0TkBCjCygWOXGAwvGtAc+i2W89clPAhaOsc2qkVUZ3XGZLUTkjRmwKCwfdimmyb17tQARARsDEymJLJtJWuPiou3xpJtJYMGYnIuutlQ17cf6msXzG7A4zLYr1Gt990rspOOOC1ggNrtYs4dMPi1+CdggmPRjbaIUcXW0VKylQWCRGHuSdmG2nDevmAz4G7BYrJvkt+KbRrJHEzFgY2DZ1OyvVxJZ+XRDwIKxLg3nt3TENMQI2AUYT/H+erX68+L/NAjsWoy86PtTO7AxMX3P8vymsrbxH1gc5vmNd1yzXN58SPFfABaNFVdE/w5RvNF60mlUBDYA9pn9AhnrKTqMZrz6AAAAAElFTkSuQmCC" alt="App Store QR">
            <span>App Store</span>
        </div>
    </a>
</div>
<!-- END FLOATING E-JURNAL WIDGET -->
"""

for file_path in glob.glob("*.html"):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip files that already have it
    if "<!-- FLOATING E-JURNAL WIDGET -->" in content:
        continue
        
    # Replace </body> with widget + </body>
    if "</body>" in content:
        new_content = content.replace("</body>", f"{widget_html}\n</body>")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Added to {file_path}")
    else:
        print(f"Warning: no </body> found in {file_path}")
