import re

with open('subnote/chapter9-원문.md', 'r', encoding='utf-8') as f:
    text = f.read()

raw = [b.strip() for b in text.split('\n\n') if b.strip()]
cleaned = [b for b in raw if b != '---' and not b.startswith('<!--')]

for i, b in enumerate(cleaned):
    if any(k in b for k in ['Table', 'FIGURE', 'Fig.', 'details', '```', 'image-']):
        print(f"[{i+1:02d}] {b[:80].replace(chr(10), ' ')}...")
