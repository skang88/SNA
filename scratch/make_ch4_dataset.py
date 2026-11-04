import json

with open('subnote/chapter4-원문.md', 'r', encoding='utf-8') as f:
    text = f.read()

raw_blocks = [b.strip() for b in text.split('\n\n') if b.strip()]
cleaned_en = [b for b in raw_blocks if b != '---' and not b.startswith('<!--')]
assert len(cleaned_en) == 96, f"Expected 96 blocks, got {len(cleaned_en)}"

# Let's inspect each block index to prepare Korean translations
print("Block count verified: 96")
