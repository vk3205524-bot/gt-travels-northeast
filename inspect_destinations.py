"""
Find the clean markers and ensure no duplicated state sections exist.
"""
import re

DEST_FILE = r"c:\Users\vk320\Downloads\tourism\destinations.html"

with open(DEST_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# Let's find all occurrences of <div class="state-section"
matches = list(re.finditer(r'<div class="state-section"[^>]*id="([^"]+)"', content))
print(f"Found {len(matches)} state sections:")
for m in matches:
    print(f"  id='{m.group(1)}' at pos {m.start()}")

