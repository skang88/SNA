import re, json

with open('subnote/chapter8-원문.md', 'r', encoding='utf-8') as f:
    text = f.read()

cleaned_text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
pure_blocks = [b.strip() for b in cleaned_text.split('\n\n') if b.strip() and b.strip() != '---']
assert len(pure_blocks) == 65, f"Expected 65, got {len(pure_blocks)}"

with open('scratch/ch8_fixed_p1.json', 'r', encoding='utf-8') as f:
    p1 = json.load(f)
with open('scratch/ch8_fixed_p2.json', 'r', encoding='utf-8') as f:
    p2 = json.load(f)

old_trans = {}
old_trans.update(p1)
old_trans.update(p2)

# Build accurate 65-block mapping
rows = []
old_idx = 1
for idx, en_b in enumerate(pure_blocks):
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

    if "image-29.png" in en_b:
        ko_b = "![그림 8.1: 재난 이전 대비 대응기 및 복구기 간 열거된 관계 유형의 가족 수준 평균 차이](image-29.png)  \n*그림 8.1 재난 이전 대비 대응기 및 복구기 간 열거된 관계 유형 수의 가족 수준 평균 차이 (독립표본 t-검정, \*p < .05, \*\*p < .01)*"
    elif "image-30.png" in en_b:
        ko_b = "![표 8.3: 시기별 이항 호의 교환 로그선형 모형의 표준화 피어슨 잔차](image-30.png)  \n*표 8.3 시기별 이항 호의 교환 로그선형 모형의 표준화 피어슨 잔차 (Standardized Pearson Residuals)*"
    else:
        ko_b = old_trans[str(old_idx)]
        old_idx += 1

    rows.append({
        "type": btype,
        "en": en_b,
        "ko": ko_b
    })

# Write chapter8_data.js
js_content = f"""window.CHAPTER_DATA = window.CHAPTER_DATA || {{}};
window.CHAPTER_DATA[8] = {{
  chapterNumber: 8,
  titleEn: "Chapter 8: The Effect of Hurricane Ike on Personal Network Tie Activation as Response and Recovery",
  titleKo: "제8장: 허리케인 아이크가 대응 및 복구로서의 개인 네트워크 유대 활성화에 미치는 영향",
  rows: {json.dumps(rows, ensure_ascii=False, indent=2)}
}};"""

with open('translation/data/chapter8_data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

# Write chapter8_대역.md
md_content = """# Chapter 8 대역본 (Original & Korean 1:1 Parallel Translation) - 100% 완전 전수 완역본

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

print(f"SUCCESS: Chapter 8 rebuild complete! Total {len(rows)} rows.")
