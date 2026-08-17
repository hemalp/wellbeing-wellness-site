#!/usr/bin/env python3
"""Generates soft placeholder images (branded, labeled) for every image
slot in the site, at the exact filenames the HTML expects. Replace these
with real photography using the SAME filenames and everything just works.
"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "images")
os.makedirs(OUT, exist_ok=True)

ACCENT = (138, 63, 31)       # #8A3F1F
ACCENT_SOFT = (234, 217, 206)  # #EAD9CE
CREAM = (251, 246, 241)      # #FBF6F1
BORDER = (229, 213, 200)     # #E5D5C8

def find_font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    for c in candidates:
        if os.path.exists(c):
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()

def placeholder(path, w, h, label, sublabel, circle=False):
    img = Image.new("RGB", (w, h), ACCENT_SOFT)
    draw = ImageDraw.Draw(img)

    # soft diagonal stripe texture
    stripe_gap = max(28, w // 22)
    for x in range(-h, w, stripe_gap):
        draw.line([(x, 0), (x + h, h)], fill=CREAM, width=max(2, stripe_gap // 8))

    if circle:
        mask = Image.new("L", (w, h), 0)
        mdraw = ImageDraw.Draw(mask)
        mdraw.ellipse((0, 0, w, h), fill=255)
        bg = Image.new("RGB", (w, h), ACCENT)
        img = Image.composite(bg, Image.new("RGB", (w, h), CREAM), mask)
        draw = ImageDraw.Draw(img)
        draw.ellipse((0, 0, w - 1, h - 1), outline=CREAM, width=max(2, w // 40))
    else:
        border_w = max(2, min(w, h) // 120)
        draw.rectangle([0, 0, w - 1, h - 1], outline=BORDER, width=border_w)

    # label text, centered
    label_size = max(16, min(w, h) // 12)
    sub_size = max(11, label_size // 2)
    font = find_font(label_size, bold=True)
    subfont = find_font(sub_size)

    text_color = CREAM if circle else ACCENT

    bbox = draw.textbbox((0, 0), label, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((w - tw) / 2, (h - th) / 2 - (sub_size if sublabel else 0)), label, fill=text_color, font=font)

    if sublabel:
        bbox2 = draw.textbbox((0, 0), sublabel, font=subfont)
        tw2, th2 = bbox2[2] - bbox2[0], bbox2[3] - bbox2[1]
        draw.text(((w - tw2) / 2, (h - th) / 2 + th + 6), sublabel, fill=text_color, font=subfont)

    img.save(path, quality=88)
    print("wrote", os.path.relpath(path, ROOT), f"{w}x{h}")

placeholder(os.path.join(OUT, "logo.png"), 200, 200, "LOGO", "replace me", circle=True)
placeholder(os.path.join(OUT, "hero.jpg"), 1200, 1300, "HERO PHOTO", "interior / clinician")
placeholder(os.path.join(OUT, "feature-1.jpg"), 900, 700, "FEATURE PHOTO 1", "Understanding Therapy")
placeholder(os.path.join(OUT, "feature-2.jpg"), 900, 700, "FEATURE PHOTO 2", "Answering Questions")
placeholder(os.path.join(OUT, "feature-3.jpg"), 900, 700, "FEATURE PHOTO 3", "Learning More")
placeholder(os.path.join(OUT, "team-yasmin.jpg"), 900, 1100, "TEAM PHOTO", "Yasmin Singh")
placeholder(os.path.join(OUT, "favicon.png"), 64, 64, "WB", "", circle=True)

print("\nDone. 7 placeholder images generated in /images.")
