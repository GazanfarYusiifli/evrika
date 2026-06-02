import re

with open('lisey2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Move the bento grid completely outside of the about-wrap.
# The grid starts at '<div class="montessori-bento-grid"' and ends at '</div>\n          </div>\n          <div class="about-img-side'
start_grid = content.find('<div class="montessori-bento-grid"')
end_grid = content.find('</div>\n          </div>\n          <div class="about-img-side')

if start_grid != -1 and end_grid != -1:
    grid_content = content[start_grid:end_grid+6] # include the closing </div> of the grid
    
    # We remove it from the current location
    content_without_grid = content[:start_grid] + content[end_grid+6:]
    
    # We want to place the grid right after the .about-wrap div finishes
    # The .about-wrap closes right after the about-img-side.
    # We can search for the end of about-wrap.
    # It looks like:
    # <div class="about-img-side reveal-left">
    #   <div class="img-placeholder" ...>
    #      <img ...>
    #   </div>
    # </div>
    # </div> (closing of about-wrap)
    
    # Let's find:
    about_img_str = '<div class="about-img-side reveal-left">'
    idx_img_start = content_without_grid.find(about_img_str)
    
    if idx_img_start != -1:
        # Find the end of this about-wrap block. It has 3 nested divs inside it roughly.
        # Actually it's simple: Just search for '</div>\n        </div>\n      </div>\n    </section>' or similar.
        # It's at the end of the section.
        end_of_section = content_without_grid.find('</section>', idx_img_start)
        
        # Insert the grid just before </section> inside the container.
        # Wait, the section ends right after the container.
        # Let's insert it just before '      </div>\n    </section>'
        container_end = content_without_grid.rfind('</div>', idx_img_start, end_of_section)
        
        # Wait, let's just do a simpler replace.
        # Update the grid CSS first:
        grid_content = grid_content.replace('grid-template-columns: 1fr;', 'grid-template-columns: 1fr;') # We'll handle @media
        # The CSS has:
        # @media(min-width: 992px) {
        #   .montessori-bento-grid {
        #     grid-template-columns: 1fr;
        #   }
        # }
        # Let's change it to:
        grid_content = grid_content.replace('grid-template-columns: 1fr;', 'grid-template-columns: repeat(3, 1fr);')
        
        # To be safe, find the exact insertion point. Let's look at the HTML structure around about-img-side
        # It goes:
        #           <div class="about-img-side reveal-left">
        #             <div class="img-placeholder" ...>
        #                <img src="assets/montessori-approach.jpg" ...>
        #             </div>
        #           </div>
        #         </div>
        #       </div>
        #     </section>
        
        insertion_target = '</div>\n        </div>\n      </div>\n    </section>'
        if insertion_target in content_without_grid:
            # We want to insert it inside the container.
            # </div> (closes about-wrap)
            # --> INSERT GRID HERE <--
            # </div> (closes container)
            # </section>
            
            replacement = '</div>\n        </div>\n' + grid_content + '\n      </div>\n    </section>'
            final_content = content_without_grid.replace(insertion_target, replacement)
            
            with open('lisey2.html', 'w', encoding='utf-8') as f:
                f.write(final_content)
            print("Successfully moved grid to full width and made it 3 columns.")
        else:
            print("Could not find insertion target.")
    else:
        print("Could not find about-img-side.")
else:
    print("Could not find start/end of grid.")

