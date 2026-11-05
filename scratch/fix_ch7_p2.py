import json

ch7_p2 = {
    "36": "<br/>",
    "37": "팔로워 네트워크의 전체적인 구조적 특성을 파악할 수 있도록, 그림 7.2는 표본에 존재하는 213개 전체 조직 간의 시간 평균(time-averaged) 인접 관계를 시각화한 것이다. 노드들은 비상 관리 생태계 내에서의 구조적 위치에 따라 배치되었으며, 밀집된 중심부(core)와 느슨하게 연결된 주변부(periphery)의 뚜렷한 코어-주변부 구조를 보여준다.",
    "38": "여기서 우리는 최적 적합 블록 모델(block model)이 코어와 주변부 사이에 상호작용이 거의 없는 형태임을 발견한다. 코어 집단을 구성하는 조직들은 대다수가 연방재난관리청(FEMA) 관련 계정들과 주 방위군(National Guard) 계정들로 확인되었다. 반면 주변부 조직들은 주로 주지사 개인 계정이나 특정 지방 소방국 등 국지적인 주체들로 구성된다.",
    "39": "![그림 7.2](image-15.png)  \n*그림 7.2 전체 213개 미국 비상 관리 관련 조직 간 주의 집중 유대의 시간 평균 네트워크. 노드는 트위터 계정, 유향 엣지는 팔로잉 관계를 나타냄.*",
    "40": "<details>\n<summary>📌 [참고: Figure 7.2 그래프에 포함된 Twitter 계정 노드 목록 접기/펼치기]</summary>",
    "41": "`brianschweitzer`, `akgovparnell`, `govgregoire`, `idahodoi`, `govwalker`, `butchotter`, `govsambrownback`, `gov_heineman`, `mearng`, `fortalezapr`, `govmalloyoffice`, `govcorbett`, `governorperry`, `govkiamelson`, `govinslee`, `govsnyder`, `govhaley`, `govbrewer`, `govkasich`, `governorquinn`, `govsandoval`, `governorva`, `govherbert`, `govhickenlooper` 등 총 213개 계정.",
    "42": "</details>",
    "43": "<br/>",
    "44": "![표 7.2](image-16.png)",
    "45": "#### Table 7.2 The Core Members of the Twitter Follower Network, Categorized by Organizational Affiliation (FEMA, National Guard, State and Federal Agencies)",
    "46": """| 소속 (Affiliation) | 트위터 계정 목록 (Twitter Accounts) |
| :--- | :--- |
| **FEMA (연방재난관리청)** | `craigatfema`, `fema`, `femaregion1`, `femaregion2`, `femaregion3`, `femaregion4`, `femaregion5`, `femaregion6`, `femaregion7`, `femaregion8`, `femaregion9`, `femaregion10`, `femalive` |
| **National Guard (주 방위군)** | `alguard`, `flguard`, `guardintel`, `ia_nationalguard`, `idahonatguard`, `inng_pa`, `kansasguard`, `mdng`, `mingonline`, `mo_guard`, `msnationalguard`, `nc_guard`, `neguard`, `newyorkguard`, `nvnationalguard`, `ohionatlguard`, `okguard`, `pagaurd`, `scnationalguard`, `txguard`, `usnationalguard`, `vaguard`, `vtguard` |
| **Federal Agencies (연방 기관)** | `cdcemergency`, `dhsgov`, `fema`, `redcross`, `usfs`, `usgs` |
| **State Agencies (주 비상 기관)** | `calema`, `coemergency`, `flsert`, `gadoema`, `in_dhs`, `ky_em`, `mdema`, `mema_info`, `ncemergency`, `okem`, `scemd`, `txdps`, `vaemergency`, `waema` |""",
    "47": "<br/>",
    "48": "이러한 광범위한 코어-주변부 구조는 조직들이 네트워크 내에서 다른 조직을 팔로우하거나 언팔로우하기로 결정하는 복잡한 동적 프로세스의 장기적인 평균 행동을 반영한다. 이제 우리는 이러한 역학이 특정 대형 재난 사건에 의해 어떻게 교란되고 반응하는지 살펴보고자 한다.",
    "49": "### DISASTER CASE STUDY: COLORADO DUCKETT FIRE",
    "50": "산불은 미국 내 여러 지역에서 가장 심각한 관심사 중 하나이다. 대형 산림 화재는 수십억 달러의 피해를 입히고 수십만 에이커의 토지를 전소시킬 수 있다. 본 연구의 사례 연구 대상인 2011년 콜로라도주 더켓 크릭 산불(Duckett Creek Fire)은 2011년 6월 12일에 발화하여 며칠 만에 4,000에이커 이상의 산림과 가옥을 위협하며 급속도로 확산되었고, 연방재난관리청의 화재 관리 지원 보조금(FMAG) 선포를 이끌어냈다.[^3]",
    "51": "[^3]: FEMA 재난 선포 일자 및 지정 구역 세부사항은 https://www.fema.gov/disaster/2923 참조.",
    "52": "![그림 7.3](image-17.png)  \n*그림 7.3 위도/경도 공간에 투영된 카운티 경계선이 포함된 콜로라도 주도. 파란색 점은 콜로라도 주 내 비상 관리 관련 트위터 계정들의 위치를 나타냄.*",
    "53": "<br/>",
    "54": "![그림 7.4](image-18.png)  \n*그림 7.4 2011년 6월 15일 미국 산림청(USFS)이 촬영하여 트위터에 게시한 더켓 산불 진화 현장의 Type 1 소방 헬리콥터 비행 모습.*",
    "55": "## METHODS",
    "56": "트위터에서 미국 비상 관리 조직 간의 주의 집중 관계의 진화하는 본질을 분석하기 위해, 우리는 동적 네트워크 회귀(DNR; Almquist & Butts, 2013, 2014b) 기법을 사용한다.",
    "57": "### NOTATION",
    "58": "사회연결망은 종종 정점 집합 $V$(예: 조직)와 엣지 집합 $E$(예: 팔로워 관계)라는 두 개의 수학적 집합으로 정의되는 '그래프(graph)'로 표현된다: $G = (V, E)$. 트위터의 팔로잉은 일방향적 관계이므로, 우리는 방향성 그래프(directed graph)를 사용한다.",
    "59": "이러한 표현은 팔로워 기능의 작동 방식에서 직접 도출된다. 즉, 누군가를 팔로우하는 것(following)은 팔로우를 받는 것(being followed)과 명확히 구분된다. 따라서 $i$가 $j$를 팔로우한다는 유향 엣지 $(i, j)$는 $i$가 $j$에게 주의를 기울이고 있음을 나타낸다.",
    "60": "이론적 논의에서는 집합론적 공식화가 흔히 사용되지만, 계산 실무에서는 0과 1의 이진 원소를 갖는 인접 행렬(adjacency matrix) $Y$를 사용하는 것이 훨씬 더 보편적이다.",
    "61": "이를 구체화하기 위해, 1일차에 존재하다가 2일차에 해체된 두 조직 간의 관계를 생각해 보면, 이는 인접 행렬에서 $Y_{ij}^{t=1} = 1$에서 $Y_{ij}^{t=2} = 0$으로의 변화에 해당한다.",
    "62": "### DYNAMIC NETWORK REGRESSION",
    "63": "우리는 시계열 횡단면 네트워크의 연속 $(\dots, Y_{t-1}, Y_t, Y_{t+1}, \dots)$에서 출발한다. 여기서 $Y_t \in \{0, 1\}^{N_t \times N_t}$이며, $N_t$는 시점 $t$에서의 노드 수이다.",
    "64": "형식적으로 주어진 시점 슬라이스에 대한 DNR 우도 함수(likelihood)는 다음과 같이 정의된다:",
    "65": "![수식 7.1](image-19.png)",
    "66": "$$\\Pr\\left(Y^t \\mid Y_{t-k}^{t-1}, X^t\\right) = \\prod_{i \\neq j \\in V^t \\times V^t} \\mathcal{B}\\left(Y_{ij}^t; \\, \\operatorname{logit}^{-1}\\left(\\theta^T u(i, j, Y_{t-k}^{t-1}, X^t)\\right)\\right)$$",
    "67": "여기서 $\\mathcal{B}$는 베르누이 확률질량함수(Bernoulli pmf)이고, $X$는 공변량 집합이며, $u$는 엣지 집합에 대한 충분통계량(sufficient statistics) 벡터이고, $\\theta$는 추정 대상인 모수(parameter) 벡터이다.[^4]",
    "68": "[^4]: 본 연구에서 사용된 모든 통계 모형은 Almquist & Butts(2013, 2014b)의 원래 코드를 기반으로 R 통계 환경(R Core Team, 2015)에서 계산되었다.",
    "69": "### MECHANISMS OF ATTENTIONAL DYNAMICS",
    "70": "우리는 '재난 중 주의 집중 상호작용의 메커니즘' 절에서 제안된 각 메커니즘을 동적 네트워크 모델의 시차를 둔 그래프 통계량(lagged graph statistics)으로 변환하여 조작화한다."
}

with open('scratch/ch7_fixed_p2.json', 'w', encoding='utf-8') as f:
    json.dump(ch7_p2, f, ensure_ascii=False, indent=2)

print(f"Ch7 Part 2 saved: {len(ch7_p2)} blocks")
