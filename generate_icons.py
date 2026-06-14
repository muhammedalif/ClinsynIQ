"""
ClinsynIQ Icon Generator
Run: python3 generate_icons.py
Requires: pip install Pillow
"""

from PIL import Image, ImageDraw, ImageFont
import os

def draw_icon(size):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    pad = int(size * 0.08)
    r = int(size * 0.22)  # corner radius

    # Background gradient simulation (dark navy)
    bg = (6, 13, 26, 255)
    draw.rounded_rectangle([pad, pad, size - pad, size - pad],
                            radius=r, fill=bg)

    # Blue accent strip (top-left edge)
    accent = (14, 165, 233, 255)
    strip_w = int(size * 0.12)
    draw.rounded_rectangle([pad, pad, pad + strip_w, size - pad],
                            radius=r, fill=(13, 110, 180, 255))

    # Inner card background
    inner = (18, 31, 52, 255)
    ip = int(size * 0.16)
    ir = int(size * 0.14)
    draw.rounded_rectangle([ip, ip, size - ip, size - ip],
                            radius=ir, fill=inner)

    # Text "CIQ"
    text_y = int(size * 0.32)
    font_size = int(size * 0.28)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except:
        font = ImageFont.load_default()

    # "C" in white
    cx = int(size * 0.22)
    draw.text((cx, text_y), "C", fill=(225, 235, 245, 255), font=font)

    # "IQ" in accent blue
    small_size = int(size * 0.18)
    try:
        font_sm = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", small_size)
    except:
        font_sm = font
    draw.text((int(size * 0.50), int(text_y + size * 0.09)),
              "IQ", fill=accent, font=font_sm)

    # Bottom label "HealthionX" (small, only for large icon)
    if size >= 512:
        label_size = int(size * 0.055)
        try:
            font_lbl = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", label_size)
        except:
            font_lbl = font_sm
        draw.text((int(size * 0.20), int(size * 0.74)),
                  "HealthionX", fill=(90, 122, 154, 255), font=font_lbl)

    return img


os.makedirs('icons', exist_ok=True)

for sz in [192, 512]:
    icon = draw_icon(sz)
    icon.save(f'icons/icon-{sz}.png')
    print(f'✅ icons/icon-{sz}.png created')

print('\nAll icons generated. Upload the icons/ folder to your GitHub repo.')
