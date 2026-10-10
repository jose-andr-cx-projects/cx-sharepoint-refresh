#!/usr/bin/env python3
"""Stamp the Last updated field only in changed Markdown project documents."""
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
import re
import subprocess
import sys

stamp = datetime.now(ZoneInfo("Australia/Melbourne")).strftime("%-d %B %Y")
changed = sys.argv[1:]
for filename in changed:
    path = Path(filename)
    if path.suffix.lower() != ".md" or not path.is_file() or not path.is_relative_to("docs"):
        continue
    source = path.read_text(encoding="utf-8")
    # Only the header field is metadata. Don't change dates within meeting evidence.
    header, sep, remainder = source.partition("\n## ")
    if not re.search(r"(?m)^Last updated:\s*.+$", header):
        print(f"SKIP (no header Last updated field): {filename}")
        continue
    updated_header = re.sub(
        r"(?m)^Last updated:\s*.+$",
        "Last updated: " + stamp,
        header,
        count=1,
    )
    updated = updated_header + (sep + remainder if sep else "")
    if updated != source:
        path.write_text(updated, encoding="utf-8")
        print(f"STAMPED {filename}: {stamp}")
