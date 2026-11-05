import json

for ch in [1, 2, 3, 4, 5, 6]:
    path = f"translation/data/chapter{ch}_data.js"
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    # extract json
    start = content.find("rows: [") + 6
    end = content.rfind("]") + 1
    rows = json.loads(content[start:end])
    
    total_en_chars = sum(len(r['en']) for r in rows)
    total_ko_chars = sum(len(r['ko']) for r in rows)
    ratio = total_ko_chars / total_en_chars if total_en_chars else 0
    print(f"Chapter {ch}: {len(rows)} rows, EN chars: {total_en_chars}, KO chars: {total_ko_chars}, Ratio: {ratio:.2f}")

    # find suspicious short translations
    short_count = 0
    for idx, r in enumerate(rows):
        if len(r['en']) > 300 and len(r['ko']) < len(r['en']) * 0.5:
            short_count += 1
    print(f"  -> Rows where KO is less than 50% of EN length: {short_count}")
