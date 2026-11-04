import re
import os

def parse_markdown(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    blocks = []
    # Split by double newlines or headers or tables
    raw_blocks = re.split(r'\n{2,}', text)
    for b in raw_blocks:
        b = b.strip()
        if not b:
            continue
        # Check if comment or hr
        if b == '---' or b.startswith('<!--'):
            continue
        blocks.append(b)
    return blocks

for i in range(1, 10):
    p = f"subnote/chapter{i}-원문.md"
    if os.path.exists(p):
        blocks = parse_markdown(p)
        print(f"Chapter {i}: {len(blocks)} blocks")
