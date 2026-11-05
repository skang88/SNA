with open('subnote/chapter7-원문.md', 'r', encoding='utf-8') as f:
    text = f.read()

raw_blocks = [b.strip() for b in text.split('\n\n') if b.strip()]
cleaned = [b for b in raw_blocks if b != '---' and not b.startswith('<!--')]

for i in range(70, len(cleaned)):
    print(f"--- Block {i+1} ---")
    print(cleaned[i][:140] + "...")
