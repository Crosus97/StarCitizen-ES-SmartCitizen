"""Replace Smart Citizen's credit line in Frontend_PU_Version with our own.

Smart Citizen appends "\\nLocalizations Enhanced with Smart Citizen vX.Y.Z" to
Frontend_PU_Version when it applies enhancements. This rewrites that suffix
(keeping the Smart Citizen version number) and leaves every other byte of the
file untouched (BOM, CRLF line endings, key order).

Idempotent: running it on an already-branded file changes nothing.

Usage: python scripts/branding.py live/global.ini
"""
import re
import sys
from pathlib import Path

BRAND = "Traducción ES by Crosus · Thord82 + Smart Citizen {version}"

path = Path(sys.argv[1] if len(sys.argv) > 1 else "live/global.ini")
data = path.read_bytes()

line_re = re.compile(rb"(^|\n)(Frontend_PU_Version=)([^\r\n]*)", re.MULTILINE)
m = line_re.search(data)
if not m:
    sys.exit("Frontend_PU_Version not found")

value = m.group(3).decode("utf-8")
sc = re.search(r"\\nLocalizations Enhanced with Smart Citizen (v[\d.]+)\s*$", value)
if not sc:
    print("No Smart Citizen credit line found; nothing to do.")
    sys.exit(0)

new_value = value[: sc.start()] + "\\n" + BRAND.format(version=sc.group(1))
new_data = data[: m.start(3)] + new_value.encode("utf-8") + data[m.end(3):]
path.write_bytes(new_data)
print(f"Frontend_PU_Version: {value!r} -> {new_value!r}")
