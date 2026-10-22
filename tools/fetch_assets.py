"""Download RÉSIVO visual evidence and optimise it for the profile README."""
import os
import urllib.request

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets")
RAW = "https://raw.githubusercontent.com/anesdevv/residence-management-system/main/docs"

# (source relative to docs/, output name, max width)
ITEMS = [
    ("screenshots/web/dashboard-1440.png", "resivo-web.png", 1100),
    ("screenshots/web/dashboard-390.png", "resivo-mobile.png", 480),
    ("screenshots/desktop/00-overview-1280.png", "resivo-desktop.png", 1100),
    ("screenshots/desktop/03-rooms-1280.png", "resivo-rooms.png", 900),
    ("screenshots/desktop/04-maintenance-1280.png", "resivo-maintenance.png", 900),
    ("screenshots/desktop/06-official_list-1280.png", "resivo-roster.png", 900),
    ("resivo_logo_transparent.png", "resivo-logo.png", 420),
]

os.makedirs(OUT, exist_ok=True)

for src, dst, max_w in ITEMS:
    url = f"{RAW}/{src}"
    dest = os.path.join(OUT, dst)
    if os.path.exists(dest):
        print(f"skip  {dst} (exists)")
        continue
    req = urllib.request.Request(url, headers={"User-Agent": "opencode"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        raw = resp.read()
    tmp = dest + ".raw"
    with open(tmp, "wb") as fh:
        fh.write(raw)
    before = len(raw)
    with Image.open(tmp) as im:
        im = im.convert("RGBA")
        if im.width > max_w:
            h = round(im.height * max_w / im.width)
            im = im.resize((max_w, h), Image.LANCZOS)
        size = im.size
        im.save(dest, "PNG", optimize=True)
    os.remove(tmp)
    after = os.path.getsize(dest)
    print(f"ok    {dst}: {before/1024:.0f}KB -> {after/1024:.0f}KB  {size}")
