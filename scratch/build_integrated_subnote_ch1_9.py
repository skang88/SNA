# -*- coding: utf-8 -*-
import os
import re
import base64

WORKDIR = "/Users/sg/Project/SNA/subnote"
os.chdir(WORKDIR)

def get_base64_img(img_name):
    if not os.path.exists(img_name):
        return ""
    mime = "image/png"
    if img_name.endswith(".jpg") or img_name.endswith(".jpeg"):
        mime = "image/jpeg"
    with open(img_name, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode("utf-8")
    return f"data:{mime};base64,{b64}"

print("1. Preparing base64 image map for Ch 1 ~ 9...")
used_imgs = ['image.png'] + [f'image-{i}.png' for i in range(1, 38)]

img_b64_map = {}
for img in used_imgs:
    if os.path.exists(img):
        img_b64_map[img] = get_base64_img(img)

print(f"Loaded {len(img_b64_map)} images into memory.")

chapters_meta = [
    {
        "num": 1,
        "title": "Ch 1. 재난 맥락에서의 사회연결망 분석 서설",
        "short": "Ch 1. SNA 서설",
        "authors": "Eric C. Jones & A.J. Faas",
        "subject": "은유적 vs 공식 네트워크, 잠재망 vs 실현망, 이중 네트워크(Dual Network) & QAP",
        "badge": "Ch 1 서설",
    },
    {
        "num": 2,
        "title": "Ch 2. 재난 연구에서의 개인 중심 사회연결망",
        "short": "Ch 2. 개인 중심 SNA",
        "authors": "A.J. Faas & Eric C. Jones",
        "subject": "결속형 자본의 어두운 면, 밀도의 역설, 코뮤니타스의 함정, Q방법론",
        "badge": "Ch 2 대인망",
    },
    {
        "num": 3,
        "title": "Ch 3. 재난 관리에서의 조직간 네트워크",
        "short": "Ch 3. 조직간 네트워크",
        "authors": "Naim Kapucu & Qian Hu",
        "subject": "NRF-ICS-ESF 다층적 거버넌스, 상호운용성, 5×5 메타 매트릭스",
        "badge": "Ch 3 조직망",
    },
    {
        "num": 4,
        "title": "Ch 4. 재난 대응, 복구 및 완화의 사회연결망 연구 전략",
        "short": "Ch 4. SNA 연구 전략",
        "authors": "Danielle M. Varda",
        "subject": "IOSP 프레임워크, 다수준 MTML 모델, QAP/ERGM, 소방 실증 프로토콜",
        "badge": "Ch 4 연구전략",
    },
    {
        "num": 5,
        "title": "Ch 5. 산불 대응 네트워크의 성과 측정 과제",
        "short": "Ch 5. 산불 성과평가",
        "authors": "Branda L. Nowell & Toddi A. Steelman",
        "subject": "성과 다원주의(Pluralism), HLM 다수준 분석, 합의수준(SD) 선행지표",
        "badge": "Ch 5 성과평가",
    },
    {
        "num": 6,
        "title": "Ch 6. 슈퍼스톰 샌디 이후 네트워크화된 협력",
        "short": "Ch 6. 슈퍼스톰 샌디",
        "authors": "Jack L. Harris & Marya L. Doerfel",
        "subject": "다원 부문(Plural Sector), 시계열적 진화(Times 1~4), 잉여적 자원 클러스터",
        "badge": "Ch 6 다원부문",
    },
    {
        "num": 7,
        "title": "Ch 7. 콜로라도 산불 당시 재난조직 간 주의(Attention) 이동",
        "short": "Ch 7. 산불 주의동학 DNR",
        "authors": "Carter T. Butts et al.",
        "subject": "트위터 팔로우 동학, 동적 네트워크 로지스틱 회귀(DNR), 사전 고착화(Lock-in)",
        "badge": "Ch 7 주의동학",
    },
    {
        "num": 8,
        "title": "Ch 8. 허리케인 아이크와 개인 네트워크 연계 활성화",
        "short": "Ch 8. 허리케인 아이크",
        "authors": "Christopher Steven Marcum et al.",
        "subject": "자연실험(Natural Experiment), 2원 혼합효과 로지스틱 회귀, 강한 유대의 역설",
        "badge": "Ch 8 연계활성화",
    },
    {
        "num": 9,
        "title": "Ch 9. 가족의 부담: 재난 다발 지역 플로리다 주민들의 사회연결망 자원",
        "short": "Ch 9. 가족의 부담",
        "authors": "Michelle Meyer",
        "subject": "에고 네트워크(Ego-net), 가족 배태성(Kin Embeddedness), 자원 불평등, 사전 인지망",
        "badge": "Ch 9 가족부담",
    }
]

chapters_data = []

print("2. Processing chapters 1 to 9...")
for meta in chapters_meta:
    ch_num = meta["num"]
    fname = f"chapter{ch_num}_subnote.html"
    with open(fname, "r", encoding="utf-8") as f:
        html = f.read()

    # Extract TOC list
    m_toc = re.search(r'<ul class=\"toc-list\"[^>]*>(.*?)</ul>', html, re.DOTALL)
    toc_raw = m_toc.group(1) if m_toc else ""

    # Extract content container
    start_tag = '<div class="content-container">'
    start_idx = html.find(start_tag)
    if start_idx == -1:
        start_tag = '<main class="content-container">'
        start_idx = html.find(start_tag)
    if start_idx == -1:
        start_tag = '<main class="main-container">'
        start_idx = html.find(start_tag)
    if start_idx == -1:
        start_tag = '<main class="main-wrapper">'
        start_idx = html.find(start_tag)
    end_idx = html.rfind('</main>')
    if end_idx == -1:
        end_idx = html.rfind('</div>\n    </div>\n  </div>')
    
    content_raw = html[start_idx + len(start_tag):end_idx].strip()
    
    # Remove trailing </div> if present
    if content_raw.endswith('</div>'):
        content_raw = content_raw[:-6].strip()

    # Find all IDs defined in this chapter content
    ids_in_content = set(re.findall(r'id=[\"\']([^\"\']+)[\"\']', content_raw))

    # Rename IDs and matching hrefs to avoid collisions across chapters
    for id_val in ids_in_content:
        content_raw = re.sub(f'id=([\"\']){re.escape(id_val)}([\"\'])', f'id=\\1ch{ch_num}-{id_val}\\2', content_raw)
        content_raw = re.sub(f'href=([\"\'])#{re.escape(id_val)}([\"\'])', f'href=\\1#ch{ch_num}-{id_val}\\2', content_raw)
        toc_raw = re.sub(f'href=([\"\'])#{re.escape(id_val)}([\"\'])', f'href=\\1#ch{ch_num}-{id_val}\\2', toc_raw)

    # Base64 replace images in content
    for img_name, b64_str in img_b64_map.items():
        content_raw = re.sub(f'src=([\"\']){re.escape(img_name)}([\"\'])', f'src=\\1{b64_str}\\2', content_raw)

    # Clean out any old chapter-select dropdown or local footer-nav links that point to external files
    content_raw = re.sub(r'<div class=\"chapter-nav-dropdown\">.*?</div>', '', content_raw, flags=re.DOTALL)
    content_raw = re.sub(r'<div class=\"footer-nav\">.*?</div>', '', content_raw, flags=re.DOTALL)
    content_raw = re.sub(r'<!-- FOOTER NAV -->.*?</div>\s*</main>', '', content_raw, flags=re.DOTALL)

    chapters_data.append({
        "meta": meta,
        "toc": toc_raw,
        "content": content_raw
    })
    print(f"Chapter {ch_num} processed successfully. (Content length: {len(content_raw):,} chars)")

print("3. Generating integrated HTML template...")

html_template = f'''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>재난관리 사회연결망 연구총서 | Chapters 1 ~ 9 통합 학술 서브노트 & 소방 실증 프로토콜</title>
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Noto+Sans+KR:wght@300;400;500;700;900&family=Outfit:wght@400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  
  <!-- MathJax Configuration & Script -->
  <script>
    window.MathJax = {{
      tex: {{
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]
      }},
      options: {{
        skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre']
      }}
    }};
  </script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <!-- Lucide Icons CDN -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <!-- Mermaid JS for diagrams -->
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', function() {{
      if (typeof mermaid !== 'undefined') {{
        try {{
          mermaid.initialize({{ 
            startOnLoad: true, 
            theme: 'dark',
            securityLevel: 'loose',
            fontFamily: 'Noto Sans KR, Inter, sans-serif'
          }});
        }} catch(e) {{
          console.warn('Mermaid initialization deferred:', e);
        }}
      }}
    }});
  </script>

  <style>
    :root {{
      --bg-primary: #0b1120;
      --bg-secondary: #131c31;
      --bg-sidebar: #0f172a;
      --bg-card: #1e293b;
      --bg-card-hover: #26354d;
      --accent-primary: #38bdf8;
      --accent-secondary: #818cf8;
      --accent-emerald: #34d399;
      --accent-amber: #fbbf24;
      --accent-rose: #fb7185;
      --accent-purple: #c084fc;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --border-color: #334155;
      --sidebar-border: #1e293b;
      --sidebar-width: 330px;
      --glass-bg: rgba(19, 28, 49, 0.88);
      --glass-border: rgba(255, 255, 255, 0.08);
      --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.25);
      --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.35);
      --shadow-lg: 0 12px 30px -6px rgba(0, 0, 0, 0.5);
      --radius: 12px;
      --radius-sm: 8px;
      --radius-lg: 16px;
      --transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    [data-theme="light"] {{
      --bg-primary: #f8fafc;
      --bg-secondary: #ffffff;
      --bg-sidebar: #ffffff;
      --bg-card: #ffffff;
      --bg-card-hover: #f1f5f9;
      --accent-primary: #0284c7;
      --accent-secondary: #6366f1;
      --accent-emerald: #059669;
      --accent-amber: #d97706;
      --accent-rose: #e11d48;
      --accent-purple: #9333ea;
      --text-main: #0f172a;
      --text-muted: #475569;
      --text-dim: #94a3b8;
      --border-color: #e2e8f0;
      --sidebar-border: #e2e8f0;
      --glass-bg: rgba(255, 255, 255, 0.92);
      --glass-border: rgba(0, 0, 0, 0.08);
      --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.06);
      --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.08);
      --shadow-lg: 0 12px 30px -6px rgba(0, 0, 0, 0.1);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html {{
      scroll-behavior: smooth;
    }}

    body {{
      font-family: 'Noto Sans KR', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-primary);
      color: var(--text-main);
      line-height: 1.7;
      letter-spacing: -0.015em;
      overflow-x: hidden;
      font-size: 15px;
    }}

    /* Global Chapter Selector Header */
    .global-nav-header {{
      position: sticky;
      top: 0;
      z-index: 1000;
      background: var(--glass-bg);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-color);
      display: flex;
      flex-direction: column;
      box-shadow: var(--shadow-sm);
    }}

    .top-bar-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.6rem 1.5rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      flex-wrap: wrap;
      gap: 0.5rem;
    }}

    .logo-area {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}

    .logo-badge {{
      background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
      color: #ffffff;
      padding: 0.25rem 0.6rem;
      border-radius: var(--radius-sm);
      font-size: 0.75rem;
      font-weight: 800;
      font-family: 'Outfit', sans-serif;
      letter-spacing: 0.05em;
    }}

    .logo-title {{
      font-family: 'Outfit', 'Noto Sans KR', sans-serif;
      font-weight: 700;
      font-size: 1.05rem;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 0.5rem;
      flex-wrap: wrap;
    }}

    .logo-sub {{
      font-size: 0.8rem;
      color: var(--text-muted);
      font-weight: 400;
    }}

    .top-actions {{
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }}

    .nav-link-btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      padding: 0.35rem 0.7rem;
      border-radius: var(--radius-sm);
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      font-size: 0.8rem;
      font-weight: 600;
      text-decoration: none;
      transition: var(--transition);
    }}

    .nav-link-btn:hover {{
      color: var(--accent-primary);
      border-color: var(--accent-primary);
      background: var(--bg-card-hover);
    }}

    .nav-link-btn.highlight {{
      background: linear-gradient(135deg, rgba(56, 189, 248, 0.15), rgba(129, 140, 248, 0.15));
      border-color: var(--accent-primary);
      color: var(--accent-primary);
    }}

    .theme-toggle-btn, .action-btn {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      width: 34px;
      height: 34px;
      border-radius: var(--radius-sm);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: var(--transition);
    }}

    .theme-toggle-btn:hover, .action-btn:hover {{
      color: var(--text-main);
      background: var(--bg-card-hover);
      border-color: var(--accent-primary);
    }}

    /* Chapter Navigation Tabs Row */
    .chapter-tabs-row {{
      display: flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.45rem 1.5rem;
      overflow-x: auto;
      scrollbar-width: none;
    }}
    .chapter-tabs-row::-webkit-scrollbar {{
      display: none;
    }}

    .ch-tab {{
      padding: 0.45rem 0.85rem;
      border-radius: var(--radius-sm);
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid transparent;
      color: var(--text-muted);
      font-size: 0.825rem;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
      transition: var(--transition);
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}

    .ch-tab:hover {{
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.08);
      border-color: var(--border-color);
    }}

    .ch-tab.active {{
      background: var(--accent-primary);
      color: #0b1120;
      font-weight: 700;
      border-color: var(--accent-primary);
      box-shadow: 0 0 14px rgba(56, 189, 248, 0.35);
    }}

    .ch-tab.all-view {{
      background: linear-gradient(135deg, rgba(192, 132, 252, 0.2), rgba(244, 63, 94, 0.2));
      border: 1px solid var(--accent-purple);
      color: var(--text-main);
    }}
    .ch-tab.all-view.active {{
      background: linear-gradient(135deg, var(--accent-purple), var(--accent-rose));
      color: #ffffff;
      border-color: transparent;
    }}

    /* Main Container Layout */
    .app-container {{
      display: flex;
      width: 100%;
      min-height: calc(100vh - 100px);
    }}

    /* Sidebar Navigation */
    .sidebar {{
      width: var(--sidebar-width);
      min-width: var(--sidebar-width);
      background: var(--bg-sidebar);
      border-right: 1px solid var(--sidebar-border);
      position: sticky;
      top: 96px;
      height: calc(100vh - 96px);
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      z-index: 100;
    }}

    .sidebar-header {{
      padding: 1.25rem 1.25rem 0.75rem 1.25rem;
      border-bottom: 1px solid var(--border-color);
    }}

    .sidebar-title {{
      font-size: 1rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 0.25rem;
      line-height: 1.4;
    }}

    .sidebar-subtitle {{
      font-size: 0.8rem;
      color: var(--text-muted);
      line-height: 1.4;
      margin-bottom: 0.85rem;
    }}

    .sidebar-search {{
      position: relative;
    }}

    .sidebar-search i {{
      position: absolute;
      left: 0.75rem;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-dim);
      width: 14px;
      height: 14px;
    }}

    .sidebar-search input {{
      width: 100%;
      padding: 0.45rem 0.75rem 0.45rem 2.2rem;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-sm);
      color: var(--text-main);
      font-size: 0.8rem;
      outline: none;
    }}
    .sidebar-search input:focus {{
      border-color: var(--accent-primary);
    }}

    .sidebar-nav-container {{
      padding: 1rem 0.75rem 2rem 0.75rem;
      flex: 1;
    }}

    .toc-label {{
      font-size: 0.7rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-dim);
      padding: 0.25rem 0.6rem 0.5rem 0.6rem;
    }}

    .toc-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 2px;
    }}

    .toc-item a {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.45rem 0.65rem;
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.825rem;
      border-radius: var(--radius-sm);
      transition: var(--transition);
      line-height: 1.4;
    }}

    .toc-item a i {{
      width: 15px;
      height: 15px;
      flex-shrink: 0;
      color: var(--text-dim);
    }}

    .toc-item a:hover {{
      color: var(--text-main);
      background: var(--bg-card-hover);
    }}

    .toc-item.active a {{
      color: var(--accent-primary);
      background: rgba(56, 189, 248, 0.1);
      font-weight: 600;
    }}
    .toc-item.active a i {{
      color: var(--accent-primary);
    }}

    .toc-badge {{
      margin-left: auto;
      font-size: 0.68rem;
      padding: 0.15rem 0.4rem;
      border-radius: 4px;
      background: rgba(255, 255, 255, 0.08);
      color: var(--text-dim);
      font-family: 'JetBrains Mono', monospace;
    }}

    /* Main Content Area */
    .main-wrapper {{
      flex: 1;
      min-width: 0;
      background: var(--bg-primary);
      padding: 2.5rem 3.5rem 6rem 3.5rem;
    }}

    @media (max-width: 1024px) {{
      .sidebar {{ display: none; }}
      .main-wrapper {{ padding: 1.5rem 1.5rem 4rem 1.5rem; }}
    }}

    /* Chapter Content Box */
    .chapter-view-box {{
      display: none;
      animation: fadeIn 0.3s ease-in-out;
    }}
    .chapter-view-box.active {{
      display: block;
    }}

    body.show-all-chapters .chapter-view-box {{
      display: block !important;
      margin-bottom: 5rem;
      padding-bottom: 4rem;
      border-bottom: 2px dashed var(--border-color);
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Progress bar */
    #progress-bar {{
      position: fixed;
      top: 0;
      left: 0;
      height: 3px;
      background: linear-gradient(90deg, var(--accent-primary), var(--accent-purple));
      z-index: 10001;
      width: 0%;
      transition: width 0.1s;
    }}

    /* Hero Banner styles */
    .hero-banner, .chapter-hero {{
      background: linear-gradient(135deg, rgba(30, 41, 59, 0.9), rgba(15, 23, 42, 0.95));
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 2.25rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow-lg);
      position: relative;
      overflow: hidden;
    }}

    .hero-tag, .hero-badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.3rem 0.75rem;
      border-radius: 9999px;
      background: rgba(56, 189, 248, 0.15);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: var(--accent-primary);
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      margin-bottom: 1rem;
      text-transform: uppercase;
      font-family: 'Outfit', sans-serif;
    }}
    .hero-badge.emerald, .hero-tag.tag-peer {{ background: rgba(52, 211, 153, 0.15); color: var(--accent-emerald); border-color: rgba(52, 211, 153, 0.3); }}
    .hero-badge.amber {{ background: rgba(251, 191, 36, 0.15); color: var(--accent-amber); border-color: rgba(251, 191, 36, 0.3); }}
    .hero-badge.rose {{ background: rgba(251, 113, 133, 0.15); color: var(--accent-rose); border-color: rgba(251, 113, 133, 0.3); }}
    .hero-badge.purple {{ background: rgba(192, 132, 252, 0.15); color: var(--accent-purple); border-color: rgba(192, 132, 252, 0.3); }}

    .hero-badge-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin-bottom: 1rem;
    }}

    .hero-title {{
      font-family: 'Outfit', 'Noto Sans KR', sans-serif;
      font-size: 2rem;
      font-weight: 800;
      line-height: 1.35;
      color: #ffffff;
      margin-bottom: 0.75rem;
      letter-spacing: -0.02em;
    }}

    .hero-subtitle, .hero-original-title {{
      font-size: 1rem;
      color: var(--text-muted);
      line-height: 1.55;
      margin-bottom: 1.5rem;
    }}

    .hero-meta, .hero-meta-grid, .author-card, .author-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 1rem;
      padding-top: 1.25rem;
      border-top: 1px solid var(--border-color);
      font-size: 0.85rem;
    }}

    .hero-meta-item, .meta-box {{
      display: flex;
      flex-direction: column;
      gap: 0.2rem;
    }}

    .hero-meta-label, .meta-label {{
      font-size: 0.7rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-dim);
      font-weight: 600;
    }}

    .hero-meta-val, .meta-value {{
      font-size: 0.88rem;
      color: var(--text-main);
      font-weight: 500;
    }}

    /* Stat Cards Grid (Ch 9 & general) */
    .stat-cards-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 1rem;
      margin: 1.5rem 0 2.5rem 0;
    }}

    .stat-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
      transition: var(--transition);
      box-shadow: var(--shadow-sm);
    }}
    .stat-card:hover {{
      transform: translateY(-2px);
      border-color: var(--accent-primary);
      box-shadow: var(--shadow-md);
    }}

    .stat-num {{
      font-size: 1.6rem;
      font-weight: 800;
      color: var(--accent-primary);
      font-family: 'Outfit', sans-serif;
    }}
    .stat-label {{
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--text-main);
    }}
    .stat-sub {{
      font-size: 0.78rem;
      color: var(--text-dim);
    }}

    /* Section styling */
    .section-block, .content-section {{
      margin-bottom: 3.5rem;
      scroll-margin-top: 110px;
    }}

    .section-header {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-bottom: 1.5rem;
      padding-bottom: 0.75rem;
      border-bottom: 1px solid var(--border-color);
    }}

    .section-icon {{
      width: 36px;
      height: 36px;
      border-radius: var(--radius-sm);
      background: rgba(56, 189, 248, 0.15);
      color: var(--accent-primary);
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .section-icon.emerald {{ background: rgba(52, 211, 153, 0.15); color: var(--accent-emerald); }}
    .section-icon.amber {{ background: rgba(251, 191, 36, 0.15); color: var(--accent-amber); }}
    .section-icon.rose {{ background: rgba(251, 113, 133, 0.15); color: var(--accent-rose); }}
    .section-icon.purple {{ background: rgba(192, 132, 252, 0.15); color: var(--accent-purple); }}

    .section-title {{
      font-family: 'Outfit', 'Noto Sans KR', sans-serif;
      font-size: 1.45rem;
      font-weight: 700;
      color: var(--text-main);
      letter-spacing: -0.01em;
    }}

    h3.sub-title, .sub-section-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text-main);
      margin: 1.75rem 0 0.85rem 0;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    p {{
      margin-bottom: 1.1rem;
      color: var(--text-muted);
      line-height: 1.8;
      font-size: 0.95rem;
    }}

    strong {{
      color: var(--text-main);
      font-weight: 600;
    }}

    /* Card & Grid */
    .card-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.25rem;
      margin: 1.25rem 0 1.75rem 0;
    }}

    .card, .content-card, .para-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 1.4rem;
      transition: var(--transition);
      box-shadow: var(--shadow-sm);
      margin-bottom: 1.25rem;
    }}

    .card:hover, .content-card:hover, .para-card:hover {{
      background: var(--bg-card-hover);
      border-color: rgba(56, 189, 248, 0.4);
      box-shadow: var(--shadow-md);
    }}

    .card-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 0.75rem;
    }}

    .card-title {{
      font-size: 1rem;
      font-weight: 700;
      color: var(--text-main);
    }}

    .card-body {{
      font-size: 0.88rem;
      color: var(--text-muted);
      line-height: 1.65;
    }}

    .card-badge {{
      font-size: 0.7rem;
      padding: 0.2rem 0.5rem;
      border-radius: 9999px;
      font-weight: 600;
      font-family: 'JetBrains Mono', monospace;
    }}
    .badge-primary, .badge-blue {{ background: rgba(56, 189, 248, 0.2); color: var(--accent-primary); }}
    .badge-emerald {{ background: rgba(52, 211, 153, 0.2); color: var(--accent-emerald); }}
    .badge-amber {{ background: rgba(251, 191, 36, 0.2); color: var(--accent-amber); }}
    .badge-rose {{ background: rgba(251, 113, 133, 0.2); color: var(--accent-rose); }}
    .badge-purple {{ background: rgba(192, 132, 252, 0.2); color: var(--accent-purple); }}

    /* Tables */
    .table-container {{
      overflow-x: auto;
      margin: 1.5rem 0 2rem 0;
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      background: var(--bg-card);
      box-shadow: var(--shadow-sm);
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
      text-align: left;
    }}

    th {{
      background: rgba(15, 23, 42, 0.6);
      color: var(--text-main);
      padding: 0.85rem 1rem;
      font-weight: 600;
      border-bottom: 1px solid var(--border-color);
      white-space: nowrap;
    }}

    td {{
      padding: 0.85rem 1rem;
      color: var(--text-muted);
      border-bottom: 1px solid var(--border-color);
      vertical-align: top;
      line-height: 1.65;
    }}

    tr:last-child td {{
      border-bottom: none;
    }}

    tr:hover td {{
      background: rgba(255, 255, 255, 0.02);
    }}

    /* Callouts & Alerts */
    .callout, .callout-box {{
      display: flex;
      gap: 1rem;
      padding: 1.25rem 1.4rem;
      border-radius: var(--radius);
      margin: 1.4rem 0;
      background: rgba(30, 41, 59, 0.5);
      border-left: 4px solid var(--accent-primary);
      box-shadow: var(--shadow-sm);
    }}

    .callout i, .callout-box i {{
      width: 20px;
      height: 20px;
      flex-shrink: 0;
      margin-top: 2px;
    }}

    .callout-title {{
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 0.35rem;
      font-size: 0.95rem;
    }}

    .callout-text, .callout-content p {{
      font-size: 0.88rem;
      color: var(--text-muted);
      line-height: 1.65;
      margin-bottom: 0;
    }}

    .callout-info {{ border-left-color: var(--accent-primary); background: rgba(56, 189, 248, 0.08); }}
    .callout-info i {{ color: var(--accent-primary); }}
    .callout-amber, .callout.amber, .callout-box.amber {{ border-left-color: var(--accent-amber); background: rgba(251, 191, 36, 0.08); }}
    .callout-amber i, .callout.amber i, .callout-box.amber i {{ color: var(--accent-amber); }}
    .callout-emerald, .callout.emerald, .callout-box.emerald {{ border-left-color: var(--accent-emerald); background: rgba(52, 211, 153, 0.08); }}
    .callout-emerald i, .callout.emerald i, .callout-box.emerald i {{ color: var(--accent-emerald); }}
    .callout-rose, .callout.rose, .callout-box.rose {{ border-left-color: var(--accent-rose); background: rgba(251, 113, 133, 0.08); }}
    .callout-rose i, .callout.rose i, .callout-box.rose i {{ color: var(--accent-rose); }}

    /* Formula & Diagram Box */
    .eq-box {{
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-sm);
      padding: 1rem 1.25rem;
      margin: 1.25rem 0;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.88rem;
    }}

    .diagram-container, .mermaid-box {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 1.5rem;
      margin: 1.75rem 0;
      text-align: center;
      box-shadow: var(--shadow-sm);
      overflow-x: auto;
    }}

    .diagram-caption {{
      margin-top: 1rem;
      font-size: 0.8rem;
      color: var(--text-dim);
      font-style: italic;
    }}

    /* Images */
    img {{
      max-width: 100%;
      height: auto;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-color);
      box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }}

    /* Integrated Chapter Footer Switcher */
    .integrated-chapter-footer {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: 4rem;
      padding-top: 2rem;
      border-top: 1px solid var(--border-color);
      flex-wrap: wrap;
      gap: 1rem;
    }}

    .chapter-switch-btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.65rem 1.25rem;
      border-radius: var(--radius-sm);
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      font-weight: 600;
      font-size: 0.85rem;
      cursor: pointer;
      transition: var(--transition);
      text-decoration: none;
    }}

    .chapter-switch-btn:hover {{
      background: var(--bg-card-hover);
      border-color: var(--accent-primary);
      color: var(--accent-primary);
    }}

    .chapter-switch-btn.primary {{
      background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
      color: #ffffff;
      border: none;
    }}

    /* Print styles */
    @media print {{
      .global-nav-header, .sidebar, #progress-bar, .integrated-chapter-footer {{
        display: none !important;
      }}
      .main-wrapper {{
        padding: 0 !important;
      }}
      .chapter-view-box {{
        display: block !important;
        page-break-after: always;
      }}
      body {{
        background: #ffffff !important;
        color: #000000 !important;
      }}
    }}
  </style>
</head>
<body>

  <!-- Reading Progress Bar -->
  <div id="progress-bar"></div>

  <!-- Global Sticky Nav Header -->
  <header class="global-nav-header">
    <div class="top-bar-row">
      <div class="logo-area">
        <span class="logo-badge">SNA COMPENDIUM</span>
        <div class="logo-title">
          <i data-lucide="shield-alert" style="color: var(--accent-primary); width:20px; height:20px;"></i>
          재난관리 사회연결망 연구총서
          <span class="logo-sub">| Chapters 1 ~ 9 완전 통합 학술 서브노트 & 소방 실증 모델</span>
        </div>
      </div>
      <div class="top-actions">
        <a href="chapter10_subnote.html" class="nav-link-btn" title="제10장 서브노트로 이동">
          <i data-lucide="arrow-right-circle"></i> Ch.10 원촨
        </a>
        <a href="chapter11_subnote.html" class="nav-link-btn" title="제11장 서브노트로 이동">
          <i data-lucide="arrow-right-circle"></i> Ch.11 캔터베리
        </a>
        <a href="../translation/index.html" class="nav-link-btn highlight" title="1:1 대역 리더로 이동">
          <i data-lucide="languages"></i> 대역 리더 (Ch 1~11)
        </a>
        <button class="action-btn" id="print-btn" title="PDF 인쇄 / 내보내기">
          <i data-lucide="printer"></i>
        </button>
        <button class="theme-toggle-btn" id="theme-toggle" title="다크/라이트 테마 변경">
          <i data-lucide="moon" id="theme-icon"></i>
        </button>
      </div>
    </div>

    <!-- Chapter Navigation Pills -->
    <div class="chapter-tabs-row" id="chapter-tabs-row">
'''

# Add tabs
for meta in chapters_meta:
    c_num = meta["num"]
    active_cls = "active" if c_num == 1 else ""
    html_template += f'''      <button class="ch-tab {active_cls}" data-ch="{c_num}">
        <i data-lucide="book-open"></i> {meta["short"]}
      </button>\n'''

html_template += '''      <button class="ch-tab all-view" data-ch="all">
        <i data-lucide="layers"></i> ★ 전체 연속보기 (All Chapters)
      </button>
    </div>
  </header>

  <!-- App Main Body Layout -->
  <div class="app-container">
    
    <!-- Sidebar Navigation -->
    <aside class="sidebar">
      <div class="sidebar-header">
        <div class="sidebar-title" id="sidebar-active-title">Ch 1. 재난 맥락에서의 사회연결망 분석 서설</div>
        <div class="sidebar-subtitle" id="sidebar-active-sub">Eric C. Jones & A.J. Faas | 은유적 vs 공식 네트워크, 잠재망 vs 실현망</div>
        <div class="sidebar-search">
          <i data-lucide="search"></i>
          <input type="text" id="sidebar-search-input" placeholder="목차 빠른 검색...">
        </div>
      </div>

      <div class="sidebar-nav-container">
        <div class="toc-label">Table of Contents</div>
'''

# Sidebar TOC containers per chapter
for ch in chapters_data:
    c_num = ch["meta"]["num"]
    disp = "block" if c_num == 1 else "none"
    html_template += f'''        <div class="chapter-toc-block" id="toc-ch-{c_num}" style="display: {disp};">
          <ul class="toc-list">
{ch["toc"]}
          </ul>
        </div>\n'''

# Sidebar All-Chapters Accordion TOC
html_template += '''        <div class="chapter-toc-block" id="toc-ch-all" style="display: none;">
          <ul class="toc-list">
'''
for ch in chapters_data:
    c_num = ch["meta"]["num"]
    html_template += f'''            <li class="toc-item" style="margin-top: 0.6rem; border-top: 1px solid var(--border-color); padding-top: 0.4rem;">
              <a href="#ch{c_num}-content" style="font-weight: 700; color: var(--accent-primary);">
                <i data-lucide="bookmark"></i> Chapter {c_num}. {ch["meta"]["short"]}
              </a>
            </li>
{ch["toc"]}
'''

html_template += '''          </ul>
        </div>
      </div>
    </aside>

    <!-- Main Content Wrapper -->
    <main class="main-wrapper" id="main-scroll-wrapper">
'''

# Content Boxes per chapter
for i, ch in enumerate(chapters_data):
    c_num = ch["meta"]["num"]
    active_cls = "active" if c_num == 1 else ""
    prev_num = c_num - 1 if c_num > 1 else None
    next_num = c_num + 1 if c_num < 9 else None

    prev_btn_html = f'''<button class="chapter-switch-btn" onclick="switchChapter({prev_num})">
      <i data-lucide="arrow-left"></i> 이전: Ch {prev_num}
    </button>''' if prev_num else '<div></div>'

    if next_num:
        next_btn_html = f'''<button class="chapter-switch-btn" onclick="switchChapter({next_num})">
          다음: Ch {next_num} <i data-lucide="arrow-right"></i>
        </button>'''
    else:
        next_btn_html = f'''<a href="chapter10_subnote.html" class="chapter-switch-btn primary">
          다음: Ch 10 원촨 대지진 <i data-lucide="arrow-right"></i>
        </a>'''

    html_template += f'''      <!-- CHAPTER {c_num} CONTENT BOX -->
      <div class="chapter-view-box {active_cls}" id="ch{c_num}-content" data-ch="{c_num}">
{ch["content"]}

        <!-- Integrated Chapter Switcher Footer -->
        <div class="integrated-chapter-footer">
          {prev_btn_html}
          <div style="font-size:0.8rem; color:var(--text-dim); font-weight:600;">
            Chapter {c_num} of 9 (LMS Integrated Compendium)
          </div>
          {next_btn_html}
        </div>
      </div>\n'''

html_template += '''    </main>
  </div>

  <script>
    // Initialize Lucide Icons
    lucide.createIcons();

    // Chapter metadata for dynamic header update
    const chaptersMeta = ''' + str(chapters_meta).replace("'", '"') + ''';

    let currentCh = 1;

    function switchChapter(ch) {
      const tabs = document.querySelectorAll('.ch-tab');
      const contentBoxes = document.querySelectorAll('.chapter-view-box');
      const tocBlocks = document.querySelectorAll('.chapter-toc-block');
      const sideTitle = document.getElementById('sidebar-active-title');
      const sideSub = document.getElementById('sidebar-active-sub');

      currentCh = ch;

      // Update tabs active class
      tabs.forEach(tab => {
        if (tab.getAttribute('data-ch') == ch) {
          tab.classList.add('active');
        } else {
          tab.classList.remove('active');
        }
      });

      if (ch === 'all') {
        document.body.classList.add('show-all-chapters');
        contentBoxes.forEach(box => box.classList.add('active'));
        tocBlocks.forEach(b => b.style.display = 'none');
        document.getElementById('toc-ch-all').style.display = 'block';
        sideTitle.innerText = "전체 9개 챕터 연속 보기";
        sideSub.innerText = "Part I, Part II & Part III 총서 전체 스크롤 및 통합 검색 모드";
      } else {
        document.body.classList.remove('show-all-chapters');
        contentBoxes.forEach(box => {
          if (box.getAttribute('data-ch') == ch) {
            box.classList.add('active');
          } else {
            box.classList.remove('active');
          }
        });
        tocBlocks.forEach(b => b.style.display = 'none');
        const targetToc = document.getElementById(`toc-ch-${ch}`);
        if (targetToc) targetToc.style.display = 'block';

        const meta = chaptersMeta.find(m => m.num == ch);
        if (meta) {
          sideTitle.innerText = meta.title;
          sideSub.innerText = `${meta.authors} | ${meta.subject}`;
        }
      }

      // Scroll top smoothly
      window.scrollTo({ top: 0, behavior: 'smooth' });

      // Re-typeset MathJax if necessary
      if (window.MathJax && window.MathJax.typesetPromise) {
        window.MathJax.typesetPromise();
      }

      // Re-create icons in active view
      lucide.createIcons();
    }

    // Attach click listeners to tabs
    document.querySelectorAll('.ch-tab').forEach(tab => {
      tab.addEventListener('click', () => {
        const ch = tab.getAttribute('data-ch');
        switchChapter(ch);
      });
    });

    // Theme Toggle
    const themeBtn = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');
    let isLight = localStorage.getItem('sna_theme') === 'light';

    function applyTheme() {
      if (isLight) {
        document.documentElement.setAttribute('data-theme', 'light');
        themeIcon.setAttribute('data-lucide', 'sun');
      } else {
        document.documentElement.removeAttribute('data-theme');
        themeIcon.setAttribute('data-lucide', 'moon');
      }
      lucide.createIcons();
    }
    applyTheme();

    themeBtn.addEventListener('click', () => {
      isLight = !isLight;
      localStorage.setItem('sna_theme', isLight ? 'light' : 'dark');
      applyTheme();
    });

    // Print Button
    document.getElementById('print-btn').addEventListener('click', () => {
      window.print();
    });

    // Reading Progress Bar
    window.addEventListener('scroll', () => {
      const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
      document.getElementById('progress-bar').style.width = scrolled + '%';
    });

    // Sidebar Live Search
    const searchInput = document.getElementById('sidebar-search-input');
    searchInput.addEventListener('input', (e) => {
      const term = e.target.value.toLowerCase();
      const activeTocContainer = (currentCh === 'all') 
        ? document.getElementById('toc-ch-all') 
        : document.getElementById(`toc-ch-${currentCh}`);
      
      if (!activeTocContainer) return;

      const links = activeTocContainer.querySelectorAll('li');
      links.forEach(li => {
        const text = li.innerText.toLowerCase();
        li.style.display = text.includes(term) ? '' : 'none';
      });
    });
  </script>
</body>
</html>'''

out_path = "sna_integrated_subnote.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"Integrated file created at {out_path} (size: {os.path.getsize(out_path)/(1024*1024):.2f} MB)")

# Also save index.html in subnote directory
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)
print("subnote/index.html also created.")
