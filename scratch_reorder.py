import re

filepath = "/Users/gazanfaryusifli/Downloads/Evrika/index.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# We need to find the beginning of the swiper wrapper and the end of the swiper wrapper.
start_idx = content.find('<div class="swiper-wrapper">')
end_idx = content.find('</div>\n\n        </div>\n        <!-- Slider Navigation (gizli) -->')

if start_idx == -1 or end_idx == -1:
    print("Could not find swiper wrapper.")
    exit(1)

wrapper_inner = content[start_idx:end_idx]

# Let's extract the individual slides.
s1_start = wrapper_inner.find('<!-- Slide 1:')
s3_start = wrapper_inner.find('<!-- Slide 3:')
s4_start = wrapper_inner.find('<!-- Slide 4:')
s5_start = wrapper_inner.find('<!-- Slide 5:')
s6_start = wrapper_inner.find('<!-- Slide 6:')

slide_video = wrapper_inner[s1_start:s3_start]
slide_betl = wrapper_inner[s3_start:s4_start]
slide_montessori = wrapper_inner[s4_start:s5_start]
slide_eduhome = wrapper_inner[s5_start:s6_start]
slide_zumrud = wrapper_inner[s6_start:]

# Desired order:
# 1. Video
# 2. Montessori
# 3. BETL
# 4. Eduhome
# 5. Zumrud

new_wrapper_inner = (
    '<div class="swiper-wrapper">\n\n            ' +
    slide_video.strip() + '\n\n            ' +
    slide_montessori.strip() + '\n\n            ' +
    slide_betl.strip() + '\n\n            ' +
    slide_eduhome.strip() + '\n\n            ' +
    slide_zumrud.strip() + '\n\n          '
)

new_content = content[:start_idx] + new_wrapper_inner + content[end_idx:]

with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Reordered slides successfully.")
