import re
import html

with open("소방_SNA_수업_연구계획서.md", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Protect code blocks and mermaid blocks
mermaid_blocks = []
def save_mermaid(match):
    idx = len(mermaid_blocks)
    mermaid_blocks.append(match.group(1).strip())
    return f"___MERMAID_BLOCK_{idx}___"

text = re.sub(r'```mermaid\n(.*?)\n```', save_mermaid, text, flags=re.DOTALL)

code_blocks = []
def save_code(match):
    idx = len(code_blocks)
    code_blocks.append(html.escape(match.group(1).strip()))
    return f"___CODE_BLOCK_{idx}___"

text = re.sub(r'```python\n(.*?)\n```', save_code, text, flags=re.DOTALL)
text = re.sub(r'```\n(.*?)\n```', save_code, text, flags=re.DOTALL)

# 2. Line by line parsing for tables, blockquotes, lists, headers
lines = text.split("\n")
output_lines = []

in_table = False
table_buffer = []

def parse_table(buffer):
    if len(buffer) < 2:
        return buffer
    header = [c.strip() for c in buffer[0].strip().split('|')[1:-1]]
    out = ["<table>", "  <thead>", "    <tr>"]
    for c in header:
        out.append(f"      <th>{c}</th>")
    out.extend(["    </tr>", "  </thead>", "  <tbody>"])
    for row in buffer[2:]:
        if not row.strip().startswith('|'):
            continue
        cells = [c.strip() for c in row.strip().split('|')[1:-1]]
        out.append("    <tr>")
        for c in cells:
            out.append(f"      <td>{c}</td>")
        out.append("    </tr>")
    out.extend(["  </tbody>", "</table>"])
    return out

in_quote = False
quote_buffer = []

def flush_quote():
    global quote_buffer, in_quote
    if quote_buffer:
        joined = "<br>".join(quote_buffer)
        output_lines.append(f'<div class="subtitle">{joined}</div>')
        quote_buffer = []
    in_quote = False

in_ul = False

for line in lines:
    stripped = line.strip()
    
    # Check table
    if stripped.startswith('|') and '|' in stripped[1:]:
        flush_quote()
        if in_ul:
            output_lines.append('</ul>')
            in_ul = False
        in_table = True
        table_buffer.append(line)
        continue
    else:
        if in_table:
            output_lines.extend(parse_table(table_buffer))
            table_buffer = []
            in_table = False
            
    # Check blockquote
    if stripped.startswith('> '):
        if in_ul:
            output_lines.append('</ul>')
            in_ul = False
        in_quote = True
        quote_buffer.append(stripped[2:])
        continue
    else:
        if in_quote:
            flush_quote()
            
    # Check lists
    if stripped.startswith('* ') or stripped.startswith('- '):
        if not in_ul:
            output_lines.append('<ul>')
            in_ul = True
        item = re.sub(r'^\s*[\*\-]\s+', '', line)
        output_lines.append(f'  <li>{item}</li>')
        continue
    else:
        if in_ul:
            output_lines.append('</ul>')
            in_ul = False
            
    # Check headers
    if stripped.startswith('# '):
        output_lines.append(f'<h1>{stripped[2:]}</h1>')
    elif stripped.startswith('## '):
        output_lines.append(f'<h2>{stripped[3:]}</h2>')
    elif stripped.startswith('### '):
        output_lines.append(f'<h3>{stripped[4:]}</h3>')
    elif stripped == '---':
        output_lines.append('<hr>')
    elif stripped == '':
        output_lines.append('')
    else:
        if not stripped.startswith('___MERMAID_') and not stripped.startswith('___CODE_'):
            output_lines.append(f'<p>{stripped}</p>')
        else:
            output_lines.append(stripped)

if in_table:
    output_lines.extend(parse_table(table_buffer))
if in_quote:
    flush_quote()
if in_ul:
    output_lines.append('</ul>')

body = "\n".join(output_lines)

# 3. Restore blocks
for idx, code in enumerate(mermaid_blocks):
    body = body.replace(f"___MERMAID_BLOCK_{idx}___", f'<div class="mermaid">\n{code}\n</div>')

for idx, code in enumerate(code_blocks):
    body = body.replace(f"___CODE_BLOCK_{idx}___", f'<pre><code>{code}</code></pre>')

# 4. Inlines: bold, italic, code
body = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', body)
body = re.sub(r'\*(.*?)\*', r'<em>\1</em>', body)
body = re.sub(r'`([^`]+)`', r'<code>\1</code>', body)

html_template = """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[SNA 세미나 연구계획서] 무전 관제로그 시계열 네트워크 마이닝 기반의 소방 현장지휘 동학 및 지휘 병목 실증 연구</title>
  
  <!-- Pretendard Font -->
  <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" />
  
  <!-- KaTeX for Math rendering -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" 
          onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});"></script>

  <!-- Mermaid.js for Diagram rendering -->
  <script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    mermaid.initialize({ 
      startOnLoad: true, 
      theme: 'base',
      themeVariables: {
        fontSize: '15px',
        fontFamily: 'Pretendard, -apple-system, sans-serif',
        primaryColor: '#e0f2fe',
        primaryTextColor: '#0369a1',
        primaryBorderColor: '#0284c7',
        lineColor: '#0284c7',
        secondaryColor: '#fef3c7',
        tertiaryColor: '#f1f5f9'
      }
    });
  </script>

  <style>
    :root {
      --primary: #0284c7;
      --primary-dark: #0369a1;
      --primary-light: #f0f9ff;
      --secondary: #d97706;
      --text: #1e293b;
      --text-muted: #64748b;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --border: #e2e8f0;
    }

    body {
      font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif;
      line-height: 1.7;
      color: var(--text);
      background-color: var(--bg);
      margin: 0;
      padding: 40px 20px;
    }

    .container {
      max-width: 1000px;
      margin: 0 auto;
      background: var(--card-bg);
      padding: 50px 60px;
      border-radius: 16px;
      box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.05), 0 2px 6px -1px rgba(0, 0, 0, 0.03);
      border: 1px solid var(--border);
    }

    h1 {
      font-size: 2.1rem;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.35;
      margin-bottom: 12px;
      letter-spacing: -0.02em;
    }

    .subtitle {
      font-size: 1.05rem;
      color: var(--primary-dark);
      background: var(--primary-light);
      padding: 14px 20px;
      border-left: 4px solid var(--primary);
      border-radius: 0 8px 8px 0;
      margin-bottom: 30px;
      line-height: 1.65;
    }

    h2 {
      font-size: 1.55rem;
      font-weight: 700;
      color: #0f172a;
      border-bottom: 2px solid #e2e8f0;
      padding-bottom: 10px;
      margin-top: 45px;
      margin-bottom: 20px;
    }

    h3 {
      font-size: 1.25rem;
      font-weight: 600;
      color: #1e293b;
      margin-top: 28px;
      margin-bottom: 14px;
    }

    p, li {
      font-size: 1.02rem;
      color: #334155;
    }

    ul, ol {
      padding-left: 24px;
      margin-bottom: 16px;
    }

    li {
      margin-bottom: 6px;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      margin: 24px 0;
      font-size: 0.95rem;
    }

    th, td {
      padding: 12px 14px;
      text-align: left;
      border: 1px solid var(--border);
      vertical-align: middle;
    }

    th {
      background-color: #f1f5f9;
      color: #1e293b;
      font-weight: 600;
    }

    tr:nth-child(even) {
      background-color: #f8fafc;
    }

    .mermaid {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      padding: 20px;
      margin: 25px 0;
      text-align: center;
    }

    code {
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 0.9em;
      background: #f1f5f9;
      padding: 2px 6px;
      border-radius: 4px;
      color: #0369a1;
    }

    pre code {
      display: block;
      padding: 16px;
      background: #1e293b;
      color: #f8fafc;
      border-radius: 8px;
      overflow-x: auto;
      line-height: 1.5;
    }

    hr {
      border: none;
      height: 1px;
      background: #e2e8f0;
      margin: 36px 0;
    }
  </style>
</head>
<body>
  <div class="container">
__BODY__
  </div>
</body>
</html>
"""

final_html = html_template.replace("__BODY__", body)
with open("소방_SNA_수업_연구계획서.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("Full HTML built cleanly!")
