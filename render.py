"""Render the summary format (headings and paragraphs) as standalone RTL HTML."""
import argparse
from html import escape
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("summary", type=Path)
source = parser.parse_args().summary
if source.suffix.lower() != ".md":
    parser.error("Expected a Markdown file")
blocks = []
for line in source.read_text(encoding="utf-8-sig").splitlines():
    if not line.strip():
        continue
    tag = "p"
    for prefix, heading in [("## ", "h2"), ("# ", "h1")]:
        if line.startswith(prefix):
            tag = heading
            line = line[len(prefix):]
            break
    blocks.append(f"<{tag}>{escape(line)}</{tag}>")
header = """<!doctype html><html lang="he" dir="rtl"><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>סיכום פגישה</title><style>body{max-width:42rem;margin:3rem auto;padding:1rem;font:18px/1.6 Arial;color:#203449}h2{border-bottom:1px solid #ccd}</style><body>"""
source.with_suffix(".html").write_text(header + "\n".join(blocks) + "</body></html>", encoding="utf-8")
