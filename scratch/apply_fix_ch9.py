import json

# Load parts
with open('scratch/ch9_fixed_p1.json', 'r', encoding='utf-8') as f:
    p1 = json.load(f)
with open('scratch/ch9_fixed_p2.json', 'r', encoding='utf-8') as f:
    p2 = json.load(f)
with open('scratch/ch9_fixed_p3.json', 'r', encoding='utf-8') as f:
    p3 = json.load(f)

merged = {}
merged.update(p1)
merged.update(p2)
merged.update(p3)

assert len(merged) == 87, f"Expected 87, got {len(merged)}"

with open('subnote/chapter9-원문.md', 'r', encoding='utf-8') as f:
    text = f.read()

raw = [b.strip() for b in text.split('\n\n') if b.strip()]
cleaned = [b for b in raw if b != '---' and not b.startswith('<!--')]
assert len(cleaned) == 87, f"Expected 87, got {len(cleaned)}"

rows = []
for idx in range(87):
    en_b = cleaned[idx]
    ko_b = merged[str(idx + 1)]

    btype = "p"
    if idx == 0:
        btype = "title"
    elif idx in [1, 2]:
        btype = "meta"
    elif en_b.startswith("## "):
        btype = "h2"
    elif en_b.startswith("### "):
        btype = "h3"
    elif en_b.startswith("#### "):
        btype = "h4"
    elif en_b.startswith("![") or "FIGURE 9." in en_b or "Fig. 9." in en_b:
        btype = "image"
    elif en_b.startswith("|"):
        btype = "table"

    # Verify header correspondence
    if en_b.startswith("## ") and not ko_b.startswith("## "):
        raise ValueError(f"Mismatch at row {idx+1}: EN={en_b[:30]}, KO={ko_b[:30]}")

    rows.append({
        "type": btype,
        "en": en_b,
        "ko": ko_b
    })

# Write chapter9_data.js
js_content = f"""window.CHAPTER_DATA = window.CHAPTER_DATA || {{}};
window.CHAPTER_DATA[9] = {{
  chapterNumber: 9,
  titleEn: "Chapter 9: The Family's Burden: Perceived Social Network Resources for Individual Disaster Assistance in Hazard-Prone Florida",
  titleKo: "제9장: 가족의 부담: 재난 취약 지역 플로리다에서 개인 재난 지원을 위한 지각된 사회적 네트워크 자원",
  rows: {json.dumps(rows, ensure_ascii=False, indent=2)}
}};"""

with open('translation/data/chapter9_data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

# Write chapter9_대역.md
md_content = """# Chapter 9 대역본 (Original & Korean 1:1 Parallel Translation) - 100% 완전 전수 완역본

> **서지정보:** Meyer, M. A. (2017). Chapter 9: The Family's Burden: Perceived Social Network Resources for Individual Disaster Assistance in Hazard-Prone Florida. In *Social Network Analysis of Disaster Response, Recovery, and Adaptation* (pp. 151–171). Elsevier.

---

"""

for idx, r in enumerate(rows):
    md_content += f"### [단락 {idx+1}] {r['type'].upper()}\n\n"
    md_content += f"**[EN]**\n{r['en']}\n\n"
    md_content += f"**[KO]**\n{r['ko']}\n\n"
    md_content += "---\n\n"

with open('translation/chapter9_대역.md', 'w', encoding='utf-8') as f:
    f.write(md_content)

en_chars = sum(len(r['en']) for r in rows)
ko_chars = sum(len(r['ko']) for r in rows)
print(f"SUCCESS: Chapter 9 100% complete rebuilt! Rows: {len(rows)}, EN: {en_chars} chars, KO: {ko_chars} chars, Ratio: {ko_chars/en_chars:.2f}")
