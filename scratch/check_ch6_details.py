import json

with open('translation/data/chapter6_data.js', 'r', encoding='utf-8') as f:
    content = f.read()
start = content.find("rows: [") + 6
end = content.rfind("]") + 1
rows = json.loads(content[start:end])

for i, r in enumerate(rows):
    if len(r['en']) > 400 and len(r['ko']) < len(r['en']) * 0.35:
        print(f"Row {i+1} short! EN: {len(r['en'])}, KO: {len(r['ko'])}")
        print(f"  EN: {r['en'][:120]}...")
        print(f"  KO: {r['ko'][:120]}...")
