with open('subnote/chapter6-원문.md', 'r', encoding='utf-8') as f:
    text = f.read()

raw_blocks = [b.strip() for b in text.split('\n\n') if b.strip()]
cleaned = [b for b in raw_blocks if b != '---' and not b.startswith('<!--')]
print(f"Total Chapter 6 blocks: {len(cleaned)}")

# preview blocks
for i in [5, 6, 7, 10, 12, 13, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 31, 32, 33]:
    print(f"=== Block {i+1} ===")
    print(cleaned[i][:170] + "...")
