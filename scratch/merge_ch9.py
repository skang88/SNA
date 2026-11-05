import json

with open('scratch/ch9_part1.json', 'r', encoding='utf-8') as f:
    p1 = json.load(f)
with open('scratch/ch9_part2.json', 'r', encoding='utf-8') as f:
    p2 = json.load(f)

merged_ko = {}
merged_ko.update(p1)
merged_ko.update(p2)

assert len(merged_ko) == 87, f"Expected 87, got {len(merged_ko)}"

with open('subnote/chapter9-원문.md', 'r', encoding='utf-8') as f:
    text = f.read()

raw_blocks = [b.strip() for b in text.split('\n\n') if b.strip()]
cleaned_en = [b for b in raw_blocks if b != '---' and not b.startswith('<!--')]
assert len(cleaned_en) == 87, f"Expected 87, got {len(cleaned_en)}"

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
    elif en_b.startswith("#### "):
        btype = "h4"
    elif en_b.startswith("![") or "FIGURE 9." in en_b:
        btype = "image"
    elif en_b.startswith("|"):
        btype = "table"

    rows.append({
        "type": btype,
        "en": en_b,
        "ko": ko_b
    })

# Write JS Data
js_content = f"""window.CHAPTER_DATA = window.CHAPTER_DATA || {{}};
window.CHAPTER_DATA[9] = {{
  chapterNumber: 9,
  titleEn: "Chapter 9: The Family's Burden: Perceived Social Network Resources for Individual Disaster Assistance in Hazard-Prone Florida",
  titleKo: "제9장: 가족의 부담: 재난 취약 지역 플로리다에서 개인 재난 지원을 위한 지각된 사회적 네트워크 자원",
  rows: {json.dumps(rows, ensure_ascii=False, indent=2)}
}};"""

with open('translation/data/chapter9_data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

# Write Parallel Markdown
md_content = """# Chapter 9 대역본 (Original & Korean 1:1 Parallel Translation) - 100% 전수 완역본

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

total_en = sum(len(r['en']) for r in rows)
total_ko = sum(len(r['ko']) for r in rows)
print(f"Chapter 9 FULLY BUILT: {len(rows)} rows, EN: {total_en} chars, KO: {total_ko} chars, Ratio: {total_ko/total_en:.2f}")
