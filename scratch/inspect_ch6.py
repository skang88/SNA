import re

with open('subnote/chapter6-원문.md', 'r', encoding='utf-8') as f:
    text = f.read()

raw_blocks = [b.strip() for b in text.split('\n\n') if b.strip()]
cleaned = [b for b in raw_blocks if b != '---' and not b.startswith('<!--')]

print(f"Total cleaned blocks: {len(cleaned)}")
for i, b in enumerate(cleaned):
    preview = b.replace('\n', ' ')[:65]
    print(f"[{i+1}] {preview}")
