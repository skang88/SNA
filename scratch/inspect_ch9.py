with open('subnote/chapter9-원문.md', 'r', encoding='utf-8') as f:
    text = f.read()

raw_blocks = [b.strip() for b in text.split('\n\n') if b.strip()]
cleaned = [b for b in raw_blocks if b != '---' and not b.startswith('<!--')]
print(f"Total Chapter 9 blocks: {len(cleaned)}")

for i in range(15):
    print(f"[{i+1}] {cleaned[i][:100]}...")
