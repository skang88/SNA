import os
import re
import subprocess
import zipfile
import shutil
import xml.etree.ElementTree as ET

WORKDIR = "/Users/sg/Project/SNA"
os.chdir(WORKDIR)

# 1. Ensure Chapter 4, 5, 6 markdown files have the complete 9-step PhD summary & Chapter 4 fire application + 5-firefighter simulation
ch4_extra_md = """

---

## [부록] 박사학위 논문 선행연구 9단계 분석 템플릿 (Chapter 4)

| 단계 | 분석 항목 | 제4장 (Varda, 2017, pp. 43–59) 핵심 내용 |
| :---: | :--- | :--- |
| **1** | **연구배경** | 허리케인 카트리나 이후 재난 대응·복구·완화 연구에서 전통적 속성(인구통계·물리적 취약성) 중심 접근의 한계가 드러남에 따라, 비공식·공식 관계망을 실증적으로 규명할 체계적 사회연결망(SNA) 방법론 전략이 요구됨. |
| **2** | **이론적 개념** | **IOSP 프레임워크**(In/Out × Seeker/Provider), **개인-집단-지역사회 3대 분석단위의 배태성(Embeddedness)**, **자아중심망(Egocentric)·전체망(Sociocentric)·다수준망(Multilevel)**, **5대 관계 범주**(인적·지식·자원·과업·조직), **다이론 다수준(MTML) 모형**, **사회적/네트워크 취약성(Social/Network Vulnerability)**. |
| **3** | **연구목적** | 재난의 특수한 맥락(시간 압축성, 경계 모호성, 종단적 재편성)에 적합한 사회연결망 연구 설계, 데이터 수집(명명생성법 vs 사전 명부), 통계적 추론(QAP, ERGM/p*), 설문 행정 전략을 종합 제시함. |
| **4** | **연구방법** | 문헌 메타 검토 및 방법론적 프레임워크 구축. 자아중심·전체·다수준 네트워크별 핵심 연구질문(Q1~Q10) 도출, PARTNER Tool 설계 원리, 결측치(20% 임계점) 및 회상 편향 통제 기법 제시. |
| **5** | **연구결과** | • **시간에 따른 네트워크 진화(Fig 4.2)**: 재난 발생 직후 비공식 연결망이 친족·핵심 연계 중심으로 급격히 **희소화(Thinning-out)**된 후 장기 복구기에 점진적으로 재건됨.<br/>• **결측치 민감성**: 무작위 결측이 **20%를 초과**하면 중심성·밀도 지표가 심각하게 왜곡됨(Valente et al., 2008). |
| **6** | **핵심 발견** | 정부의 공식 원조나 개인의 사회경제적 조건과 독립적으로 **비공식 관계망이 재난 구호와 복구에 결정적 역할**을 수행하며, **'사회적으로 고립된 생존자(Socially Isolated Survivors)'**가 가장 치명적인 네트워크 취약 집단임. |
| **7** | **연구의 한계** | 재난 직후 현장 접근성 제약, 사후 회상(Recall) 설문에 따른 기억 왜곡, 다단계 네트워크 설문의 높은 응답 피로도 및 조직 대리 응답으로 인한 호혜성 측정 한계. |
| **8** | **이론적 시사점** | 재난 연구의 패러다임을 '개별 행위자 속성'에서 **'관계적 구조와 다수준 상호의존성(MTML)'**으로 전환하고, 전통적 물리적 취약성을 넘어 **'네트워크 취약성'** 개념을 정립함. |
| **9** | **후속 연구 시사점** | (1) 네트워크 고립 노드의 **공간적·지리적 상관성(Spatial Correlates)** 결합을 통한 정밀 구호 표적화, (2) 공공-민간(Public-Private) 및 지역-외부(Local-External) 네트워크 시너지 실증. |

---

# 8. ★ [내 연구 적용] 소방공무원 안전 책무성·협력 네트워크 실증 분석 (SNA & 넷마이너 7단계 프로토콜 및 5인 가상 시뮬레이션)

본 장(Chapter 4)의 사회연결망 연구 전략(SNA)을 **[의령소방서 119구조대 및 관내 현장 출동부서의 안전 리더십, 안전 책무성(Accountability) 및 다기관 협업 네트워크 분석]**에 직접 적용하기 위해, 순수 사회연결망 분석 및 넷마이너(NetMiner) 실증 절차 7단계와 가상 소방관 5인 시뮬레이션으로 체계화한 방법론 설계입니다.

### 1. 연구질문 (Research Questions)
Chapter 4에서 제시된 자아중심망, 전체망, 다수준망 연구 질문(Q1~Q10)의 논리를 소방 현장 안전 관리 맥락에 투영하여 5대 핵심 연구 질문을 도출합니다.
- **RQ 1 (구조적 중심성 & 중개자 - Centrality)**: 의령소방서 119구조대 및 출동부서의 안전 소통망에서 **핵심 안전 정보 중개자(Broker/Bridge; 매개 중심성)**와 **고립 대원(Isolates; 인입 연결정도 최하위)**은 누구이며, 계급(지휘관리층, 중간관리층, 일선대원층)별로 중심성 분포는 어떻게 차이를 보이는가?
- **RQ 2 (하위집단 & 동질선호 - Subgroups)**: 안전 소통 및 전술 조언망 내에서 비공식적 군집(Cliques)이나 동질선호(Homophily; 동일 계급·동일 팀 편중) 현상이 존재하는가? 이것이 상하 계급 간 **'안전 침묵(Safety Silence)'**이나 정보 전달 병목(Bottleneck)을 유발하는가?
- **RQ 3 (관계의 다중성 - Multiplexity)**: 공식 업무 지시망(Command), 전문 지식/전술 조언망(Advice), 비상 장비 공유망(Resource), 아차사고(Near-Miss) 신뢰망(Trust) 간의 구조적 상관성(QAP Matrix Correlation)은 어떻게 나타나는가?
- **RQ 4 (출동 생애주기별 동태성 - Dynamics)**: 출동 생애주기(평시 대비기 $\rightarrow$ 현장 진입/대응기 $\rightarrow$ 초진/철수기 $\rightarrow$ 사후 디브리핑기)의 진행에 따라 안전 네트워크의 밀도(Density)와 집중도(Centralization)는 어떻게 축소·재편(Thinning-out & Rebuilding)되는가?
- **RQ 5 (네트워크 성과 & 취약성 - Vulnerability)**: 네트워크 내 고립도 및 중심성 격차는 현장 대원의 안전사고(아차사고 은폐, 안전수칙 위반) 및 조직의 안전 책무성(RAA 삼원조 정합성) 성과와 어떠한 통계적 인과관계를 갖는가?

### 2. 확인한 연구결과 (Key Findings from Literature)

| 이론 및 챕터 출처 | 선행연구 핵심 실증 결과 | 본 소방 안전 네트워크 연구로의 연계 시사점 |
| :--- | :--- | :--- |
| **IOSP 프레임워크<br/>(Chapter 4; Varda et al., 2009)** | 재난 네트워크 행위자를 공간(In/Out)과 역할(Seeker/Provider)로 분리 측정. 상호의존적 자원 탐색과 제공 구조화. | 현장 진입 대원(In/Seeker; 작업중지권), 지휘관/안전점검관(In/Provider; 위험성평가·RIT), 상황실(Out/Seeker), 통제단 유관기관(Out/Provider) 매핑. |
| **5대 관계 범주<br/>(Chapter 4; Kapucu, 2005)** | 인적(People), 지식(Knowledge), 자원(Resource), 과업(Task), 조직(Organizational) 관계의 다차원적 분리 측정. | 소방 안전 책무성(RAA 삼원조)의 책임-권한-책무성과 정합하는 4대 매트릭스(의사소통, 조언, 장비차용, 신뢰망) 분리 설계. |
| **동태적 진화 모델<br/>(Chapter 4; Fig 4.2)** | 재난 충격 시 네트워크가 극도로 희소화(Thinning-out)되어 친족·핵심 연계로 축소된 후 복구기 점진적 재건. | 출동 시 2인 1조(Buddy) 연계로의 축소 및 Mayday 비상탈출망 가동 $\rightarrow$ 귀소 후 아차사고 자발적 등록을 통한 다원적 망 재건 모델 입증. |
| **사회적/네트워크 취약성<br/>(Chapter 4; Valente et al., 2008)** | 물리적 취약성보다 네트워크 내 '사회적으로 고립된 노드(Isolates)'의 복구 지체 및 사고 위험이 극심함. 결측치 20% 초과 시 지표 왜곡. | 조직 내에서 안전 조언과 소통이 단절된 **'네트워크 고립 소방관(Isolated Firefighter)'**의 위험성 선제 스크리닝 및 결측치 15% 이하 통제. |
| **다원주의 & HLM 실증<br/>(Chapter 5; Nowell et al., 2017)** | 성과 평가 변량의 **83%~97%가 사건 간이 아닌 개인 간(Within-incident)에 존재** (Table 5.4). 중앙지휘팀(IMT) 나홀로 고평가 편향. | 단일 리커트 평균점수 비교를 지양하고, 다층 위계 조직(계급별) 내부의 소통 격차 및 지휘부 편향을 통계적으로 분리 검증. |

### 3. 연구절차 (Research Procedure: 6단계 표준 프로세스)
1. **[STEP 1] 연구 0점 & 경계 설정**: 의령소방서 119구조대 및 현장출동부서 전수 정의
2. **[STEP 2] 설문 도구 설계**: 사전 명부(Prepared Roster) 기반 다중 관계 측정 도구 설계
3. **[STEP 3] 전수 데이터 수집**: 교대근무 주기를 반영한 모바일/서면 병행 전수 조사
4. **[STEP 4] 데이터 정제 & 코딩**: 1-mode 정방행렬($N \times N$) 및 노드 속성 테이블 구축
5. **[STEP 5] 넷마이너(NetMiner) 분석**: 시각화, 중심성, 하위집단(E-I 지수), QAP/MRQAP 검정
6. **[STEP 6] 결과 해석 & 정책 제언**: 고립 대원 멘토링 및 선행 안전 KPI 도출

### 4. 네트워크 분석단위 및 분석지표 (Units & Network Metrics)
- **노드 수준 (Node-level, 미시 분석)**: 개별 소방공무원 노드($N \approx 50$명)의 **In-Degree Centrality**(신뢰받는 안전 리더 지수), **Out-Degree Centrality**(자원 요청 활성도), **Betweenness Centrality**(소통 교량 Bridge 또는 병목 Bottleneck), **Eigenvector Centrality**(핵심 인력 연계 영향력).
- **하위집단 수준 (Subgroup-level, 중범위 분석)**: 계급별(지휘층·중간층·일선대원층) 및 팀별(1·2·3팀) 집단의 **E-I Index**(집단 내부 vs 외부 연계 비율; $-1$에 가까울수록 계급 간 소통이 단절된 폐쇄적 파벌), **Cliques 및 K-core 분석**.
- **전체망 수준 (Whole-level, 거시 분석)**: 의령소방서 출동부서 전체망의 **Network Density**(네트워크 밀도), **Network Centralization**(특정 지휘관 독점 집중도), **Reciprocity**(상호 호혜적 안전 지원 비율).

### 5. 네트워크 데이터 구조 및 코딩처리 방식 (Data & Coding Method)

| 구분 | 데이터 형식 | 변수 구성 및 코딩 기준 |
| :--- | :--- | :--- |
| **노드 속성 데이터<br/>(Node Properties)** | 1-mode 엑셀 테이블<br/>(행 = 소방관 $i$) | • **ID**: 고유 식별코드 (FF01 ~ FF50)<br/>• **Rank (계급)**: 1=지휘관리층(령·경), 2=중간관리층(위·장), 3=일선대원층(교·사)<br/>• **Team (근무팀)**: 1팀, 2팀, 3팀 / **Role (직무)**: 1=구조, 2=진압, 3=구급, 4=운전<br/>• **Tenure (경력)**: 소방 근무 연수(연 단위 연속형 변수) |
| **관계 매트릭스 1<br/>(현장 소통망 $M_{\text{comm}}$)** | $N \times N$ 정방 행렬 | "현장 출동 시 안전 정보 및 작전 상황을 얼마나 자주 소통하는가?" (1점~5점, 4점 이상 이진화 병행) |
| **관계 매트릭스 2<br/>(전술 조언망 $M_{\text{advice}}$)** | $N \times N$ 정방 행렬 | "비정형 고위험(산악·수난) 현장에서 위험 판단 및 구조 전술에 대해 누구에게 조언을 구하는가?" |
| **관계 매트릭스 3<br/>(장비 차용망 $M_{\text{resource}}$)** | $N \times N$ 정방 행렬 | "긴급 상황 발생 시 특수 장비, 유압장비, 로프 등을 상호 융통하고 지원받는 관계는 누구인가?" |
| **관계 매트릭스 4<br/>(신뢰/아차사고망 $M_{\text{trust}}$)** | $N \times N$ 정방 행렬 | "현장에서 겪은 아차사고(Near-Miss)나 실수를 문책 걱정 없이 솔직하게 털어놓고 의논할 수 있는 동료는 누구인가?" |

### 6. [실전 적용 시뮬레이션] 가상 소방관 5인 데이터로 보는 네트워크 데이터 수집부터 넷마이너 분석까지의 전 과정

> [!TIP] **일반 설문조사(R방법론) vs 네트워크 분석(SNA)의 결정적 차이**  
> • **일반 설문조사 (R방법론)**: "당신은 현장 안전수칙을 잘 지킵니까? (1~5점)" $\rightarrow$ 개인 점수의 단순 평균만 산출하여 조직 내 소통 혈관의 막힘을 볼 수 없음.  
> • **네트워크 분석 (SNA)**: "당신은 현장에서 위험에 직면했을 때 **동료 중 누구에게** 무전을 치고 전술 조언을 구합니까?" $\rightarrow$ 사람과 사람 사이에 흐르는 **관계(화살표) 데이터**를 수집하여 소통 병목과 고립 대원을 정밀 진단함.

#### [Step 1] 현장에 배포되는 실제 설문지 양식 (명부형 Roster 방식 예시: 응답자 = D. 최대원)

| 대상 동료 (Alters) | 전혀 안 함 (0점) | 가끔 의논 (1점) | 보통 (2점) | 자주 의논 (3점) | 매우 자주 의논 (4점) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **A. 김서장 (지휘관리층)** | [ V ] | | | | |
| **B. 이팀장 (중간관리층)** | | | [ V ] | | |
| **C. 박주임 (구조주임/베테랑)** | | | | | **[ V ]** |
| **D. 최대원 (본인)** | - | - | - | - | - |
| **E. 정신임 (신규 임용 구조대원)** | | [ V ] | | | |

#### [Step 2] 설문 응답의 엑셀 관계 매트릭스(Adjacency Matrix, $5 \times 5$) 변환

| 보내는 사람 $\downarrow$ \ 받는 사람 $\rightarrow$ | A. 김서장 | B. 이팀장 | C. 박주임 | D. 최대원 | E. 정신임 | 해석 요약 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **A. 김서장 (지휘관리)** | 0 | **4** | 0 | 0 | 0 | 서장은 공식 보고 라인인 이팀장(B)에게만 지시/소통 |
| **B. 이팀장 (중간관리)** | **4** | 0 | **4** | **3** | 0 | 팀장은 서장(A), 주임(C), 대원(D)과 활발히 연결 |
| **C. 박주임 (구조베테랑)** | 0 | **4** | 0 | **4** | **4** | 주임은 팀장(B), 대원(D), 신임(E) 모두에게 조언 제공 |
| **D. 최대원 (일선대원)** | 0 | **2** | **4** | 0 | **1** | 대원은 위험 시 베테랑 박주임(C)에게 전적으로 의존 |
| **E. 정신임 (신규임용)** | 0 | 0 | **4** | **1** | 0 | 신임은 박주임(C) 외에는 거의 아무와도 소통하지 못함 |

#### [Step 3] 넷마이너(NetMiner)가 계산해 낸 3대 핵심 발견 및 진단 비교
1. **실질적 현장 안전 리더 발견 (In-Degree 1위 = C. 박주임)**: 계급장과 무관하게 대원 전원이 실제 위기 시 가장 신뢰하고 조언을 구하는 핵심 안전 리더가 박주임임을 데이터로 입증.
2. **소통 병목(Bottleneck) 발견 (Betweenness 1위 = C. 박주임, 80% 이상 독점)**: 지휘부(A, B)와 일선 대원(D, E)을 연결하는 다리가 박주임 1명뿐이므로, 박주임 부재·사고 시 지휘 소통망이 단절되는 구조적 취약성 포착.
3. **순직·사고 위험 고립 대원 발견 (Isolates 경고 = E. 정신임)**: 박주임 외에는 누구와도 연결되지 못한 고립 상태로, 현장 진입 시 위험 경고를 받지 못할 위험이 가장 높음 $\rightarrow$ **(1) 박주임을 공식 현장 안전 코디네이터로 지정, (2) 신임 대원 전담 멘토링 매칭, (3) 지휘부-대원 다이렉트 비상 무전 채널 신설**이라는 즉각적 정책 환류 도출.
"""

ch5_extra_md = """

---

## [부록] 박사학위 논문 선행연구 9단계 분석 템플릿 (Chapter 5)

| 단계 | 분석 항목 | 제5장 (Nowell & Steelman, 2017, pp. 63–74) 핵심 내용 |
| :---: | :--- | :--- |
| **1** | **연구배경** | 대규모 산불 대응과 같이 단일 기관이 감당할 수 없는 재난에서 다기관 네트워크(Incident Response Networks)가 필수적이나, 네트워크 전체 및 하위 기능별 성과를 누구의 관점에서 어떻게 측정할 것인가에 대한 방법론적 난제가 존재함. |
| **2** | **이론적 개념** | **네트워크 분석의 4대 층위**(이원관계·서브네트워크·하위집단·전체망), **성과 평가 5대 원칙**, **실재론적 객관주의(Realist Objectivism) vs 다원주의(Pluralism)**, **인지 이론 3대 프로세스**(지각 Sensing · 의미구성 Sensemaking · 평가 Evaluating). |
| **3** | **연구목적** | 산불 대응 네트워크 내 다양한 참여 주체(연방 사고지휘팀 IMT, 국유림 담당관, 지역 카운티 재난관리자·보안관·소방서) 간에 네트워크 성과 평가의 유의미한 시각차(다원주의)가 존재하는지 다수준 모형(HLM)으로 실증 규명함. |
| **4** | **연구방법** | 2009~2010년 미국 서부 5개 주에서 발생한 **21건의 대규모 산불 사건**, **457명의 대응 참여자** 설문 데이터 수집. 30개 기능 문항을 탐색적 요인분석(EFA)하여 4대 핵심 수행 영역(상호작용 규칙, 공공정보, 피난 관리, 인프라 보호; $\alpha = .85 \sim .93$) 도출 후 **2수준 위계선형모형(HLM)** 분석 수행. |
| **5** | **연구결과** | • **분산 구성요소(Table 5.4)**: 성과 평가 총 변량의 **83%~97%가 산불 사건 간(Between-incident)이 아니라 동일 산불 내부의 개인 간(Within-incident)에 존재**함(ICC = .03 ~ .17).<br/>• **집단별 효과(Table 5.5)**: 외부에서 파견된 **사고지휘팀(IMT)**은 모든 영역에서 성과를 유의미하게 높게 평가($\beta = 0.25 \sim 0.45, p < .01$)한 반면, **지역 카운티 대응자**는 인프라 보호 성과를 유의미하게 낮게 평가($\beta = -0.35, p < .05$)함. |
| **6** | **핵심 발견** | 전통적인 실재론적 객관주의 가정(참여자 점수를 단순 평균하여 네트워크 성과로 삼는 방식)은 동일 사건 내 **83~97%에 달하는 내부 인식 격차를 측정 오차로 은폐**하는 심각한 방법론적 오류를 범함. |
| **7** | **연구의 한계** | 미 서부 산불 대응이라는 특정 제도적 맥락(ICS/IMT 체계)에 국한된 횡단적 사후 설문 데이터이며, 객관적 물리적 피해 지표와 주관적 다원 평가 간의 결합 분석은 후속 과제로 남겨짐. |
| **8** | **이론적 시사점** | 네트워크 성과 측정에서 **다원주의(Pluralism) 패러다임**을 실증적으로 확립하고, 네트워크 내 위치·소속에 따라 지각(Sensing), 의미구성(Sensemaking), 평가(Evaluating)가 체계적으로 분화됨을 규명함. |
| **9** | **후속 연구 시사점** | (1) 다원적 관점 기반 표본추출 설계 의무화, (2) 단일 평균점수 대신 **응답자 간 합의 수준(표준편차 SD, 변량)**을 핵심 독립/종속변수로 활용하는 **다원주의적 반영 평가 모델(Pluralistic Reflection Model)** 도입. |
"""

ch6_extra_md = """

---

## [부록] 박사학위 논문 선행연구 9단계 분석 템플릿 (Chapter 6)

| 단계 | 분석 항목 | 제6장 (Harris & Doerfel, 2017, pp. 75–91) 핵심 내용 |
| :---: | :--- | :--- |
| **1** | **연구배경** | 2012년 슈퍼스톰 샌디로 가옥 2,100채 중 1,200채가 파손(700채는 50% 이상 반파·전파)되고 시청·경찰서·구급대가 파괴된 뉴저지주 해안 마을 오션포트(Oceanport)가 자체 구호와 인근 해안지역 광역 거점(staging area) 역할을 동시에 수행함. |
| **2** | **이론적 개념** | **사회적 회복탄력성(Social Resilience)**, **강한/약한/잠재적 연계(Strong/Weak/Latent ties)**, 연결·매개 중심성 및 네트워크 집중화, 민츠버그(Mintzberg, 2015)의 **다원 부문(Plural Sector)**, **잉여적 자원 클러스터(Redundant resource clusters)**. |
| **3** | **연구목적** | (1) 응급 대응에서 장기 복구로 이동함에 따라 네트워크 집중화(centralization)가 변하는가? (2) 지역 조직과 전국 조직 중 누가 더 중심적인가? (3) 재난 대비·대응·복구 정책(NRF 등)에 주는 시사점은 무엇인가? |
| **4** | **연구방법** | 샌디 상륙 직후 약 3개월(2012.10.29~12.24)을 4개 시점(Times 1&2, Time 3, Time 4)으로 구분. 2년간의 참여관찰·문서분석·인터뷰·설문 등을 통해 26개 활동 조직($n=26$)의 양방향 커뮤니케이션 네트워크를 구축하고 UCINET으로 연결 중심성, 프리먼 매개 중심성, 집중화 분석 수행. |
| **5** | **연구결과** | • **네트워크 집중화**: Time 1(61%) $\rightarrow$ Time 3(59%, 일시 감소) $\rightarrow$ Time 4(78%, 급증).<br/>• **조직 구성 변화**: 지역 조직 비중 감소(87% $\rightarrow$ 73%), 전국 조직 비중 증가(13% $\rightarrow$ 18%).<br/>• **중심성 결과**: 전 기간에 걸쳐 **Oceanport OEM**과 **Oceanport Cares**가 연결·매개 중심성 최상위 기록(Time 4에는 Cares가 1위). FEMA와 적십자사는 초기 지역 커뮤니케이션 망에서 주변부(peripheral)에 머묾. |
| **6** | **핵심 발견** | 공식 지자체 조직(**Oceanport OEM**)과 자생적 시민 자원봉사 조직(**Oceanport Cares**, 이후 501c3 법인화) 두 지역 브로커가 공식 응급대응망과 비공식 사회적 지원망을 결합하여 충격 지점(point of impact)에 **잉여적 자원 클러스터**를 창출함으로써 외부 의존성을 낮추고 회복탄력성을 달성함. |
| **7** | **연구의 한계** | 샌디 이후 3개월간 소규모 중산층 지역사회를 다룬 단일 현장 사례 연구임. 대규모 도시에서는 다수의 풀뿌리 집단이 경쟁하여 OEM의 조정이 어려울 수 있으며, 공식 제도와 결합한 오션포트 사례는 공식 제도 밖에서 작동한 Occupy Sandy와는 대조됨. |
| **8** | **이론적 시사점** | 재난 피해 지역사회 연구에 민츠버그(2015)의 **다원 부문(plural sector)** 프레임워크를 최초로 실증 적용한 연구 중 하나이며, 피해 당사자인 지역 조직이 물리적·네트워크적 위치를 통해 효율적 자원 브로커리지를 수행함을 규명함. |
| **9** | **정책·후속 시사점** | 국가대응프레임워크(NRF) 등 공식 재난 계획에서 자생적 자원봉사자와 지역 다원 부문을 부수적(ancillary) 존재로 치부하지 말고, 지역 이해관계자 네트워크를 공식 계획 및 운영 활동에 적극 통합·지원하도록 정책 프레임워크를 재검토해야 함. |
"""

# Append to chapter4-subnote.md, chapter5-subnote.md, chapter6-subnote.md if not already present
with open("chapter4-subnote.md", "r", encoding="utf-8") as f:
    c4 = f.read()
if "박사학위 논문 선행연구 9단계 분석 템플릿 (Chapter 4)" not in c4:
    c4 += ch4_extra_md
    with open("chapter4-subnote.md", "w", encoding="utf-8") as f:
        f.write(c4)
    print("Updated chapter4-subnote.md with 9-step template & fire service protocol + 5-person simulation.")

with open("chapter5-subnote.md", "r", encoding="utf-8") as f:
    c5 = f.read()
if "박사학위 논문 선행연구 9단계 분석 템플릿 (Chapter 5)" not in c5:
    # insert right before "# 11. ★ [내 연구 적용]"
    target = "# 11. ★ [내 연구 적용]"
    if target in c5:
        c5 = c5.replace(target, ch5_extra_md.strip() + "\n\n---\n\n" + target)
    else:
        c5 += ch5_extra_md
    with open("chapter5-subnote.md", "w", encoding="utf-8") as f:
        f.write(c5)
    print("Updated chapter5-subnote.md with 9-step template.")

with open("chapter6-subnote.md", "r", encoding="utf-8") as f:
    c6 = f.read()
if "박사학위 논문 선행연구 9단계 분석 템플릿 (Chapter 6)" not in c6:
    target = "## 7. ★ [내 연구 적용]"
    if target in c6:
        c6 = c6.replace(target, ch6_extra_md.strip() + "\n\n---\n\n" + target)
    else:
        c6 += ch6_extra_md
    with open("chapter6-subnote.md", "w", encoding="utf-8") as f:
        f.write(c6)
    print("Updated chapter6-subnote.md with 9-step template.")

# 2. Build the Master Integrated Markdown file (SNA_통합_서브노트_Ch1-7.md)
master_header = """# 재난관리 사회연결망 연구총서 (Chapters 1 ~ 7 통합 학술 서브노트 & 소방 실증 프로토콜)

**원전 총서**: *Social Network Analysis of Disaster Response, Recovery, and Adaptation* (Edited by Eric C. Jones & A.J. Faas, Elsevier, 2017)  
**구성 범위**: Part I (이론 및 방법론: 제1장 ~ 제4장) & Part II (재난 대응 실증 연구: 제5장 ~ 제7장) 전 7개 챕터 완전판  
**포함 특집**: 박사학위 논문 선행연구 9단계 분석 템플릿 + 소방 조직·현장 대응 실증 연구 설계(NetMiner 프로토콜, 법령 매핑 KPI, 5인 가상 시뮬레이션)

---

## [총괄 요약] 전 7개 챕터 핵심 아키텍처 및 소방 연구 연계 일람

| 장 (Chapter) | 원제 및 저자 | 핵심 학술 이론 및 분석 모형 | 소방 조직·현장 대응 실증 적용 주제 |
| :---: | :--- | :--- | :--- |
| **제1장** | *An Introduction to Social Network Analysis in Disaster Contexts*<br/>(Eric C. Jones & A.J. Faas, pp. 3–9) | 은유적 vs 공식적 SNA, 대인망-조직망 결합, 잠재적 연계(Potential) vs 실현된 연계(Realized), 네트워크 존재론과 물신화 경계 | 평시 신뢰 잠재망($M_{\text{potential}}$)과 출동 무전 실현망($M_{\text{realized}}$)의 이중 네트워크(Dual Network) QAP 일치도 및 정보 왜곡 분석 |
| **제2장** | *Social Network Analysis Focused on Individuals Facing Hazards and Disasters*<br/>(A.J. Faas & Eric C. Jones, pp. 11–23) | 결속형·교량형·연계형 사회적 자본, **밀도의 역설(Paradox of Density)**, 코뮤니타스와 원조 자격의 정치, 표층 구조 vs 심층 구조 | 소방 조직 내 기수·연고 결속망의 부작용(안전 침묵) 규명을 위한 SNA 하위집단 분석 및 주관성 연구(Q방법론) 결합 모델 |
| **제3장** | *Interorganizational Networks in Disaster Management*<br/>(Naim Kapucu & Qian Hu, pp. 25–41) | 다층적 거버넌스(NRF-NIMS-ICS-ESF), 공식·비공식 대비망-대응망 전이, 협업 저해 4대 장벽, **5×5 메타 매트릭스(Meta-Matrix)** | 긴급구조통제단 다기관(소방·경찰·지자체·군·의료) 상호운용성 진단 및 행위자·지식·자원·과업·조직 5×5 메타 매트릭스 분석 |
| **제4장** | *Social Network Research Strategies for Disaster Response, Recovery, and Mitigation*<br/>(Danielle M. Varda, pp. 43–59) | **IOSP 프레임워크**(In/Out × Seeker/Provider), 다이론 다수준(MTML) 모델, QAP 및 ERGM($p^*$), 결측치(20% 임계점), 네트워크 취약성 | 의령소방서 119구조대 안전 책무성 4대 다중 매트릭스 설계, 넷마이너 7단계 프로토콜 및 **가상 소방관 5인 전 과정 시뮬레이션** |
| **제5장** | *Sensemaking and Evaluation in Incident Response Networks*<br/>(Branda Nowell & Toddi Steelman, pp. 63–74) | 성과 평가 5대 원칙, **실재론적 객관주의 vs 성과 다원주의(Pluralism)**, 21개 산불 HLM 실증(사건 내 개인 간 변량 83~97%), 지각-의미구성-평가 | 지휘부(IMT) 나홀로 고평가 편향 타파, 계급 간(지휘층-중간층-일선대원) 안전 인식 격차(SD 합의지표) 및 HLM·넷마이너 실증 |
| **제6장** | *Interorganizational Resilience: Networked Collaborations in Communities After Superstorm Sandy*<br/>(Jack L. Harris & Marya L. Doerfel, pp. 75–91) | 사회적 회복탄력성, **민츠버그의 다원 부문(Plural Sector)**, 시계열 진화(Times 1~4), 로컬 브로커리지(OEM & Cares), 잉여적 자원 클러스터 | 태풍·수해 시 소방서-의용소방대-자생단체 간 시계열(Times 1~4) 구호 네트워크 진화 및 의용소방대 로컬 브로커리지 KPI 도출 |
| **제7장** | *Shifting Attention: Modeling Follower Relationship Dynamics Among US Emergency Management-Related Organizations During a Colorado Wildfire*<br/>(Carter T. Butts et al., pp. 93–113) | 온라인 주의(Attention) 이동 동학, **동적 네트워크 로지스틱 회귀(DNR)**, 단기(1~3일) 도태 vs 장기(4~7일) 고착화 대칭 전환, 사전 고착화(Lock-in) | 대형 산불 시 재난관리 유관기관 간 시계열 상황전파·주의 네트워크 동학(DNR) 분석 및 발화 후 72시간 내 골든타임 주의 연결 KPI |

---
"""

chapters_md_list = []
toc_rows = []
for i in range(1, 8):
    with open(f"chapter{i}-subnote.md", "r", encoding="utf-8") as f:
        ch_md = f.read().strip()
    chapters_md_list.append(ch_md)
    # Extract H1 and H2 headings for static Master Table of Contents
    ch_title = ""
    sec_list = []
    for line in ch_md.splitlines():
        m1 = re.match(r'^#\s+(.+)$', line.strip())
        m2 = re.match(r'^##\s+(.+)$', line.strip())
        if m1:
            t = m1.group(1).strip()
            if t.startswith(f"제{i}장"):
                ch_title = t
            else:
                sec_list.append(f"• {t}")
        elif m2:
            t = m2.group(1).strip()
            if not t.startswith("[개요]") and not t.startswith("CHAPTER OUTLINE"):
                sec_list.append(f"• {t}")
    toc_rows.append(f"| **제{i}장** | **{ch_title}** | {'<br/>'.join(sec_list)} |")

static_toc_md = "## [전체 상세 목차] Chapters 1 ~ 7 통합 서브노트 목차 (Table of Contents)\n\n| 구분 | 챕터 제목 | 주요 절(Section) 및 특집 구성 |\n| :---: | :--- | :--- |\n" + "\n".join(toc_rows) + "\n\n---\n"

full_integrated_md = master_header + "\n" + static_toc_md + "\n" + "\n\n---\n\n".join(chapters_md_list) + "\n"

with open("SNA_통합_서브노트_Ch1-7.md", "w", encoding="utf-8") as f:
    f.write(full_integrated_md)

print(f"Saved SNA_통합_서브노트_Ch1-7.md ({len(full_integrated_md):,} chars).")

# 3. Convert Mermaid blocks into structured Word Diagram Tables for the DOCX build
def mermaid_to_md_table(match):
    code = match.group(1).strip()
    lines = [l.strip() for l in code.splitlines() if l.strip()]
    if not lines:
        return ""
    header_line = lines[0]

    # Parse node labels id["label"] or id[label] or id{"label"}
    node_map = {}
    for l in lines[1:]:
        for m in re.finditer(r'([A-Za-z0-9_가-힣]+)\s*[\[\(\{]+[\"\']?(.*?)[\"\']?[\]\)\}]+', l):
            nid, nlabel = m.group(1), m.group(2)
            nlabel = nlabel.replace("<br/>", " / ").replace("<br>", " / ").strip()
            node_map[nid] = nlabel

    rows = []
    current_group = "전체 흐름"

    if header_line.startswith("pie"):
        title_m = re.search(r'title\s+(.+)', header_line)
        p_title = title_m.group(1).strip() if title_m else "비율 분포 다이어그램"
        for l in lines[1:]:
            pm = re.match(r'[\"\'](.+?)[\"\']\s*:\s*([0-9.]+)', l)
            if pm:
                rows.append((p_title, pm.group(1), f"{pm.group(2)}%"))
        if rows:
            out = ["\n| 📊 다이어그램 구분 | 항목 (Category) | 비중 / 수치 |", "| :--- | :--- | :--- |"]
            for r in rows:
                out.append(f"| **{r[0]}** | {r[1]} | **{r[2]}** |")
            return "\n".join(out) + "\n"

    if header_line.startswith("classDiagram"):
        cls_name = "구조 분류"
        for l in lines[1:]:
            if l.startswith("class "):
                cm = re.match(r'class\s+([A-Za-z0-9_가-힣]+)', l)
                if cm:
                    cls_name = cm.group(1)
            elif l.startswith("+"):
                item = l[1:].strip()
                if ":" in item:
                    k, v = item.split(":", 1)
                    rows.append((cls_name, k.strip(), v.strip()))
                else:
                    rows.append((cls_name, item, "핵심 구성요소"))
        if rows:
            out = ["\n| 📊 구조 다이어그램 분류 | 세부 구성 항목 | 핵심 내용 및 특성 |", "| :--- | :--- | :--- |"]
            for r in rows:
                out.append(f"| **{r[0]}** | **{r[1]}** | {r[2]} |")
            return "\n".join(out) + "\n"

    # Flowchart TD / LR
    for l in lines[1:]:
        if l.startswith("style ") or l.startswith("classDef ") or l.startswith("class "):
            continue
        if l.startswith("subgraph "):
            sg_m = re.search(r'subgraph\s+[A-Za-z0-9_가-힣]+\s*\[[\"\']?(.*?)[\"\']?\]', l)
            if sg_m:
                current_group = sg_m.group(1).replace("<br/>", " ")
            else:
                current_group = l.replace("subgraph", "").strip().strip('"\'[]')
            continue
        if l == "end":
            current_group = "전체 흐름"
            continue

        # Check edge patterns: A --> B, A -- "label" --> B, A <-->|label| B, etc.
        # Clean inline node definitions first by replacing nid[...] with nid
        l_clean = l
        for m in re.finditer(r'([A-Za-z0-9_가-힣]+)\s*[\[\(\{]+[\"\']?(.*?)[\"\']?[\]\)\}]+', l):
            nid, nlabel = m.group(1), m.group(2).replace("<br/>", " / ").replace("<br>", " / ").strip()
            node_map[nid] = nlabel

        # Edge with label: -- "text" --> or -->|text| or -. "text" .->
        edge_lbl = "➔ (전개/영향)"
        em1 = re.search(r'--\s*[\"\'](.*?)[\"\']\s*-->', l)
        em2 = re.search(r'-\.\s*[\"\'](.*?)[\"\']\s*\.->', l)
        em3 = re.search(r'[<=-]+>\s*\|(.*?)\|', l)
        if em1:
            edge_lbl = f"➔ ({em1.group(1)})"
        elif em2:
            edge_lbl = f"⇢ ({em2.group(1)})"
        elif em3:
            edge_lbl = f"➔ ({em3.group(1)})"
        elif "<-->" in l or "<==>" in l:
            edge_lbl = "↔ (상호작용)"
        elif "-.->" in l or "-.-" in l:
            edge_lbl = "⇢ (제약/연계)"

        # Extract left and right node IDs around arrow
        arrow_split = re.split(r'\s*(?:<-->|<==>|--\s*[\"\'].*?[\"\']\s*-->|-\.\s*[\"\'].*?[\"\']\s*\.->|[<=-]+>\s*\|.*?\|-->|==>|-.->|-\.-|-->|<--)\s*', l)
        if len(arrow_split) >= 2:
            for idx_s in range(len(arrow_split) - 1):
                lhs_raw = arrow_split[idx_s].strip()
                rhs_raw = arrow_split[idx_s + 1].strip()
                lhs_id = re.match(r'^([A-Za-z0-9_가-힣]+)', lhs_raw)
                rhs_id = re.match(r'^([A-Za-z0-9_가-힣]+)', rhs_raw)
                lhs_txt = node_map.get(lhs_id.group(1), lhs_raw) if lhs_id else lhs_raw
                rhs_txt = node_map.get(rhs_id.group(1), rhs_raw) if rhs_id else rhs_raw
                rows.append((current_group, lhs_txt, f"{edge_lbl} **{rhs_txt}**"))
        else:
            # Standalone node inside subgraph
            nid_m = re.match(r'^([A-Za-z0-9_가-힣]+)', l)
            if nid_m and nid_m.group(1) in node_map:
                n_txt = node_map[nid_m.group(1)]
                if " : " in n_txt or ": " in n_txt:
                    parts = n_txt.split(":", 1)
                    rows.append((current_group, parts[0].strip(), parts[1].strip()))
                elif " / " in n_txt:
                    parts = n_txt.split(" / ", 1)
                    rows.append((current_group, parts[0].strip(), parts[1].strip()))
                else:
                    rows.append((current_group, nid_m.group(1), n_txt))

    if rows:
        out = ["\n| 📊 구조 모형 / 단계 구분 | 출발 노드 · 핵심 개념 | 연결 방향 및 도달 결과 (Flow & Mechanism) |", "| :--- | :--- | :--- |"]
        for r in rows:
            g = r[0].replace("|", "/")
            c1 = r[1].replace("|", "/")
            c2 = r[2].replace("|", "/")
            out.append(f"| **{g}** | {c1} | {c2} |")
        return "\n".join(out) + "\n"
    return ""

docx_ready_md = re.sub(r'```mermaid\n(.*?)```', mermaid_to_md_table, full_integrated_md, flags=re.S)

# Transform GitHub callout markers [!NOTE], [!IMPORTANT], [!TIP], [!WARNING], [!CAUTION] into styled labels
callout_replacements = {
    "[!NOTE]": "📘 **[학술 노트 / NOTE]** ",
    "[!IMPORTANT]": "🚨 **[핵심 원칙 / IMPORTANT]** ",
    "[!TIP]": "💡 **[연구 팁 / TIP]** ",
    "[!WARNING]": "⚠️ **[주의사항 / WARNING]** ",
    "[!CAUTION]": "🛑 **[경고 / CAUTION]** ",
}
for k, v in callout_replacements.items():
    docx_ready_md = docx_ready_md.replace(k, v)

temp_md_path = "/Users/sg/Project/SNA/scratch/temp_docx_source.md"
with open(temp_md_path, "w", encoding="utf-8") as f:
    f.write(docx_ready_md)

# 4. Write Lua filter to handle HTML inline tags (<br/>, <b>, <sub>, <sup>) cleanly in Pandoc
lua_filter_path = "/Users/sg/Project/SNA/scratch/docx_filter.lua"
lua_code = """
function RawInline(el)
  if el.format:match 'html' then
    local t = el.text:lower()
    if t:match '^<br%s*/?>' then
      return pandoc.LineBreak()
    elseif t:match '^</?b>' or t:match '^</?strong>' or t:match '^</?i>' or t:match '^</?em>' or t:match '^</?sub>' or t:match '^</?sup>' then
      return pandoc.Str('')
    end
  end
end
"""
with open(lua_filter_path, "w", encoding="utf-8") as f:
    f.write(lua_code)

raw_docx_path = "/Users/sg/Project/SNA/scratch/raw_output.docx"
final_docx_path = "/Users/sg/Project/SNA/SNA_통합_서브노트_Ch1-7.docx"

print("Running Pandoc to generate base DOCX (without dynamic TOC field to prevent Word security popup)...")
cmd = [
    "pandoc",
    temp_md_path,
    "-f", "markdown",
    "-t", "docx",
    "--lua-filter=" + lua_filter_path,
    "--resource-path=/Users/sg/Project/SNA",
    "-o", raw_docx_path
]
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode != 0:
    print("Pandoc error:", res.stderr)
    raise RuntimeError("Pandoc failed")
print("Pandoc base DOCX created successfully.")

# 5. Post-process DOCX XML (word/document.xml & word/styles.xml) for publication-grade styling
W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
ET.register_namespace("w", W_NS)
ET.register_namespace("r", "http://schemas.openxmlformats.org/officeDocument/2006/relationships")
ET.register_namespace("wp", "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing")
ET.register_namespace("a", "http://schemas.openxmlformats.org/drawingml/2006/main")
ET.register_namespace("pic", "http://schemas.openxmlformats.org/drawingml/2006/picture")
ET.register_namespace("m", "http://schemas.openxmlformats.org/officeDocument/2006/math")

def w_tag(name):
    return f"{{{W_NS}}}{name}"

extract_dir = "/Users/sg/Project/SNA/scratch/docx_extracted"
if os.path.exists(extract_dir):
    shutil.rmtree(extract_dir)
with zipfile.ZipFile(raw_docx_path, 'r') as z:
    z.extractall(extract_dir)

# Update word/styles.xml for Korean/English fonts and Heading styles
styles_xml_path = os.path.join(extract_dir, "word", "styles.xml")
styles_tree = ET.parse(styles_xml_path)
styles_root = styles_tree.getroot()

# Set default fonts in docDefaults
for rFonts in styles_root.iter(w_tag("rFonts")):
    rFonts.set(w_tag("ascii"), "Malgun Gothic")
    rFonts.set(w_tag("hAnsi"), "Malgun Gothic")
    rFonts.set(w_tag("eastAsia"), "Malgun Gothic")
    rFonts.set(w_tag("cs"), "Malgun Gothic")
    for attr in [w_tag("asciiTheme"), w_tag("hAnsiTheme"), w_tag("eastAsiaTheme"), w_tag("cstheme")]:
        if attr in rFonts.attrib:
            del rFonts.attrib[attr]

# Style Headings in styles.xml
heading_configs = {
    "Heading1": {"color": "0F172A", "sz": "32", "border_color": "0284C7", "space_before": "360", "space_after": "160"},
    "Heading2": {"color": "0369A1", "sz": "26", "border_color": "BAE6FD", "space_before": "280", "space_after": "120"},
    "Heading3": {"color": "1E3A8A", "sz": "23", "border_color": None, "space_before": "200", "space_after": "80"},
    "Heading4": {"color": "334155", "sz": "21", "border_color": None, "space_before": "160", "space_after": "60"},
}

for style in styles_root.findall(w_tag("style")):
    sid = style.get(w_tag("styleId"))
    if sid in heading_configs:
        cfg = heading_configs[sid]
        rPr = style.find(w_tag("rPr"))
        if rPr is None:
            rPr = ET.SubElement(style, w_tag("rPr"))
        # Bold
        if rPr.find(w_tag("b")) is None:
            ET.SubElement(rPr, w_tag("b"))
        # Color
        clr = rPr.find(w_tag("color"))
        if clr is None:
            clr = ET.SubElement(rPr, w_tag("color"))
        clr.set(w_tag("val"), cfg["color"])
        # Size
        sz = rPr.find(w_tag("sz"))
        if sz is None:
            sz = ET.SubElement(rPr, w_tag("sz"))
        sz.set(w_tag("val"), cfg["sz"])
        szCs = rPr.find(w_tag("szCs"))
        if szCs is None:
            szCs = ET.SubElement(rPr, w_tag("szCs"))
        szCs.set(w_tag("val"), cfg["sz"])

        pPr = style.find(w_tag("pPr"))
        if pPr is None:
            pPr = ET.SubElement(style, w_tag("pPr"))
        spc = pPr.find(w_tag("spacing"))
        if spc is None:
            spc = ET.SubElement(pPr, w_tag("spacing"))
        spc.set(w_tag("before"), cfg["space_before"])
        spc.set(w_tag("after"), cfg["space_after"])

        if cfg["border_color"]:
            pBdr = pPr.find(w_tag("pBdr"))
            if pBdr is None:
                pBdr = ET.SubElement(pPr, w_tag("pBdr"))
            btm = pBdr.find(w_tag("bottom"))
            if btm is None:
                btm = ET.SubElement(pBdr, w_tag("bottom"))
            btm.set(w_tag("val"), "single")
            btm.set(w_tag("sz"), "12" if sid == "Heading1" else "6")
            btm.set(w_tag("space"), "4")
            btm.set(w_tag("color"), cfg["border_color"])

styles_tree.write(styles_xml_path, xml_declaration=True, encoding="utf-8")

# Update word/document.xml for tables, blockquotes/callouts, page setup, and chapter page breaks
doc_xml_path = os.path.join(extract_dir, "word", "document.xml")
doc_tree = ET.parse(doc_xml_path)
doc_root = doc_tree.getroot()
body = doc_root.find(w_tag("body"))

# Page setup (A4: w=11906, h=16838, margins=1247 dxa ~ 2.2cm)
sectPr = body.find(w_tag("sectPr"))
if sectPr is None:
    sectPr = ET.SubElement(body, w_tag("sectPr"))
pgSz = sectPr.find(w_tag("pgSz"))
if pgSz is None:
    pgSz = ET.SubElement(sectPr, w_tag("pgSz"))
pgSz.set(w_tag("w"), "11906")
pgSz.set(w_tag("h"), "16838")

pgMar = sectPr.find(w_tag("pgMar"))
if pgMar is None:
    pgMar = ET.SubElement(sectPr, w_tag("pgMar"))
for side in ["top", "bottom", "left", "right"]:
    pgMar.set(w_tag(side), "1247")
pgMar.set(w_tag("header"), "708")
pgMar.set(w_tag("footer"), "708")

# Style Paragraphs: Page break before Chapter titles ("제1장" ~ "제7장"), Callout boxes for BlockText
for p in body.iter(w_tag("p")):
    pPr = p.find(w_tag("pPr"))
    pStyle = pPr.find(w_tag("pStyle")) if pPr is not None else None
    style_val = pStyle.get(w_tag("val")) if pStyle is not None else ""

    # Get full text of paragraph
    p_text = "".join(t.text for t in p.iter(w_tag("t")) if t.text)

    # Add pageBreakBefore on main Chapter headings ("제1장 " ~ "제7장 ")
    if style_val == "Heading1" and re.match(r'^제[1-7]장\s', p_text.strip()):
        if pPr.find(w_tag("pageBreakBefore")) is None:
            ET.SubElement(pPr, w_tag("pageBreakBefore"))

    # Style BlockText / Quotations as Callout cards
    if style_val in ("BlockText", "Quotations", "Quote"):
        pBdr = pPr.find(w_tag("pBdr"))
        if pBdr is None:
            pBdr = ET.SubElement(pPr, w_tag("pBdr"))
        left_b = pBdr.find(w_tag("left"))
        if left_b is None:
            left_b = ET.SubElement(pBdr, w_tag("left"))
        left_b.set(w_tag("val"), "single")
        left_b.set(w_tag("sz"), "24")  # 3pt bar
        left_b.set(w_tag("space"), "8")
        # Pick accent color based on callout type
        if "핵심 원칙" in p_text or "주의사항" in p_text or "경고" in p_text:
            left_b.set(w_tag("color"), "D97706")
            fill_hex = "FFFBEB"
        elif "연구 팁" in p_text:
            left_b.set(w_tag("color"), "059669")
            fill_hex = "ECFDF5"
        else:
            left_b.set(w_tag("color"), "0284C7")
            fill_hex = "F0F9FF"

        shd = pPr.find(w_tag("shd"))
        if shd is None:
            shd = ET.SubElement(pPr, w_tag("shd"))
        shd.set(w_tag("val"), "clear")
        shd.set(w_tag("color"), "auto")
        shd.set(w_tag("fill"), fill_hex)

# Style all Tables (<w:tbl>) with full borders, Navy/Teal Header Row, White Header Text, Zebra striping, and Cell Padding
table_count = 0
for tbl in body.iter(w_tag("tbl")):
    table_count += 1
    tblPr = tbl.find(w_tag("tblPr"))
    if tblPr is None:
        tblPr = ET.Element(w_tag("tblPr"))
        tbl.insert(0, tblPr)

    # Full width (100% = 5000 pct)
    tblW = tblPr.find(w_tag("tblW"))
    if tblW is None:
        tblW = ET.SubElement(tblPr, w_tag("tblW"))
    tblW.set(w_tag("w"), "5000")
    tblW.set(w_tag("type"), "pct")

    # Table Borders
    tblBorders = tblPr.find(w_tag("tblBorders"))
    if tblBorders is not None:
        tblPr.remove(tblBorders)
    tblBorders = ET.SubElement(tblPr, w_tag("tblBorders"))
    for b_name, b_sz, b_clr in [
        ("top", "12", "1E293B"),
        ("bottom", "12", "1E293B"),
        ("left", "4", "CBD5E1"),
        ("right", "4", "CBD5E1"),
        ("insideH", "4", "CBD5E1"),
        ("insideV", "4", "CBD5E1"),
    ]:
        b_el = ET.SubElement(tblBorders, w_tag(b_name))
        b_el.set(w_tag("val"), "single")
        b_el.set(w_tag("sz"), b_sz)
        b_el.set(w_tag("space"), "0")
        b_el.set(w_tag("color"), b_clr)

    # Table Cell Margins (padding)
    tblCellMar = tblPr.find(w_tag("tblCellMar"))
    if tblCellMar is not None:
        tblPr.remove(tblCellMar)
    tblCellMar = ET.SubElement(tblPr, w_tag("tblCellMar"))
    for m_side, m_val in [("top", "100"), ("bottom", "100"), ("left", "140"), ("right", "140")]:
        m_el = ET.SubElement(tblCellMar, w_tag(m_side))
        m_el.set(w_tag("w"), m_val)
        m_el.set(w_tag("type"), "dxa")

    rows = tbl.findall(w_tag("tr"))
    if not rows:
        continue

    # Check if this is a Diagram Table (starts with 📊)
    first_row_text = "".join(t.text for t in rows[0].iter(w_tag("t")) if t.text)
    is_diagram_tbl = "📊" in first_row_text
    header_bg = "0F172A" if not is_diagram_tbl else "0369A1"

    for r_idx, tr in enumerate(rows):
        trPr = tr.find(w_tag("trPr"))
        if trPr is None:
            trPr = ET.Element(w_tag("trPr"))
            tr.insert(0, trPr)

        if r_idx == 0:
            if trPr.find(w_tag("tblHeader")) is None:
                ET.SubElement(trPr, w_tag("tblHeader"))

        for tc in tr.findall(w_tag("tc")):
            tcPr = tc.find(w_tag("tcPr"))
            if tcPr is None:
                tcPr = ET.Element(w_tag("tcPr"))
                tc.insert(0, tcPr)

            # Vertical alignment center for header, top for body
            vAlign = tcPr.find(w_tag("vAlign"))
            if vAlign is None:
                vAlign = ET.SubElement(tcPr, w_tag("vAlign"))
            vAlign.set(w_tag("val"), "center" if r_idx == 0 else "top")

            # Shading
            shd = tcPr.find(w_tag("shd"))
            if shd is not None:
                tcPr.remove(shd)
            if r_idx == 0:
                shd = ET.SubElement(tcPr, w_tag("shd"))
                shd.set(w_tag("val"), "clear")
                shd.set(w_tag("color"), "auto")
                shd.set(w_tag("fill"), header_bg)
            elif r_idx % 2 == 0:
                shd = ET.SubElement(tcPr, w_tag("shd"))
                shd.set(w_tag("val"), "clear")
                shd.set(w_tag("color"), "auto")
                shd.set(w_tag("fill"), "F8FAFC" if not is_diagram_tbl else "F0F9FF")

            # Format runs inside cells
            for r in tc.iter(w_tag("r")):
                rPr = r.find(w_tag("rPr"))
                if rPr is None:
                    rPr = ET.Element(w_tag("rPr"))
                    r.insert(0, rPr)
                # Font size in tables: 19 half-points (9.5pt) for clean fit
                sz = rPr.find(w_tag("sz"))
                if sz is None:
                    sz = ET.SubElement(rPr, w_tag("sz"))
                sz.set(w_tag("val"), "19")
                szCs = rPr.find(w_tag("szCs"))
                if szCs is None:
                    szCs = ET.SubElement(rPr, w_tag("szCs"))
                szCs.set(w_tag("val"), "19")

                if r_idx == 0:
                    # Header text: bold white
                    if rPr.find(w_tag("b")) is None:
                        ET.SubElement(rPr, w_tag("b"))
                    clr = rPr.find(w_tag("color"))
                    if clr is None:
                        clr = ET.SubElement(rPr, w_tag("color"))
                    clr.set(w_tag("val"), "FFFFFF")

doc_tree.write(doc_xml_path, xml_declaration=True, encoding="utf-8")

# Re-pack into final DOCX
with zipfile.ZipFile(final_docx_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root_dir, dirs, files in os.walk(extract_dir):
        for file in files:
            full_path = os.path.join(root_dir, file)
            rel_path = os.path.relpath(full_path, extract_dir)
            zf.write(full_path, rel_path)

print(f"Styled {table_count} tables and created final DOCX at: {final_docx_path} ({os.path.getsize(final_docx_path)/(1024*1024):.2f} MB)")
