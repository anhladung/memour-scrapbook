import os
from PIL import Image

dest_dir = r"C:\Users\TTC\Documents\scrapbook-genz\static\assets"

icon = Image.open(os.path.join(dest_dir, "logo_icon.png")).convert("RGBA")
text = Image.open(os.path.join(dest_dir, "logo_text.png")).convert("RGBA")
slogan = Image.open(os.path.join(dest_dir, "logo_slogan.png")).convert("RGBA")

# We want: Icon on left, Text on right, Slogan underneath Text.
# Icon is 1.5x the height of the text block!
# Let's say text height is 60px
target_text_h = 60
target_text_w = int(text.width * (target_text_h / text.height))
resized_text = text.resize((target_text_w, target_text_h), Image.Resampling.LANCZOS)

# Slogan height approx 14px
target_slogan_h = 13
target_slogan_w = int(slogan.width * (target_slogan_h / slogan.height))
if target_slogan_w > target_text_w:
    target_slogan_w = target_text_w
    target_slogan_h = int(slogan.height * (target_slogan_w / slogan.width))
resized_slogan = slogan.resize((target_slogan_w, target_slogan_h), Image.Resampling.LANCZOS)

# Right block total height: text_h (60) + gap (6) + slogan_h (13) = ~79px
right_block_h = target_text_h + 6 + target_slogan_h

# Icon height = 1.5 * text_h = 1.5 * 60 = 90px
target_icon_h = int(target_text_h * 1.5)
target_icon_w = int(icon.width * (target_icon_h / icon.height))
resized_icon = icon.resize((target_icon_w, target_icon_h), Image.Resampling.LANCZOS)

total_w = target_icon_w + 16 + max(target_text_w, target_slogan_w)
total_h = max(target_icon_h, right_block_h)

# Canvas with transparent background
canvas = Image.new("RGBA", (total_w, total_h), (255, 255, 255, 0))

# Paste icon on left (centered vertically)
icon_y = (total_h - target_icon_h) // 2
canvas.paste(resized_icon, (0, icon_y), resized_icon)

# Paste right block (centered vertically or aligned nicely)
right_x = target_icon_w + 16
right_y = (total_h - right_block_h) // 2

canvas.paste(resized_text, (right_x, right_y), resized_text)
slogan_y = right_y + target_text_h + 6
canvas.paste(resized_slogan, (right_x, slogan_y), resized_slogan)

out_path = os.path.join(dest_dir, "logo_horizontal.png")
canvas.save(out_path, "PNG")
print(f"Generated logo_horizontal.png: size {canvas.size}")
