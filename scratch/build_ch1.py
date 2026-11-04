import json

rows = [
    {
        "type": "title",
        "en": "# CHAPTER 1: AN INTRODUCTION TO SOCIAL NETWORK ANALYSIS IN DISASTER CONTEXTS",
        "ko": "# 제1장: 재난 맥락에서의 사회연결망 분석 서설"
    },
    {
        "type": "meta",
        "en": "**Authors:** Eric C. Jones¹, A.J. Faas²\n¹University of Texas Health Science Center at Houston, El Paso, TX, United States\n²San Jose State University, San Jose, CA, United States",
        "ko": "**저자:** Eric C. Jones¹, A.J. Faas²\n¹텍사스 대학교 휴스턴 보건과학센터, 엘패소, 텍사스, 미국\n²산호세 주립대학교, 산호세, 캘리포니아, 미국"
    },
    {
        "type": "meta",
        "en": "**Source:** *Social Network Analysis of Disaster Response, Recovery, and Adaptation*. http://dx.doi.org/10.1016/B978-0-12-805196-2.00001-7\nCopyright © 2017 Elsevier Inc. All rights reserved. (pp. 3–9)",
        "ko": "**출처:** *재난 대응, 복구 및 적응의 사회연결망 분석 (Social Network Analysis of Disaster Response, Recovery, and Adaptation)*. http://dx.doi.org/10.1016/B978-0-12-805196-2.00001-7\nCopyright © 2017 Elsevier Inc. All rights reserved. (pp. 3–9)"
    },
    {
        "type": "h2",
        "en": "## CHAPTER OUTLINE",
        "ko": "## 챕터 목차 개요"
    },
    {
        "type": "p",
        "en": "* **Introduction** (p. 3)\n* **The Content and Layout of the Book** (p. 4)\n* **Highlights and Things to Watch for** (p. 6)\n  * Roles (p. 6)\n  * Levels of Networks (p. 6)\n  * Interdisciplinarity (p. 6)\n  * Potential Versus Realized Ties (p. 7)\n  * The Ethics of Naming Vulnerable People (p. 7)\n  * Applications (p. 8)\n* **Disasters and the Question of Network Ontologies** (p. 8)\n* **Conclusions** (p. 8)",
        "ko": "* **서론 (Introduction)** (p. 3)\n* **본서의 내용 및 구성 체계 (The Content and Layout of the Book)** (p. 4)\n* **주요 핵심 및 주목할 사항 (Highlights and Things to Watch for)** (p. 6)\n  * 역할 (Roles) (p. 6)\n  * 네트워크의 수준 (Levels of Networks) (p. 6)\n  * 학제간 융합 연구 (Interdisciplinarity) (p. 6)\n  * 잠재적 관계 대 실현된 관계 (Potential Versus Realized Ties) (p. 7)\n  * 취약 계층 실명 표기의 윤리적 문제 (The Ethics of Naming Vulnerable People) (p. 7)\n  * 실무적 적용 (Applications) (p. 8)\n* **재난과 네트워크 존재론에 대한 질문 (Disasters and the Question of Network Ontologies)** (p. 8)\n* **결론 (Conclusions)** (p. 8)"
    },
    {
        "type": "h2",
        "en": "## INTRODUCTION",
        "ko": "## 서론"
    },
    {
        "type": "p",
        "en": "Hazards become disasters as the opportunities and constraints for maintaining a safe and secure life and livelihood become too strained for many people. Anecdotally and through many case studies, we know that social interactions exacerbate or mitigate those strains. However, we need a concerted intellectual effort to understand the variation in how ties within and between groups, communities, and organizations both respond to and are affected by hazards and disasters. Network research allows us to be incredibly creative in the ways that we capture the subtle, intricate, and dynamic power of relationships and interactions in the areas of disaster response, recovery, and adaptation.",
        "ko": "위험(Hazards)은 안전하고 안정된 삶과 생계를 유지하기 위한 기회와 제약이 수많은 사람들에게 감당하기 어려울 정도로 과중해질 때 재난(Disasters)으로 발전한다. 일화적 경험과 수많은 사례 연구들을 통해, 우리는 사회적 상호작용이 이러한 부담과 긴장을 악화시키거나 완화한다는 사실을 알고 있다. 그러나 집단, 지역사회, 조직 내부 및 이들 간의 관계적 연결망(ties)이 위험과 재난에 어떻게 대응하고 어떠한 영향을 받는지에 대한 차이와 다양성을 이해하기 위해서는 일치된 지적 노력이 필요하다. 네트워크 연구는 재난 대응, 복구, 적응 분야에서 관계와 상호작용이 지닌 미묘하고 복잡하며 동태적인 힘을 포착하는 데 있어 믿을 수 없을 만큼 창의적인 접근을 가능하게 해준다."
    },
    {
        "type": "p",
        "en": "Before, during, and after a disaster, people, agencies, and organizations help and hinder each other, alternatively opening up new possibilities and hamstringing others. To be sure, exposures to hazards become disasters in large part as a result of relational patterns in societies, and our responses to disasters—emergency deployment, mitigation, coping, and adaptation—are likewise facilitated and obstructed by variations in coordination and support between networks of actors. The social network is therefore a seductive concept in the social science of disasters—a potentially robust tool for investigating complex patterns of social relations and human-environment entanglements.",
        "ko": "재난의 이전, 도중, 이후에 걸쳐 사람, 기관 및 조직은 서로를 돕기도 하고 방해하기도 하며, 새로운 가능성을 열어주거나 반대로 다른 이들의 발목을 잡기도 한다. 분명히, 위험에 대한 노출이 재난으로 이어지는 것은 사회 내의 관계적 패턴에 기인하는 바가 크며, 비상 대응 전개, 피해 완화, 대처, 적응과 같은 재난에 대한 우리의 대응 역시 행위자 네트워크 간의 조정과 지원의 차이에 의해 촉진되거나 방해받는다. 따라서 사회연결망(Social Network)은 재난 사회과학 분야에서 대단히 매력적인 개념이며, 사회적 관계의 복잡한 양상과 인간-환경 간의 얽힘을 탐구할 수 있는 강력한 잠재력을 지닌 도구이다."
    },
    {
        "type": "p",
        "en": "Social networks are typically invoked in one of two general ways in social science research: (1) metaphorically or heuristically, as descriptive or analytical concepts that summarize researchers’ perceived patterns of relationships or interactions in particular contexts, or else as guides for systematic observations of relationships and interactions; and (2) as a formal system of measurement of either personal or whole (i.e., community or institutional) patterns of relationships or interaction employing one or more measures derived from graph theory (e.g., density, centralization, bridging, etc.) and, more recently, examining complexity and network change. This book is principally focused on the second broad approach to network analysis, though contributors draw heavily on concepts and empirical trends identified in studies that engage networks more metaphorically.",
        "ko": "사회연결망은 사회과학 연구에서 일반적으로 다음 두 가지 방식 중 하나로 다루어진다: (1) 특정 맥락에서 연구자가 인식한 관계나 상호작용의 패턴을 요약하는 서술적·분석적 개념으로서, 혹은 관계와 상호작용에 대한 체계적 관찰의 지침으로서 은유적(metaphorically) 또는 발견적(heuristically)으로 사용되는 방식; (2) 그래프 이론에서 파생된 하나 이상의 측정치(예: 밀도, 중심화, 교량 등)를 활용하여 개인적 또는 전체적(즉, 지역사회나 제도적) 관계·상호작용 패턴을 측정하는 공식적인 측정 시스템으로서, 최근에는 복잡성과 네트워크 변화를 규명하는 데까지 확장된 방식이다. 본서는 주로 네트워크 분석에 대한 두 번째 포괄적 접근법에 초점을 맞추고 있으나, 기고진들은 네트워크를 보다 은유적으로 다룬 연구들에서 규명된 개념과 실증적 경향성 역시 적극적으로 차용하고 있다."
    },
    {
        "type": "p",
        "en": "This book is the first of its kind; it presents a great deal of the diversity in network approaches to better understanding how people and groups experience extreme events. Since both network analysis and disaster studies are often separated out into the publishing confines of multiple disciplines—and we do not always read outside of these disciplines—this cutting-edge scholarly work would otherwise be scattered in disparate journals and books. Not only does this book bring this work from different disciplines together but it brings together the relatively minimally interacting fields of interpersonal disaster networks and interorganizational disaster networks. By doing so, we can start to explore the theoretical disconnects between the ways networks are deployed by scholars. For example, we note that the study of bridging—or being a relatively unique connection between at least a couple of parts of a network—in the field of interpersonal networks usually means we are examining power, vulnerability, or assets/liabilities, while in the field of interorganizational networks we are typically examining the effectiveness of communication and, to a lesser extent, goal alignment.",
        "ko": "본서는 해당 분야 최초의 저작으로서, 개인과 집단이 극단적 사건(extreme events)을 어떻게 경험하는지 더 깊이 이해하기 위한 네트워크 접근법의 다채로운 다양성을 제시한다. 네트워크 분석과 재난 연구는 흔히 여러 학문 분야의 출판 영역으로 파편화되어 있고 연구자들 또한 자신의 학문 분야 밖의 문헌을 항상 찾아 읽지는 못하기 때문에, 이러한 최첨단 학술 연구들은 본서가 아니었다면 각기 다른 저널과 서적에 흩어져 있었을 것이다. 본서는 이처럼 상이한 학문 분야의 성과들을 한곳에 모았을 뿐만 아니라, 그동안 상호교류가 상대적으로 미미했던 개인 간 재난 네트워크(interpersonal disaster networks) 분야와 조직 간 재난 네트워크(interorganizational disaster networks) 분야를 하나로 융합하였다. 이를 통해 우리는 학자들이 네트워크를 활용하는 방식 사이에 존재하는 이론적 단절을 규명하기 시작할 수 있다. 예를 들어, 네트워크의 최소 둘 이상의 영역을 비교적 독특하게 이어주는 연결을 의미하는 '교량(bridging)' 연구의 경우, 개인 간 네트워크 분야에서는 대체로 권력, 취약성, 또는 자산/부채를 탐색하는 반면, 조직 간 네트워크 분야에서는 전형적으로 의사소통의 효과성과 (다소 낮은 비중으로) 목표 일치도를 탐색한다는 점에 주목할 수 있다."
    },
    {
        "type": "p",
        "en": "We have tried to keep the studies in this book to those that revolve around identifiable disasters and that use systematic qualitative or quantitative analysis of dyadic data—the specific kinds of relationships between specific individuals, roles, or institutions. This said, we would like even more studies to go beyond dyadic analyses and to engage the entire web of relationships involved in disasters. In other words, exchange and dyadic interaction is a minimum in our mind for the study of relationships and disasters, but it does not fully leverage the possibilities of social network analysis because the dependence of a dyad on other individuals and dyads and cliques (and the rest of the network) is left unexamined when only paying attention to dyads. While we have chosen studies for this book that we consider to use the methodologies of social network analysis, our interest is less on the importance of conducting social network analysis and more on the kinds of things it can tell us about human behavior in extreme settings.",
        "ko": "우리는 본서에 수록된 연구들이 구체적으로 식별 가능한 재난을 중심으로 하며, 특정 개인, 역할, 또는 기관 간의 구체적인 관계 유형을 다루는 이원적 데이터(dyadic data)에 대한 체계적인 질적 또는 양적 분석을 사용하는 연구들로 국한되도록 노력하였다. 그렇기는 하나, 우리는 더 많은 후속 연구들이 이원적(dyadic) 분석의 수준을 넘어 재난에 얽혀 있는 전체 관계망(entire web of relationships)을 다루기를 희망한다. 다시 말해, 교환과 이원적 상호작용은 관계와 재난을 연구하는 데 있어서 최소한의 기준선에 불과하며, 오직 이원적 관계에만 주목할 경우 특정 관계 쌍(dyad)이 다른 개인, 다른 관계 쌍, 소집단(파벌, cliques), 그리고 네트워크의 나머지 부분에 의존하는 양상을 규명하지 못하기 때문에 사회연결망 분석이 지닌 잠재력을 온전히 활용하지 못하게 된다. 본서에서는 사회연결망 분석의 방법론을 엄밀하게 적용한 연구들을 엄선하였으나, 우리의 궁극적 관심은 사회연결망 분석 수행 자체의 중요성에 있기보다는 그것이 극한 상황에서의 인간 행동에 관해 무엇을 규명해 줄 수 있는가에 있다."
    },
    {
        "type": "h2",
        "en": "## THE CONTENT AND LAYOUT OF THE BOOK",
        "ko": "## 본서의 내용 및 구성 체계"
    },
    {
        "type": "p",
        "en": "This first section provides orientations to theory on individual and organizational networks in disaster settings plus a methodological overview of the loosely organized field. Then empirical work comprises the sections on response, recovery, and adaptation/mitigation. Each empirical chapter also addresses methodological and theoretical concerns. Since we are addressing a fairly new and somewhat specialized field, we end the book with a chapter that provides insight into how this new and specialized knowledge can be applied to improve response, recovery, and adaptation.",
        "ko": "본서의 제1부(first section)는 재난 상황에서의 개인 및 조직 네트워크 이론에 대한 오리엔테이션과 함께, 아직은 느슨하게 조직화된 이 분야의 방법론적 개요를 제공한다. 이어지는 실증 연구들은 대응(response), 복구(recovery), 적응 및 피해완화(adaptation/mitigation) 부문으로 구성된다. 각각의 실증 챕터들 또한 방법론적·이론적 쟁점들을 깊이 있게 다룬다. 우리는 매우 새롭고 다소 전문화된 학문 영역을 다루고 있으므로, 책의 마지막 장에서는 이러한 새롭고 전문화된 지식이 어떻게 재난 대응, 복구 및 적응을 실질적으로 개선하는 데 적용될 수 있는지에 대한 통찰을 제공하며 책을 마무리한다."
    },
    {
        "type": "p",
        "en": "The authors in this book cover some major events of our times like Hurricanes Katrina, Sandy, and Ike in the United States, the Wenchuan earthquake in China, the Kobe earthquake in Japan, and the Canterbury earthquakes in New Zealand, plus some lesser known events, like volcanic eruptions in Ecuador and Mexico, landslides in Mexico, a day care fire in Mexico, a typhoon in Fiji, wildfires in the United States, and drought in East Africa. These studies include those in contexts of geophysical and hydrometeorological hazards (volcanoes and mudslides—Tobin and colleagues; earthquakes—Stevenson, Lee and Sugiura, Lu; hurricanes—Marcum and colleagues, Harris and Doerfel, Meyer; typhoons—Takasaki; droughts—Moritz; wildfires—Nowell and colleagues, Almquist and colleagues), and those caused by human carelessness or recklessness (a building fire—Rangel and colleagues). We purposefully avoided including events of conflict or mass terror since—although we see them theoretically as extreme events, too—intentionality in such events often involves some very different responses and adaptations.",
        "ko": "본서의 저자들은 미국의 허리케인 카트리나, 샌디, 아이크, 중국의 원촨 대지진, 일본의 고베 대지진, 뉴질랜드의 캔터베리 지진과 같은 우리 시대의 주요 대형 사건들뿐만 아니라, 에콰도르와 멕시코의 화산 폭발, 멕시코의 산사태와 어린이집 화재, 피지의 태풍, 미국의 산불, 동아프리카의 가뭄 등 상대적으로 덜 알려진 사건들까지 폭넓게 다루고 있다. 이러한 연구들에는 지구물리학적 및 수문기상학적 위험 맥락(화산 및 이류—Tobin 연구진; 지진—Stevenson, Lee and Sugiura, Lu; 허리케인—Marcum 연구진, Harris and Doerfel, Meyer; 태풍—Takasaki; 가뭄—Moritz; 산불—Nowell 연구진, Almquist 연구진)뿐만 아니라, 인간의 부주의나 태만으로 초래된 사건(건물 화재—Rangel 연구진)에 관한 연구들이 망라되어 있다. 우리는 분쟁(conflict)이나 대규모 테러 사건은 의도적으로 제외하였는데, 이는 이론적으로는 이 역시 극단적 사건에 속하지만, 그러한 사건들에 내재된 '고의성/의도성(intentionality)'은 종종 전혀 다른 차원의 대응과 적응 양상을 수반하기 때문이다."
    },
    {
        "type": "p",
        "en": "Table 1.1 presents the general focus and methodological approach of each empirical chapter. These chapters cover considerable variation in the kinds of networks that are studied. There is not always a clear division between egocentric networks that focus on the ties in each individual’s or organization’s own network versus sociocentric networks that focus on an identifiable group or interaction sphere. However, it is worth noting the degree to which this book’s chapters cover networks that are more methodologically relying on ties focused on a given individual/organization versus ties that exist within a group of people/institutions that are likely to interact. Among the book’s 12 case study chapters, only two chapters break the pattern of egocentric networks being about individuals and sociocentric networks being about organizations. Similarly, few chapters cover network structure (e.g., density, cohesion, bridging, path distance) or employ longitudinal design. It was not our goal to have all chapters cover structure or network dynamics/change, but it is clear that these approaches are not in the majority for disaster network research.",
        "ko": "표 1.1은 각 실증 챕터의 전반적인 초점과 방법론적 접근 방식을 제시한다. 이 챕터들은 연구 대상이 된 네트워크의 유형 면에서 상당한 다양성을 포괄하고 있다. 각 개인이나 조직 자체의 연결망에 존재하는 관계에 초점을 맞추는 '자아중심 네트워크(egocentric networks)'와, 식별 가능한 집단이나 상호작용 영역에 초점을 맞추는 '전체 네트워크(sociocentric networks)' 사이에 언제나 명확한 구분이 존재하는 것은 아니다. 그러나 본서의 챕터들이 특정 개인/조직 중심의 관계에 방법론적으로 의존하는 네트워크와 상호작용할 가능성이 있는 사람/기관 집단 내에 존재하는 관계에 의존하는 네트워크를 어느 정도로 다루고 있는지는 주목할 가치가 있다. 본서에 수록된 12편의 사례 연구 챕터 중, 자아중심 네트워크는 개인을 다루고 전체 네트워크는 조직을 다룬다는 기존의 전형적 패턴을 벗어난 연구는 단 두 편에 불과하다. 마찬가지로, 네트워크 구조(예: 밀도, 응집도, 교량, 경로 거리)를 다루거나 종단적 설계(longitudinal design)를 채택한 챕터는 소수에 불과하다. 모든 챕터가 구조나 네트워크의 동태성/변화를 다루도록 하는 것이 우리의 목표는 아니었으나, 이러한 접근법들이 현재 재난 네트워크 연구에서 다수를 차지하지 못하고 있다는 점만은 분명하다."
    },
    {
        "type": "p",
        "en": "To the extent the data allowed, the authors have tried to address temporal aspects of networks, although we only marked them as longitudinal when comparable data was collected at two or more points in time. Since people may rely on different kinds of people for different things at different points as hazards, the contributors have attempted to account for dynamic shifts in needs, constraints, and help seeking.",
        "ko": "데이터가 허용하는 한, 저자들은 네트워크의 시간적 측면을 다루고자 노력하였으나, 우리는 비교 가능한 데이터가 두 시점 이상에서 수집된 경우에만 '종단적 연구'로 엄격히 표시하였다. 위험이 전개됨에 따라 사람들은 서로 다른 시점에 서로 다른 일들을 위해 서로 다른 유형의 사람들에게 의존할 수 있으므로, 기고진들은 필요, 제약, 도움 요청 행동에서 발생하는 동태적 변화(dynamic shifts)를 규명하고자 시도하였다."
    },
    {
        "type": "h3",
        "en": "### Table 1.1: Approaches and Foci of the Empirical Chapters",
        "ko": "### 표 1.1: 실증 챕터들의 접근 방식 및 연구 초점"
    },
    {
        "type": "table",
        "en": "| Chapters | Egocentric / Sociocentric, and Individuals / Organizations | Social Support | Coordination | Structure | Longitudinal |\n| :---: | :--- | :---: | :---: | :---: | :---: |\n| **5** | Sociocentric—organizations | | X | X | |\n| **6** | Sociocentric—organizations | | X | X | X |\n| **7** | Sociocentric—organizations | | X | X | |\n| **8** | Egocentric—individuals | X | | | |\n| **9** | Egocentric—individuals | X | | | |\n| **10** | Sociocentric—organizations | | X | X | |\n| **11** | Egocentric—organizations | | X | | |\n| **12** | Sociocentric—individuals | X | | X | |\n| **13** | Egocentric—individuals | X | | | |\n| **14** | Egocentric—individuals (households) | X | | | |\n| **15** | Egocentric—individuals | X | | | |\n| **16** | Egocentric—individuals | X | | X | X |",
        "ko": "| 챕터 | 자아중심/전체 네트워크, 및 개인/조직 구분 | 사회적 지원 | 조정 및 협력 | 구조적 분석 | 종단적 설계 |\n| :---: | :--- | :---: | :---: | :---: | :---: |\n| **5** | 전체 네트워크(Sociocentric)—조직 | | X | X | |\n| **6** | 전체 네트워크(Sociocentric)—조직 | | X | X | X |\n| **7** | 전체 네트워크(Sociocentric)—조직 | | X | X | |\n| **8** | 자아중심 네트워크(Egocentric)—개인 | X | | | |\n| **9** | 자아중심 네트워크(Egocentric)—개인 | X | | | |\n| **10** | 전체 네트워크(Sociocentric)—조직 | | X | X | |\n| **11** | 자아중심 네트워크(Egocentric)—조직 | | X | | |\n| **12** | 전체 네트워크(Sociocentric)—개인 | X | | X | |\n| **13** | 자아중심 네트워크(Egocentric)—개인 | X | | | |\n| **14** | 자아중심 네트워크(Egocentric)—개인(가구) | X | | | |\n| **15** | 자아중심 네트워크(Egocentric)—개인 | X | | | |\n| **16** | 자아중심 네트워크(Egocentric)—개인 | X | | X | X |"
    },
    {
        "type": "h2",
        "en": "## HIGHLIGHTS AND THINGS TO WATCH FOR",
        "ko": "## 주요 핵심 및 주목할 사항"
    },
    {
        "type": "p",
        "en": "We want to highlight a few things that we generally think are missing in disaster network research. This observation is less of a criticism than it is an encouragement to those of us in this field to undertake an exercise in systematically thinking beyond a study to hopefully imagine what might provide the next contribution or breakthrough in the field.",
        "ko": "우리는 재난 네트워크 연구에서 전반적으로 결여되어 있다고 생각되는 몇 가지 사항을 강조하고자 한다. 이러한 지적은 비판이라기보다는, 우리 분야의 연구자들이 개별 연구를 넘어 체계적으로 사유함으로써 향후 이 학문 분야에 어떤 기여나 돌파구(breakthrough)를 마련할 수 있을지 상상해 보도록 독려하기 위함이다."
    },
    {
        "type": "h3",
        "en": "### Roles",
        "ko": "### 역할 (Roles)"
    },
    {
        "type": "p",
        "en": "When we’re studying organizational networks, we should remember that many of those network ties or relationships are actually interpersonal relationships. Some of those relationships are more like friendships or relationships based on personality and common history, while other interpersonal relationships between organizations really are between roles—the relationship can continue if one or more people leave their role and are replaced by someone else. Yet other relationships between institutions are very far removed from individuals and roles. Financial institutions that transfer money have individuals in roles transferring the money, or even deciding to transfer the money, but these interactions have no interpersonal and no interrole qualities.",
        "ko": "우리가 조직 네트워크를 연구할 때, 그러한 네트워크 관계나 연결 중 상당수가 실제로는 개인 간의 관계(interpersonal relationships)라는 점을 기억해야 한다. 이러한 관계 중 일부는 성격이나 공유된 과거 경험에 기반한 우정이나 사적 관계에 가까운 반면, 조직 간의 다른 대인 관계는 진정한 의미에서 '역할(roles)' 간의 관계이다—즉, 특정 역할을 맡은 한 명 이상의 인물이 직책을 떠나 다른 사람으로 교체되더라도 그 관계는 지속될 수 있다. 그러나 기관 간의 또 다른 관계들은 개인이나 역할로부터 매우 멀리 떨어져 있다. 자금을 이체하는 금융 기관의 경우 자금을 이체하거나 이체를 결정하는 역할을 맡은 개인이 존재하지만, 이러한 상호작용은 개인적 특성도, 역할 간의 특성도 전혀 띠지 않는다."
    },
    {
        "type": "h3",
        "en": "### Levels of Networks",
        "ko": "### 네트워크의 수준 (Levels of Networks)"
    },
    {
        "type": "p",
        "en": "Levels of analysis are construed various ways, sometimes depending on the discipline or the objective of a project. Rather than propose a concrete list of levels of networks, we want to point out that levels of networks can be joined to arrive at new insights in disaster response, recovery, and adaptation. For example, personal networks that influence individual behavior can be joined together into a representative community network that provides greater context for the distribution of the various kinds of personal networks. Nowell and colleagues in Chapter 5 use their case study to tackle head on this issue of intersecting levels of analysis.",
        "ko": "분석 수준(Levels of analysis)은 학문 분야나 프로젝트의 목표에 따라 다양하게 해석된다. 우리는 네트워크 수준에 대한 구체적인 목록을 규정하기보다는, 네트워크의 여러 수준이 서로 결합됨으로써 재난 대응, 복구 및 적응 분야에서 새로운 통찰에 도달할 수 있다는 점을 지적하고자 한다. 예를 들어, 개인의 행동에 영향을 미치는 사적 네트워크들은 다양한 유형의 개인 네트워크 분포에 대한 거시적 맥락을 제공하는 대표적인 지역사회 네트워크로 통합·연계될 수 있다. 본서 제5장에서 Nowell 연구진은 자신들의 사례 연구를 활용하여 이러한 '분석 수준의 교차' 문제를 정면으로 다루고 있다."
    },
    {
        "type": "p",
        "en": "Importantly, several authors have lamented the low level of integration between research in the area of social network analysis with research on interorganizational networks (Bergenholtz & Waldstrøøm, 2011; Knobben & Oerlemans, 2006; Roijakkers & Hagedoorn, 2006). Some of this is due to real distinctions between the organizational and individual levels of analysis, but, while interorganizational networks can be conceived of as metaphors for multiagency interdependencies, it is feasible to analyze the social structure between organizations. This book therefore includes studies both of social networks and of interorganizational networks to attempt to synthesize some of the cutting-edge developments in both hitherto disparate bodies of research.",
        "ko": "중요한 점은, 여러 학자들이 사회연결망 분석 분야의 연구와 조직 간 네트워크 연구 사이의 낮은 통합 수준에 대해 아쉬움을 표명해 왔다는 사실이다(Bergenholtz & Waldstrøøm, 2011; Knobben & Oerlemans, 2006; Roijakkers & Hagedoorn, 2006). 이러한 현상의 일부는 조직 수준과 개인 수준의 분석 사이에 실재하는 본질적 차이에 기인하지만, 조직 간 네트워크를 다기관 상호의존성에 대한 은유로 파악할 수 있는 동시에 조직들 간의 사회적 구조(social structure)를 실증적으로 분석하는 것 역시 충분히 가능하다. 따라서 본서는 지금까지 파편화되어 있던 두 연구 영역의 최첨단 학술적 발전을 종합적으로 융합하고자 사회연결망 연구와 조직 간 네트워크 연구를 모두 포괄하고 있다."
    },
    {
        "type": "h3",
        "en": "### Interdisciplinarity",
        "ko": "### 학제간 융합 연구 (Interdisciplinarity)"
    },
    {
        "type": "p",
        "en": "The theoretical approaches used by the authors in this book are sometimes constrained by them being single-authored studies, and because most of the coauthored papers come from a single discipline. That said, the following disciplines are represented in this book: public administration (Chapters 3–5 and 10), sociology (Chapters 7–9), communication (Chapter 6), anthropology (Chapters 2, 12, 13, 16, and 17), geography (Chapter 11), and economics (Chapters 14 and 17). A few of these chapters are somewhat interdisciplinary, but that is not the norm. As you read the book, imagine how the authors, other scholars, or you yourself might arrive at more complete understandings in any of these studies by increasing the input from some other disciplines.",
        "ko": "본서의 저자들이 사용한 이론적 접근법은 단독 저자 연구라는 한계나, 공동 저술된 논문들의 대다수가 단일 학문 분과 출신이라는 점으로 인해 제약을 받는 경우가 있다. 그럼에도 불구하고, 본서에는 다음과 같은 다양한 학문 분야가 망라되어 있다: 행정학(제3~5장 및 제10장), 사회학(제7~9장), 커뮤니케이션학(제6장), 인류학(제2장, 제12장, 제13장, 제16장, 제17장), 지리학(제11장), 경제학(제14장 및 제17장). 이들 중 몇몇 챕터는 다소 학제간적 성격을 띠고 있으나 그것이 일반적인 표준은 아니다. 독자 여러분은 책을 읽으면서 저자들이나 다른 학자들, 혹은 연구자 본인이 다른 학문 분야의 관점을 접목함으로써 이 연구들 중 어느 하나에서라도 어떻게 더 완전한 이해에 도달할 수 있을지 상상해 보기 바란다."
    },
    {
        "type": "h3",
        "en": "### Potential Versus Realized Ties",
        "ko": "### 잠재적 관계 대 실현된 관계 (Potential Versus Realized Ties)"
    },
    {
        "type": "p",
        "en": "In Chapter 2, we provide a very brief discussion of how the measurement of network potential (i.e., existing ties concerning affect or orientation) produces somewhat unclear sets of predictions for a variety of postdisaster outcomes, while the measurement of network activation (i.e., instrumental ties) indicates more clear relationships and mechanisms between network behavior and the postdisaster outcomes of interest. Additionally, the relationship between network potential and network activation is often not clear. As you read through the various chapters, imagine what the network potential is or might be, how it compares to network activation, and what might be some useful ways to bridge the gap between the two. Additionally, when trying to make these observations, thinking in terms of a full network instead of just sets of dyadic ties makes the puzzle harder but probably more interesting.",
        "ko": "제2장에서 우리는 네트워크 잠재성(network potential, 즉 정서나 지향성과 관련된 기존의 관계)의 측정이 다양한 재난 이후 결과에 대해 다소 불명확한 예측만을 낳는 반면, 네트워크 활성화(network activation, 즉 도구적 관계)의 측정은 네트워크 행위와 주요 관심사인 재난 이후 결과 간의 보다 명확한 관계와 메커니즘을 보여준다는 점에 대해 짤막하게 논의한다. 나아가 네트워크 잠재성과 네트워크 활성화 간의 관계 또한 명확하지 않은 경우가 많다. 다양한 챕터를 읽어가면서, 독자들은 네트워크 잠재성이 무엇이고 무엇이 될 수 있는지, 그것이 네트워크 활성화와 어떻게 비교되는지, 그리고 그 둘 사이의 격차를 좁힐 수 있는 유용한 방법은 무엇인지 상상해 보기 바란다. 아울러 이러한 관찰을 시도할 때, 단순한 이원적 관계 쌍의 집합이 아니라 '전체 네트워크(full network)' 관점에서 사고하는 것은 문제를 더 어렵게 만들지만 틀림없이 훨씬 더 흥미롭게 만들어 줄 것이다."
    },
    {
        "type": "h3",
        "en": "### The Ethics of Naming Vulnerable People",
        "ko": "### 취약 계층 실명 표기의 윤리적 문제 (The Ethics of Naming Vulnerable People)"
    },
    {
        "type": "p",
        "en": "Concerns of confidentiality are not unique to studies of disasters nor to studies of social networks. However, both kinds of studies present added issues to consider above those that many other social science studies may not encounter.",
        "ko": "비밀 보장(confidentiality)에 대한 우려는 재난 연구나 사회연결망 연구만의 고유한 문제는 아니다. 그러나 이 두 가지 유형의 연구는 다른 많은 사회과학 연구들이 겪지 않을 수 있는 추가적인 고려 사항들을 제기한다."
    },
    {
        "type": "p",
        "en": "First, people in disaster settings are typically more vulnerable than in other settings. This means that people might be more suggestible when consenting to and answering interviews, and it means that the information they share might be more sensitive than it would be in another setting since the information highlights their level of vulnerability.",
        "ko": "첫째, 재난 상황에 처한 사람들은 일반적으로 다른 일상적 환경의 사람들보다 훨씬 더 취약하다. 이는 연구 참여에 동의하고 면담에 응할 때 피조사자가 다른 사람의 제안에 더 취약하게 영향을 받을(suggestible) 수 있음을 의미하며, 그들이 공유하는 정보가 그들의 취약성 수준을 직접적으로 드러내기 때문에 다른 환경에서보다 훨씬 더 민감할 수 있음을 뜻한다."
    },
    {
        "type": "p",
        "en": "Second, social network research usually involves the naming of people who have not consented to being named or who have not been approached to participate in the study. A respondent might be asked to give information on faith, wealth, attitude, health issues, politics, and other characteristics of each person that they name in a network study. They also often report on the types of interactions and exchanges they have had with these other people. This means that researchers often possess information (whether accurate or not) about various people that don’t know they are now in your study. One protection on this data is the de-identification of people in the networks by giving them unique identifiers. This is not always a quick or easy process, since the same person might be named by several people and, thus, spelling issues, nicknames, variation in reported characteristics, and lack of information may make it hard to determine if they are the same person.",
        "ko": "둘째, 사회연결망 연구는 일반적으로 자신의 이름이 거론되는 것에 동의하지 않았거나 연구 참여를 위해 사전에 접촉되지 않은 사람들의 실명을 지목(naming)하는 과정을 수반한다. 응답자는 네트워크 연구에서 자신이 지목한 개별 인물들의 종교, 재산, 태도, 건강 문제, 정치적 성향 및 기타 특성에 관한 정보를 제공하도록 요청받을 수 있다. 또한 응답자들은 종종 이러한 타인들과 가졌던 상호작용 및 자원 교환의 유형에 대해 보고한다. 이는 연구자가 자신이 연구 대상이 되었다는 사실조차 알지 못하는 수많은 사람들에 관한 정보(그것이 정확하든 그렇지 않든)를 보유하게 됨을 의미한다. 이러한 데이터를 보호하기 위한 한 가지 조치는 네트워크 내 인물들에게 고유 식별자(unique identifiers)를 부여하여 '비식별화(de-identification)'하는 것이다. 그러나 동일한 인물이 여러 응답자에 의해 동시에 지목될 수 있고 철자 문제, 별명, 보고된 특성의 불일치, 정보 부족 등으로 인해 그들이 동일 인물인지 판별하기 어렵기 때문에 이것이 언제나 빠르고 쉬운 과정인 것은 아니다."
    },
    {
        "type": "p",
        "en": "As with all social science research, the process of protecting research subjects from adverse consequences of participating in a study can present some procedural challenges. We feel strongly that every effort should be made to maintain a primary ethical obligation to research subjects and prevent and minimize any potential harm that may result from participation. Beyond minimizing harm, the best research endeavors—especially in disaster contexts—should attempt to apply study findings to maximize the benefits to our subjects and to others who endure the vulnerabilities of disaster and environmental crisis. In the case that network findings are used to directly engage respondents to improve agency or belonging, there is an incredible opportunity for self-evaluation—like looking in a mirror—by the respondent or group of respondents. However, whether the goal is social justice, process improvement, or some other outcome, such an application requires careful management of the interaction with respondents over the results so that people have buy in but also are guided toward solutions that avoid competitive comparisons or jockeying to improve one’s situation at the expense of others.",
        "ko": "모든 사회과학 연구가 그러하듯, 연구 참여로 인한 부정적 결과로부터 연구 대상을 보호하는 과정은 절차상 여러 가지 난관을 수반할 수 있다. 우리는 연구 대상에 대한 일차적 윤리적 책무를 다하고 참여로 인해 발생할 수 있는 잠재적 위해를 예방하고 최소화하기 위해 모든 노력을 기울여야 한다고 굳게 확신한다. 위해를 최소화하는 것을 넘어, 최상의 연구 노력은—특히 재난 맥락에서—연구 대상자와 재난 및 환경 위기의 취약성을 견뎌내고 있는 다른 사람들에게 돌아가는 혜택을 극대화할 수 있도록 연구 결과를 적극 적용해야 한다. 네트워크 분석 결과가 응답자들의 행위주체성(agency)이나 소속감을 향상시키기 위해 응답자들을 직접 참여시키는 데 사용되는 경우, 응답자 개인이나 집단에게는 거울을 들여다보는 것과 같은 놀라운 자기 평가(self-evaluation)의 기회가 주어진다. 그러나 연구의 목표가 사회 정의이든, 절차 개선이든, 아니면 다른 어떤 결과물이든 간에, 이러한 실무적 적용은 사람들이 결과에 공감(buy-in)하면서도 경쟁적 비교나 타인의 희생을 발판 삼아 자신의 처지만을 개선하려는 과열 경쟁을 지양하는 해결책으로 유도될 수 있도록, 결과물을 둘러싼 응답자들과의 상호작용을 세심하게 관리할 것을 요구한다."
    },
    {
        "type": "h3",
        "en": "### Applications",
        "ko": "### 실무적 적용 (Applications)"
    },
    {
        "type": "p",
        "en": "The International Federation of Red Cross and Red Crescent Societies’ (2014) *World Disasters Report 2014* pays extensive attention to the roles of community networks in disaster contexts around the world. Such large and important humanitarian organizations are looking to shape policy and practice that is sensitive to and supportive of informal community networks. A 2011 United Nations International Strategy for Disaster Reduction report refers to social networks as a type of “community competence” that is a driver of effective response, recovery, and adaptation (UNISDR, 2011). One hope is that disaster risk reduction policy and practice will help build and support such competencies—not simply conclude that community problem-solving capacity is hindered by poor networks or social capital. The care to such detail of support, exchange, coordination, and emergent network dynamics provides one avenue to find a better fit between local cultural dynamics, relational patterns, and broader efforts of disaster risk reduction, prevention, mitigation, response, and recovery. Network heuristics and metaphors may be “good to think” (Descola, 1994), but if we want to see networks effectively engaged in policy and practice, we have to be sure that we do better than “satisficing” (Simon, 1957).",
        "ko": "국제적십자사·적신월사연맹(IFRC)의 2014년 보고서 *World Disasters Report 2014*는 전 세계 재난 상황에서 지역사회 네트워크가 수행하는 역할에 지대한 관심을 기울이고 있다. 이처럼 거대하고 중대한 인도주의 기구들은 비공식 지역사회 네트워크에 민감하게 반응하고 이를 지원하는 정책과 실무를 수립하고자 모색하고 있다. 2011년 유엔 국제재난경감전략(UNISDR) 보고서는 사회연결망을 효과적인 대응, 복구 및 적응의 원동력이 되는 일종의 '지역사회 역량(community competence)'으로 규정하였다(UNISDR, 2011). 한 가지 바람은 재난 위험 경감 정책과 실무가 단순히 빈약한 네트워크나 사회적 자본 때문에 지역사회의 문제 해결 역량이 저해된다고 단정해 버리는 것에 그치지 않고, 이러한 역량을 실제로 구축하고 지원하도록 돕는 것이다. 지원, 자원 교환, 조정 및 창발적 네트워크 동태성의 세부 사항에 대한 이러한 세심한 배려는 지역의 문화적 역학, 관계적 패턴, 그리고 보다 광범위한 재난 위험 경감·예방·완화·대응·복구 노력 사이의 더 나은 적합성(fit)을 찾아내는 하나의 경로를 제공한다. 네트워크에 대한 발견적 기법과 은유는 '사유하기에 유용(good to think)'할 수 있지만(Descola, 1994), 네트워크가 정책과 실무에 실질적으로 기여하는 것을 보고자 한다면 우리는 단순한 '만족화(satisficing)' 수준(Simon, 1957)을 넘어서야만 한다."
    },
    {
        "type": "h2",
        "en": "## DISASTERS AND THE QUESTION OF NETWORK ONTOLOGIES",
        "ko": "## 재난과 네트워크 존재론에 대한 질문"
    },
    {
        "type": "p",
        "en": "We feel compelled to state at the outset that networks, strictly speaking, cannot properly be said to exist outside of formal organizations. They are, instead, analytical abstractions—sets of researcher-specified relationships around which analysts impose theoretically derived boundaries. Social networks, as objective things, do not exist except as formal organizational structures (in contrast to informal organizational structures), plans for action, cognitive models, or forensic traces of patterns of interaction. Networks themselves have no agency, except perhaps in terms of Andrew Pickering’s (1995) loose definition of material (i.e., nonhuman) agency as things “doing things in the world.” But networks are scarcely even “things” or any category of objective being at all. Networks, rather, are cumulative—often emergent—patterns of dyadic and triadic relationships that are specified by the researcher.",
        "ko": "우리는 엄밀히 말해 네트워크가 공식 조직의 외부에서 독립적으로 존재한다고 말할 수 없다는 점을 서두에서 분명히 밝힐 필요성을 느낀다. 네트워크는 그 대신 분석적 추상물(analytical abstractions)—즉, 분석가가 이론적으로 도출된 경계를 부여한 연구자 지정 관계들의 집합—이다. 객관적인 실체로서의 사회연결망은 공식적인 조직 구조(비공식적 조직 구조와 대비되는), 행동 계획, 인지 모델, 또는 상호작용 패턴의 법의학적 흔적(forensic traces)으로서 존재하는 경우를 제외하고는 실재하지 않는다. 네트워크 그 자체는 사물이 '세상에서 무언가를 행하는 것'이라는 앤드루 피커링(Pickering, 1995)의 물질적(즉, 비인간적) 행위주체성에 관한 느슨한 정의를 따르는 경우를 제외하면 어떠한 행위주체성(agency)도 지니지 않는다. 사실 네트워크는 '사물'이나 객관적 실재의 어떠한 범주에도 거의 속하지 않는다. 오히려 네트워크는 연구자에 의해 규정되는, 이원적(dyadic) 및 삼원적(triadic) 관계들이 누적되어 나타나는—종종 창발적인(emergent)—패턴인 것이다."
    },
    {
        "type": "p",
        "en": "To the extent that there is any agency to networks—again, according to Pickering’s relaxed criterion for material agency—there can be no telos, no intentionality to social networks. Instead, we examine patterns of connection and interaction between actors—either individuals or organizations—whose actions and intentions are facilitated or constrained by emergent patterns of connectivity. Even with these connections, it is tricky to speak of the kinds of flows that occur across the connections. For example, does information really flow? Or does it get upgraded, downgraded, revised, and obfuscated as much (or more so) than it gets passed on as some bit of information? Actors in networks broker and constrain the transmission of information and materials. How do the authors in this book translate these phenomena into and out of social network analysis in disaster response, recovery, and adaptation?",
        "ko": "네트워크에 어떠한 행위주체성이 존재한다고 하더라도—다시 말해 물질적 행위주체성에 대한 피커링의 완화된 기준에 따르더라도—사회연결망에는 궁극적 목적(telos)이나 지향성(intentionality)이 존재할 수 없다. 대신 우리는 행위자(개인이든 조직이든) 간의 연결 및 상호작용 패턴을 연구하며, 이들의 행동과 의도는 창발적인 연결 패턴에 의해 촉진되거나 제약받는다. 이러한 연결이 존재한다 하더라도, 그 연결망을 통해 어떠한 종류의 흐름(flows)이 일어나는가를 말하는 것은 매우 까다롭다. 예를 들어, 정보가 실제로 '흐르는' 것일까? 아니면 어떤 정보 단위로서 전달되는 과정에서 전파되는 것 못지않게(혹은 그 이상으로) 정보가 상향 수정되고, 하향 격하되며, 왜곡되고 은폐되는 것일까? 네트워크 내의 행위자들은 정보와 물자의 전파를 중개하거나 제약한다. 본서의 저자들은 재난 대응, 복구, 적응 과정에서 이러한 현상들을 어떻게 사회연결망 분석의 틀 안팎으로 해석해 내고 있는가?"
    },
    {
        "type": "h2",
        "en": "## CONCLUSIONS",
        "ko": "## 결론"
    },
    {
        "type": "p",
        "en": "We hope this book starts to congregate the confirmed generalizations, the conceptual devices, the modes of translation, the definitions, the recognized facts, and the applications of studying relationships and interactions in disaster settings. We especially hope it begins to showcase the nature of variation in human, group and community interactional and exchange behaviors in the face of disaster and as its aftermath unfolds. We do not expect major patterns to be immediately apparent nor do we expect so many patterns to hold in most places or among most populations. However, applying a networks understanding to disasters means that we are able to gather the greatest insight possible into interactions that are ephemeral in and of themselves and that belong to that very liminal space of disasters—where normalcy seems distant even though that normalcy is reeled in daily through those social networks.",
        "ko": "우리는 본서가 재난 환경에서의 관계와 상호작용 연구에 관한 확증된 일반화, 개념적 장치, 번역 모드, 정의, 공인된 사실들, 그리고 실무적 적용 방안들을 한데 모으는 출발점이 되기를 희망한다. 특히 재난에 직면하고 그 여파가 전개되는 과정에서 인간, 집단, 지역사회의 상호작용 및 자원 교환 행위에 나타나는 다양성의 본질을 본격적으로 보여주기 시작하기를 기대한다. 우리는 거시적 주요 패턴이 즉각적으로 명백히 드러날 것으로 기대하지 않으며, 그러한 수많은 패턴들이 대부분의 지역이나 대부분의 인구 집단에서 그대로 유지될 것이라고 생각하지도 않는다. 그러나 재난에 네트워크적 이해를 적용한다는 것은, 그 자체로 일시적(ephemeral)이며 재난이라는 극도의 '경계적 공간(liminal space)'—사회연결망을 통해 일상이 매일같이 힘겹게 회복되어 가고 있음에도 불구하고 정상성이 아득하게만 느껴지는 그 공간—에 속하는 상호작용에 대해 가능한 가장 심오한 통찰을 수집할 수 있음을 의미한다."
    }
]

# Write JS Data
js_content = f"window.CHAPTER_DATA = window.CHAPTER_DATA || {{}};\nwindow.CHAPTER_DATA[1] = {{\n  chapterNumber: 1,\n  titleEn: 'Chapter 1: An Introduction to Social Network Analysis in Disaster Contexts',\n  titleKo: '제1장: 재난 맥락에서의 사회연결망 분석 서설',\n  rows: {json.dumps(rows, ensure_ascii=False, indent=2)}\n}};"

with open('translation/data/chapter1_data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

# Write Parallel Markdown
md_content = """# Chapter 1 대역본 (Original & Korean 1:1 Parallel Translation)

> **서지정보:** Jones, E. C., & Faas, A. J. (2017). Chapter 1: An Introduction to Social Network Analysis in Disaster Contexts. In *Social Network Analysis of Disaster Response, Recovery, and Adaptation* (pp. 3–9). Elsevier.

---

"""

for idx, r in enumerate(rows):
    md_content += f"### [단락 {idx+1}] {r['type'].upper()}\n\n"
    md_content += f"**[EN]**\n{r['en']}\n\n"
    md_content += f"**[KO]**\n{r['ko']}\n\n"
    md_content += "---\n\n"

with open('translation/chapter1_대역.md', 'w', encoding='utf-8') as f:
    f.write(md_content)

print(f"Successfully generated Chapter 1 data with {len(rows)} rows!")
