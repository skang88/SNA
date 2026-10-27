# -*- coding: utf-8 -*-
"""
Build Chapter 8 Subnote HTML with 100% completeness (no abbreviation).
Matches subnote/chapter8-subnote.md exactly with premium styling.
"""

import os

html_content = r"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>재난관리연구방법론 | Chapter 8. 허리케인 아이크가 개인 네트워크 연계 활성화에 미친 영향</title>
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Noto+Sans+KR:wght@300;400;500;700;900&family=Outfit:wght@400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  
  <!-- MathJax Configuration & Script -->
  <script>
    window.MathJax = {
      tex: {
        inlineMath: [['$', '$'], ['\\(', '\\)']],
        displayMath: [['$$', '$$'], ['\\[', '\\]']]
      },
      options: {
        skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre']
      }
    };
  </script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <!-- Lucide Icons CDN -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <!-- Mermaid JS for diagrams -->
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      if (typeof mermaid !== 'undefined') {
        try {
          mermaid.initialize({ 
            startOnLoad: true, 
            theme: 'dark',
            securityLevel: 'loose',
            fontFamily: 'Noto Sans KR, Inter, sans-serif'
          });
        } catch(e) {
          console.warn('Mermaid initialization deferred:', e);
        }
      }
    });
  </script>

  <style>
    :root {
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
      --glass-bg: rgba(19, 28, 49, 0.85);
      --glass-border: rgba(255, 255, 255, 0.08);
      --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.25);
      --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.35);
      --shadow-lg: 0 12px 30px -6px rgba(0, 0, 0, 0.5);
      --radius: 12px;
      --radius-sm: 8px;
      --radius-lg: 16px;
      --transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    }

    [data-theme="light"] {
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
      --glass-bg: rgba(255, 255, 255, 0.9);
      --glass-border: rgba(0, 0, 0, 0.08);
      --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.06);
      --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.08);
      --shadow-lg: 0 12px 30px -6px rgba(0, 0, 0, 0.1);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
    }

    body {
      font-family: 'Noto Sans KR', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-primary);
      color: var(--text-main);
      line-height: 1.85;
      transition: background-color 0.3s ease, color 0.3s ease;
      min-height: 100vh;
    }

    #progress-bar {
      position: fixed;
      top: 0;
      left: 0;
      height: 3px;
      background: linear-gradient(90deg, var(--accent-primary), var(--accent-emerald), var(--accent-amber));
      width: 0%;
      z-index: 1000;
      transition: width 0.1s ease-out;
    }

    .app-layout {
      display: flex;
      min-height: 100vh;
      position: relative;
    }

    /* LEFT SIDEBAR */
    .sidebar {
      width: var(--sidebar-width);
      flex-shrink: 0;
      height: 100vh;
      position: sticky;
      top: 0;
      background: var(--bg-sidebar);
      border-right: 1px solid var(--border-color);
      display: flex;
      flex-direction: column;
      z-index: 100;
      box-shadow: var(--shadow-sm);
    }

    .sidebar-header {
      padding: 1.5rem 1.25rem 1rem 1.25rem;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .sidebar-brand {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .brand-badge {
      background: linear-gradient(135deg, var(--accent-primary), var(--accent-emerald));
      color: #ffffff;
      font-weight: 800;
      font-size: 0.75rem;
      padding: 0.25rem 0.65rem;
      border-radius: 6px;
      letter-spacing: 0.5px;
    }

    .theme-toggle-btn {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 0.45rem;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: var(--transition);
      width: 34px;
      height: 34px;
    }

    .theme-toggle-btn:hover {
      background: var(--bg-card-hover);
      color: var(--accent-primary);
      transform: rotate(15deg);
    }

    .sidebar-title {
      font-family: 'Outfit', 'Noto Sans KR', sans-serif;
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text-main);
      line-height: 1.35;
    }

    .sidebar-subtitle {
      font-size: 0.8rem;
      color: var(--text-muted);
      font-weight: 500;
    }

    .sidebar-search {
      position: relative;
      margin-top: 0.25rem;
    }

    .sidebar-search input {
      width: 100%;
      padding: 0.5rem 0.75rem 0.5rem 2.2rem;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-color);
      background: var(--bg-secondary);
      color: var(--text-main);
      font-size: 0.85rem;
      outline: none;
      transition: var(--transition);
    }

    .sidebar-search input:focus {
      border-color: var(--accent-primary);
      box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.2);
    }

    .sidebar-search i {
      position: absolute;
      left: 0.75rem;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-dim);
      width: 16px;
      height: 16px;
    }

    .sidebar-nav-container {
      flex: 1;
      overflow-y: auto;
      padding: 1rem 0.75rem;
    }

    .sidebar-nav-container::-webkit-scrollbar {
      width: 5px;
    }
    .sidebar-nav-container::-webkit-scrollbar-thumb {
      background: var(--border-color);
      border-radius: 4px;
    }

    .toc-label {
      font-size: 0.7rem;
      font-weight: 800;
      color: var(--text-dim);
      letter-spacing: 1px;
      margin-bottom: 0.75rem;
      padding-left: 0.5rem;
    }

    .toc-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
    }

    .toc-item a {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      padding: 0.45rem 0.65rem;
      border-radius: var(--radius-sm);
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.825rem;
      font-weight: 500;
      transition: var(--transition);
    }

    .toc-item.sub-toc a {
      padding-left: 1.75rem;
      font-size: 0.785rem;
      color: var(--text-dim);
    }

    .toc-item a:hover {
      background: var(--bg-card-hover);
      color: var(--accent-primary);
    }

    .toc-item.active a {
      background: rgba(56, 189, 248, 0.12);
      color: var(--accent-primary);
      font-weight: 600;
      border-left: 3px solid var(--accent-primary);
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
    }

    .toc-badge {
      margin-left: auto;
      font-size: 0.7rem;
      font-family: 'JetBrains Mono', monospace;
      color: var(--text-dim);
      background: var(--bg-card);
      padding: 0.1rem 0.4rem;
      border-radius: 4px;
    }

    .sidebar-footer {
      padding: 1rem 1.25rem;
      border-top: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 0.8rem;
      color: var(--text-dim);
    }

    .sidebar-footer a {
      color: var(--accent-primary);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 0.3rem;
    }

    /* MAIN CONTENT */
    .main-wrapper {
      flex: 1;
      min-width: 0;
      display: flex;
      flex-direction: column;
    }

    .top-header {
      position: sticky;
      top: 0;
      height: 60px;
      background: var(--glass-bg);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 2rem;
      z-index: 90;
    }

    .breadcrumbs {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.85rem;
      color: var(--text-dim);
    }

    .breadcrumbs a {
      color: var(--text-muted);
      text-decoration: none;
    }

    .breadcrumbs a:hover {
      color: var(--accent-primary);
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .action-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.4rem 0.85rem;
      border-radius: var(--radius-sm);
      font-size: 0.825rem;
      font-weight: 600;
      text-decoration: none;
      transition: var(--transition);
      cursor: pointer;
      border: 1px solid var(--border-color);
      background: var(--bg-secondary);
      color: var(--text-main);
    }

    .action-btn:hover {
      background: var(--bg-card-hover);
      border-color: var(--accent-primary);
      color: var(--accent-primary);
    }

    .action-btn.primary {
      background: var(--accent-primary);
      color: #0b1120;
      border-color: var(--accent-primary);
    }

    .action-btn.primary:hover {
      background: #7dd3fc;
    }

    .content-container {
      max-width: 1040px;
      width: 100%;
      margin: 0 auto;
      padding: 2.5rem 2rem 5rem 2rem;
    }

    /* CHAPTER HERO */
    .chapter-hero {
      background: linear-gradient(135deg, rgba(30, 41, 59, 0.7), rgba(15, 23, 42, 0.9));
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 2.5rem;
      margin-bottom: 2.5rem;
      position: relative;
      overflow: hidden;
      box-shadow: var(--shadow-lg);
    }

    .chapter-hero::before {
      content: '';
      position: absolute;
      top: -50px;
      right: -50px;
      width: 200px;
      height: 200px;
      background: radial-gradient(circle, rgba(56, 189, 248, 0.2) 0%, transparent 70%);
      border-radius: 50%;
      pointer-events: none;
    }

    .hero-meta {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-bottom: 1rem;
      flex-wrap: wrap;
    }

    .hero-tag {
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.2rem 0.6rem;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .tag-ch {
      background: rgba(56, 189, 248, 0.15);
      color: var(--accent-primary);
      border: 1px solid rgba(56, 189, 248, 0.3);
    }

    .tag-peer {
      background: rgba(52, 211, 153, 0.15);
      color: var(--accent-emerald);
      border: 1px solid rgba(52, 211, 153, 0.3);
    }

    .hero-title {
      font-family: 'Outfit', 'Noto Sans KR', sans-serif;
      font-size: 1.85rem;
      font-weight: 800;
      line-height: 1.35;
      color: var(--text-main);
      margin-bottom: 0.75rem;
    }

    .hero-original-title {
      font-size: 0.95rem;
      color: var(--accent-secondary);
      font-weight: 500;
      margin-bottom: 1.25rem;
      line-height: 1.5;
    }

    .author-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1rem;
      margin-top: 1.5rem;
      padding-top: 1.5rem;
      border-top: 1px solid var(--border-color);
    }

    .author-card {
      display: flex;
      flex-direction: column;
      gap: 0.2rem;
    }

    .author-name {
      font-weight: 700;
      font-size: 0.9rem;
      color: var(--text-main);
    }

    .author-affil {
      font-size: 0.8rem;
      color: var(--text-muted);
    }

    .hero-footer-info {
      margin-top: 1.25rem;
      font-size: 0.8rem;
      color: var(--text-dim);
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
    }

    .hero-footer-info span {
      display: flex;
      align-items: center;
      gap: 0.35rem;
    }

    /* SECTION BLOCK */
    .section-block {
      margin-bottom: 3.5rem;
      scroll-margin-top: 80px;
    }

    .section-title {
      font-family: 'Outfit', 'Noto Sans KR', sans-serif;
      font-size: 1.4rem;
      font-weight: 800;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 0.65rem;
      margin-bottom: 1.5rem;
      padding-bottom: 0.75rem;
      border-bottom: 2px solid var(--border-color);
    }

    .section-title i {
      color: var(--accent-primary);
    }

    .subsection-block {
      margin-bottom: 2.25rem;
      scroll-margin-top: 80px;
    }

    .subsection-title {
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--accent-secondary);
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    /* PARAGRAPH CARD */
    .para-card {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 1.5rem 1.75rem;
      margin-bottom: 1.5rem;
      box-shadow: var(--shadow-sm);
      transition: var(--transition);
    }

    .para-card:hover {
      border-color: rgba(56, 189, 248, 0.4);
      box-shadow: var(--shadow-md);
    }

    .para-header {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--accent-secondary);
      margin-bottom: 0.75rem;
      padding-bottom: 0.5rem;
      border-bottom: 1px dashed var(--border-color);
    }

    .para-content {
      font-size: 0.95rem;
      color: var(--text-main);
      line-height: 1.85;
    }

    .para-content p {
      margin-bottom: 0.75rem;
    }

    .para-content p:last-child {
      margin-bottom: 0;
    }

    .para-content ul, .para-content ol {
      margin-left: 1.5rem;
      margin-top: 0.5rem;
      margin-bottom: 0.75rem;
    }

    .para-content li {
      margin-bottom: 0.45rem;
    }

    /* CALLOUT BOX / NOTE CARD */
    .callout-box {
      background: rgba(30, 41, 59, 0.65);
      border-left: 4px solid var(--accent-primary);
      border-top: 1px solid var(--border-color);
      border-right: 1px solid var(--border-color);
      border-bottom: 1px solid var(--border-color);
      border-radius: 0 var(--radius) var(--radius) 0;
      padding: 1.5rem 1.75rem;
      margin: 2rem 0;
    }

    .callout-title {
      font-size: 1rem;
      font-weight: 700;
      color: var(--accent-primary);
      display: flex;
      align-items: center;
      gap: 0.5rem;
      margin-bottom: 0.75rem;
    }

    .callout-content {
      font-size: 0.92rem;
      color: var(--text-muted);
      line-height: 1.8;
    }

    /* FIGURES & TABLES */
    .figure-container {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 1.5rem;
      margin: 2rem 0;
      text-align: center;
      box-shadow: var(--shadow-md);
    }

    .figure-container img {
      max-width: 100%;
      height: auto;
      border-radius: var(--radius-sm);
      margin-bottom: 1rem;
      border: 1px solid var(--border-color);
      background: #ffffff;
    }

    .figure-caption {
      font-size: 0.85rem;
      color: var(--text-muted);
      font-style: italic;
      line-height: 1.6;
      text-align: left;
      padding: 0.5rem 0.75rem;
      background: var(--bg-card);
      border-radius: var(--radius-sm);
    }

    .table-container {
      overflow-x: auto;
      margin: 2rem 0;
      border-radius: var(--radius);
      border: 1px solid var(--border-color);
      background: var(--bg-secondary);
      box-shadow: var(--shadow-md);
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.875rem;
      text-align: left;
    }

    th {
      background: var(--bg-card);
      color: var(--text-main);
      font-weight: 700;
      padding: 0.85rem 1rem;
      border-bottom: 2px solid var(--border-color);
      white-space: nowrap;
    }

    td {
      padding: 0.75rem 1rem;
      border-bottom: 1px solid var(--border-color);
      color: var(--text-main);
      vertical-align: middle;
    }

    tr:last-child td {
      border-bottom: none;
    }

    tr:hover td {
      background: var(--bg-card-hover);
    }

    .sig-star {
      color: var(--accent-rose);
      font-weight: 800;
    }

    /* MERMAID DIAGRAM BOX */
    .mermaid-box {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 1.75rem 1.5rem;
      margin: 2rem 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      box-shadow: var(--shadow-md);
    }

    .mermaid-caption {
      font-size: 0.85rem;
      color: var(--text-muted);
      font-weight: 600;
      margin-top: 1rem;
      text-align: center;
    }

    /* EQUATION BOX */
    .eq-box {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 1.5rem;
      margin: 1.5rem 0;
      text-align: center;
      box-shadow: var(--shadow-sm);
    }

    /* BADGES */
    .badge-pill {
      display: inline-block;
      padding: 0.15rem 0.5rem;
      border-radius: 9999px;
      font-size: 0.725rem;
      font-weight: 700;
      margin-right: 0.35rem;
    }
    .badge-blue { background: rgba(56, 189, 248, 0.2); color: var(--accent-primary); }
    .badge-green { background: rgba(52, 211, 153, 0.2); color: var(--accent-emerald); }
    .badge-amber { background: rgba(251, 191, 36, 0.2); color: var(--accent-amber); }
    .badge-rose { background: rgba(251, 113, 133, 0.2); color: var(--accent-rose); }

    @media (max-width: 1024px) {
      .sidebar {
        display: none;
      }
      .content-container {
        padding: 2rem 1.5rem 4rem 1.5rem;
      }
    }
  </style>
</head>
<body>
  <div id="progress-bar"></div>

  <div class="app-layout">
    <!-- LEFT SIDEBAR -->
    <aside class="sidebar">
      <div class="sidebar-header">
        <div class="sidebar-brand">
          <span class="brand-badge">SNA RESEARCH</span>
          <button class="theme-toggle-btn" id="theme-toggle" title="테마 전환">
            <i data-lucide="moon" id="theme-icon"></i>
          </button>
        </div>
        <div class="sidebar-title">제8장 개인망 연계 활성화</div>
        <div class="sidebar-subtitle">Marcum, Wilkinson, & Koehly (2017)</div>
        
        <div class="sidebar-search">
          <i data-lucide="search"></i>
          <input type="text" id="search-input" placeholder="목차 및 키워드 검색...">
        </div>
      </div>

      <div class="sidebar-nav-container">
        <div class="toc-label">CHAPTER OUTLINE</div>
        <ul class="toc-list" id="toc-list">
          <li class="toc-item active"><a href="#sec-intro"><i data-lucide="book-open"></i>1. 서론 (Introduction) <span class="toc-badge">p.113</span></a></li>
          <li class="toc-item"><a href="#sec-event"><i data-lucide="cloud-lightning"></i>2. 가족 맥락의 재난 사건 <span class="toc-badge">p.114</span></a></li>
          <li class="toc-item"><a href="#sec-support"><i data-lucide="shield"></i>3. 재난 후 지지의 원천 <span class="toc-badge">p.115</span></a></li>
          <li class="toc-item sub-toc"><a href="#subsec-family"><i data-lucide="chevron-right"></i>1) 가족 지지 (Family Support) <span class="toc-badge">p.115</span></a></li>
          <li class="toc-item sub-toc"><a href="#subsec-other-rel"><i data-lucide="chevron-right"></i>2) 기타 유형의 관계 <span class="toc-badge">p.116</span></a></li>
          <li class="toc-item sub-toc"><a href="#subsec-space"><i data-lucide="chevron-right"></i>3) 공간을 초월한 연계 <span class="toc-badge">p.116</span></a></li>
          <li class="toc-item sub-toc"><a href="#subsec-coping"><i data-lucide="chevron-right"></i>4) 네트워크와 대처 <span class="toc-badge">p.117</span></a></li>
          <li class="toc-item"><a href="#sec-methods"><i data-lucide="database"></i>4. 데이터 및 연구 방법 <span class="toc-badge">p.118</span></a></li>
          <li class="toc-item sub-toc"><a href="#subsec-sample"><i data-lucide="chevron-right"></i>1) 표본 및 자료수집 <span class="toc-badge">p.118</span></a></li>
          <li class="toc-item sub-toc"><a href="#subsec-periods"><i data-lucide="chevron-right"></i>2) 자연실험 시기 구분 <span class="toc-badge">p.119</span></a></li>
          <li class="toc-item sub-toc"><a href="#subsec-dyads"><i data-lucide="chevron-right"></i>3) 호의 교환 다이애드 구성 <span class="toc-badge">p.119</span></a></li>
          <li class="toc-item sub-toc"><a href="#subsec-models"><i data-lucide="chevron-right"></i>4) 통계 분석 모형 <span class="toc-badge">p.119</span></a></li>
          <li class="toc-item"><a href="#sec-results"><i data-lucide="bar-chart-2"></i>5. 실증 분석 결과 <span class="toc-badge">p.119</span></a></li>
          <li class="toc-item sub-toc"><a href="#subsec-res-demo"><i data-lucide="chevron-right"></i>1) 표본 인구통계 동질성 <span class="toc-badge">p.119</span></a></li>
          <li class="toc-item sub-toc"><a href="#subsec-res-h1"><i data-lucide="chevron-right"></i>2) 가설 1 (네트워크 규모) <span class="toc-badge">p.120</span></a></li>
          <li class="toc-item sub-toc"><a href="#subsec-res-h2"><i data-lucide="chevron-right"></i>3) 가설 2 (친족/친구 분화) <span class="toc-badge">p.121</span></a></li>
          <li class="toc-item sub-toc"><a href="#subsec-res-h3"><i data-lucide="chevron-right"></i>4) 가설 3 (호의 교환 상호성) <span class="toc-badge">p.122</span></a></li>
          <li class="toc-item"><a href="#sec-tables-figures"><i data-lucide="layout"></i>6. 표 및 그림 정밀 분석 <span class="toc-badge">자료</span></a></li>
          <li class="toc-item sub-toc"><a href="#subsec-table81"><i data-lucide="chevron-right"></i>Table 8.1 기술통계표 <span class="toc-badge">p.120</span></a></li>
          <li class="toc-item sub-toc"><a href="#subsec-table82"><i data-lucide="chevron-right"></i>Table 8.2 규모 선형회귀표 <span class="toc-badge">p.121</span></a></li>
          <li class="toc-item sub-toc"><a href="#subsec-fig81"><i data-lucide="chevron-right"></i>Figure 8.1 평균차이 t-test <span class="toc-badge">p.121</span></a></li>
          <li class="toc-item sub-toc"><a href="#subsec-table83"><i data-lucide="chevron-right"></i>Table 8.3 호의 로그선형 잔차표 <span class="toc-badge">p.122</span></a></li>
          <li class="toc-item"><a href="#sec-discussion"><i data-lucide="message-square"></i>7. 논의 및 학술적 시사점 <span class="toc-badge">p.123</span></a></li>
          <li class="toc-item"><a href="#sec-template"><i data-lucide="file-text"></i>8. 선행연구 9단계 템플릿 <span class="toc-badge">부록</span></a></li>
          <li class="toc-item"><a href="#sec-fire-application"><i data-lucide="flame"></i>★ 9. 내 연구 적용: 소방 지지망 연구 <span class="toc-badge">적용</span></a></li>
        </ul>
      </div>

      <div class="sidebar-footer">
        <span>SNA Sub-Note Series</span>
        <a href="chapter7_subnote.html"><i data-lucide="arrow-left"></i> Ch.7 이동</a>
      </div>
    </aside>

    <!-- MAIN CONTENT -->
    <div class="main-wrapper">
      <header class="top-header">
        <div class="breadcrumbs">
          <a href="index.html">SNA Home</a>
          <i data-lucide="chevron-right" style="width:14px; height:14px;"></i>
          <span>Chapter 8</span>
          <i data-lucide="chevron-right" style="width:14px; height:14px;"></i>
          <span style="color:var(--text-main);">Sub-Note (완전판)</span>
        </div>
        <div class="header-actions">
          <a href="chapter8-원문.md" class="action-btn"><i data-lucide="file-code"></i> 원문 마크다운</a>
          <a href="chapter8-subnote.md" class="action-btn"><i data-lucide="file-text"></i> 서브노트 MD</a>
          <a href="index.html" class="action-btn primary"><i data-lucide="grid"></i> 통합 포털</a>
        </div>
      </header>

      <main class="content-container">
        <!-- CHAPTER HERO -->
        <div class="chapter-hero">
          <div class="hero-meta">
            <span class="hero-tag tag-ch">Chapter 8</span>
            <span class="hero-tag tag-peer">Natural Experiment & Personal Network</span>
            <span class="hero-tag" style="background:rgba(192,132,252,0.15); color:var(--accent-purple); border:1px solid rgba(192,132,252,0.3);">Communal Coping & Equity</span>
          </div>
          <h1 class="hero-title">제8장 허리케인 아이크가 개인 네트워크 연계 활성화에 미친 영향: 대응 및 복구 단계의 전개 과정 (Sub-Note)</h1>
          <div class="hero-original-title">
            THE EFFECT OF HURRICANE IKE ON PERSONAL NETWORK TIE ACTIVATION AS RESPONSE AND RECOVERY UNFOLDED
          </div>
          <div class="author-grid">
            <div class="author-card">
              <span class="author-name">Christopher Steven Marcum<sup>1</sup></span>
              <span class="author-affil">National Institutes of Health, Bethesda, MD, United States</span>
            </div>
            <div class="author-card">
              <span class="author-name">Anna V. Wilkinson<sup>2</sup></span>
              <span class="author-affil">University of Texas Health Science Center at Houston, Houston, TX, United States</span>
            </div>
            <div class="author-card">
              <span class="author-name">Laura M. Koehly<sup>1</sup></span>
              <span class="author-affil">National Institutes of Health, Bethesda, MD, United States</span>
            </div>
          </div>
          <div class="hero-footer-info">
            <span><i data-lucide="book" style="width:14px; height:14px;"></i> <em>Social Network Analysis of Disaster Response, Recovery, and Adaptation</em> (Elsevier, 2017)</span>
            <span><i data-lucide="compass" style="width:14px; height:14px;"></i> pp. 113–126</span>
            <span><i data-lucide="link" style="width:14px; height:14px;"></i> DOI: http://dx.doi.org/10.1016/B978-0-12-805196-2.00008-X</span>
          </div>
        </div>

        <!-- 1. 서론 및 이론적 배경 -->
        <section class="section-block" id="sec-intro">
          <h2 class="section-title"><i data-lucide="book-open"></i> 1. 서론 및 이론적 배경 (INTRODUCTION) <span class="toc-badge">pp. 113–114</span></h2>

          <div class="para-card">
            <div class="para-header"><i data-lucide="info"></i> [문단 1] 재난과 사회구조의 동태적 교란, 개인 네트워크 연구의 공백</div>
            <div class="para-content">
              <p>재난(Disasters)은 시간에 따라 전개되는 규범적 과정(normative processes)을 파괴함으로써 사회구조(social structure)가 어떻게 영향을 받는지 규명할 수 있는 최적의 연구 환경(opportune settings)을 제공합니다(Drabek, 1986).</p>
              <ul>
                <li><strong>잠재적 연계의 활성화(Activation of Latent Ties)</strong>: 재난 피해 주민들에게 이러한 충격은 사회연결망 경로를 따라 급속히 파급되며, 개인들은 긴급한 지원 요청에 부응하기 위해 평소 휴면 상태(dormant)로 유지되던 관계망을 호출하고 활성화(reaching out and activating ties)하게 됩니다(Smith & McCarty, 1996).</li>
                <li><strong>기존 연구 경향</strong>: 과거 재난 대응 연구는 주로 피난 이동 패턴(Drabek & Boggs, 1968; Gray & Mueller, 2012), 피해 지역 인구통계학적 구성 변화(Donner & Rodríguez, 2008; Smith & McCarty, 1996), 피난 시점(Huang et al., 2012; Ng et al., 2015), 사회적 지지를 통한 적응(Norris & Kaniasty, 1996) 등을 탐구해 왔습니다.</li>
                <li><strong>연구의 공백(Research Gap)</strong>: 그러나 재난이 <strong>가족 내 개인 네트워크(personal networks within families)</strong>에 미치는 구체적 영향에 대해서는 거의 알려져 있지 않습니다. 기존 재난 네트워크 연구는 개인망이든 전체망이든 네트워크를 '원인(독립변수)'으로만 다루었을 뿐, <strong>재난 충격에 따라 네트워크 자체가 어떻게 변화하는가(종속변수/결과변수)</strong>에 대한 실증적 탐색은 매우 드뭅니다.</li>
              </ul>
            </div>
          </div>

          <div class="para-card">
            <div class="para-header"><i data-lucide="sparkles"></i> [문단 2] 자연실험(Natural Experiment)으로서의 연구 설계 기회</div>
            <div class="para-content">
              <p>본 연구는 자연에 의해 실험군과 대조군 조건이 부여된 실증적 시나리오인 <strong>자연실험(Natural Experiment)</strong>(Dunning, 2012)을 활용합니다.</p>
              <ul>
                <li><strong>연구 배경</strong>: 2008년 여름~가을, 연구팀은 미국 텍사스주 그레이터 휴스턴(Greater Houston) 지역에 거주하는 멕시코계 가족(Mexican-origin families)을 대상으로 다중 정보제공자 종단적 가족 네트워크 조사(Project RAMA)를 진행하고 있었습니다.</li>
                <li><strong>허리케인 아이크(Hurricane Ike)의 급습</strong>: 대상자 모집 및 데이터 수집 도중 2등급 대형 허리케인 아이크가 해당 지역을 강타했습니다.</li>
                <li><strong>연구 기회</strong>: 재난 충격은 예측 불가능하여 개인 네트워크 수준에서 종단적 비교를 수행하기 극히 어렵지만, 기존에 진행 중이던 대규모 코호트 조사 도중 허리케인이 우연히 겹침으로써 재난 발생 전, 중, 후의 개인망 변화를 체계적으로 추적할 수 있는 독보적인 자연실험 데이터가 확보되었습니다(Butts et al., 2012).</li>
              </ul>
            </div>
          </div>

          <div class="para-card">
            <div class="para-header"><i data-lucide="target"></i> [문단 3] 3대 핵심 가설(Hypotheses) 수립</div>
            <div class="para-content">
              <p>연구진은 재난 대응 과정에서 개인들이 로컬 및 원거리 구성원 모두와 접촉하면서 잠재적 연계를 활성화한다고 상정하고, <strong>사전(Predisaster) - 대응(Response) - 복구(Recovery)</strong>의 3시기에 걸쳐 3가지 핵심 가설을 검정합니다:</p>
              <ol>
                <li><strong>가설 1 (H1: 네트워크 규모 확대)</strong>: 재난 대응기(Response period)에 응답자들은 사전 단계나 복구 단계에 비해 <strong>평균적으로 더 많은 수의 개인 네트워크 구성원(alters)을 열거할 것이다.</strong></li>
                <li><strong>가설 2 (H2: 친족 관계 유형의 차별적 활성화)</strong>: 재난 대응기에는 1차 친족(부모, 자녀, 배우자)이나 비친족(친구)보다 <strong>원거리 2차 친족(삼촌, 이모, 고모 등)</strong>이 상대적으로 더 많이 열거될 것이다.</li>
                <li><strong>가설 3 (H3: 상호적 호의 교환의 확률적 초과)</strong>: 재난 대응기에는 우연(기저확률)에 의한 기댓값보다 <strong>더 많은 상호적 호의(reciprocal favors) 교환이 발생할 것</strong>이며, 재난 사전 및 복구 단계에서는 유의한 이탈이 없을 것이다.</li>
              </ol>
            </div>
          </div>
        </section>

        <!-- 2. THE EVENT IN FAMILY CONTEXT -->
        <section class="section-block" id="sec-event">
          <h2 class="section-title"><i data-lucide="cloud-lightning"></i> 2. 가족 맥락에서의 재난 사건 (THE EVENT IN FAMILY CONTEXT) <span class="toc-badge">pp. 114–115</span></h2>

          <div class="para-card">
            <div class="para-header"><i data-lucide="alert-triangle"></i> [문단 1] 허리케인 아이크의 피해 규모와 가족 수준의 충격</div>
            <div class="para-content">
              <ul>
                <li><strong>상륙 시점 및 경로</strong>: 2008년 9월 13일 이른 아침, 허리케인 아이크(카테고리 2)가 텍사스주 갤버스턴 섬(Galveston Island)에 상륙한 후 북동쪽 휴스턴으로 진입했습니다(Emmett, 2013).</li>
                <li><strong>물적·인적 피해</strong>: 약 100만 명의 이재민이 발생했고, 갤버스턴 및 해리스 카운티에서만 최소 3,500가구가 즉시 파괴되어 홈리스가 되었습니다. 피해액은 약 380억 달러로, 카트리나($1,250억), 샌디($710억)에 이어 미국 역사상 세 번째로 큰 재산 피해를 기록했습니다. 미국 내 사망자는 195명(휴스턴-갤버스턴 일대 74명)이었습니다(Zane et al., 2011).</li>
              </ul>
            </div>
          </div>

          <div class="para-card">
            <div class="para-header"><i data-lucide="users"></i> [문단 2] 대피 결정에서의 사회연결망 역할</div>
            <div class="para-content">
              <ul>
                <li><strong>대피 명령과 잔류 선택</strong>: 텍사스 주지사의 대피령과 국립기상청(NWS)의 극단적 경고 방송, 연방 비상사태 선포에도 불구하고 10만 명 이상의 주민들이 대피하지 않고 현장에 머물며 피난(shelter in place)을 선택했습니다(Cutter & Smith, 2009). 주택 소유 여부, 과거 경험, 가구 구조 등이 대피 판단에 복합적으로 작용했습니다(Adger et al., 2005; Riad et al., 1999).</li>
                <li><strong>가족 네트워크의 결정적 영향</strong>: Drabek & Boggs(1968)의 초기 연결망 연구에 따르면, <strong>의지할 수 있는 사회적 연결망(social ties)이 적을수록 대피할 가능성이 낮아졌으며, 대응 기간 동안 활용된 사회적 관계의 대다수는 '가족 구성원'이었습니다.</strong> 이는 재난 대응 시 확장된 가족 연계망이 활성화된다는 가설의 강력한 선행 근거가 됩니다.</li>
              </ul>
            </div>
          </div>

          <div class="para-card">
            <div class="para-header"><i data-lucide="clock"></i> [문단 3] 대응기에서 복구기로의 전환과 가족 연계의 부각</div>
            <div class="para-content">
              <ul>
                <li><strong>공식 대응기의 전개</strong>: 허리케인 상륙 후 즉각적 의사결정 외에도 공식적인 대응 국면은 수개월 동안 지속되었습니다. 연방재난관리청(FEMA)의 주거 복구 프로그램은 11월에야 시작되었으며, 이는 공식적으로 대응기에서 복구기로 전환되었음을 나타내는 지표입니다(Jadacki, 2011).</li>
                <li><strong>가족의 중요성(Salience of Family) 심화</strong>: 복구 기간 동안 개인들은 비상 연락처를 확인하고 단절되었던 가족 구성원들과 재회하려 노력하면서 광범위한 가족 네트워크에 대한 인식이 크게 높아집니다(Blake & Stevenson, 2009). 이러한 인지적·구조적 과정은 재난 전-중-후에 네트워크 자원을 동원하는 양상을 질적으로 분화시킵니다.</li>
              </ul>
            </div>
          </div>
        </section>

        <!-- 3. SOURCES OF SUPPORT FOLLOWING DISASTERS -->
        <section class="section-block" id="sec-support">
          <h2 class="section-title"><i data-lucide="shield"></i> 3. 재난 후 사회적 지지의 원천과 대처 (SOURCES OF SUPPORT) <span class="toc-badge">pp. 115–118</span></h2>

          <div class="subsection-block" id="subsec-family">
            <h3 class="subsection-title"><i data-lucide="home"></i> 1) Family Support (가족 지지) `[pp. 115–116]`</h3>
            <div class="para-card">
              <div class="para-content">
                <ul>
                  <li><strong>진정한 최초 대응자(True First Responders)</strong>: Enrico Quarantelli(1960)는 동거하는 직계 가족 구성원이야말로 진정한 최초 대응자라고 역설했습니다. 가족은 위기 시 서로의 안전을 평가하고, 구호를 제공하며, 집단(collective)으로서 대응합니다.</li>
                  <li><strong>지리적 근접성과 사회적 안전망</strong>: 가족은 물리적으로 가장 가까이에 상주하므로 재난 발생 시 지원을 제공할 수 있는 가장 가용성 높은 자원입니다(Sampson, 1991; Bales & Parsons, 1956). 전통적 사회학 연구에서도 가족은 위기 후 사회 보존, 피난 및 재결합, 경제적 적응의 핵심 단위로 다루어졌습니다(Fogleman & Parenton, 1959; Form et al., 1956; Killian, 1952; Litwak & Szelenyi, 1969; Drabek, 1969; Kunreuther, 1967).</li>
                </ul>
              </div>
            </div>
          </div>

          <div class="subsection-block" id="subsec-other-rel">
            <h3 class="subsection-title"><i data-lucide="users"></i> 2) Other Kinds of Relationships (기타 유형의 관계) `[p. 116]`</h3>
            <div class="para-card">
              <div class="para-content">
                <ul>
                  <li><strong>제2 방어선(Second Line)</strong>: 직계 가족을 넘어 확장 친족(extended kin), 친구, 이웃은 위기 극복의 필수적인 2차 방어선 역할을 수행합니다(Quarantelli, 1960).</li>
                  <li><strong>시간적 역할 분담</strong>: Drabek et al.(1975)과 Nigg(1995)에 따르면, <strong>직계 가족 연계는 긴급 대응기(response period)</strong>에 더 활발하게 가동되는 반면, <strong>확장 친족은 장기 복구기(recovery period)</strong>에 임시 주거, 육아, 식사, 재정적 지원 등 도구적 지원(instrumental support)을 제공하는 핵심 역할을 담당합니다(Casagrande et al., 2015; Kaniasty & Norris, 2000).</li>
                  <li><strong>심리적 지지와 친구의 역할</strong>: 걸프전 당시 이스라엘 하이파 미사일 공격 연구(Shavit et al., 1994)에서는 친구가 직계 가족보다 심리적 지지(psychological support) 제공에서 더 큰 역할을 수행했음이 확인되었습니다. 이웃 간의 강한 유대는 고베 지진 복구 만족도를 높이는 핵심 요인이었습니다(Nakagawa & Shaw, 2004).</li>
                </ul>
              </div>
            </div>
          </div>

          <div class="subsection-block" id="subsec-space">
            <h3 class="subsection-title"><i data-lucide="map-pin"></i> 3) Ties Across Space (공간을 초월한 연계) `[pp. 116–117]`</h3>
            <div class="para-card">
              <div class="para-content">
                <ul>
                  <li><strong>지리적 인접성(Propinquity)과 피난처 기능</strong>: 직계 가족은 지리적으로 가깝고, 확장 친족은 멀리 떨어져 있는 경우가 많습니다. 먼 친척은 평시에는 자주 접촉하지 않지만, <strong>지역 전체가 초토화된 재난 상황에서는 파괴된 환경을 탈출해 피난할 수 있는 안전한 안식처(evacuation destination)</strong>가 되기 때문에 긴급히 활성화됩니다(Lu et al., 2012; 2010년 아이티 지진 사례). 근거리 친구나 이웃은 스스로도 재난 피해를 수습하느라 지지 자원으로서의 가용성이 일시적으로 떨어집니다(Haines et al., 1996).</li>
                  <li><strong>불평등의 축(Axes of Inequality)</strong>: 반면 저소득층 및 이민자 가족의 경우, 원거리 친족과의 연계가 지리적·법적 장벽(국경, 추방 위험 등)으로 가로막혀 취약성이 가중됩니다(Tierney, 2006; Phillips et al., 1994; Foner & Dreby, 2011; Treas, 2008). 히스패닉 가족은 공식 대피소(24%)나 친구(13%)보다 친척 집으로 피난하는 비율(63%)이 비히스패닉 가족보다 월등히 높으며, 친족 네트워크 의존도가 높을수록 공식 기관에 대한 지원 의존도는 반비례하는 경향을 보입니다(Hurlbert et al., 2001).</li>
                </ul>
              </div>
            </div>
          </div>

          <div class="subsection-block" id="subsec-coping">
            <h3 class="subsection-title"><i data-lucide="refresh-cw"></i> 4) Networks and Coping (네트워크와 대처) `[pp. 117–118]`</h3>
            <div class="para-card">
              <div class="para-content">
                <ul>
                  <li><strong>공동 대처 이론(Communal Coping Theory)</strong>: 사회적 단위(가족 또는 공동체) 구성원들이 스트레스 사건을 개별 문제가 아닌 <strong>공동의 문제(common problem)</strong>로 인식하고 협력적 대처 행동을 취하는 이론입니다(Lyons et al., 1998; Lin et al., 1985; Schwarzer & Luszczynska, 2012; Schwarzer et al., 2014; Arnberg et al., 2012).</li>
                  <li><strong>상호적 교환(Reciprocal Exchange)</strong>: 공동 대처는 상호 간 자원 교환 프로세스로 구체화됩니다(Gouldner, 1960; Molm, 1994). 특히 라틴계/히스패닉 문화권에서는 개인망 구성원 간 상호성에 대한 기대가 매우 높은 반면(Dilworth-Anderson & Marshall, 1996), 허리케인 앤드루 당시 복구 단계에서 자원 고갈을 겪은 바 있습니다(Kaniasty & Norris, 2000). 또한 계층 간 상호교환의 불평등이 관찰되기도 합니다(Jones et al., 2015).</li>
                </ul>
              </div>
            </div>
          </div>
        </section>

        <!-- 4. DATA AND METHODS -->
        <section class="section-block" id="sec-methods">
          <h2 class="section-title"><i data-lucide="database"></i> 4. 데이터 및 연구 방법 (DATA AND METHODS) <span class="toc-badge">pp. 118–119</span></h2>

          <div class="subsection-block" id="subsec-sample">
            <h3 class="subsection-title"><i data-lucide="check-circle"></i> 1) 표본 및 자료수집 (Project RAMA)</h3>
            <div class="para-card">
              <div class="para-content">
                <ul>
                  <li><strong>모집단 및 표본</strong>: 텍사스 대학교 M.D. 앤더슨 암센터의 코호트(Mano-a-Mano Cohort)에서 모집된 휴스턴 거주 멕시코계 162개 가족, 총 <strong>497명의 개인(가구당 3~4명)</strong>을 대상으로 대면 방문 인터뷰 수행(Chow et al., 2015; Wilkinson et al., 2005; Koehly et al., 2011; Marcum & Koehly, 2015).</li>
                  <li><strong>측정 방식</strong>: 가족 구성원 모두가 가정에 모여 동시에 참여하되, 정보 교환을 제한하기 위해 분리된 공간에서 개별 면접. 참여자 1인당 $20 현금 보상. 추적 조사 유지율 93%.</li>
                  <li><strong>네트워크 측정 도구(Ego-Alter Generator)</strong>:
                    <ul>
                      <li>응답자 본인(Ego) 기준 1차 친족(부모, 자녀, 배우자, 형제자매) 및 2차 친족(조부모, 삼촌, 고모, 이모 등) 전수 조사.</li>
                      <li>지난 1년 동안 "자신의 삶에서 중요한 역할을 했다"고 인식한 인물 최대 20명(친구, 이웃, 직장 동료 등) 추가 열거.</li>
                      <li>분석 대상: 인터뷰 시점에 생존해 있는 알터(Alters) 및 그들과의 관계 속성. 총 8,335개 다이애드 수집. 본 장에서는 기저(baseline) 네트워크 평가에 집중.</li>
                    </ul>
                  </li>
                </ul>
              </div>
            </div>
          </div>

          <div class="subsection-block" id="subsec-periods">
            <h3 class="subsection-title"><i data-lucide="calendar"></i> 2) 자연실험 시기 구분 (Time Periods)</h3>
            <div class="para-card">
              <div class="para-content">
                <p>허리케인 아이크의 상륙(2008.09.13)과 FEMA 주거 복구 프로그램 개시(2008.11월)를 기준으로 명확한 생애주기적 경계를 설정함:</p>
                <ol>
                  <li><strong>사전 단계 (Predisaster)</strong>: 2008년 6월 6일 ~ 2008년 9월 10일 (주지사 대피령 직전까지, 35가구 107명)</li>
                  <li><strong>대응 단계 (Response)</strong>: 2008년 9월 11일 ~ 2008년 11월 중순 (약 2개월간; 재난 직후 2주간의 조사 중단 기간을 제외한 실질 모집 기간 약 6주, 45가구 137명)</li>
                  <li><strong>복구 단계 (Recovery)</strong>: 2008년 11월 중순 ~ 2009년 3월 13일 (FEMA 주거 복구 프로그램 개시 시점, 82가구 253명)</li>
                </ol>
                <p><em>* 가족 구성원 전원이 동일 시점에 면접을 받았으므로 시기 간 가족 분할은 전혀 없음.</em></p>
              </div>
            </div>
          </div>

          <div class="subsection-block" id="subsec-dyads">
            <h3 class="subsection-title"><i data-lucide="git-commit"></i> 3) 사회적 상호작용 측정: 호의(Favors)의 다이애드 구성</h3>
            <div class="para-card">
              <div class="para-content">
                <p>응답자가 알터에게 부탁/호의를 베풀었는지, 알터로부터 호의를 받았는지의 2개 이진 문항을 결합하여 4가지 이항 조합(Dyad)으로 범주화:</p>
                <div class="table-container" style="margin: 1rem 0;">
                  <table>
                    <thead>
                      <tr>
                        <th>다이애드 범주</th>
                        <th>발신 (Sent)</th>
                        <th>수신 (Received)</th>
                        <th>네트워크적 의미</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td><strong>No Favors</strong></td><td>0</td><td>0</td><td>호의 교환 없음 (비활성 관계)</td></tr>
                      <tr><td><strong>Received Only</strong></td><td>0</td><td>1</td><td>알터로부터 지원을 받기만 함</td></tr>
                      <tr><td><strong>Sent Only</strong></td><td>1</td><td>0</td><td>알터에게 지원을 제공하기만 함 (일방적 자원 유출)</td></tr>
                      <tr><td><strong>Reciprocated Favors</strong></td><td>1</td><td>1</td><td>상호 호혜적 교환 (전통적 상호성 네트워크 척도)</td></tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>

          <div class="subsection-block" id="subsec-models">
            <h3 class="subsection-title"><i data-lucide="cpu"></i> 4) 통계 분석 모형</h3>
            <div class="para-card">
              <div class="para-content">
                <ol>
                  <li><strong>표본 동질성 검정 (교차분석/분산분석)</strong>: 시기별 응답자 인구통계학적 특성 차이 검정 ($\chi^2$ 검정 및 $F$-검정) $\to$ 외생적 표본 추출 편향 배제.</li>
                  <li><strong>가설 1 검정 (선형회귀분석, OLS)</strong>: 시기(독립변수)에 따른 열거된 네트워크 규모(종속변수) 차이 검정.</li>
                  <li><strong>가설 2 검정 (독립표본 t-test)</strong>: 시기별 가족 내 관계 유형(자녀, 부모, 배우자, 형제자매, 친척, 친구 등) 평균 차이 검정.</li>
                  <li><strong>가설 3 검정 (다이애드 로그선형모형, Log-Linear Model)</strong>: 시기 $\times$ 호의 교환 유형 분할표에서 기대빈도 대비 관측빈도의 <strong>표준화 피어슨 잔차(Standardized Pearson Residuals)</strong> 산출.</li>
                </ol>
              </div>
            </div>
          </div>
        </section>

        <!-- 5. RESULTS -->
        <section class="section-block" id="sec-results">
          <h2 class="section-title"><i data-lucide="bar-chart-2"></i> 5. 실증 분석 결과 (RESULTS) <span class="toc-badge">pp. 119–123</span></h2>

          <div class="subsection-block" id="subsec-res-demo">
            <h3 class="subsection-title"><i data-lucide="check"></i> 1) 표본의 인구통계학적 동질성 (Table 8.1 검증)</h3>
            <div class="para-card">
              <div class="para-content">
                <ul>
                  <li>총 162가구, 497명 응답자 (사전 35가구 107명, 대응 45가구 137명, 복구 82가구 253명), 총 다이애드 수 8,335개.</li>
                  <li>여성 비율(54~55%), 평균 연령(40.5~41.4세), 외국 출생 비율(68~69%), 기혼 비율(69~71%), 자가·차량 동시 소유 비율(62~66%) 모두 시기 간 통계적으로 유의한 차이가 없음 ($p > .85$).</li>
                  <li><strong>의의</strong>: 허리케인 아이크라는 외생적 충격이 연구의 표본 추출 설계를 왜곡하지 않았음을 확인 (자연실험 조건 충족).</li>
                </ul>
              </div>
            </div>
          </div>

          <div class="subsection-block" id="subsec-res-h1">
            <h3 class="subsection-title"><i data-lucide="trending-up"></i> 2) 가설 1 검정: 네트워크 규모의 확대 (Table 8.2)</h3>
            <div class="para-card">
              <div class="para-content">
                <ul>
                  <li>선형회귀분석 결과, 사전 단계(기준집단, 평균 16.19명) 대비 <strong>대응 단계에서 응답자들은 평균 1.84명 더 많은 네트워크 구성원을 열거함 ($\beta = 1.84, p < .01$).</strong></li>
                  <li>가구 단위(pooled family level)로 환산하면, 아이크 대응 과정에서 <strong>가구당 평균 2.5명의 고유한 가족 구성원이 추가로 포착</strong>되었습니다.</li>
                  <li>복구 단계에서는 사전 단계와 유의한 차이가 없었음 ($\beta = 0.15, p = .81$). $\to$ <strong>가설 1 (H1) 완전 지지.</strong></li>
                </ul>
              </div>
            </div>
          </div>

          <div class="subsection-block" id="subsec-res-h2">
            <h3 class="subsection-title"><i data-lucide="activity"></i> 3) 가설 2 검정: 친족 및 친구 관계의 선택적 활성화 (Figure 8.1)</h3>
            <div class="para-card">
              <div class="para-content">
                <ul>
                  <li><strong>삼촌/고모/이모(Uncle/Aunt)의 급증</strong>: 대응기에는 사전 대비 2차 친족인 삼촌/이모의 수가 유의하게 증가함 ($t = 2.439, df = 752, p < .017$, 평균 4.4명 증가).</li>
                  <li><strong>친구(Friend) 관계의 유의한 감소</strong>: 반면 친구 열거 수는 대응기($t = -2.086, df = 512, p < .042$)와 복구기($t = -2.200, df = 462, p < .033$) 모두에서 유의하게 감소함.</li>
                  <li>직계가족(자녀, 부모, 배우자)이나 조부모는 유의한 차이가 없었음.</li>
                  <li><strong>의의</strong>: 위기 시 개인은 제한된 인지적·사회적 용량으로 인해 친구 관계를 일시적으로 탈락시키고, 위기 대응에 필요한 확장 친족(삼촌/이모 등 2차 친족)을 집중적으로 활성화함. $\to$ <strong>가설 2 (H2) 부분적 지지.</strong></li>
                </ul>
              </div>
            </div>
          </div>

          <div class="subsection-block" id="subsec-res-h3">
            <h3 class="subsection-title"><i data-lucide="git-pull-request"></i> 4) 가설 3 검정: 호의 교환의 상호성 및 불균형 (Table 8.3)</h3>
            <div class="para-card">
              <div class="para-content">
                <p>로그선형모형 분석 결과, 전체 모형은 극히 유의함 ($\chi^2 = 64.7482, df = 6, p < 4.856 \times 10^{-12}$).</p>
                <ul>
                  <li><strong>사전 단계 (Predisaster)</strong>:
                    <ul>
                      <li>'주기만 함(Sent Only)'은 기대치보다 극도로 적음 (잔차 <strong>-5.697</strong>, $p < .001$).</li>
                      <li>'상호적 교환(Reciprocated Favors)'은 기대치를 크게 상회함 (잔차 <strong>+3.828</strong>, $p < .01$). $\to$ 평시에는 엄격한 상호 호혜성이 지배함.</li>
                    </ul>
                  </li>
                  <li><strong>대응 단계 (Response)</strong>:
                    <ul>
                      <li>모든 호의 교환 유형(No Favors, Received Only, Sent Only, Reciprocated)이 우연적 기대치와 일치함 (통계적으로 유의한 편차 없음).</li>
                      <li>즉, 대응기에는 상호 호의 교환이 기대치를 초과할 것이라는 가설과 달리, 무작위적 기댓값 수준을 유지함. $\to$ <strong>가설 3 (H3) 기각.</strong></li>
                    </ul>
                  </li>
                  <li><strong>복구 단계 (Recovery)의 결정적 발견</strong>:
                    <ul>
                      <li>'주기만 함(Sent Only)'이 기대치보다 유의하게 폭증함 (잔차 <strong>+2.627</strong>, $p < .05$).</li>
                      <li>'상호적 교환(Reciprocated Favors)'은 기대치보다 유의하게 급감함 (잔차 <strong>-2.398</strong>, $p < .05$).</li>
                      <li><strong>의의</strong>: 복구 단계에서는 호의를 베풀기만 하고 되돌려받지 못하는 <strong>'상호성 결여 및 일방적 자원 유출(Perceived Inequity)'</strong>이 심각하게 발생함.</li>
                    </ul>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </section>

        <!-- 6. TABLES & FIGURES -->
        <section class="section-block" id="sec-tables-figures">
          <h2 class="section-title"><i data-lucide="layout"></i> 6. 표 및 그림 정밀 분석 (Tables & Figures) <span class="toc-badge">자료</span></h2>

          <!-- Table 8.1 -->
          <div class="subsection-block" id="subsec-table81">
            <h3 class="subsection-title"><i data-lucide="table"></i> Table 8.1 연구참여자 및 가구 기술통계표 `[p. 120]`</h3>
            <div class="table-container">
              <table>
                <thead>
                  <tr>
                    <th>특성 (Characteristic)</th>
                    <th>사전 단계 (Predisaster)</th>
                    <th>대응 단계 (Response)</th>
                    <th>복구 단계 (Recovery)</th>
                    <th>유의확률 ($Pr(>|x|)$)</th>
                  </tr>
                </thead>
                <tbody>
                  <tr><td><strong>정보제공자 수 (No. informants)</strong></td><td>107명</td><td>137명</td><td>253명</td><td>–</td></tr>
                  <tr><td><strong>가구 수 (No. families)</strong></td><td>35가구</td><td>45가구</td><td>82가구</td><td>–</td></tr>
                  <tr><td><strong>다이애드 수 (No. dyads)</strong></td><td>1,732개</td><td>2,470개</td><td>4,133개</td><td>–</td></tr>
                  <tr><td><strong>여성 비율 (Pct. female)</strong></td><td>54%</td><td>54%</td><td>55%</td><td>0.96<sup>α</sup></td></tr>
                  <tr><td><strong>평균 연령 (Mean age)</strong></td><td>41.4세</td><td>40.5세</td><td>40.7세</td><td>0.89<sup>β</sup></td></tr>
                  <tr><td><strong>외국 출생 비율 (Pct. foreign born)</strong></td><td>69%</td><td>68%</td><td>69%</td><td>0.98<sup>α</sup></td></tr>
                  <tr><td><strong>혼인 상태 (Marital status)</strong></td><td></td><td></td><td></td><td>0.97<sup>α</sup></td></tr>
                  <tr><td>- 이혼 (Divorced)</td><td>1%</td><td>1%</td><td>2%</td><td>–</td></tr>
                  <tr><td>- 기혼 (Married)</td><td>71%</td><td>69%</td><td>70%</td><td>–</td></tr>
                  <tr><td>- 미혼 (Never married)</td><td>25%</td><td>28%</td><td>25%</td><td>–</td></tr>
                  <tr><td>- 별거 (Separated)</td><td>3%</td><td>2%</td><td>2%</td><td>–</td></tr>
                  <tr><td>- 사별 (Widowed)</td><td>1%</td><td>1%</td><td>1%</td><td>–</td></tr>
                  <tr><td><strong>주택 및 차량 동시 소유 (Owns house & car)</strong></td><td>62%</td><td>65%</td><td>66%</td><td>0.85<sup>α</sup></td></tr>
                </tbody>
              </table>
            </div>
            <div class="para-card" style="margin-top:0.75rem;">
              <div class="para-content" style="font-size:0.85rem; color:var(--text-muted);">
                *주: p-value는 <sup>α</sup>카이제곱 검정($\chi^2$) 및 <sup>β</sup>F-검정 기준.
              </div>
            </div>
          </div>

          <!-- Table 8.2 -->
          <div class="subsection-block" id="subsec-table82">
            <h3 class="subsection-title"><i data-lucide="table"></i> Table 8.2 열거된 네트워크 규모 선형회귀분석표 `[p. 121]`</h3>
            <div class="table-container">
              <table>
                <thead>
                  <tr>
                    <th>독립변수 (Variable)</th>
                    <th>회귀계수 $\beta$ (표준오차)</th>
                    <th>통계적 유의성</th>
                  </tr>
                </thead>
                <tbody>
                  <tr><td><strong>상수항 (Constant)</strong></td><td>16.19 (0.53)</td><td><span class="sig-star">***</span> ($p < .001$)</td></tr>
                  <tr><td colspan="3"><strong>시기 구분 (기준집단: 사전 단계)</strong></td></tr>
                  <tr><td>- 대응 단계 (Response phase)</td><td><strong>+1.84</strong> (0.71)</td><td><span class="sig-star">**</span> ($p < .01$)</td></tr>
                  <tr><td>- 복구 단계 (Recovery phase)</td><td>+0.15 (0.64)</td><td>n.s. ($p = .81$)</td></tr>
                  <tr><td><strong>관측치 (Observations)</strong></td><td>497명</td><td></td></tr>
                  <tr><td><strong>결정계수 ($R^2$ / Adj $R^2$)</strong></td><td>0.020 / 0.016</td><td></td></tr>
                  <tr><td><strong>잔차 표준오차 (Residual Std. Error)</strong></td><td>5.51 (자유도 $df = 494$)</td><td></td></tr>
                  <tr><td><strong>$F$-통계량 (F-Statistic)</strong></td><td>4.96** (자유도 $df = 2, 494$)</td><td><span class="sig-star">**</span> ($p < .01$)</td></tr>
                </tbody>
              </table>
            </div>
            <div class="para-card" style="margin-top:0.75rem;">
              <div class="para-content" style="font-size:0.85rem; color:var(--text-muted);">
                *주: **p < .01; ***p < .001.
              </div>
            </div>
          </div>

          <!-- Figure 8.1 -->
          <div class="subsection-block" id="subsec-fig81">
            <h3 class="subsection-title"><i data-lucide="image"></i> Figure 8.1 시기별 관계 유형 평균차이 t-test 막대그래프 `[p. 121]`</h3>
            
            <div class="figure-container">
              <img src="image-29.png" alt="FIGURE 8.1 Family-level average differences in number of relations enumerated">
              <div class="figure-caption">
                <strong>FIGURE 8.1</strong> Family-level average differences in number of relations enumerated comparing pre-disaster with response and recovery phases. (*p < .05, **p < .01)
              </div>
            </div>

            <div class="para-card">
              <div class="para-header"><i data-lucide="activity"></i> 🔍 [그래프 정밀 분석]</div>
              <div class="para-content">
                <ol>
                  <li><strong>대응기 vs 사전기 (좌측 패널)</strong>:
                    <ul>
                      <li>삼촌/이모(Uncle/Aunt)의 평균 열거 수가 <strong>+4.4명으로 폭증</strong>하며 통계적으로 매우 유의함 ($p < .01$).</li>
                      <li>반면 친구(Friend)는 <strong>약 -0.8명 감소</strong>하여 유의한 음(-)의 차이를 보임 ($p < .05$).</li>
                      <li>자녀, 부모, 배우자, 형제자매 등 1차 친족은 0 근처에서 유의한 변화가 없음.</li>
                    </ul>
                  </li>
                  <li><strong>복구기 vs 사전기 (우측 패널)</strong>:
                    <ul>
                      <li>친구(Friend)의 열거 감소 추세가 복구기에도 지속적으로 유지됨 ($-0.8$명, $p < .05$).</li>
                      <li>삼촌/이모 열거 수는 약 $+1.4$명으로 다소 높지만 통계적 유의수준에는 미달하여 평시 수준으로 점차 회귀하는 양상을 나타냄.</li>
                    </ul>
                  </li>
                </ol>
              </div>
            </div>
          </div>

          <!-- Table 8.3 -->
          <div class="subsection-block" id="subsec-table83">
            <h3 class="subsection-title"><i data-lucide="table"></i> Table 8.3 호의 교환 로그선형모형 표준화 피어슨 잔차표 `[p. 122]`</h3>

            <div class="figure-container">
              <img src="image-30.png" alt="Table 8.3 Standardized Pearson Residuals from Log-Linear Model">
              <div class="figure-caption">
                <strong>Table 8.3</strong> Standardized Pearson Residuals from the Log-Linear Model of Dyadic Favor Exchanges on Time Period ($\chi^2 = 64.7482; df = 6; p < 4.856 \times 10^{-12}$)
              </div>
            </div>

            <div class="table-container">
              <table>
                <thead>
                  <tr>
                    <th>시기 (Period)</th>
                    <th>No Favors (교환 없음)</th>
                    <th>Received Only (받기만 함)</th>
                    <th>Sent Only (주기만 함)</th>
                    <th>Reciprocated Favors (상호 교환)</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>사전 단계 (Predisaster)</strong></td>
                    <td>-0.619</td>
                    <td>0.766</td>
                    <td><strong style="color:var(--accent-rose);">-5.697***</strong></td>
                    <td><strong style="color:var(--accent-emerald);">+3.828**</strong></td>
                  </tr>
                  <tr>
                    <td><strong>대응 단계 (Response)</strong></td>
                    <td>-0.776</td>
                    <td>0.282</td>
                    <td>+1.353</td>
                    <td>-0.087</td>
                  </tr>
                  <tr>
                    <td><strong>복구 단계 (Recovery)</strong></td>
                    <td>+0.995</td>
                    <td>+0.710</td>
                    <td><strong style="color:var(--accent-rose);">+2.627*</strong></td>
                    <td><strong style="color:var(--accent-rose);">-2.398*</strong></td>
                  </tr>
                </tbody>
              </table>
            </div>

            <div class="para-card">
              <div class="para-header"><i data-lucide="search"></i> 🔍 [잔차 분석 정밀 해석]</div>
              <div class="para-content">
                <ul>
                  <li><strong>양의 잔차 ($> +1.96$)</strong>: 해당 셀의 실제 빈도가 무작위 확률적 기댓값보다 통계적으로 유의하게 많음을 의미.</li>
                  <li><strong>음의 잔차 ($< -1.96$)</strong>: 해당 셀의 실제 빈도가 무작위 확률적 기댓값보다 통계적으로 유의하게 적음을 의미.</li>
                  <li><strong>해석 핵심</strong>: 사전 단계에는 상호 호혜적 교환($+3.828$)이 규범이었으나, 장기 복구 단계로 넘어가면서 지원을 일방적으로 제공하기만 하고($+2.627$) 되돌려받지 못하는($-2.398$) 자원 고갈 및 관계적 불균형(Inequity) 현상이 실증됨.</li>
                </ul>
              </div>
            </div>
          </div>
        </section>

        <!-- 7. DISCUSSION -->
        <section class="section-block" id="sec-discussion">
          <h2 class="section-title"><i data-lucide="message-square"></i> 7. 논의 및 학술적 시사점 (DISCUSSION) <span class="toc-badge">pp. 123–124</span></h2>

          <div class="para-card">
            <div class="para-header"><i data-lucide="file-check"></i> 연구 프로토콜 보존의 중요성 [45 CFR 46.115(b)]</div>
            <div class="para-content">
              허리케인 아이크로 인한 연구 교란에도 불구하고 핵심 건강 소통 결과 변수에는 왜곡이 없었음을 진단했습니다(Dunning, 2012). 특히 미국 연방 규정상 3년 보관 의무를 넘어 연구 기록을 영구적으로 디지털 아카이빙해 둔 덕분에 재난 시기별 모집 시점을 정확히 재구성할 수 있었습니다. 재난 취약 지역 연구자들에게 연구 기록의 장기 보존 프로토콜 수립을 권고합니다.
            </div>
          </div>

          <div class="para-card">
            <div class="para-header"><i data-lucide="compass"></i> 1) 왜 2차 친족(삼촌/이모)이 급증했는가?</div>
            <div class="para-content">
              <ul>
                <li><strong>세대 간 관찰과 의사소통 활성화</strong>: 조사에 참여한 부모 세대가 재난 대응 과정에서 자신의 형제자매(성인 자녀 기준 삼촌·고모·이모)와 긴급 연락 및 지원을 주고받는 모습을 성인 자녀들이 목격하면서, 자녀들의 개인망 인지에서 삼촌/이모의 중요도(salience)가 급상승함(Foner & Dreby, 2011; Treas, 2008).</li>
                <li><strong>문화적 특수성 (<em>Compadrazgo</em>)</strong>: 멕시코계 가족의 특수한 '콤파드레(Compadre, 대부모)' 문화가 반영되었을 가능성. 혈연관계가 아니더라도 가족처럼 깊게 의지하는 부모의 절친한 친구를 자녀들이 삼촌/이모로 호칭하여 열거했을 개연성이 존재함(Kana’Iaupuni et al., 2005).</li>
              </ul>
            </div>
          </div>

          <div class="para-card">
            <div class="para-header"><i data-lucide="user-minus"></i> 2) 왜 친구 관계는 단절·감소되었는가? (Social Signature 이론)</div>
            <div class="para-content">
              Saramäki et al.(2014)의 '사회적 서명(Social Signature)' 이론과 일치합니다. 인간의 인지적 통신 용량(communication capacity)에는 한계가 있기 때문에, 재난이라는 극단적 상황에서 생존과 피난에 필수적인 친족 연계를 긴급히 활성화하는 대신, 일상적 친구 관계를 일시적으로 비활성화(drop ties)하는 <strong>자원 배분의 상충(Trade-off)</strong>이 발생합니다.
            </div>
          </div>

          <div class="para-card">
            <div class="para-header"><i data-lucide="scale"></i> 3) 복구기 호의 교환 불균형과 심리적 영향: 공정성 이론 vs 공동 대처</div>
            <div class="para-content">
              <ul>
                <li><strong>공정성 이론(Equity Theory, Hatfield et al., 1978)</strong>: 주는 것에 비해 받는 것이 없는 불균형은 분노, 좌절, 심리적 고통(distress)을 유발하며 관계 갈등을 촉발함(Väänänen et al., 2005; Whatley et al., 1999).</li>
                <li><strong>적응적 공동 대처(Adaptive Communal Coping, Walsh, 2007)</strong>: 반면 가족 체계에서는 대가를 바라지 않는 이타적 자원 제공이 가족 회복탄력성을 지탱하는 핵심 동력으로 작용할 수 있음(Lawrence & Schigelone, 2002; Rook, 1987; Kaniasty & Norris, 2000; Liang et al., 2001; Riad et al., 1999). 그러나 이것이 장기화될 경우 지지 제공자의 심각한 피로(compassion fatigue)로 이어질 수 있음.</li>
              </ul>
            </div>
          </div>
        </section>

        <!-- 8. TEMPLATE -->
        <section class="section-block" id="sec-template">
          <h2 class="section-title"><i data-lucide="file-text"></i> 8. 선행연구 검토 9단계 표준 템플릿 (Chapter 8) <span class="toc-badge">부록</span></h2>

          <div class="mermaid-box">
            <div class="mermaid">
flowchart LR
    A["1. 연구배경<br/>(개인망 동학 부재)"] --> B["2. 이론적 개념<br/>(자연실험·공동대처)"]
    B --> C["3. 연구목적<br/>(아이크 전·중·후 3단계)"]
    C --> D["4. 연구방법<br/>(RAMA 코호트 497명)"]
    D --> E["5. 연구결과<br/>(규모+1.84, 친족급증)"]
    E --> F["6. 핵심 발견<br/>(복구기 상호성 붕괴)"]
    F --> G["7. 연구한계<br/>(단일문화·GIS 미연계)"]
    G --> H["8. 이론적 시사점<br/>(네트워크를 종속변수화)"]
    H --> I["9. 후속 시사점<br/>(장기복구 소진 예방)"]
            </div>
            <div class="mermaid-caption">[다이어그램] 박사학위 논문 선행연구 검토 9단계 표준 프로세스 (Chapter 8)</div>
          </div>

          <div class="table-container">
            <table>
              <thead>
                <tr>
                  <th style="width:12%;">순서</th>
                  <th style="width:23%;">분석 단계</th>
                  <th style="width:65%;">제8장 핵심 요약 및 연구자 통제 관점 (Marcum et al., 2017)</th>
                </tr>
              </thead>
              <tbody>
                <tr><td><strong>1</strong></td><td><strong>연구배경 (Background)</strong></td><td>대형 재난이 사회구조에 미치는 영향 연구 중, 가족 내 개인 네트워크(Personal Network)가 재난 전개(대응-복구)에 따라 어떻게 변화하는지에 대한 실증 연구는 극히 부재함.</td></tr>
                <tr><td><strong>2</strong></td><td><strong>이론적 개념 (Concepts)</strong></td><td>잠재적 연계 활성화(Latent Tie Activation); 자연실험(Natural Experiment); 공동 대처 이론(Communal Coping); 공정성 이론(Equity Theory); 호의 교환 다이애드 구조; 사회적 서명(Social Signature).</td></tr>
                <tr><td><strong>3</strong></td><td><strong>연구목적 (Objective)</strong></td><td>2008년 허리케인 아이크 당시 수집된 멕시코계 162가구 497명의 데이터를 바탕으로, 재난 사전-대응-복구 시기별 개인망 규모, 친족 유형 활성화, 상호 호의 교환 구조의 동태적 변화를 실증 규명함.</td></tr>
                <tr><td><strong>4</strong></td><td><strong>연구방법 (Methodology)</strong></td><td>RAMA 코호트 종단 데이터 활용. 사전(35가구), 대응(45가구), 복구(82가구) 자연실험 분할. OLS 선형회귀분석(규모), 독립표본 t-검정(관계유형), 4개 다이애드 범주 로그선형모형(호의교환 잔차).</td></tr>
                <tr><td><strong>5</strong></td><td><strong>연구결과 (Results)</strong></td><td>대응기 네트워크 규모 유의한 증가(+1.84명, 가구당 +2.5명); 2차 친족(삼촌/이모) 급증 및 친구 관계 유의한 감소; 복구기 호의 교환의 심각한 불균형(주기만 함 폭증 +2.627, 상호성 급감 -2.398).</td></tr>
                <tr><td><strong>6</strong></td><td><strong>핵심 발견 (Findings)</strong></td><td>위기 시 개인은 친구를 배제하고 원거리 2차 친족을 선택적으로 활성화하며, 재난 대응기에는 기댓값 수준이던 상호성이 장기 복구기에는 일방적 자원 유출로 붕괴되는 '관계적 불평등'을 실증함.</td></tr>
                <tr><td><strong>7</strong></td><td><strong>연구의 한계 (Limitations)</strong></td><td>텍사스 휴스턴 멕시코계 이민자 가족이라는 단일 민족·지역 표본에 국한되어 문화적 일반화에 한계가 있으며, 대피 장소와 이동 경로에 대한 지리정보시스템(GIS) 좌표 미연계.</td></tr>
                <tr><td><strong>8</strong></td><td><strong>이론적 시사점 (Implications)</strong></td><td>네트워크를 단순 독립변수가 아닌 '외생적 재난 충격에 반응하는 동태적 결과변수'로 정립하고, 로그선형모형 표준화 잔차를 통해 재난 복구기 상호성 붕괴 메커니즘을 최초 규명.</td></tr>
                <tr><td><strong>9</strong></td><td><strong>후속 연구 시사점 (Future Scope)</strong></td><td>재난 피해 주민 및 현장 긴급구조대원의 장기 복구기 사회적 지지망 고갈(Burnout) 예방 프로토콜 및 비친족 지원망 붕괴 보완 정책 수립 필요.</td></tr>
              </tbody>
            </table>
          </div>
        </section>

        <!-- 9. FIRE SERVICE APPLICATION -->
        <section class="section-block" id="sec-fire-application">
          <h2 class="section-title" style="color:var(--accent-amber);"><i data-lucide="flame"></i> ★ 9. [내 연구 적용] 대형 재난 현장출동 소방대원의 개인 사회적 지지망 동학과 동료 지원(Peer Support) 상호성 붕괴 연구 <span class="toc-badge">적용</span></h2>

          <div class="callout-box" style="border-left-color:var(--accent-amber);">
            <div class="callout-title" style="color:var(--accent-amber);"><i data-lucide="zap"></i> 챕터 8 연구 기법의 소방 보건안전 적용 컨셉</div>
            <div class="callout-content">
              본 장(Chapter 8)의 <strong>자연실험(Natural Experiment) 설계</strong>, <strong>개인 네트워크 평가(Personal Ego-Net Assessment)</strong>, <strong>관계 유형별 선택적 활성화/탈락(t-test)</strong> 및 <strong>로그선형모형(Log-Linear Model) 기반 호의 교환 잔차 분석</strong> 기법을 <strong>[대형 참사(산불·이태원·오송 참사 등) 투입 소방공무원의 재난 전·대응·복구 단계별 지지망 동학 및 PTSD/소진(Burnout) 연구]</strong>에 직접 적용합니다.
            </div>
          </div>

          <div class="mermaid-box">
            <div class="mermaid">
flowchart LR
    S1["1. 연구질문<br/>(자연실험·개인망)"] --> S2["2. 확인한 연구결과<br/>(Ch.8 실증근거)"]
    S2 --> S3["3. 연구절차<br/>(6단계 프로세스)"]
    S3 --> S4["4. 분석단위·지표<br/>(Ego/Alter/Dyad)"]
    S4 --> S5["5. 데이터·코딩<br/>(사전-대응-복구 분할표)"]
    S5 --> S6["6. 자료수집 전략<br/>(설문+출동이력 결합)"]
    S6 --> S7["7. 통계분석 프로토콜<br/>(OLS+t-test+로그선형)"]
    S7 --> S8["8. 소방 협업 KPI<br/>(법령 조문 강제 매핑)"]
            </div>
            <div class="mermaid-caption">[다이어그램] 소방공무원 개인 사회적 지지망 동학 및 소진 연구 전체 연구 체계</div>
          </div>

          <!-- 1. 연구질문 -->
          <div class="para-card">
            <div class="para-header"><i data-lucide="help-circle"></i> 1. 연구질문 (Research Questions)</div>
            <div class="para-content">
              <ul>
                <li><strong>RQ 1 (재난 충격과 개인망 규모 변화)</strong>: 관할 구역 내 대형 참사(대응 2·3단계 발령 재난)에 출동한 소방관들은 참사 투입 전, 현장 대응기, 수습 및 복구기(3~6개월 후)에 걸쳐 의지하는 <strong>개인 사회적 지지망(가족, 동료, 지인)의 규모가 어떻게 변화하는가?</strong></li>
                <li><strong>RQ 2 (직무 동료 vs 외부 지인의 선택적 활성화)</strong>: 재난 대응기 동안 참사 트라우마를 공유하는 <strong>직무 동료(119구조대·구급대 팀원) 연계는 급격히 활성화</strong>되는 반면, <strong>비직무 지인(일반 친구, 사회적 모임)과의 관계망은 일시적으로 탈락·단절되는가?</strong></li>
                <li><strong>RQ 3 (동료 지지의 상호성 붕괴와 심리적 소진)</strong>: 참사 수습 후 복구기 동안, 동료들에게 정서적·도구적 지지를 지속적으로 베풀기만 하고 상호 되돌려받지 못하는 <strong>'일방적 지지 제공(Sent Only)'이 발생하는 소방관일수록 직무소진(Burnout) 및 외상후스트레스장애(PTSD) 위험이 통계적으로 유의하게 폭증하는가?</strong></li>
                <li><strong>RQ 4 (가족의 완충 효과와 이차 외상 스트레스)</strong>: 직계 가족(배우자)과의 긴밀한 소통망이 참사 대응기에는 보호 요인으로 작용하지만, 복구기에 이르러 가족에게 트라우마가 전이되는 '이차 외상 스트레스(Secondary Traumatic Stress)'를 유발하는가?</li>
              </ul>
            </div>
          </div>

          <!-- 2. 확인한 연구결과 및 연구 매핑 -->
          <div class="para-card">
            <div class="para-header"><i data-lucide="link"></i> 2. 확인한 연구결과 및 연구 매핑 (Key Findings from Chapter 8)</div>
            <div class="para-content">
              <div class="table-container" style="margin:0.5rem 0;">
                <table>
                  <thead>
                    <tr>
                      <th style="width:25%;">이론 및 챕터 출처</th>
                      <th style="width:40%;">선행연구 핵심 실증 결과 (Marcum et al., 2017)</th>
                      <th style="width:35%;">본 소방 안전 네트워크 연구로의 연계 적용</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>재난 시 개인망 규모 확대<br/>(Chapter 8; Table 8.2)</strong></td>
                      <td>허리케인 대응기 동안 응답자들은 평균 1.84명 더 많은 네트워크 구성원을 열거함 ($p < .01$).</td>
                      <td>대형 참사 투입 직후 소방대원들이 동료, 선후배, 가족 등 생존 지지망을 긴급 확장하는 양상 검증.</td>
                    </tr>
                    <tr>
                      <td><strong>관계 유형의 선택적 분화<br/>(Chapter 8; Figure 8.1)</strong></td>
                      <td>2차 친족(삼촌/이모)은 폭증(+4.4명)한 반면, 친구 관계는 유의하게 감소($-0.8$명)하여 상충(trade-off) 발생.</td>
                      <td>참사 대응기 동안 일반 친구망은 단절되고 현장 동료(Peer) 연계망으로 자원이 집중되는 쏠림 현상 규명.</td>
                    </tr>
                    <tr>
                      <td><strong>복구기 상호성 결여<br/>(Chapter 8; Table 8.3)</strong></td>
                      <td>복구기 동안 '주기만 함(Sent Only)' 잔차는 폭증(+2.627)하고, '상호 교환' 잔차는 급감($-2.398$)하여 불균형 발생.</td>
                      <td>참사 수습 후 동료 상담사 역할을 도맡은 고참 대원이 일방적 지지 유출로 인해 심각한 소진을 겪는 기전 입증.</td>
                    </tr>
                    <tr>
                      <td><strong>공동 대처와 자원 고갈<br/>(Chapter 8; Discussion)</strong></td>
                      <td>공동 대처(Communal Coping)가 초기에는 적응적이나 장기화될 경우 관계적 불평등과 분노, 피로를 촉발함.</td>
                      <td>초기 동료 지원(Peer Support) 프로그램이 장기 복구기에는 '동료 상담자의 지지 자원 고갈'로 이어지는 부작용 통제.</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>

          <!-- 3. 연구절차 -->
          <div class="para-card">
            <div class="para-header"><i data-lucide="list-ordered"></i> 3. 연구절차 (Research Procedure: 6단계 표준 프로세스)</div>
            <div class="para-content">
              <div class="mermaid-box" style="margin: 0.5rem 0 1rem 0;">
                <div class="mermaid">
flowchart LR
    S1["[STEP 1]<br/>자연실험 설계<br/>(대응 2단계 이상 참사 관할)"] --> S2["[STEP 2]<br/>개인망 측정 도구 설계<br/>(Ego-Net 설문지)"]
    S3["[STEP 3]<br/>3단계 시계열 추적<br/>(참사 전·중·후 6개월)"] --> S4["[STEP 4]<br/>데이터 정제 & 다이애드 코딩<br/>(4대 지지교환 범주화)"]
    S5["[STEP 5]<br/>OLS & 로그선형 분석<br/>(표준화 피어슨 잔차)"] --> S6["[STEP 6]<br/>소방 보건안전 환류<br/>(동료상담 SOP & KPI)"]
    S1 --> S2 --> S3 --> S4 --> S5 --> S6
                </div>
                <div class="mermaid-caption">[다이어그램] 소방대원 지지망 6단계 정밀 연구 절차</div>
              </div>
              <ol>
                <li><strong>[STEP 1] 자연실험 경계 설정</strong>: 관내 대응 2단계 이상 대형 참사(대형 산불, 이태원/오송 참사 등) 투입 소방서 선정.</li>
                <li><strong>[STEP 2] 개인망 측정 도구 설계</strong>: 소방관 맞춤형 Ego-Net 생성기(동료, 가족, 친구 지지망 척도) 개발.</li>
                <li><strong>[STEP 3] 3단계 시계열 추적</strong>: 참사 전(평시), 참사 직후(대응기 1~2개월), 수습 및 복구기(3~6개월 후) 추적 조사.</li>
                <li><strong>[STEP 4] 데이터 정제 및 다이애드 코딩</strong>: 호의/지지 송수신 4가지 이항 조합(No Support, Received, Sent, Reciprocal) 코딩.</li>
                <li><strong>[STEP 5] OLS 및 로그선형모형 추정</strong>: 네트워크 규모 회귀, 관계유형 t-검정, 표준화 피어슨 잔차 산출.</li>
                <li><strong>[STEP 6] 소방 보건안전 제도 환류</strong>: 동료상담 안식제 신설 및 KPI 조문 매핑.</li>
              </ol>
            </div>
          </div>

          <!-- 4. 네트워크 분석단위 및 지표 -->
          <div class="para-card">
            <div class="para-header"><i data-lucide="layers"></i> 4. 네트워크 분석단위 및 지표 (Units & Network Metrics)</div>
            <div class="para-content">
              <ol>
                <li><strong>에고 수준 (Ego-level - 소방대원 본인)</strong>:
                  <ul>
                    <li><strong>Network Size (전체 지지망 규모)</strong>: 에고가 열거한 전체 알터(직무 동료 + 가족 + 지인)의 총수.</li>
                    <li><strong>Kin/Peer Ratio (동료 대비 친족 비율)</strong>: 지지망 내 소방 직무 동료의 구성비율 $\to$ 직무 쏠림도.</li>
                  </ul>
                </li>
                <li><strong>다이애드 수준 (Dyadic-level - 에고와 알터 간 쌍)</strong>:
                  <ul>
                    <li><strong>4가지 정서적·도구적 지지 교환 유형</strong>:
                      <ul>
                        <li><code>No Support (0, 0)</code>: 상호 지지 교환 부재</li>
                        <li><code>Received Only (0, 1)</code>: 에고가 동료/가족으로부터 받기만 함</li>
                        <li><code>Sent Only (1, 0)</code>: 에고가 상대방에게 지지를 베풀기만 함 (자원 유출)</li>
                        <li><code>Reciprocal (1, 1)</code>: 상호 호혜적 지지 교환</li>
                      </ul>
                    </li>
                  </ul>
                </li>
                <li><strong>집단/팀 수준 (Team-level - 119구조구급대 단위)</strong>:
                  <ul>
                    <li><strong>팀 내 지지 교환 밀도(Density) 및 상호성 비율(Reciprocity Rate)</strong>.</li>
                  </ul>
                </li>
              </ol>
            </div>
          </div>

          <!-- 5. 데이터 구조 및 코딩 기준 -->
          <div class="para-card">
            <div class="para-header"><i data-lucide="database"></i> 5. 데이터 구조 및 코딩 기준 (Data & Coding Protocol)</div>
            <div class="para-content">
              <div class="table-container" style="margin: 0.5rem 0;">
                <table>
                  <thead>
                    <tr>
                      <th style="width:25%;">구분</th>
                      <th style="width:25%;">데이터 형식</th>
                      <th style="width:50%;">변수 구성 및 코딩 기준</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>소방관 속성 데이터<br/>(Ego Demographics)</strong></td>
                      <td>1-mode 엑셀 테이블<br/>(행 = 소방관 $i$, $N = 300$)</td>
                      <td>• <strong>ID</strong>: FF001, FF002 ...<br/>• <strong>Role</strong>: 1=구조, 2=구급, 3=진압, 4=상황관리<br/>• <strong>Rank</strong>: 소방사~소방령<br/>• <strong>Disaster_Phase</strong>: 1=평시(사전), 2=대응기(출동중), 3=복구기(수습후)<br/>• <strong>PTSD_Score</strong>: IES-R 외상후 스트레스 점수<br/>• <strong>Burnout_Score</strong>: MBI 직무소진 척도</td>
                    </tr>
                    <tr>
                      <td><strong>개인망 알터 데이터<br/>(Alter Matrix)</strong></td>
                      <td>Ego-Alter 연계 테이블<br/>(최대 15명 열거)</td>
                      <td>• <strong>Alter_Type</strong>: 1=소방서 팀원, 2=타소방서 동료, 3=직계가족, 4=확장친족, 5=친구/지인<br/>• <strong>Proximity</strong>: 지리적 거주 거리 (관내 vs 원거리)<br/>• <strong>Frequency</strong>: 주간 연락 빈도</td>
                    </tr>
                    <tr>
                      <td><strong>다이애드 지지 교환 분할표<br/>(Contingency Table)</strong></td>
                      <td>$3 \times 4$ 교차 행렬<br/>(시기 $\times$ 4대 지지유형)</td>
                      <td>• <strong>행</strong>: Predisaster vs Response vs Recovery<br/>• <strong>열</strong>: No Support, Received Only, Sent Only, Reciprocal</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>

          <!-- 6. 통계분석 실행 프로토콜 -->
          <div class="para-card">
            <div class="para-header"><i data-lucide="cpu"></i> 6. 통계분석 실행 프로토콜 (Statistical Analysis Protocol)</div>
            <div class="para-content">
              <ol>
                <li><strong>Step 1: OLS 다중선형회귀분석 (네트워크 규모 변화 검정)</strong>:
                  <div class="eq-box">
                    $$Y_i (\text{Network Size}) = \beta_0 + \beta_1 (\text{Response}) + \beta_2 (\text{Recovery}) + \gamma X_i + \epsilon_i$$
                  </div>
                </li>
                <li><strong>Step 2: 독립표본 t-검정 (동료 vs 일반 친구 관계 수 평균 비교)</strong>:
                  대응기 및 복구기 동안 소방 동료 수($N_{\text{Peer}}$)와 일반 친구 수($N_{\text{Friend}}$)의 증감 검정.
                </li>
                <li><strong>Step 3: 다이애드 로그선형모형(Log-Linear Model) 추정</strong>:
                  <ul>
                    <li>시기($P$)와 지지유형($S$) 간의 독립성 검정:
                      <div class="eq-box">
                        $$\ln (m_{ij}) = \mu + \lambda_i^P + \lambda_j^S + \lambda_{ij}^{PS}$$
                      </div>
                    </li>
                    <li>각 셀별 <strong>표준화 피어슨 잔차(Standardized Pearson Residual)</strong> 산출:
                      <div class="eq-box">
                        $$r_{ij} = \frac{n_{ij} - \hat{m}_{ij}}{\sqrt{\hat{m}_{ij}}}$$
                      </div>
                    </li>
                    <li>복구기에서 <code>Sent Only</code> 셀의 $r > +1.96$ 여부 및 <code>Reciprocal</code> 셀의 $r < -1.96$ 여부 집중 검증.</li>
                  </ul>
                </li>
              </ol>
            </div>
          </div>

          <!-- 7. 소방 보건안전 환류 -->
          <div class="para-card">
            <div class="para-header"><i data-lucide="award"></i> 7. 소방 보건안전 환류: 맞춤형 KPI 도출 및 법적 근거 매핑</div>
            <div class="para-content">
              <h4 style="color:var(--accent-secondary); margin-bottom:0.5rem; font-size:1rem;">1) 소방 실무 개선 환류 정책</h4>
              <ul>
                <li><strong>'동료상담사(Peer Supporter) 지지 고갈 안식제' 도입</strong>: 참사 수습 후 동료들의 심리 상담을 도맡아 일방적 지지 유출(`Sent Only`)을 경험하는 고참 대원에게 의무적 휴식 및 외부 전문 심리지원 제공 (번아웃 방지).</li>
                <li><strong>'재난 복구기 소방관 사회적 지지망 회복 프로토콜' 수립</strong>: 참사 대응기 동안 단절되었던 일반 친구·가족 관계망을 복원할 수 있도록 '회복 힐링 캠프' 및 가족 참여 프로그램 정례화.</li>
              </ul>

              <h4 style="color:var(--accent-secondary); margin-top:1.25rem; margin-bottom:0.5rem; font-size:1rem;">2) 소방 맞춤형 핵심성과지표 (KPI 가중치: 고유 70% / 협업 30%)</h4>
              <div class="table-container" style="margin: 0.5rem 0 1rem 0;">
                <table>
                  <thead>
                    <tr>
                      <th style="width:20%;">지표 구분</th>
                      <th style="width:40%;">핵심 성과지표 (KPI)</th>
                      <th style="width:15%;">가중치</th>
                      <th style="width:25%;">산출 공식 및 목표치</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td rowspan="2"><strong>고유 지표<br/>(소방 내부 관리 70%)</strong></td>
                      <td><strong>참사 복구기 동료 지지 상호성 유지율</strong></td>
                      <td>40%</td>
                      <td>$\frac{\text{상호 지지(Reciprocal) 대원 수}}{\text{전체 출동 대원 수}} \times 100 \ge 60\%$</td>
                    </tr>
                    <tr>
                      <td><strong>동료상담 대원 일방적 지지 유출(`Sent Only`) 모니터링 지수</strong></td>
                      <td>30%</td>
                      <td>고위험 노출 대원의 조기 스크리닝 및 순환 배치율 100% 달성</td>
                    </tr>
                    <tr>
                      <td><strong>협업 지표<br/>(보건복지부 협업 30%)</strong></td>
                      <td><strong>소방-지역사회 전문 심리치료망 연계율</strong></td>
                      <td>30%</td>
                      <td>내부 지지망 고갈 시 외부 국립트라우마센터로의 신속 전원율 90% 이상</td>
                    </tr>
                  </tbody>
                </table>
              </div>

              <div class="callout-box" style="margin-top:1rem; border-left-color:var(--accent-emerald);">
                <div class="callout-title" style="color:var(--accent-emerald);"><i data-lucide="scale"></i> 3) 관련 법적 근거 매핑 (조문 단위 강제 연계)</div>
                <div class="callout-content">
                  <ul>
                    <li><strong>소방공무원 보건안전 및 복지 기본법 제10조(소방공무원의 건강관리 등)</strong>: 소방청장은 소방활동으로 인하여 신체적·정신적 위험에 노출된 소방공무원의 건강관리를 위한 대책을 수립·시행하여야 함.</li>
                    <li><strong>소방공무원 보건안전 및 복지 기본법 제11조(정신건강 관리 등)</strong>: 소방청장 및 소방본부장은 외상후스트레스장애(PTSD), 우울증 등 정신건강 장애의 예방 및 치료를 위한 상담·치료 프로그램을 운영하여야 함.</li>
                    <li><strong>재난 및 안전관리 기본법 제65조의3(재난관리 참여자 등의 심리지원)</strong>: 재난 현장에서 구호 및 수습 활동에 참여한 긴급구조요원에 대한 심리지원 의무 명시.</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- BOTTOM NAVIGATION -->
        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:3.5rem; padding-top:2rem; border-top:1px solid var(--border-color); flex-wrap:wrap; gap:1rem;">
          <a href="chapter7_subnote.html" class="action-btn" style="padding:0.75rem 1.25rem; font-size:0.9rem;">
            <i data-lucide="arrow-left"></i> 이전: Chapter 7 주의의 이동
          </a>
          <a href="index.html" class="action-btn primary" style="padding:0.75rem 1.25rem; font-size:0.9rem;">
            <i data-lucide="grid"></i> SNA 통합 포털로 이동
          </a>
        </div>

      </main>
    </div>
  </div>

  <script>
    // Lucide Icons Render
    lucide.createIcons();

    // Reading Progress Bar
    window.addEventListener('scroll', () => {
      const winScroll = document.documentElement.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (winScroll / height) * 100;
      document.getElementById('progress-bar').style.width = scrolled + '%';
    });

    // Theme Toggle
    const themeBtn = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');
    let isLight = false;

    themeBtn.addEventListener('click', () => {
      isLight = !isLight;
      if (isLight) {
        document.documentElement.setAttribute('data-theme', 'light');
        themeIcon.setAttribute('data-lucide', 'sun');
      } else {
        document.documentElement.removeAttribute('data-theme');
        themeIcon.setAttribute('data-lucide', 'moon');
      }
      lucide.createIcons();
    });

    // TOC Active State on Scroll
    const trackedBlocks = document.querySelectorAll('.section-block, .subsection-block');
    const navItems = document.querySelectorAll('.toc-item');

    window.addEventListener('scroll', () => {
      let current = '';
      trackedBlocks.forEach(block => {
        const blockTop = block.offsetTop;
        if (window.pageYOffset >= blockTop - 130) {
          current = block.getAttribute('id');
        }
      });

      navItems.forEach(item => {
        item.classList.remove('active');
        const link = item.querySelector('a');
        if (link && link.getAttribute('href') === `#${current}`) {
          item.classList.add('active');
        }
      });
    });

    // Sidebar Search Filter
    const searchInput = document.getElementById('search-input');
    const tocList = document.getElementById('toc-list');
    const tocLinks = tocList.getElementsByTagName('li');

    searchInput.addEventListener('input', (e) => {
      const term = e.target.value.toLowerCase();
      Array.from(tocLinks).forEach(li => {
        const text = li.innerText.toLowerCase();
        if (text.includes(term)) {
          li.style.display = 'block';
        } else {
          li.style.display = 'none';
        }
      });
    });
  </script>
</body>
</html>
"""

target_path = "/Users/sg/Project/SNA/subnote/chapter8_subnote.html"
with open(target_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated full {target_path} (size: {len(html_content)} bytes)")
