import re

with open('subnote/chapter4-원문.md', 'r', encoding='utf-8') as f:
    text = f.read()

raw_blocks = [b.strip() for b in text.split('\n\n') if b.strip()]

cleaned = []
for idx, b in enumerate(raw_blocks):
    if b == '---' or b.startswith('<!--'):
        continue
    cleaned.append((idx, b))

print(f"Total cleaned blocks: {len(cleaned)}")
for i, (orig_idx, b) in enumerate(cleaned):
    preview = b.replace('\n', ' ')[:70]
    print(f"[{i+1}] ({len(b)} chars): {preview}...")
