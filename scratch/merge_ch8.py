import json

with open('scratch/ch8_part1.json', 'r', encoding='utf-8') as f:
    p1 = json.load(f)
with open('scratch/ch8_part2.json', 'r', encoding='utf-8') as f:
    p2 = json.load(f)

merged_ko = {}
merged_ko.update(p1)
merged_ko.update(p2)

assert len(merged_ko) == 64, f"Expected 64, got {len(merged_ko)}"

with open('subnote/chapter8-원문.md', 'r', encoding='utf-8') as f:
    text = f.read()

raw_blocks = [b.strip() for b in text.split('\n\n') if b.strip()]
cleaned_en = [b for b in raw_blocks if b != '---' and not b.startswith('<!--')]
assert len(cleaned_en) == 64

rows = []
for idx in range(64):
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
    elif en_b.startswith("![") or "FIGURE 8." in en_b:
        btype = "image"
    elif en_b.startswith("|"):
        btype = "table"

    rows.append({
        "type": btype,
        "en": en_b,
        "ko": ko_b
    })

# Write JS Data
js_content = f"window.CHAPTER_DATA = window.CHAPTER_DATA || {{}};\nwindow.CHAPTER_DATA[8] = {{\n  chapterNumber: 8,\n  titleEn: 'Chapter 8: The Effect of Hurricane Ike on Personal Network Tie Activation as Response and Recovery',\n  titleKo: '제8장: 허리케인 아이크가 대응 및 복구로서의 개인 네트워크 유대 활성화에 미치는 영향',\n  rows: {json.dumps(rows, ensure_ascii=False, indent=2)}\n}};"

with open('translation/data/chapter8_data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

# Write Parallel Markdown
md_content = """# Chapter 8 대역본 (Original & Korean 1:1 Parallel Translation) - 100% 전수 완역본

> **서지정보:** Marcum, C. S., Wilkinson, A. V., & Koehly, L. M. (2017). Chapter 8: The Effect of Hurricane Ike on Personal Network Tie Activation as Response and Recovery. In *Social Network Analysis of Disaster Response, Recovery, and Adaptation* (pp. 131–150). Elsevier.

---

"""

for idx, r in enumerate(rows):
    md_content += f"### [단락 {idx+1}] {r['type'].upper()}\n\n"
    md_content += f"**[EN]**\n{r['en']}\n\n"
    md_content += f"**[KO]**\n{r['ko']}\n\n"
    md_content += "---\n\n"

with open('translation/chapter8_대역.md', 'w', encoding='utf-8') as f:
    f.write(md_content)

total_en = sum(len(r['en']) for r in rows)
total_ko = sum(len(r['ko']) for r in rows)
print(f"Chapter 8 FULLY BUILT: {len(rows)} rows, EN: {total_en} chars, KO: {total_ko} chars, Ratio: {total_ko/total_en:.2f}")
