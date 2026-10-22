"""Build a light-background badge variant of the RÉSIVO logo for GitHub dark theme."""
import os

from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "assets")

src = Image.open(os.path.join(ASSETS, "resivo-logo.png")).convert("RGBA")

PAD = 46
RADIUS = 28
CARD = (248, 250, 252, 255)  # slate-50

w, h = src.size
card = Image.new("RGBA", (w + PAD * 2, h + PAD * 2), (0, 0, 0, 0))
draw = ImageDraw.Draw(card)
draw.rounded_rectangle((0, 0, card.width - 1, card.height - 1), radius=RADIUS, fill=CARD)
draw.rounded_rectangle(
    (0, 0, card.width - 1, card.height - 1), radius=RADIUS, outline=(226, 232, 240, 255), width=2
)
card.alpha_composite(src, (PAD, PAD))

out = os.path.join(ASSETS, "resivo-logo-dark.png")
card.save(out, "PNG", optimize=True)
print(f"ok resivo-logo-dark.png {card.size} {os.path.getsize(out)//1024}KB")
