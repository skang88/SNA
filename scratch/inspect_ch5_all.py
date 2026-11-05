with open('subnote/chapter5-원문.md', 'r', encoding='utf-8') as f:
    text = f.read()

raw_blocks = [b.strip() for b in text.split('\n\n') if b.strip()]
cleaned = [b for b in raw_blocks if b != '---' and not b.startswith('<!--')]
print(f"Total Chapter 5 blocks: {len(cleaned)}")

# Let's inspect blocks 6 to 30
for i in [5, 6, 7, 8, 11, 13, 14, 15, 20, 21, 22, 25, 27, 29]:
    print(f"=== Block {i+1} ===")
    print(cleaned[i][:180] + "...")
