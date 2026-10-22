"""Render Lebenslauf.html to PDF via headless Chrome and report the page count."""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(ROOT, "Lebenslauf.html")
PDF = os.path.join(ROOT, "Lebenslauf.pdf")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PROFILE = r"C:\Users\Admin\AppData\Local\Temp\opencode\chrome-cv"

if os.path.exists(PDF):
    os.remove(PDF)

cmd = [
    CHROME,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    f"--user-data-dir={PROFILE}",
    "--no-pdf-header-footer",
    f"--print-to-pdf={PDF}",
    "file:///" + HTML.replace("\\", "/"),
]
res = subprocess.run(cmd, capture_output=True, text=True, timeout=180)

if not os.path.exists(PDF):
    print("FAILED to produce PDF")
    print(res.stdout, res.stderr)
    sys.exit(1)

data = open(PDF, "rb").read()
pages = len(re.findall(rb"/Type\s*/Page[^s]", data))
print(f"OK {os.path.basename(PDF)}  {len(data)//1024}KB  pages={pages}")
sys.exit(0 if pages == 1 else 1)
