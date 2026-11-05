import json

with open('scratch/ch5_part1.json', 'r', encoding='utf-8') as f:
    p1 = json.load(f)
with open('scratch/ch5_part2.json', 'r', encoding='utf-8') as f:
    p2 = json.load(f)
with open('scratch/ch5_part3.json', 'r', encoding='utf-8') as f:
    p3 = json.load(f)

merged_ko = {}
merged_ko.update(p1)
merged_ko.update(p2)
merged_ko.update(p3)

assert len(merged_ko) == 87, f"Expected 87, got {len(merged_ko)}"

with open('subnote/chapter5-원문.md', 'r', encoding='utf-8') as f:
    text = f.read()

raw_blocks = [b.strip() for b in text.split('\n\n') if b.strip()]
cleaned_en = [b for b in raw_blocks if b != '---' and not b.startswith('<!--')]
assert len(cleaned_en) == 87

rows = []
for idx in range(87):
    en_b = cleaned_en[idx]
    ko_b = merged_ko[str(idx + 1)]
    
    btype = "p"
    if idx == 0:
        btype = "title"
    elif idx in [1]:
        btype = "meta"
    elif en_b.startswith("## "):
        btype = "h2"
    elif en_b.startswith("### "):
        btype = "h3"
    elif en_b.startswith("![Table") or "Table 5." in en_b:
        if en_b.startswith("|"):
            btype = "table"
        elif en_b.startswith("!["):
            btype = "image"
    elif en_b.startswith("|"):
        btype = "table"

    rows.append({
        "type": btype,
        "en": en_b,
        "ko": ko_b
    })

# Write JS Data
js_content = f"window.CHAPTER_DATA = window.CHAPTER_DATA || {{}};\nwindow.CHAPTER_DATA[5] = {{\n  chapterNumber: 5,\n  titleEn: 'Chapter 5: Perspective Matters: The Challenges of Performance Measurement in Multisector, Multiorganizational Disaster Response Networks',\n  titleKo: '제5장: 관점의 중요성: 다부문·다조직 재난 대응 네트워크에서의 성과 측정 과제',\n  rows: {json.dumps(rows, ensure_ascii=False, indent=2)}\n}};"

with open('translation/data/chapter5_data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

# Write Parallel Markdown
md_content = """# Chapter 5 대역본 (Original & Korean 1:1 Parallel Translation) - 100% 전수 완역본

> **서지정보:** Nowell, B. L., Steelman, T. A., & Velez, A. L. (2017). Chapter 5: Perspective Matters: The Challenges of Performance Measurement in Multisector, Multiorganizational Disaster Response Networks. In *Social Network Analysis of Disaster Response, Recovery, and Adaptation* (pp. 59–84). Elsevier.

---

"""

for idx, r in enumerate(rows):
    md_content += f"### [단락 {idx+1}] {r['type'].upper()}\n\n"
    md_content += f"**[EN]**\n{r['en']}\n\n"
    md_content += f"**[KO]**\n{r['ko']}\n\n"
    md_content += "---\n\n"

with open('translation/chapter5_대역.md', 'w', encoding='utf-8') as f:
    f.write(md_content)

total_en = sum(len(r['en']) for r in rows)
total_ko = sum(len(r['ko']) for r in rows)
print(f"Chapter 5 FULLY RESTORED: {len(rows)} rows, EN: {total_en} chars, KO: {total_ko} chars, Ratio: {total_ko/total_en:.2f}")
