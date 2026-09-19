import os
from PIL import Image

src_path = r"C:\Users\TTC\Documents\scrapbook-genz\static\assets\logo.png"
dest_dir = r"C:\Users\TTC\Documents\scrapbook-genz\static\assets"

img = Image.open(src_path).convert("RGBA")
w, h = img.size
print(f"Original image size: {w} x {h}")

# The image has:
# Top portion: Scrapbook + Polaroid symbol (approx y: 0.10*h to 0.52*h, x: 0.25*w to 0.75*w)
# Middle portion: MEMOUR text (approx y: 0.52*h to 0.72*h, x: 0.15*w to 0.85*w)
# Bottom portion: EVERY MEMORY HAS A STORY (approx y: 0.72*h to 0.85*h, x: 0.15*w to 0.85*w)

# Let's crop the icon (symbol)
# To find exact bounds, let's scan non-white pixels
# In this image, background is white (255, 255, 255)
def make_transparent(cropped_img, threshold=245):
    datas = cropped_img.getdata()
    new_data = []
    for item in datas:
        # If pixel is near white
        if item[0] > threshold and item[1] > threshold and item[2] > threshold:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
    cropped_img.putdata(new_data)
    return cropped_img

# Let's crop the icon:
# Top part: y from 0.08 to 0.53, x from 0.25 to 0.76
icon_box = (int(w * 0.26), int(h * 0.07), int(w * 0.76), int(h * 0.53))
icon_img = img.crop(icon_box)

# Auto trim border
# Get non-white bbox
def get_content_bbox(im, threshold=245):
    # Find bounding box of non-white pixels
    pixels = im.load()
    iw, ih = im.size
    min_x, min_y, max_x, max_y = iw, ih, 0, 0
    for y in range(ih):
        for x in range(iw):
            r, g, b, a = pixels[x, y]
            if not (r > threshold and g > threshold and b > threshold):
                if x < min_x: min_x = x
                if x > max_x: max_x = x
                if y < min_y: min_y = y
                if y > max_y: max_y = y
    if min_x < max_x and min_y < max_y:
        return (min_x, min_y, max_x + 1, max_y + 1)
    return (0, 0, iw, ih)

bbox_icon = get_content_bbox(icon_img)
icon_trimmed = icon_img.crop(bbox_icon)
icon_transparent = make_transparent(icon_trimmed.copy())

icon_out = os.path.join(dest_dir, "logo_icon.png")
icon_transparent.save(icon_out, "PNG")
print(f"Saved logo_icon.png: size {icon_transparent.size}")

# Let's crop the text MEMOUR
text_box = (int(w * 0.14), int(h * 0.52), int(w * 0.90), int(h * 0.73))
text_img = img.crop(text_box)
bbox_text = get_content_bbox(text_img)
text_trimmed = text_img.crop(bbox_text)
text_transparent = make_transparent(text_trimmed.copy())

text_out = os.path.join(dest_dir, "logo_text.png")
text_transparent.save(text_out, "PNG")
print(f"Saved logo_text.png: size {text_transparent.size}")

# Let's crop the slogan
slogan_box = (int(w * 0.14), int(h * 0.72), int(w * 0.90), int(h * 0.85))
slogan_img = img.crop(slogan_box)
bbox_slogan = get_content_bbox(slogan_img)
slogan_trimmed = slogan_img.crop(bbox_slogan)
slogan_transparent = make_transparent(slogan_trimmed.copy())

slogan_out = os.path.join(dest_dir, "logo_slogan.png")
slogan_transparent.save(slogan_out, "PNG")
print(f"Saved logo_slogan.png: size {slogan_transparent.size}")
