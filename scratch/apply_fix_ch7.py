import json

with open('scratch/ch7_fixed_p1.json', 'r', encoding='utf-8') as f:
    p1 = json.load(f)
with open('scratch/ch7_fixed_p2.json', 'r', encoding='utf-8') as f:
    p2 = json.load(f)
with open('scratch/ch7_fixed_p3.json', 'r', encoding='utf-8') as f:
    p3 = json.load(f)

merged = {}
merged.update(p1)
merged.update(p2)
merged.update(p3)

assert len(merged) == 105, f"Expected 105, got {len(merged)}"

with open('subnote/chapter7-원문.md', 'r', encoding='utf-8') as f:
    text = f.read()

raw = [b.strip() for b in text.split('\n\n') if b.strip()]
cleaned = [b for b in raw if b != '---' and not b.startswith('<!--')]
assert len(cleaned) == 105, f"Expected 105, got {len(cleaned)}"

rows = []
for idx in range(105):
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
    elif en_b.startswith("![") or "image-" in en_b:
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

# Write chapter7_data.js
js_content = f"""window.CHAPTER_DATA = window.CHAPTER_DATA || {{}};
window.CHAPTER_DATA[7] = {{
  chapterNumber: 7,
  titleEn: "Chapter 7: Shifts in Attention: Networked Dynamics of Twitter Communication During the Colorado Wildfires",
  titleKo: "제7장: 주의 집중의 이동: 콜로라도 산불 기간 동안 트위터 커뮤니케이션의 네트워크 역학",
  rows: {json.dumps(rows, ensure_ascii=False, indent=2)}
}};"""

with open('translation/data/chapter7_data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

# Write chapter7_대역.md
md_content = """# Chapter 7 대역본 (Original & Korean 1:1 Parallel Translation) - 100% 완전 전수 완역본

> **서지정보:** Almquist, Z. W., Spiro, E. S., & Butts, C. T. (2017). Chapter 7: Shifts in Attention: Modeling Follower Relationship Dynamics Among US Emergency Management-Related Organizations During a Colorado Wildfire. In *Social Network Analysis of Disaster Response, Recovery, and Adaptation* (pp. 107–130). Elsevier.

---

"""

for idx, r in enumerate(rows):
    md_content += f"### [단락 {idx+1}] {r['type'].upper()}\n\n"
    md_content += f"**[EN]**\n{r['en']}\n\n"
    md_content += f"**[KO]**\n{r['ko']}\n\n"
    md_content += "---\n\n"

with open('translation/chapter7_대역.md', 'w', encoding='utf-8') as f:
    f.write(md_content)

en_chars = sum(len(r['en']) for r in rows)
ko_chars = sum(len(r['ko']) for r in rows)
print(f"SUCCESS: Chapter 7 100% complete rebuilt! Rows: {len(rows)}, EN: {en_chars} chars, KO: {ko_chars} chars, Ratio: {ko_chars/en_chars:.2f}")
