import json

with open('translation/data/chapter4_data.js', 'r', encoding='utf-8') as f:
    content = f.read()
start = content.find("rows: [") + 6
end = content.rfind("]") + 1
rows = json.loads(content[start:end])

for i in [6, 8, 11, 22, 23, 33, 40, 51, 62, 70, 78]:
    r = rows[i]
    print(f"=== Row {i+1} ({r['type']}) ===")
    print(f"[EN len: {len(r['en'])}]\n{r['en'][:200]}...")
    print(f"[KO len: {len(r['ko'])}]\n{r['ko']}")
    print()
