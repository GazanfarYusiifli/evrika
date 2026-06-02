import re

with open('lisey2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS
css_old = """    @media(min-width: 992px) {
      .montessori-bento-grid {
        grid-template-columns: 1fr;
      }
    }"""
css_new = """    @media(min-width: 992px) {
      .montessori-bento-grid {
        grid-template-columns: repeat(3, 1fr);
      }
    }"""

content = content.replace(css_old, css_new)
content = content.replace('grid-template-columns: 1fr;', 'grid-template-columns: repeat(1, 1fr);') # Initial is 1fr for mobile

# 2. Extract the grid and move it out of about-text-side
grid_start = content.find('<div class="montessori-bento-grid"')
grid_end = content.find('</div>\n          </div>\n<div class="about-img-side')

if grid_start != -1 and grid_end != -1:
    grid_html = content[grid_start:grid_end+6]
    
    # Remove the grid from current location
    content = content[:grid_start] + content[grid_end+6:]
    
    # Find the end of the about-wrap. 
    # Currently it is:
    #           </div>
    # <div class="about-img-side reveal-left">
    #             <div class="img-placeholder" style="padding:0; overflow:hidden; border-radius:40px; border:1px solid rgba(255,255,255,0.2); box-shadow: 0 40px 100px rgba(0,0,0,0.5); height: 500px;">
    #                <img src="assets/montessori-approach.jpg" style="width:100%; height:100%; object-fit:cover; display:block;" alt="Montessori Approach">
    #             </div>
    #           </div>
    #         </div>
    
    about_img_str = '<div class="about-img-side reveal-left">'
    about_img_idx = content.find(about_img_str)
    
    if about_img_idx != -1:
        # Find where the about-wrap closes
        wrap_close = content.find('</div>', content.find('</div>', content.find('</div>', about_img_idx) + 1) + 1)
        # Wait, inside about-img-side:
        # <div img-placeholder>
        #  <img>
        # </div>
        # </div> (closes about-img-side)
        # </div> (closes about-wrap)
        
        # Let's just use string replace for the exact tail of the block
        tail_str = """          </div>
<div class="about-img-side reveal-left">
            <div class="img-placeholder" style="padding:0; overflow:hidden; border-radius:40px; border:1px solid rgba(255,255,255,0.2); box-shadow: 0 40px 100px rgba(0,0,0,0.5); height: 500px;">
               <img src="assets/montessori-approach.jpg" style="width:100%; height:100%; object-fit:cover; display:block;" alt="Montessori Approach">
            </div>
          </div>
        </div>"""
        
        if tail_str in content:
            new_tail = tail_str + "\n\n        <!-- Full Width Bento Grid -->\n" + grid_html
            content = content.replace(tail_str, new_tail)
            
            with open('lisey2.html', 'w', encoding='utf-8') as f:
                f.write(content)
            print("Successfully moved grid and updated CSS.")
        else:
            print("Could not find tail_str to insert grid.")
    else:
        print("Could not find about-img-side.")
else:
    print("Could not find grid start or end.")

