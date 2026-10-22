"""Attach discovery topics to the projects that matter for an Ausbildung application."""
import json
import subprocess
import sys

TOPICS = {
    "residence-management-system": [
        "resivo", "studentenwohnheim", "university-residence", "astro", "pyside6", "qt6",
        "supabase", "postgresql", "plpgsql", "typescript", "tailwindcss", "mcp",
        "cloudflare-workers", "rls", "dashboard", "verwaltungssystem", "fachinformatiker", "ausbildung",
    ],
    "ulvic-admin-panel": [
        "ulvic-console", "ulvik-print", "inventory", "ledger", "kpi", "accounting",
        "react", "typescript", "supabase", "dashboard", "algeria", "daten-und-prozessanalyse",
    ],
    "ulvik-print": [
        "e-commerce", "react", "typescript", "vite", "tailwindcss", "supabase",
        "algeria", "custom-printing", "anwendungsentwicklung",
    ],
    "flow-voice": [
        "flowvoice", "whisper", "offline", "electron", "dictation", "privacy", "local-first",
        "speech-to-text", "python", "javascript", "desktop", "systemintegration",
    ],
    "anes-journey": [
        "flutter", "dart", "productivity", "habits", "supabase", "mobile",
        "anwendungsentwicklung",
    ],
    "lycee-yaghmouracen": [
        "python", "pyside6", "qt6", "sqlite", "pytest", "school-management",
        "desktop", "verwaltungssystem", "daten-und-prozessanalyse",
    ],
    "infinite-xo": ["game", "typescript", "tic-tac-toe", "browser-game", "web-game"],
}

failures = []
for repo, names in TOPICS.items():
    payload = json.dumps({"names": names})
    res = subprocess.run(
        ["gh", "api", "--method", "PUT", f"repos/anesdevv/{repo}/topics", "--input", "-"],
        input=payload, capture_output=True, text=True, timeout=120,
    )
    if res.returncode == 0:
        print(f"ok   {repo}: {len(names)} topics")
    else:
        failures.append(repo)
        print(f"FAIL {repo}: {res.stderr.strip()}")

sys.exit(1 if failures else 0)
