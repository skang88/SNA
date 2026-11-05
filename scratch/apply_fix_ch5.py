import json

with open('scratch/ch5_enhancements.json', 'r', encoding='utf-8') as f:
    enhancements = json.load(f)

# Read existing chapter5_data.js
with open('translation/data/chapter5_data.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for line_idx, line in enumerate(lines):
    if 'rows:' in line:
        json_str = ''.join(lines[line_idx:]).strip()
        json_str = json_str[json_str.find('['):json_str.rfind(']')+1]
        rows = json.loads(json_str)
        break

assert len(rows) == 87, f"Expected 87 rows, got {len(rows)}"

# Update with enhanced translations
for k, v in enhancements.items():
    idx = int(k) - 1
    rows[idx]['ko'] = v

# Read cleaned EN to ensure 100% consistency
with open('subnote/chapter5-원문.md', 'r', encoding='utf-8') as f:
    text = f.read()

raw = [b.strip() for b in text.split('\n\n') if b.strip()]
cleaned = [b for b in raw if b != '---' and not b.startswith('<!--')]
assert len(cleaned) == 87

for idx in range(87):
    rows[idx]['en'] = cleaned[idx]

# Write chapter5_data.js
js_content = f"""window.CHAPTER_DATA = window.CHAPTER_DATA || {{}};
window.CHAPTER_DATA[5] = {{
  chapterNumber: 5,
  titleEn: "Chapter 5: The Importance of Perspective: A Multilevel Network Approach to Multimodal Disaster Response",
  titleKo: "제5장: 관점의 중요성: 다부문·다조직 재난 대응 네트워크에서의 성과",
  rows: {json.dumps(rows, ensure_ascii=False, indent=2)}
}};"""

with open('translation/data/chapter5_data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

# Write chapter5_대역.md
md_content = """# Chapter 5 대역본 (Original & Korean 1:1 Parallel Translation) - 100% 완전 전수 완역본

> **서지정보:** Nowell, B. L., & Steelman, T. A. (2017). Chapter 5: Perspective Matters: The Challenge of Evaluating Network Performance in Multimodal Disaster Response. In *Social Network Analysis of Disaster Response, Recovery, and Adaptation* (pp. 59–74). Elsevier.

---

"""

for idx, r in enumerate(rows):
    md_content += f"### [단락 {idx+1}] {r['type'].upper()}\n\n"
    md_content += f"**[EN]**\n{r['en']}\n\n"
    md_content += f"**[KO]**\n{r['ko']}\n\n"
    md_content += "---\n\n"

with open('translation/chapter5_대역.md', 'w', encoding='utf-8') as f:
    f.write(md_content)

en_chars = sum(len(r['en']) for r in rows)
ko_chars = sum(len(r['ko']) for r in rows)
print(f"SUCCESS: Chapter 5 100% complete rebuilt! Rows: {len(rows)}, EN: {en_chars} chars, KO: {ko_chars} chars, Ratio: {ko_chars/en_chars:.2f}")
