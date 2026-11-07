# -*- coding: utf-8 -*-
import os

workdir = "/Users/sg/Project/SNA"
os.chdir(workdir)

# Read Ch 1-7
with open("subnote/SNA_통합_서브노트_Ch1-7.md", "r", encoding="utf-8") as f:
    ch1_7_text = f.read()

# Read Ch 8
with open("subnote/chapter8-subnote.md", "r", encoding="utf-8") as f:
    ch8_text = f.read()

# Read Ch 9
with open("subnote/chapter9-subnote.md", "r", encoding="utf-8") as f:
    ch9_text = f.read()

# Overview table rows for Ch 8 and 9
ch8_overview = """| **제8장** | *The Effect of Hurricane Ike on Personal Network Tie Activation as Response and Recovery Unfolded*<br/>(Christopher Steven Marcum et al., pp. 113–126) | 자연실험(Natural Experiment), **2원 혼합효과 로지스틱 회귀**, 지리적 근접성 vs 기능적 지지, 일상 네트워크의 재난 전이 | 대형 태풍·풍수해 시 소방관 개인·가족 지원 네트워크 활성화 및 출동대원 외상 후 스트레스(PTSD) 완충 모델 |
| **제9장** | *The Family’s Burden: Perceived Social Network Resources for Individual Disaster Assistance in Hazard-Prone Florida*<br/>(Michelle Meyer, pp. 127–141) | **가족 배태성(Kin Embeddedness)**, 에고 네트워크(Ego-net), 네트워크 자원의 불평등, 사전 인지된 사회적 지지망 | 독거노인·재난약자의 '가족의 부담' 경감을 위한 119안심콜 및 소방안전돌봄 네트워크 구축 모델 |"""

# TOC rows for Ch 8 and 9
ch8_toc = """| **제8장** | **제8장 허리케인 아이크가 개인 네트워크 연계 활성화에 미친 영향 (Sub-Note)** | • 1. 서론 (Introduction)<br/>• 2. 가족 맥락에서의 재난 사건 (The Event in Family Context)<br/>• 3. 재난 후 지지의 원천 (Sources of Support Following Disasters)<br/>• 4. 데이터 및 연구 방법 (Data and Methods)<br/>• 5. 분석 결과 (Results)<br/>• 6. 논의: 가족 네트워크와 재난 (Discussion)<br/>• [부록] 박사학위 논문 선행연구 9단계 분석 템플릿 (Chapter 8)<br/>• 7. ★ [내 연구 적용] 대형 풍수해 시 소방관 개인·가족 지원 네트워크 활성화 및 현장 대응 프로토콜 |
| **제9장** | **제9장 가족의 부담: 재난 다발 지역 플로리다 주민들이 인지하는 개인 재난 지원 사회연결망 자원 (Sub-Note)** | • 1. 서론 및 이론적 배경 (Introduction)<br/>• 2. 연구 방법 및 표본 (Methods)<br/>• 3. 재난 지원 네트워크: 규모와 자원 (Size and Resources)<br/>• 4. 재난 지원 네트워크: 구성과 가족의 부담 (Composition)<br/>• 5. 사회연결망 인식과 사회경제적 지위 (Socioeconomic Status)<br/>• 6. 논의 및 학술적 시사점 (Discussion)<br/>• [부록] 박사학위 논문 선행연구 9단계 분석 템플릿 (Chapter 9)<br/>• 7. ★ [내 연구 적용] 재난 취약계층의 '가족의 부담' 완화 및 소방안전돌봄 네트워크 구축 모델 |"""

# Replace title and intro in Ch1-7 text
updated_header = ch1_7_text

# Update header title
updated_header = updated_header.replace(
    "# 재난관리 사회연결망 연구총서 (Chapters 1 ~ 7 통합 학술 서브노트 & 소방 실증 프로토콜)",
    "# 재난관리 사회연결망 연구총서 (Chapters 1 ~ 9 통합 학술 서브노트 & 소방 실증 프로토콜)"
)
updated_header = updated_header.replace(
    "**구성 범위**: Part I (이론 및 방법론: 제1장 ~ 제4장) & Part II (재난 대응 실증 연구: 제5장 ~ 제7장) 전 7개 챕터 완전판",
    "**구성 범위**: Part I (이론 및 방법론: 제1장 ~ 제4장), Part II (재난 대응 실증 연구: 제5장 ~ 제7장), Part III (개인 중심 복구 및 적응: 제8장 ~ 제9장) 전 9개 챕터 완전판"
)
updated_header = updated_header.replace(
    "## [총괄 요약] 전 7개 챕터 핵심 아키텍처 및 소방 연구 연계 일람",
    "## [총괄 요약] 전 9개 챕터 핵심 아키텍처 및 소방 연구 연계 일람"
)
updated_header = updated_header.replace(
    "## [전체 상세 목차] Chapters 1 ~ 7 통합 서브노트 목차 (Table of Contents)",
    "## [전체 상세 목차] Chapters 1 ~ 9 통합 서브노트 목차 (Table of Contents)"
)

# Insert Ch 8 and 9 into overview table (after Ch 7)
ch7_row = '| **제7장** | *Shifting Attention: Modeling Follower Relationship Dynamics Among US Emergency Management-Related Organizations During a Colorado Wildfire*<br/>(Carter T. Butts et al., pp. 93–113) | 온라인 주의(Attention) 이동 동학, **동적 네트워크 로지스틱 회귀(DNR)**, 단기(1~3일) 도태 vs 장기(4~7일) 고착화 대칭 전환, 사전 고착화(Lock-in) | 대형 산불 시 재난관리 유관기관 간 시계열 상황전파·주의 네트워크 동학(DNR) 분석 및 발화 후 72시간 내 골든타임 주의 연결 KPI |'
if ch7_row in updated_header:
    updated_header = updated_header.replace(ch7_row, ch7_row + "\n" + ch8_overview)

# Insert Ch 8 and 9 into TOC table (after Ch 7)
ch7_toc_row = '| **제7장** | **제7장 주의의 이동: 콜로라도 산불 당시 미국 재난관리 유관 조직 간 팔로워 관계 동학 모델링 (Sub-Note)** | • INTRODUCTION (서론) `[원문 pp. 94–95]`<br/>• LITERATURE REVIEW (문헌 검토) `[원문 pp. 95–97]`<br/>• MECHANISMS OF ATTENTIONAL INTERACTION DURING A DISASTER (재난 시 주의 상호작용의 메커니즘) `[원문 pp. 97–98]`<br/>• DATA (데이터) `[원문 pp. 98–103]`<br/>• METHODS (연구 방법) `[원문 pp. 103–107]`<br/>• RESULTS (분석 결과) `[원문 pp. 107–109]`<br/>• DISCUSSION (논의) `[원문 pp. 109–111]`<br/>• SUMMARY (요약) `[원문 pp. 111–112]`<br/>• ACKNOWLEDGMENTS (사사) `[원문 p. 112]`<br/>• [부록] 박사학위 논문 선행연구 9단계 분석 템플릿<br/>• 8. ★ [내 연구 적용] 대형 산불 시 재난관리 유관기관 간 온라인 주의(Attention) 네트워크 동학과 정보 고착화 연구 (동적 네트워크 회귀 DNR & 넷마이너 8대 표준 프로토콜) |'
if ch7_toc_row in updated_header:
    updated_header = updated_header.replace(ch7_toc_row, ch7_toc_row + "\n" + ch8_toc)

# Append Ch 8 and Ch 9 body
full_md = updated_header.rstrip() + "\n\n---\n\n" + ch8_text.strip() + "\n\n---\n\n" + ch9_text.strip() + "\n"

out_file = "subnote/SNA_통합_서브노트_Ch1-9.md"
with open(out_file, "w", encoding="utf-8") as f:
    f.write(full_md)

print(f"Generated {out_file} (size: {len(full_md):,} bytes)")
