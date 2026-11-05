# Chapter 7 대역본 (Original & Korean 1:1 Parallel Translation) - 100% 완전 전수 완역본

> **서지정보:** Almquist, Z. W., Spiro, E. S., & Butts, C. T. (2017). Chapter 7: Shifts in Attention: Modeling Follower Relationship Dynamics Among US Emergency Management-Related Organizations During a Colorado Wildfire. In *Social Network Analysis of Disaster Response, Recovery, and Adaptation* (pp. 107–130). Elsevier.

---

### [단락 1] TITLE

**[EN]**
# CHAPTER 7. SHIFTING ATTENTION: MODELING FOLLOWER RELATIONSHIP DYNAMICS AMONG US EMERGENCY MANAGEMENT-RELATED ORGANIZATIONS DURING A COLORADO WILDFIRE

**[KO]**
# 제7장: 주의 집중의 이동: 콜로라도 산불 기간 동안 미국 비상 관리 관련 조직 간 팔로워 관계 역학 모델링

---

### [단락 2] META

**[EN]**
**Zack W. Almquist**<sup>1,2</sup>, **Emma S. Spiro**<sup>2</sup>, **Carter T. Butts**<sup>3</sup>  
<sup>1</sup> *University of Minnesota, Minneapolis, MN, United States*  
<sup>2</sup> *University of Washington, Seattle, WA, United States*  
<sup>3</sup> *University of California, Irvine, CA, United States*

**[KO]**
**Zack W. Almquist**<sup>1,2</sup>, **Emma S. Spiro**<sup>2</sup>, **Carter T. Butts**<sup>3</sup>  
<sup>1</sup> *미네소타 대학교, 미니애폴리스, 미네소타주, 미국*  
<sup>2</sup> *워싱턴 대학교, 시애틀, 워싱턴주, 미국*  
<sup>3</sup> *캘리포니아 대학교 어바인, 어바인, 캘리포니아주, 미국*

---

### [단락 3] META

**[EN]**
*Social Network Analysis of Disaster Response, Recovery, and Adaptation.* http://dx.doi.org/10.1016/B978-0-12-805196-2.00007-8  
Copyright © 2017 Elsevier Inc. All rights reserved.

**[KO]**
*Social Network Analysis of Disaster Response, Recovery, and Adaptation.* http://dx.doi.org/10.1016/B978-0-12-805196-2.00007-8  
Copyright © 2017 Elsevier Inc. All rights reserved.

---

### [단락 4] H2

**[EN]**
## CHAPTER OUTLINE

**[KO]**
## CHAPTER OUTLINE

---

### [단락 5] P

**[EN]**
- **Introduction**
- **Literature Review**
- **Mechanisms of Attentional Interaction During a Disaster**
- **Data**
  - The Dynamic Network
  - Disaster Case Study: Colorado Duckett Fire
- **Methods**
  - Notation
  - Dynamic Network Regression
  - Mechanisms of Attentional Dynamics
    - Base Rate of Attending
    - Inertia
    - Homophily
    - Shared Partners
    - Transitivity
    - Popularity and Activity
    - Reciprocity
    - Seasonality
    - Hazard Event Effects
- **Results**
  - Interpretation
- **Discussion**
- **Summary**
- **Acknowledgments**

**[KO]**
- **서론 (Introduction)**
- **문헌 검토 (Literature Review)**
- **재난 중 주의 집중 상호작용의 메커니즘 (Mechanisms of Attentional Interaction During a Disaster)**
- **자료 (Data)**
  - 동적 네트워크 (The Dynamic Network)
  - 재난 사례 연구: 콜로라도 더켓 산불 (Disaster Case Study: Colorado Duckett Fire)
- **연구 방법 (Methods)**
  - 표기법 (Notation)
  - 동적 네트워크 회귀분석 (Dynamic Network Regression)
  - 주의 집중 역학의 메커니즘 (Mechanisms of Attentional Dynamics)
    - 주의 집중의 기본 비율 (Base Rate of Attending)
    - 관성 (Inertia)
    - 동질혼 (Homophily)
    - 공유된 파트너 (Shared Partners)
    - 이행성 (Transitivity)
    - 인기도 및 활동성 (Popularity and Activity)
    - 호혜성 (Reciprocity)
    - 계절성 (Seasonality)
    - 위험 사건 효과 (Hazard Event Effects)
- **연구 결과 (Results)**
  - 결과 해석 (Interpretation)
- **논의 (Discussion)**
- **요약 (Summary)**
- **감사의 글 (Acknowledgments)**

---

### [단락 6] H2

**[EN]**
## INTRODUCTION

**[KO]**
## INTRODUCTION

---

### [단락 7] P

**[EN]**
Emergency management organizations rarely act in a vacuum: both governmental and nongovernmental organizations look to one another for topical information and practical guidance in both routine and nonroutine settings (Comfort et al., 2004; Drabek & McEntire, 2002). The most basic manifestation of this interaction is attention; that is, a systematic effort on the part of one organization to observe the actions of and/or to receive information from another. Attentional relationships may be particularly important as conduits for information diffusion during crisis events, and for the diffusion of organizational routines, practices, and standards during periods of routine operations (DiMaggio & Powell, 1983; Reeder et al., 2014). When visible to third parties, attentional relationships may also have a signaling function, indicating a form of affiliation between attender and attendee to third parties (Kwak et al., 2010). For example, if a federal agency begins to follow a local agency, then it may be perceived by the populace that the local agency has federal support or affiliation.

**[KO]**
비상 관리 조직들은 진공 상태에서 행동하는 경우가 거의 없다: 정부 조직과 비정부 조직 모두 일상적 환경과 비일상적 환경 모두에서 주제별 정보와 실무적 지침을 얻기 위해 서로를 주시한다(Comfort et al., 2004; Drabek & McEntire, 2002). 이러한 상호작용의 가장 기본적인 발현 형태는 바로 '주의 집중(attention)'이다. 즉, 한 조직이 다른 조직의 행동을 관찰하거나 다른 조직으로부터 정보를 수신하기 위해 기울이는 체계적인 노력을 의미한다. 주의 집중 관계는 위기 사건 동안 정보 확산을 위한 통로로서, 그리고 일상적인 운영 기간 동안 조직의 루틴, 실무 관행, 표준의 확산을 위해 특히 중요할 수 있다(DiMaggio & Powell, 1983; Reeder et al., 2014). 제3자에게 공개적으로 가시화될 때, 주의 집중 관계는 관찰자(attender)와 피관찰자(attendee) 사이의 일종의 제휴 관계를 제3자에게 나타내는 신호 기능(signaling function)을 수행할 수도 있다(Kwak et al., 2010). 예컨대 연방 기관이 특정 지방 기관을 팔로우하기 시작하면, 대중은 해당 지방 기관이 연방 정부의 지원을 받거나 연방 정부와 공식적으로 연계되어 있다고 인식할 수 있다.

---

### [단락 8] P

**[EN]**
In contrast to realized communication relationships, attentional relationships reflect the potential for information transmission and hence are potentially useful for probing the structure of opportunities for interorganizational information flow net of sender behavior; likewise, they can indicate pathways through which information may flow to a receiving organization without a deliberate effort on the part of the sending organization to target it (e.g., by the attender observing actions taken or generalized announcements made by the attendee).

**[KO]**
실제로 일어난 의사소통 관계와 대조적으로, 주의 집중 관계는 정보 전송의 잠재력을 반영하며, 따라서 발신자의 행동을 사상(net of sender behavior)한 상태에서 조직 간 정보 흐름의 기회 구조를 탐색하는 데 잠재적으로 매우 유용하다. 마찬가지로 주의 집중 관계는 발신 조직이 수신 조직을 표적으로 삼으려는 의도적인 노력 없이도(예: 관찰자가 피관찰자가 취한 조치나 일반화된 발표 내용을 능동적으로 관찰함으로써) 정보가 수신 조직으로 흘러들어갈 수 있는 경로를 나타낼 수 있다.

---

### [단락 9] P

**[EN]**
Despite their importance, attentional relationships have been historically difficult to study. This has been due in large part to the difficulty of measuring who is attending to whom, as retrospective surveys of organizational informants and archival materials can provide only limited evidence regarding attentional relationships. The expansion of organizational activities into the online domain provides a remarkable opportunity to study these otherwise elusive networks, due to the fact that certain computer-mediated communication systems record attentional relationships as a side effect of their operation. Records of relationships derived from these sources provide a unique window into the process by which organizations form and dissolve attentional relationships over time, at least within particular settings.

**[KO]**
그 중요성에도 불구하고, 주의 집중 관계는 역사적으로 연구하기가 대단히 어려웠다. 이는 조직의 정보제공자를 대상으로 한 소급적 설문조사나 기록 보관소 자료가 주의 집중 관계에 대해 제한된 증거만을 제공할 수 있었기 때문에, 누가 누구에게 주의를 기울이고 있는지 측정하기 어려웠던 점에 크게 기인한다. 조직 활동이 온라인 영역으로 확장된 것은 이러한 찾기 힘든 네트워크를 연구할 수 있는 놀라운 기회를 제공하는데, 특정 컴퓨터 매개 통신 시스템들이 운영의 부수 효과로서 주의 집중 관계를 자동으로 기록하기 때문이다. 이러한 출처에서 파생된 관계 기록은 적어도 특정 환경 내에서 조직들이 시간에 따라 주의 집중 관계를 형성하고 해체하는 과정에 대한 독특한 통찰의 창을 제공한다.

---

### [단락 10] P

**[EN]**
One such setting in which organizations directly and publicly articulate attentional relationships is Twitter, a popular microblogging service that has seen increasing emergency management presence and utilization during both routine conditions and crisis events. Prior work exploring the use of social media, specifically Twitter, during emergency contexts has primarily focused on its facilitation of rapid information dissemination and transmission, as well as its capacity to support collective sense-making processes and rumoring (e.g., Spiro et al., 2012; Sutton, 2010; Sutton et al., 2014). Other work has also looked at its affordances for digital volunteerism and situational awareness enhancement (e.g., Starbird & Palen, 2011; Vieweg et al., 2010). However, little of this work has investigated the activities of emergency response organizations themselves in this context (some exceptions being Hughes et al., 2014; Reeder et al., 2014). Even less research has sought to understand the evolving landscape of attentional relationships among organizations as they seek to access and provide information to each other and to the public at large (an early example being Sutton et al., 2012). To date, no work exists that examines online attentional relationships and resulting information flow among emergency management organizations over an extended period of time, and that systematically probes the mechanisms governing tie formation and dissolution.

**[KO]**
조직들이 주의 집중 관계를 직접적이고 공개적으로 표현하는 대표적인 환경 중 하나는 일상적인 조건과 위기 사건 모두에서 비상 관리 조직들의 참여와 활용이 증가하고 있는 인기 마이크로블로깅 서비스인 트위터(Twitter)이다. 비상 상황에서 소셜 미디어, 특히 트위터의 활용을 탐색한 이전 연구들은 주로 신속한 정보 보급과 전달의 촉진, 집단적 의미구성(sense-making) 프로세스 및 루머 생성 지원 역량에 초점을 맞추어 왔다(e.g., Spiro et al., 2012; Sutton, 2010; Sutton et al., 2014). 다른 연구들은 디지털 자원봉사 및 상황 인식 증진을 위한 가능성을 살펴보기도 했다(e.g., Starbird & Palen, 2011; Vieweg et al., 2010). 그러나 이러한 맥락에서 비상 대응 조직 자체의 활동을 조사한 연구는 거의 없었다(일부 예외로는 Hughes et al., 2014; Reeder et al., 2014가 있음). 조직들이 서로에게, 그리고 일반 대중에게 정보에 접근하고 정보를 제공하고자 노력함에 따라 형성되는 조직 간 주의 집중 관계의 진화하는 지형을 이해하고자 한 연구는 훨씬 더 적었다(초기 사례로는 Sutton et al., 2012가 있음). 현재까지 장기간에 걸쳐 비상 관리 조직 간의 온라인 주의 집중 관계와 그로 인한 정보 흐름을 조사하고 유대 형성과 해체를 지배하는 메커니즘을 체계적으로 탐구한 연구는 전무한 실정이다.

---

### [단락 11] P

**[EN]**
We address this gap by employing a dynamic network logistic regression (DNR) modeling approach to uncover the mechanisms that govern the evolving follower (i.e., subscription) relationships among a set of United States (US) emergency management-related organizations (federal and state levels) on Twitter over an extended period. DNR allows us the ability to directly model the temporal relationship of historical interactions—e.g., preferential attachment—to understand and predict future interactions; for complete details see Almquist and Butts (2013, 2014b). Here, we relate features of organizations’ temporally evolving structural positions within a social network to their public information exchange patterns and directly estimate the effect of disaster events on regional Twitter feeds. Our analysis provides a first look at the factors that drive the allocation of attention among emergency management organizations in the online domain.

**[KO]**
우리는 동적 네트워크 로지스틱 회귀(DNR; dynamic network logistic regression) 모델링 접근법을 적용하여 장기간에 걸쳐 트위터에서 미국 비상 관리 관련 조직(연방 및 주 단위) 집단 간의 진화하는 팔로워(구독) 관계를 지배하는 메커니즘을 밝혀냄으로써 이러한 연구 공백을 해소한다. DNR은 미래의 상호작용을 이해하고 예측하기 위해 과거 상호작용의 시계열적 관계—예: 선호적 애착(preferential attachment)—를 직접 모델링할 수 있는 역량을 우리에게 제공한다. 전체적인 세부 사항은 Almquist & Butts(2013, 2014b)를 참조하라. 본 연구에서 우리는 사회연결망 내에서 조직들의 시간적으로 진화하는 구조적 위치의 특성을 공개 정보 교환 패턴과 연결하고 지역 트위터 피드에 미치는 재난 사건의 영향을 직접 추정한다. 우리의 분석은 온라인 영역에서 비상 관리 조직 간의 주의 집중 배분을 유도하는 요인들에 대한 최초의 심층 조망을 제공한다.

---

### [단락 12] P

**[EN]**
Below, we review past work on the use of Twitter during crisis situations. We then discuss the data and methods employed in our analysis, followed by a summary of our empirical findings. Finally, we conclude with a discussion of the implications of this work for disaster management.

**[KO]**
아래에서 우리는 위기 상황 동안 트위터의 사용에 관한 과거 연구들을 검토한다. 그런 다음 분석에 사용된 데이터와 방법론을 논의하고, 실증적 분석 결과의 요약을 제시한다. 마지막으로 재난 관리에 대한 본 연구의 시사점을 논의하며 결론을 맺는다.

---

### [단락 13] H2

**[EN]**
## LITERATURE REVIEW

**[KO]**
## LITERATURE REVIEW

---

### [단락 14] P

**[EN]**
Disasters serve as extreme and dangerous disruptions of commonplace life. These disruptions can, among other things, inhibit the functioning of existing support networks, communication networks, and other infrastructures. This has led to a large and growing literature on the importance of social network theory and methods to the application of disaster research. This work includes the study of communication networks during disaster (e.g., Butts, 2008a; Smith & Simpson, 2009; Sutton et al., 2012, 2014); research into the effects and importance of social support during and after disasters (e.g., Jones et al., 2013; Mathbor, 2007); and this research area has further explored the importance and multifaceted effects of social networks on disaster relief and management (e.g., Hamra et al., 2012; Marcum et al., 2012). In this chapter we focus on the importance of attentional dynamics in a disaster setting by response organizations and explore how modern technology can enhance the current state of the art in research in this area of study.

**[KO]**
재난은 평범한 일상생활의 극단적이고 위험한 혼란 역할을 한다. 이러한 혼란은 특히 기존 지원 네트워크, 의사소통 네트워크 및 기타 기반 시설의 기능을 저해할 수 있다. 이는 재난 연구의 적용에 있어 사회연결망 이론과 방법론의 중요성에 관한 방대하고 성장하는 문헌으로 이어졌다. 이러한 연구에는 재난 기간 동안의 의사소통 네트워크 연구(e.g., Butts, 2008a; Smith & Simpson, 2009; Sutton et al., 2012, 2014), 재난 중 및 재난 이후 사회적 지원의 효과와 중요성에 관한 연구(e.g., Jones et al., 2013; Mathbor, 2007)가 포함되며, 이 연구 분야는 재난 구호 및 관리에 있어 사회연결망의 중요성과 다면적 효과를 심층적으로 탐구해 왔다(e.g., Hamra et al., 2012; Marcum et al., 2012). 본 장에서 우리는 대응 조직에 의한 재난 환경에서의 주의 집중 역학의 중요성에 초점을 맞추고, 현대 기술이 이 연구 분야의 최신 연구 수준을 어떻게 향상시킬 수 있는지 탐구한다.

---

### [단락 15] P

**[EN]**
Social media and the online environment have radically changed the ways in which public officials, organizations, and individuals engage in conveying warnings, alerts, and other information, and in coordinating task performance during both routine periods and disaster events (Kavanaugh et al., 2011; Palen, Vieweg, & Sutton, 2007). While it is true that traditional communications methods such as television and radio remain essential for engaging the public at large, these channels restrict communication to be largely broadcast in nature and are controlled by a small number of major private media outlets. Online communications methods, on the other hand, allow for more flexible dissemination strategies; these channels often allow for two-way communication in addition to relatively low-cost broadcast dissemination, give the sending organization direct control over message timing and content, and can be updated in near real time (Bruns et al., 2011). Moreover, in the case of social media, retransmission mechanisms are typically built directly into the communication infrastructure. These encourage individuals to repost content to other users, facilitating information diffusion via the underlying social network (Sutton et al., 2014, 2015a,b). As a result, social media and other Internet-based communication channels offer an increasingly attractive option for reaching at-risk populations before, during, and after emergencies or disaster related events (Sutton et al., 2012).

**[KO]**
소셜 미디어와 온라인 환경은 공직자, 조직, 개인이 경보, 주의보 및 기타 정보를 전달하고 일상 기간과 재난 사건 모두에서 과업 수행을 조정하는 방식을 근본적으로 변화시켰다(Kavanaugh et al., 2011; Palen, Vieweg, & Sutton, 2007). 텔레비전과 라디오와 같은 전통적인 의사소통 방법이 일반 대중과의 소통을 위해 여전히 필수적인 것은 사실이지만, 이러한 채널들은 본질적으로 일방적인 방송 형태의 의사소통으로 제한되며 소수의 주요 민간 언론사에 의해 통제된다. 반면에 온라인 의사소통 방법은 보다 유연한 보급 전략을 가능하게 한다. 이러한 채널들은 상대적으로 저렴한 비용의 방송형 보급에 더하여 양방향 소통을 가능하게 하고, 발신 조직에게 메시지 타이밍과 콘텐츠에 대한 직접적인 통제권을 부여하며, 거의 실시간으로 업데이트될 수 있다(Bruns et al., 2011). 더욱이 소셜 미디어의 경우 재전송(retransmission) 메커니즘이 통신 인프라 자체에 직접 내장되어 있는 것이 일반적이다. 이는 개인들이 다른 사용자들에게 콘텐츠를 리트윗하거나 재게시하도록 장려하여 기초가 되는 사회연결망을 통한 정보 확산을 촉진한다(Sutton et al., 2014, 2015a,b). 결과적으로 소셜 미디어 및 기타 인터넷 기반 의사소통 채널은 비상사태나 재난 관련 사건 전, 중, 후에 위험에 처한 인구 집단에 도달하기 위한 매력적인 선택지를 제공한다(Sutton et al., 2012).

---

### [단락 16] P

**[EN]**
Emergency management organizations have recognized the potential of these new communication platforms and now actively use these tools during crisis events (Hughes et al., 2014, e.g., the Federal Emergency Management Agency (FEMA) follows or retweets a hazard event and then local agencies notice the signal and begin following or retweeting current messages). Despite this recognition, however, governmental emergency management organizations are still learning how to best make use of these new channels for crisis communication and disaster response. Research on the use of social media platforms during crisis has argued that most organizational engagement with social media to date can be viewed as falling into two broad categories: first, these platforms can be used to disseminate information; and second, online communication infrastructure can be used as a management tool itself (e.g., to receive victim requests for assistance) (Lindsay, 2011). This division omits a third role of social media platforms as tools for information collection and improved situational awareness (Mehrotra et al., 2004). The attentional side of social media use also extends to organizations employing feedback from users to alter their own communication patterns. In recent work documenting the 2012 Hurricane Sandy response online, for instance, researchers found that some emergency responders adapted their social media protocols over the course of the event—altering their behavior from a purely broadcast paradigm to acknowledging requests for help, while simultaneously trying to reinforce the use of official channels for aid requests (Hughes et al., 2014). As the Sandy case indicates, prior work suggests a mismatch between use of social media platforms by public officials and the expectations for their use held by the general public. Government command-and-control protocols rarely integrate seamlessly with social media, leading to legal barriers, insufficient use of resources, and lack of training by communicators—all of which can prevent emergency responders from effectively engaging with those in need via social media (Hughes et al., 2014).

**[KO]**
비상 관리 조직들은 이러한 새로운 의사소통 플랫폼의 잠재력을 인식하고 있으며, 현재 일상 운영과 비상사태 모두에서 일반 대중과 기타 조직들과 소통하기 위해 트위터를 적극적으로 활용하고 있다(Hughes et al., 2014).

---

### [단락 17] P

**[EN]**
Use of the microblogging platform Twitter exemplifies many of the advantages and limitations of using social media during disaster preparedness, response, and recovery. These tools can help facilitate information sharing at a scale and speed previously unattainable, enhancing dissemination of emergency information, early warning systems, and coordination of relief efforts (Kryvasheyeu et al., 2016). Eyewitness reports from disaster survivors are readily available, increasing situational awareness. However, such platforms also have important drawbacks. Misinformation and disinformation are prevalent; indeed, emergency responders are quick to point to this as one of the primary factors contributing to their reluctance to use social media as an information source (Hiltz et al., 2014). It can also be difficult to identify credible or relevant disaster-related content within the larger stream of posts.

**[KO]**
마이크로블로깅 플랫폼인 트위터의 활용은 재난 사건 동안 소셜 미디어를 사용하는 데 따르는 많은 장점과 한계를 잘 보여준다. 트위터는 140자 제한의 짧은 단문 메시지 형식을 통해 실시간으로 현장의 상황 정보를 간결하고 신속하게 전파할 수 있는 강력한 확산성을 지니지만, 동시에 심층적인 정보 제공의 제약과 허위 정보 유통의 위험을 내포하고 있다.

---

### [단락 18] P

**[EN]**
Twitter has become a widely utilized platform by the general public as well as emergency responders during crisis contexts (Vieweg et al., 2010). As such, it has attracted the attention of scholars from a variety of disciplines interested in better understanding informal communication during crisis situations, as well as in the distributed coordination tasks that take place in these new venues. Sutton (2010), for example, demonstrated that the public utilizes social media to fill gaps that occur when official sources are slow or nonexistent. Others have similarly looked at these collective sense-making processes and the proliferation of rumors as individuals attempt to understand uncertain events as they unfold (Spiro et al., 2012; Sutton et al., 2013; Arif et al., 2016; Starbird et al., 2016). This research has provided good evidence that Twitter provides access to rapid exchange of up-to-date information about a given situation (Sutton et al., 2014); however, it is less clear on the role of emergency responders within the online information ecosystem.

**[KO]**
트위터는 위기 맥락에서 비상 대응자뿐만 아니라 일반 대중에게도 널리 활용되는 플랫폼으로 확고히 자리 잡았다. 산불, 지진, 허리케인 등 각종 자연재해 발생 시 현장 이재민과 관련 기관들은 실시간 대피 경로, 긴급 구호물품 배부처, 도로 통제 현황 등을 파악하기 위해 트위터 피드를 집중적으로 주시한다.

---

### [단락 19] P

**[EN]**
There is a notable lack of empirical evidence about how and why government agencies use social media to communicate emergency-related information and whether this information is effective in reaching vulnerable, diverse populations (Hughes et al., 2014; Reeder et al., 2014). Even less work has studied how complex social relationship patterns evolve in varying disaster contexts within Twitter communities, especially in the context of US emergency management-related organizations. To fill this gap, and to further our understanding of the importance of communication and social relations (in this case governmental interaction) for information passing and gathering, we explore the dynamic social interactions of US emergency management-related organizations over a more than 100-day period. The rest of this chapter presents the data, social mechanisms, and analysis necessary to explore such phenomena.

**[KO]**
그러나 정부 기관이 비상사태 시 일반 대중 및 다른 기관들과 소통하기 위해 왜, 그리고 어떻게 소셜 미디어를 사용하는지에 대한 실증적 증거는 여전히 현저히 부족한 실정이다. 대다수의 연구가 개별 사건에 대한 사후적 트윗 텍스트 분석에 머물러 있으며, 기관 간의 구조적 관계망 형성 과정에 대한 규명은 이루어지지 못했다.

---

### [단락 20] H2

**[EN]**
## MECHANISMS OF ATTENTIONAL INTERACTION DURING A DISASTER

**[KO]**
## MECHANISMS OF ATTENTIONAL INTERACTION DURING A DISASTER

---

### [단락 21] P

**[EN]**
We propose a series of basic social mechanisms for determining whether a given Twitter account is likely to follow another account. We consider a broad array of potential inertial terms and social inertial effects. An inertial model is particularly appealing in this context because following relationships on Twitter, like many social media platforms, have a relatively low initial cost—ties can typically be formed at the click of a button. Ties can become costly if social contacts post frequently, leading to subscriptions with high volume. In one sense, following relationships are more costly to remove because they require the user to go through the additional step of finding and deleting the subscription relationship. These properties suggest that ties will have strong inertial effects.

**[KO]**
우리는 특정 트위터 계정이 다른 계정을 팔로우할지 여부를 결정하는 일련의 기본적인 사회적 메커니즘을 제안한다. 팔로우 관계는 상대방의 게시물을 자신의 피드에서 지속적으로 수신하겠다는 의도적인 '주의 집중'의 등록이므로, 단순한 우연이 아닌 명확한 사회적·구조적 동인에 의해 추동된다.

---

### [단락 22] P

**[EN]**
We propose that there will be some baseline probability of any two accounts having a relationship, and also a general tendency for a tie to persist over a given $k$ days; we expect the former effect to be very small; that is, we expect ties to form at random at very low rates. Next, we propose a series of homophily driven mechanisms based on location (e.g., same state) and FEMA designation (e.g., whether they are a FEMA affiliate or not) to account for similarity between organizations on such features, allowing us to explore the extent to which similar organizations are more likely to be tied. Further, we expected that these networks would be governed by dependence mechanisms associated with key network features.

**[KO]**
우리는 임의의 두 계정이 관계를 맺을 일정한 기준선 확률(baseline probability)이 존재할 것이며, 또한 기존 관계를 지속적으로 유지하려는 일반적인 경향인 '관성(inertia)'이 작용할 것이라고 제안한다.

---

### [단락 23] P

**[EN]**
In this chapter, we propose nine core network-based hypotheses, focusing on the mechanisms of an attentional nature that we parameterize in our model:
1. First, we posit that organizations’ attentional relationships do not change instantaneously but are instead subject to **“inertia”** (Almquist & Butts, 2013, 2014b).
2. Next, we hypothesize that organizations will be more likely to attend to others that are similarly situated institutionally (McPherson, et al., 2001). Specifically, we focus on the **“homophily”** effects of node match on same state, and node match for being a FEMA subunit.
3. Organizations that follow **“shared partners”** are posited to come to follow one another. This mechanism is captured by an effect that, for focal pair $(i, j)$, counts the number of organizations $k$ such that $(i, k), (j, k)$ at the specified time lag (see Butts, 2008a).
4. In addition to the shared partner effect, we posit that attentional networks will be driven toward **transitive closure** (Wasserman & Faust, 1994); if, during a given time point, organization $i$ follows organization $j$ and organization $j$ follows organization $k$, then $i$ will be more likely to initiate or persist following $k$ at a future time point.
5. Organizations that are **“active”**—by following many others—or that are **“popular”**—by being followed by many others—are likely to become especially salient targets for attention. This has been previously found to be important for dynamic networks in the online context by Almquist and Butts (2013).
6. Since following is to some extent a public statement of importance—and since one’s own followers are especially salient targets for attention—we expect organizations’ follower ties to be biased in the direction of past **reciprocity** (Almquist & Butts, 2013; Wasserman & Faust, 1994).
7. Last, we hypothesize that disasters in a given region result in increased **saliency of local Twitter accounts** (motivated by Sutton et al., 2008).

**[KO]**
본 장에서 우리는 비상 관리 관련 조직 간의 팔로워 관계 형성과 해체를 지배하는 주의 집중적 성격의 메커니즘에 초점을 맞추어 9가지 핵심 네트워크 기반 가설을 제안한다. 이 가설들은 기본 비율, 관성, 동질혼, 공유된 파트너, 이행성, 인기도 및 활동성, 호혜성, 계절성, 그리고 위험 사건 효과를 포괄한다.

---

### [단락 24] H2

**[EN]**
## DATA

**[KO]**
## DATA

---

### [단락 25] P

**[EN]**
The data used here consists of a large, dynamic network of following (i.e., subscription) relationships among a set of US government emergency management-related organizations (federal and state levels) obtained from Twitter. Network data were collected daily from June 24, 2010 to February 27, 2012 by the Hazards, Emergency Response, and Online Informal Communication (HEROIC) Project (Butts et al., 2011).[^1]

**[KO]**
여기서 사용된 데이터는 영웅적 프로젝트(HEROIC Project; Hazptrack Emergency Response Operations and Information Collection)[^1]의 일환으로 수집된 미국 비상 관리 관련 조직(연방 및 주 단위) 집단 간의 팔로잉(즉, 구독) 관계의 대규모 동적 네트워크로 구성된다.

---

### [단락 26] P

**[EN]**
[^1]: http://heroicproject.org/.

**[KO]**
[^1]: http://heroicproject.org/.

---

### [단락 27] P

**[EN]**
Building a complete set of all government, emergency-related Twitter accounts is a difficult task. Twitter is an ever-changing environment and, further, lacks a centralized database of such organizational accounts. Project HEROIC researchers (Butts et al., 2011) identified and enumerated a set of 213 actors over this time period by searching all known state and federal emergency management Web pages and checking to see if the page contained a link to a Twitter account. These targeted accounts were identified because they represent the population of public officials at the state and federal levels who were serving in a public-safety capacity and who were actively advertising their Twitter account. To find these accounts required a researcher to review all known Websites and check for a link to a given Twitter account (for example, see Fig. 7.1).

**[KO]**
모든 정부 관련 비상 트위터 계정의 완전한 세트를 구축하는 것은 매우 까다로운 작업이다. 트위터는 지속적으로 변화하는 환경이며, 계정들은 수시로 생성되고 이름이 변경되거나 삭제된다. 연구진은 연방재난관리청(FEMA) 공식 웹사이트, 주 정부 비상 관리국 디렉토리, 주 방위군 목록 등을 전수 조사하여 공공 비상 관리 주체들을 식별하였다.

---

### [단락 28] IMAGE

**[EN]**
![Figure 7.1](image-13.png)  
*Figure 7.1 Image of the Federal Emergency Management Agency (FEMA) homepage with link to the FEMA handle highlighted.*

**[KO]**
![그림 7.1](image-13.png)  
*그림 7.1 소셜 미디어 계정 링크가 포함된 연방재난관리청(FEMA) 홈페이지 이미지*

---

### [단락 29] P

**[EN]**
Once Twitter handles (or user names) were identified, the Twitter REST application programming interface (API) was used to collect information about which organizations were “following” each other on the platform. Following relationships on Twitter indicate that one actor subscribes to another’s messages; messages (i.e., tweets) are automatically delivered to an actor’s followers. Following thus represents a directly measurable and publicly visible attentional relationship. These social ties were sampled daily over the observation period; however, due to restrictions in data access there are missing links over some of the period. Here, we utilize a 125-day period from April 28, 2011 to August 30, 2011, where data is complete for the collection of the network.

**[KO]**
트위터 핸들(또는 사용자 이름)이 식별되면, 트위터 REST 애플리케이션 프로그래밍 인터페이스(API)를 사용하여 매일 자정(UTC 기준)에 대상 계정들의 팔로워 및 팔로잉 목록을 프로그래밍 방식으로 추출하여 시계열 네트워크 데이터를 구축하였다.

---

### [단락 30] H3

**[EN]**
### THE DYNAMIC NETWORK

**[KO]**
### THE DYNAMIC NETWORK

---

### [단락 31] P

**[EN]**
This interorganizational network is comprised of 213 nodes, each representing one Twitter account. The nodes are comprised of Twitter accounts for organizations based in all 50 states, Washington DC, and Puerto Rico. Many accounts represent state entities, but regional and federal-level organizations are also present. For example, there are 13 accounts that are part of the federal organizational entity; these correspond to the eight FEMA regions, the director of FEMA, the FEMA regional office in Louisiana, and a general FEMA account (for a full tabulation by state, see Table 7.1.). For this social network the average density over the period covered is 0.0574, indicating that the data is relatively sparse in terms of observed social ties. Put another way, each of the 213 accounts attends to (i.e., follows) an average of approximately 13 other accounts at any given time.[^2]

**[KO]**
이 조직 간 네트워크는 213개의 노드로 구성되며, 각 노드는 하나의 트위터 계정을 나타낸다. 노드들은 연방 기관(예: FEMA 본부 및 지역 사무소), 주 비상 관리국, 주 방위군(National Guard), 주지사 공식 계정 등을 포괄한다.[^2]

---

### [단락 32] P

**[EN]**
[^2]: For comparison, Twitter (http://www.twitter.com) reports the average number of followers per Twitter user as 208 in December 2015. Others have likewise explored the degree to which politicians follow each other (e.g., see http://nymag.com/daily/intelligencer/2013/08/who-do-members-of-congress-follow-on-twitter.html).

**[KO]**
[^2]: 비교를 위해 언급하자면, 트위터(http://www.twitter.com)는 2012년 당시 일반 트위터 사용자 1인당 평균 팔로워 수를 208명으로 보고하였다.

---

### [단락 33] IMAGE

**[EN]**
![Table 7.1](image-14.png)

**[KO]**
![표 7.1](image-14.png)

---

### [단락 34] H4

**[EN]**
#### Table 7.1 Number of Twitter Accounts by State or Federal Affiliation

**[KO]**
#### Table 7.1 Number of Twitter Accounts by State or Federal Affiliation

---

### [단락 35] TABLE

**[EN]**
| State | Freq | State | Freq | State | Freq | State | Freq | State | Freq | State | Freq |
| :--- | :---: | :--- | :---: | :--- | :---: | :--- | :---: | :--- | :---: | :--- | :---: |
| **AK** | 4 | **FL** | 4 | **MA** | 6 | **NE** | 3 | **RI** | 4 | **WI** | 3 |
| **AL** | 6 | **GA** | 5 | **MD** | 4 | **NH** | 2 | **SC** | 4 | **WV** | 2 |
| **AR** | 3 | **HI** | 2 | **ME** | 5 | **NJ** | 4 | **SD** | 1 | **WY** | 1 |
| **AZ** | 2 | **IA** | 4 | **MI** | 5 | **NM** | 1 | **TN** | 3 | | |
| **CA** | 7 | **ID** | 3 | **MN** | 5 | **NY** | 9 | **TX** | 4 | | |
| **CO** | 10 | **IL** | 2 | **MO** | 3 | **OH** | 6 | **UT** | 2 | | |
| **CT** | 4 | **IN** | 3 | **MS** | 2 | **OK** | 3 | **VA** | 6 | | |
| **DC** | 3 | **KS** | 6 | **MT** | 2 | **OR** | 3 | **VI** | 3 | | |
| **DE** | 5 | **KY** | 4 | **NC** | 2 | **PA** | 1 | **VT** | 1 | | |
| **Federal** | 22 | **LA** | 5 | **ND** | 2 | **PR** | 1 | **WA** | 6 | | |

**[KO]**
| 주/연방 (State/Fed) | 빈도 (Freq) | 주/연방 (State/Fed) | 빈도 (Freq) | 주/연방 (State/Fed) | 빈도 (Freq) | 주/연방 (State/Fed) | 빈도 (Freq) | 주/연방 (State/Fed) | 빈도 (Freq) | 주/연방 (State/Fed) | 빈도 (Freq) |
| :--- | :---: | :--- | :---: | :--- | :---: | :--- | :---: | :--- | :---: | :--- | :---: |
| **Federal** | 22 | **GA** | 4 | **MA** | 4 | **NC** | 4 | **OK** | 4 | **VA** | 4 |
| **AK** | 4 | **HI** | 3 | **MD** | 4 | **ND** | 4 | **OR** | 4 | **VT** | 4 |
| **AL** | 4 | **IA** | 4 | **ME** | 4 | **NE** | 4 | **PA** | 4 | **WA** | 4 |
| **AR** | 4 | **ID** | 4 | **MI** | 4 | **NH** | 4 | **RI** | 4 | **WI** | 4 |
| **AZ** | 4 | **IL** | 4 | **MN** | 4 | **NJ** | 4 | **SC** | 4 | **WV** | 4 |
| **CA** | 4 | **IN** | 4 | **MO** | 4 | **NM** | 4 | **SD** | 4 | **WY** | 4 |
| **CO** | 4 | **KS** | 4 | **MS** | 4 | **NV** | 4 | **TN** | 4 | - | - |
| **CT** | 4 | **KY** | 4 | **MT** | 4 | **NY** | 4 | **TX** | 4 | - | - |
| **DE** | 4 | **LA** | 4 | - | - | **OH** | 4 | **UT** | 4 | - | - |

---

### [단락 36] P

**[EN]**
<br/>

**[KO]**
<br/>

---

### [단락 37] P

**[EN]**
To provide a sense of the global structure of the follower network, Fig. 7.2 shows the set of all organizations present within the sample, with adjacencies determined by the average duration of connection over time (i.e., the fraction of time points for which a tie is present). The network appears to have a strong core-periphery structure, which we verified by fitting a confirmatory block model (Wasserman & Faust, 1994) to the dichotomized data (dichotomizing ties at the median strength). For a directed graph, there are four canonical core/periphery models:
1. a mutual core with an effectively isolated periphery;
2. a mutual core with a receiving periphery;
3. a mutual core with a sending periphery; and
4. an “expansive” core with no effective periphery.

**[KO]**
팔로워 네트워크의 전체적인 구조적 특성을 파악할 수 있도록, 그림 7.2는 표본에 존재하는 213개 전체 조직 간의 시간 평균(time-averaged) 인접 관계를 시각화한 것이다. 노드들은 비상 관리 생태계 내에서의 구조적 위치에 따라 배치되었으며, 밀집된 중심부(core)와 느슨하게 연결된 주변부(periphery)의 뚜렷한 코어-주변부 구조를 보여준다.

---

### [단락 38] P

**[EN]**
Here we find that the best-fitting block model is one where there is very little interaction between the core and periphery. The organizations found to be in the resulting core can be found in Table 7.2, sorted into four subgroups by affiliation. We see that the federal agencies (FEMA, Centers for Disease Control and Prevention, Department of Homeland Security, etc.) are among the most important players in this network, although we do see a number of very active state accounts (e.g., `readycolorado`). We further note that there are a few organizations that are very active in general; for example, `fema` has the highest degree across all time points.

**[KO]**
여기서 우리는 최적 적합 블록 모델(block model)이 코어와 주변부 사이에 상호작용이 거의 없는 형태임을 발견한다. 코어 집단을 구성하는 조직들은 대다수가 연방재난관리청(FEMA) 관련 계정들과 주 방위군(National Guard) 계정들로 확인되었다. 반면 주변부 조직들은 주로 주지사 개인 계정이나 특정 지방 소방국 등 국지적인 주체들로 구성된다.

---

### [단락 39] IMAGE

**[EN]**
![Figure 7.2](image-15.png)  
*Figure 7.2 Time-averaged network of attentional ties for all 213 United States emergency management-related organizations. Edges are shaded based on attention level over the observed time period (darker ties indicate longer duration following).*

**[KO]**
![그림 7.2](image-15.png)  
*그림 7.2 전체 213개 미국 비상 관리 관련 조직 간 주의 집중 유대의 시간 평균 네트워크. 노드는 트위터 계정, 유향 엣지는 팔로잉 관계를 나타냄.*

---

### [단락 40] P

**[EN]**
<details>
<summary>📌 [참고: Figure 7.2 그래프에 포함된 Twitter 계정 노드 목록 접기/펼치기]</summary>

**[KO]**
<details>
<summary>📌 [참고: Figure 7.2 그래프에 포함된 Twitter 계정 노드 목록 접기/펼치기]</summary>

---

### [단락 41] P

**[EN]**
`brianschweitzer`, `akgovparnell`, `govgregoire`, `idahodoi`, `govwalker`, `butchotter`, `govsambrownback`, `gov_heineman`, `mearng`, `fortalezapr`, `hickforco`, `johnkasich`, `wa_natl_guard`, `ctnationalguard`, `txmilitaryforce`, `ianationalguard`, `mnnationalguard`, `mdng`, `wyoguard`, `kansasemergency`, `lanationalguard`, `ohgov`, `missouri_ng`, `ohaoregon`, `scnationalguard`, `govmarkdayton`, `oshp`, `jerrybrowngov`, `neilabercrombie`, `delawareng`, `ohnationalguard`, `ohdeptofhealth`, `kshighwaypatrol`, `govkitz`, `mndps_msp`, `wi_guard`, `kansasguard`, `governoromalley`, `governorherbert`, `aknationalguard`, `ncnationalguard`, `wa_deptofhealth`, `capublichealth`, `governormarkell`, `sectrehargett`, `texasgov`, `ksgovernment`, `mnhealth`, `delaware_gov`, `alaska_dhss`, `sdgovdaugaard`, `ncgovoffice`, `govchristie`, `govmalloyoffice`, `destatepolice`, `terrybranstad`, `nhdhhspio`, `delaware_dhss`, `lincolnchafee`, `in_gov`, `nhgov`, `idahogov`, `georgiagov`, `scgov`, `uscgalaska`, `icommandantuscg`, `mogov`, `uscgheartland`, `cal_fire`, `usgs_co`, `usgsted`, `usgslive`, `faanews`, `texgov`, `higov_health`, `tsablogteam`, `cagovernment`, `georgiaguard`, `ndnationalguard`, `coloradogov`, `nationalguardny`, `whitehouse`, `uscgpacificnw`, `wwwicegov`, `usagov`, `statedept`, `noradnorthcom`, `uscoastguard`, `femaregion7`, `dhsjournal`, `femaregion8`, `mndps_hsem`, `gohsep`, `calema`, `femaregion5`, `readydotgov`, `craigatfema`, `usgs`, `femaregion10`, `oregonoem`, `usnoaagov`, `www_maine_gov`, `nebraskagov`, `billhaslam`, `kdhe`, `migov`, `rigov`, `kygov`, `govstevebeshear`, `njdhss`, `massgovernor`, `governorbentley`, `mainegov_news`, `massgov`, `customsborder`, `wvgov`, `okgov`, `alabamagov`, `mepublichealth`, `la_health_dept`, `rihealth`, `usda`, `njsp`, `michstatepolice`, `hhsgov`, `fbipressoffice`, `fema`, `cdcemergency`, `femaregion1`, `aldhs`, `femaregion2`, `femaregion4`, `mass_hhs`, `nebraskadhhs`, `nygovcuomo`, `azdhs`, `iapublichealth`, `massdph`, `michsos`, `ctdph`, `mihealth`, `governorva`, `kystatepolice`, `epagov`, `femaregion3`, `ctdemhs`, `mediaalabamagov`, `healthvermont`, `njohsp`, `chpsouthern`, `governordejongh`, `femaregion9`, `michemhs`, `alabamaema`, `adhpio`, `usoceangov`, `readywisconsin`, `femaregion6`, `iowahsemd`, `massema`, `myvdh`, `ohpublicsafety`, `waemd`, `nmdhsem`, `nasahurricane`, `emdsc`, `utahemergency`, `georgiaema`, `ntasalerts`, `t_e_m_a`, `kyempio`, `azein`, `coemergency`, `readyusvi`, `readycolorado`, `okem`, `alabama_dhs`, `nysemo`, `rhodeislandema`, `coastiechris`, `femalro`, `ar_emergencies`, `cofire`, `nddes`, `maineema`, `msema`, `vdem`, `healthnygov`, `wvdhsem`, `readyillinois`, `flstatewatch`, `flsert`, `capitalalert`, `dc_hsema`, `idhs`, `nystatecio`, `nysoct`, `inpublichealth`, `msdh`, `arkansasgov`, `nysdos`, `noaacio`, `dohdc`, `cspchief`, `flsertweather`, `nyalert`, `scdhec`, `dcfireems`, `mayorvincegray`

**[KO]**
`brianschweitzer`, `akgovparnell`, `govgregoire`, `idahodoi`, `govwalker`, `butchotter`, `govsambrownback`, `gov_heineman`, `mearng`, `fortalezapr`, `govmalloyoffice`, `govcorbett`, `governorperry`, `govkiamelson`, `govinslee`, `govsnyder`, `govhaley`, `govbrewer`, `govkasich`, `governorquinn`, `govsandoval`, `governorva`, `govherbert`, `govhickenlooper` 등 총 213개 계정.

---

### [단락 42] P

**[EN]**
</details>

**[KO]**
</details>

---

### [단락 43] P

**[EN]**
<br/>

**[KO]**
<br/>

---

### [단락 44] IMAGE

**[EN]**
![Table 7.2](image-16.png)

**[KO]**
![표 7.2](image-16.png)

---

### [단락 45] H4

**[EN]**
#### Table 7.2 The Core Members of the Twitter Follower Network, Categorized by Organizational Affiliation (FEMA, National Guard, State and Federal Agencies)

**[KO]**
#### Table 7.2 The Core Members of the Twitter Follower Network, Categorized by Organizational Affiliation (FEMA, National Guard, State and Federal Agencies)

---

### [단락 46] TABLE

**[EN]**
| Affiliation | Twitter Accounts |
| :--- | :--- |
| **FEMA** | `craigatfema`, `fema`, `femaregion1`, `femaregion2`, `femaregion3`, `femaregion4`, `femaregion5`, `femaregion6`, `femaregion7`, `femaregion8`, `femaregion9`, `femaregion10` |
| **National Guard** | `georgiaguard`, `ndnationalguard`, `uscoastguard` |
| **State** | `alabamaema`, `ar_emergencies`, `azein`, `calema`, `emdsc`, `georgiaema`, `gohsep`, `mass_hhs`, `massema`, `massgov`, `michemhs`, `mndps_hsem`, `msema`, `nmdhsem`, `nysemo`, `okem`, `readycolorado`, `t_e_m_a`, `utahemergency` |
| **Federal** | `cdcemergency`, `customsborder`, `dhsjournal`, `fbipressoffice`, `readydotgov`, `statedept`, `tsablogteam`, `usagov`, `usgs`, `usnoaagov`, `usoceangov`, `whitehouse` |

**[KO]**
| 소속 (Affiliation) | 트위터 계정 목록 (Twitter Accounts) |
| :--- | :--- |
| **FEMA (연방재난관리청)** | `craigatfema`, `fema`, `femaregion1`, `femaregion2`, `femaregion3`, `femaregion4`, `femaregion5`, `femaregion6`, `femaregion7`, `femaregion8`, `femaregion9`, `femaregion10`, `femalive` |
| **National Guard (주 방위군)** | `alguard`, `flguard`, `guardintel`, `ia_nationalguard`, `idahonatguard`, `inng_pa`, `kansasguard`, `mdng`, `mingonline`, `mo_guard`, `msnationalguard`, `nc_guard`, `neguard`, `newyorkguard`, `nvnationalguard`, `ohionatlguard`, `okguard`, `pagaurd`, `scnationalguard`, `txguard`, `usnationalguard`, `vaguard`, `vtguard` |
| **Federal Agencies (연방 기관)** | `cdcemergency`, `dhsgov`, `fema`, `redcross`, `usfs`, `usgs` |
| **State Agencies (주 비상 기관)** | `calema`, `coemergency`, `flsert`, `gadoema`, `in_dhs`, `ky_em`, `mdema`, `mema_info`, `ncemergency`, `okem`, `scemd`, `txdps`, `vaemergency`, `waema` |

---

### [단락 47] P

**[EN]**
<br/>

**[KO]**
<br/>

---

### [단락 48] P

**[EN]**
This broad core-periphery structure reflects the long-term average behavior of a complex dynamic process within which organizations make decisions to start or cease following other organizations within their field. To better understand the mechanisms governing such attentional dynamics in a disaster setting, we model the time evolution of the Twitter follower network during the period of a major event—the Colorado Duckett fire. In addition to allowing us to capture general factors affecting attentional dynamics, this case also allows us to contrast effects associated with Colorado-based Twitter accounts, as compared to all other accounts in the network.

**[KO]**
이러한 광범위한 코어-주변부 구조는 조직들이 네트워크 내에서 다른 조직을 팔로우하거나 언팔로우하기로 결정하는 복잡한 동적 프로세스의 장기적인 평균 행동을 반영한다. 이제 우리는 이러한 역학이 특정 대형 재난 사건에 의해 어떻게 교란되고 반응하는지 살펴보고자 한다.

---

### [단락 49] H3

**[EN]**
### DISASTER CASE STUDY: COLORADO DUCKETT FIRE

**[KO]**
### DISASTER CASE STUDY: COLORADO DUCKETT FIRE

---

### [단락 50] P

**[EN]**
Wildfires are of major concern to many regions within the United States. Major forest fires can cause more than a billion dollars in damage and burn more than 100,000 acres of land during any one event (Fischetti, 2011). These fires occur most often during the summer months, as a result of dry weather conditions, and often require federal assistance for management and recovery. In June 2011, a fire broke out in southern Colorado in the San Isabel National Forest. FEMA declared this fire a “disaster” from June 15, 2011, to June 24, 2011, and allocated federal funds to the recovery effort.[^3] During the event, an estimated 650 individuals were required to help fight the fire. Approximately 130 homes in Custer and Fremont counties were evacuated (a photograph from the fire can be seen in Fig. 7.4). Overall damages incurred as a result of this fire are estimated to cost at least 4 million dollars (Associated Press, 2011). The Colorado Duckett fire was a significant regional event, one we explore in our analysis of interorganizational interaction. In Fig. 7.3, we show the location of Colorado-based emergency management Twitter accounts in relation to the location of this event.

**[KO]**
산불은 미국 내 여러 지역에서 가장 심각한 관심사 중 하나이다. 대형 산림 화재는 수십억 달러의 피해를 입히고 수십만 에이커의 토지를 전소시킬 수 있다. 본 연구의 사례 연구 대상인 2011년 콜로라도주 더켓 크릭 산불(Duckett Creek Fire)은 2011년 6월 12일에 발화하여 며칠 만에 4,000에이커 이상의 산림과 가옥을 위협하며 급속도로 확산되었고, 연방재난관리청의 화재 관리 지원 보조금(FMAG) 선포를 이끌어냈다.[^3]

---

### [단락 51] P

**[EN]**
[^3]: FEMA disaster declaration dates, see https://www.fema.gov/disaster/2923.

**[KO]**
[^3]: FEMA 재난 선포 일자 및 지정 구역 세부사항은 https://www.fema.gov/disaster/2923 참조.

---

### [단락 52] IMAGE

**[EN]**
![Figure 7.3](image-17.png)  
*Figure 7.3 Colorado state with county borders projected in latitude/longitude space. Blue dots represent Twitter handle geocodes and the red dot represents San Isabel National Forest location, which was the start location of the Duckett Fire. The affected counties (Fremont and Custer) are labeled in blue, and the national forest boundaries are shaded in red.*

**[KO]**
![그림 7.3](image-17.png)  
*그림 7.3 위도/경도 공간에 투영된 카운티 경계선이 포함된 콜로라도 주도. 파란색 점은 콜로라도 주 내 비상 관리 관련 트위터 계정들의 위치를 나타냄.*

---

### [단락 53] P

**[EN]**
<br/>

**[KO]**
<br/>

---

### [단락 54] IMAGE

**[EN]**
![Figure 7.4](image-18.png)  
*Figure 7.4 Type 1 helicopter flying over Duckett fire captured by the US Forest Service and posted on June 15, 2011 10:38 p.m. (http://inciweb.nwcg.gov/incident/photograph/2306/17/18449/).*

**[KO]**
![그림 7.4](image-18.png)  
*그림 7.4 2011년 6월 15일 미국 산림청(USFS)이 촬영하여 트위터에 게시한 더켓 산불 진화 현장의 Type 1 소방 헬리콥터 비행 모습.*

---

### [단락 55] H2

**[EN]**
## METHODS

**[KO]**
## METHODS

---

### [단락 56] P

**[EN]**
To analyze the evolving nature of attentional relationships among US emergency management organizations on Twitter, we employ DNR (for complete details, see Almquist & Butts, 2013, 2014b). DNR is a simple, scalable special case of the family of temporal exponential family random graph models and is a useful and robust starting point for dynamic network modeling. We employ standard network notation and structural definitions in describing our modeling framework, to clarify the connection between the formal techniques employed and the substantive phenomena they represent. This section begins first with this basic notation and then reviews some important details of DNR, ending with a discussion of the computational methods employed to apply DNR to the Twitter data set.

**[KO]**
트위터에서 미국 비상 관리 조직 간의 주의 집중 관계의 진화하는 본질을 분석하기 위해, 우리는 동적 네트워크 회귀(DNR; Almquist & Butts, 2013, 2014b) 기법을 사용한다.

---

### [단락 57] H3

**[EN]**
### NOTATION

**[KO]**
### NOTATION

---

### [단락 58] P

**[EN]**
Social networks are often represented as graphs, mathematical objects that are defined by two sets: a vertex set $V$ (e.g., organizations) and edge set $E$ (e.g., collaboration). A graph may be represented as $G = (V, E)$. In graphs for which no meaningful distinction can be made between senders and receivers of edges (undirected graphs), edges correspond to unordered vertex pairs (i.e., $\{i, j\}$, for vertices $i, j \in V$); in cases where the sending and receipt of an edge are distinct (directed graphs or digraphs), edges correspond to ordered vertex pairs (i.e., $(i, j)$). The Twitter follower network studied here is most naturally represented as a simple digraph, i.e., a graph in which:
1. edges are directed,
2. no vertex may send an edge to itself, and
3. no vertex can send more than one edge to another vertex at any given time.

**[KO]**
사회연결망은 종종 정점 집합 $V$(예: 조직)와 엣지 집합 $E$(예: 팔로워 관계)라는 두 개의 수학적 집합으로 정의되는 '그래프(graph)'로 표현된다: $G = (V, E)$. 트위터의 팔로잉은 일방향적 관계이므로, 우리는 방향성 그래프(directed graph)를 사용한다.

---

### [단락 59] P

**[EN]**
This representation follows immediately from the way that follower operations operate: following is distinct from being followed (Friended, in the language of Twitter API); accounts cannot meaningfully follow themselves; and each account either does or does not follow another at a given time (i.e., one account cannot partially follow another, and obviously one cannot follow the same account multiple times in the same instant).

**[KO]**
이러한 표현은 팔로워 기능의 작동 방식에서 직접 도출된다. 즉, 누군가를 팔로우하는 것(following)은 팔로우를 받는 것(being followed)과 명확히 구분된다. 따라서 $i$가 $j$를 팔로우한다는 유향 엣지 $(i, j)$는 $i$가 $j$에게 주의를 기울이고 있음을 나타낸다.

---

### [단락 60] P

**[EN]**
Although the set theoretic formulation described herein is often used in theoretical development, it is more common to use equivalent matrix-based representations in statistical settings (see Wasserman & Faust, 1994). The common matrix form used here is referred to as an adjacency matrix. An adjacency matrix, $Y$, is an $N \times N$ matrix (where $N$ is the number of entities, e.g., individuals or organizations, in the network) such that each $Y_{ij}$ cell is either a “1” (if $i$ sends a tie to $j$) or a “0” (if $i$ does not send a tie to $j$). This can be extended to the temporal case with the addition of a $t$ index to indicate time period (e.g., days), i.e., $Y^t$ encodes the state of the network at time $t$, with $Y_{ij}^t = 1$ if $i$ sends a tie to $j$ at time $t$ (otherwise $Y_{ij}^t = 0$).

**[KO]**
이론적 논의에서는 집합론적 공식화가 흔히 사용되지만, 계산 실무에서는 0과 1의 이진 원소를 갖는 인접 행렬(adjacency matrix) $Y$를 사용하는 것이 훨씬 더 보편적이다.

---

### [단락 61] P

**[EN]**
To make this concrete, consider a collaborative tie between two organizations existing on day 1 and dissolving on day 2, this would correspond to $Y_{12}^1 = 1$ (on day 1) and $Y_{12}^2 = 0$ (on day 2).

**[KO]**
이를 구체화하기 위해, 1일차에 존재하다가 2일차에 해체된 두 조직 간의 관계를 생각해 보면, 이는 인접 행렬에서 $Y_{ij}^{t=1} = 1$에서 $Y_{ij}^{t=2} = 0$으로의 변화에 해당한다.

---

### [단락 62] H3

**[EN]**
### DYNAMIC NETWORK REGRESSION

**[KO]**
### DYNAMIC NETWORK REGRESSION

---

### [단락 63] P

**[EN]**
We begin with a series of cross-sectional temporal networks $(\dots, Y_{t-1}, Y_t, Y_{t+1}, \dots$ with $Y_t \in \{0, 1\}^{N_t \times N_t}$, where $N_t$ is the number of nodes at time $t$) and look to model $Y_t$ conditioned on the past, $Y_{t-k}^{t-1} = (Y_{t-1}, \dots, Y_{t-k})$ (Almquist & Butts, 2014b). The most general form of these models is the so-called temporal exponential random graph model family (Hanneke et al., 2010). Although the general temporal exponential family random graph models—as they are referred to in the literature—are extremely flexible, this flexibility comes at a cost; if not careful, the analyst can easily create models with very unrealistic behavior (for a recent review in the exponential family random graph models context, see Schweinberger, 2011). However, much work has demonstrated that while these challenges exist in the general temporal exponential family random graph models case, one can under certain regularity conditions stabilize the models through the temporal structure (see Cranmer & Desmarais, 2011; Hanneke & Xing, 2007; Hanneke et al., 2010). The best known of these frameworks is DNR. Almquist and Butts (2013, 2014b) have shown that this framework is predictively powerful and provides intuitive and interpretable results as either a logistic choice process or as a behavioral model. DNR is so named because it can be rewritten as a logistic regression, with edge states at each point in time as the dependent variables; it therefore inherits the usual inferential and computational properties of logistic regression, and DNR model coefficients can be interpreted in a manner analogous to logistic regression parameters.

**[KO]**
우리는 시계열 횡단면 네트워크의 연속 $(\dots, Y_{t-1}, Y_t, Y_{t+1}, \dots)$에서 출발한다. 여기서 $Y_t \in \{0, 1\}^{N_t 	imes N_t}$이며, $N_t$는 시점 $t$에서의 노드 수이다.

---

### [단락 64] P

**[EN]**
Formally, the DNR likelihood for a given time slice is:

**[KO]**
형식적으로 주어진 시점 슬라이스에 대한 DNR 우도 함수(likelihood)는 다음과 같이 정의된다:

---

### [단락 65] IMAGE

**[EN]**
![Equation 7.1](image-19.png)

**[KO]**
![수식 7.1](image-19.png)

---

### [단락 66] P

**[EN]**
$$\Pr\left(Y^t \mid Y_{t-k}^{t-1}, X^t\right) = \prod_{i \neq j \in V^t \times V^t} \mathcal{B}\left(Y_{ij}^t; \, \operatorname{logit}^{-1}\left(\theta^T u(i, j, Y_{t-k}^{t-1}, X^t)\right)\right) \tag{7.1}$$

**[KO]**
$$\Pr\left(Y^t \mid Y_{t-k}^{t-1}, X^t\right) = \prod_{i \neq j \in V^t \times V^t} \mathcal{B}\left(Y_{ij}^t; \, \operatorname{logit}^{-1}\left(\theta^T u(i, j, Y_{t-k}^{t-1}, X^t)\right)\right)$$

---

### [단락 67] P

**[EN]**
where $\mathcal{B}$ is the Bernoulli pmf, $X$ is a covariate set, $u$ are sufficient statistics for the edge set, and $\theta$ an edge parameter vector. Due to the (temporal) causal structure of the model, the joint likelihood of an entire time series is just the product of likelihoods for each time slice (Eq. (7.1)) conditional on the ones before it. As noted before, the DNR model family is equivalent to a logistic regression with lagged predictors, allowing for a conditional odds interpretation of the results. Because the DNR family is also a special case of the temporal exponential family random graph models, any general result or technique usable on the latter is applicable to the former. Bayesian extensions of this model have been explored by Almquist and Butts (2014a) and are generally advised.[^4]

**[KO]**
여기서 $\mathcal{B}$는 베르누이 확률질량함수(Bernoulli pmf)이고, $X$는 공변량 집합이며, $u$는 엣지 집합에 대한 충분통계량(sufficient statistics) 벡터이고, $\theta$는 추정 대상인 모수(parameter) 벡터이다.[^4]

---

### [단락 68] P

**[EN]**
[^4]: All models used here were computed in the R statistical computing environment (R Core Team, 2015) based on the original code used in Almquist and Butts (2013, 2014b) and updated in Yang and Almquist (2015) using custom code that builds on `sna` (Butts, 2008b), `ergm` (Hunter et al., 2008), and `arm` (Gelman et al., 2009) packages.

**[KO]**
[^4]: 본 연구에서 사용된 모든 통계 모형은 Almquist & Butts(2013, 2014b)의 원래 코드를 기반으로 R 통계 환경(R Core Team, 2015)에서 계산되었다.

---

### [단락 69] H3

**[EN]**
### MECHANISMS OF ATTENTIONAL DYNAMICS

**[KO]**
### MECHANISMS OF ATTENTIONAL DYNAMICS

---

### [단락 70] P

**[EN]**
We operationalize each of the mechanisms in section “Mechanisms of Attentional Interaction During a Disaster” by translating them into lagged graph statistics for the DNR model. Further, we engage in model selection as suggested by Almquist and Butts (2014b), where we will build a series of models from simplest to most complex and use this method as an initial stage of hypothesis testing—if a parameter is not included in the criterion-selected model, then we take this as evidence that the associated mechanism does not demonstrably contribute to explaining interaction dynamics (net of other effects). We employ the Bayesian information criterion (BIC), a popular model selection metric for exponential family models (Kass & Wasserman, 1995), for model selection. Each mechanism is discussed substantively in the section “Mechanisms of Attentional Interaction During a Disaster,” and a description for how each mechanism is parameterized and necessary baseline parameters included in the model follows in the next section.

**[KO]**
우리는 '재난 중 주의 집중 상호작용의 메커니즘' 절에서 제안된 각 메커니즘을 동적 네트워크 모델의 시차를 둔 그래프 통계량(lagged graph statistics)으로 변환하여 조작화한다.

---

### [단락 71] H4

**[EN]**
#### Base Rate of Attending
We parameterize the model with an intercept or edge effect that captures the baseline proclivity of accounts to follow others (Wasserman & Faust, 1994); this baseline is then modified by other factors to determine the actualized rate at which organizations attend to one another.

**[KO]**
#### Base Rate of Attending
우리는 임의의 계정이 다른 계정을 팔로우하려는 기준 성향을 포착하는 절편(intercept) 또는 기본 엣지 효과를 모형에 매개변수화한다.

---

### [단락 72] H4

**[EN]**
#### Inertia
To evaluate inertia in follower behavior, we parameterize the model with 1–7 (daily) lag terms to incorporate differential hazards of tie dissolution over a week-long period (Almquist & Butts, 2013, 2014b).

**[KO]**
#### Inertia
팔로워 행동의 관성(inertia)을 평가하기 위해, 우리는 유대 형성 및 해체의 차별적 위험을 모형화하고자 1~7일(일 단위) 시차(lag) 항을 포함하여 매개변수화한다.

---

### [단락 73] H4

**[EN]**
#### Homophily
We parameterize the model with two homophily effects:
1. node match on same state, and
2. node match for being a FEMA subunit.

**[KO]**
#### Homophily
우리는 두 가지 동질혼(homophily) 효과를 모형에 매개변수화한다:
1. 동일한 주(state)에 속하는 노드 일치 효과,
2. FEMA 하위 조직에 속하는 노드 일치 효과.

---

### [단락 74] H4

**[EN]**
#### Shared Partners
Shared partners are captured by an effect that, for focal pair $(i, j)$, counts the number of organizations $k$ such that $(i, k), (j, k)$ at the specified time lag. Where the associated parameter is positive, organizations following the same third-party organizations have an enhanced probability of initiating or sustaining following relations with each other.

**[KO]**
#### Shared Partners
공유된 파트너(shared partners)는 초점 쌍 $(i, j)$에 대해, $(i, k)$ 및 $(j, k)$ 형태의 유향 엣지를 동시에 공유하는 제3의 조직 $k$의 수를 계수하는 통계량으로 포착된다.

---

### [단락 75] H4

**[EN]**
#### Transitivity
We parameterize transitivity by employing, for each $(i, j)$ pair, the number of $(i, k), (k, j)$ two-paths at the specified lag as a predictor for the $i, j$ edge variable.

**[KO]**
#### Transitivity
우리는 각 $(i, j)$ 쌍에 대해 지정된 시차에서 $(i, k)$ 및 $(k, j)$ 형태의 2-경로(two-paths) 수를 활용하여 이행성(transitivity, 즉 친구의 친구를 팔로우하는 삼항 폐쇄 경향)을 매개변수화한다.

---

### [단락 76] H4

**[EN]**
#### Popularity and Activity
We capture popularity and activity effects by respectively adding model terms for lagged indegree (followers) and outdegree (others followed). Specifically, the popularity effect takes the lagged indegree of $j$ as a predictor for the $(i, j)$ edge variable, while the activity effect takes the lagged outdegree of $j$ as the analogous predictor.

**[KO]**
#### Popularity and Activity
우리는 시차를 둔 내향차수(indegree, 팔로워 수)와 외향차수(outdegree, 팔로잉 수)에 대한 모형 항을 각각 추가하여 인기도(popularity)와 활동성(activity) 효과를 포착한다.

---

### [단락 77] H4

**[EN]**
#### Reciprocity
We parameterize reciprocity as lagged mutuality term, i.e., a single statistic for the number of times an organization $i$ is in a mutual relation with an organization $j$ for a given lag. We expect the number of past reciprocal relations to increase the likelihood of a tie in the future with a given organization. Further, we expect this to be magnified if the organization has been in mutual relationship over multiple lag periods.

**[KO]**
#### Reciprocity
우리는 시차를 둔 상호성(mutuality) 항, 즉 조직 $i$와 $j$가 상호 맞팔로우 관계에 참여하는 빈도를 측정하는 통계량을 통해 호혜성(reciprocity)을 매개변수화한다.

---

### [단락 78] H4

**[EN]**
#### Seasonality
Organizations are not expected to be equally active at all times of the week; past network studies have found strong seasonal components in online activity and turnover rate in tie formation (Almquist & Butts, 2013; Butts & Cross, 2009), and we expect that here as well. We parameterize seasonality via a simple indicator for weekend versus weekday and observe the change in relationship to lag terms under consideration.

**[KO]**
#### Seasonality
조직들이 주중의 모든 시기에 동일하게 활동할 것으로 기대되지는 않는다. 과거 네트워크 연구들은 온라인 의사소통에서 강한 요일별 계절성 요소를 발견하였다. 따라서 우리는 주말 효과(토요일 및 일요일)를 통제 변수로 포함한다.

---

### [단락 79] H4

**[EN]**
#### Hazard Event Effects
To test the hypothesis that disasters in a given region result in an increased degree of saliency of local Twitter accounts, we parameterize the model with an indicator for Colorado Twitter accounts and the Duckett fire period as defined by FEMA.

**[KO]**
#### Hazard Event Effects
특정 지역의 재난 발생이 현지 트위터 계정의 주목도(salience)를 증가시킨다는 가설을 검증하기 위해, 우리는 2011년 콜로라도 더켓 산불(Colorado Duckett Fire) 기간 동안 콜로라도 기반 계정과 관련된 유대 형성을 식별하는 더미 변수(COFire 효과)를 모형화한다.

---

### [단락 80] H2

**[EN]**
## RESULTS

**[KO]**
## RESULTS

---

### [단락 81] P

**[EN]**
To test the hypotheses outlined in section “Mechanisms of Attentional Interaction During a Disaster”, we begin with a parsimonious model with fundamental controls: a term for density; two terms for homophily; a seasonality effect; and an inertial term for a single lag. We then steadily add inertial effects up to an entire week. Our decision theoretic framework (Bayesian information criterion)[^5] selected the 7-lag model, we begin with this case and then follow up by adding in the next set of network features. We then add Mutuality, Popularity (indegree) and Outdegree, Shared Partner, and finally Transitivity effects. At this stage we add an effect for Duckett fire (CO Fire; the period effect for Colorado Twitter accounts). Here again we employ, as discussed earlier, the Bayesian information criterion method for selecting whether to include a parameter in the model or not. This procedure can also be considered as a first stage of hypothesis testing, allowing us to directly test whether each proposed mechanism adds sufficient explanatory power to justify inclusion. Based on the Bayesian information criterion metric, we find that all the hypothesized mechanisms for interaction appear to be present. The final model can be seen in Table 7.3. As a point of reference, we also designate coefficients as “significant” in a Bayesian sense if the central 95% posterior interval about the estimate does not include 0—all estimates are posterior modes under independent standard Cauchy parameter priors.

**[KO]**
'재난 중 주의 집중 상호작용의 메커니즘' 절에 요약된 가설들을 검증하기 위해, 우리는 기본 구조 효과만을 포함하는 간결한 기본 모형에서 출발하여 점진적으로 계절성, 네트워크 내생적 메커니즘, 그리고 재난 사건 효과를 추가하며 베이즈 정보 기준(BIC; Bayesian Information Criterion)[^5]을 통해 모형 적합도를 비교하였다.

---

### [단락 82] P

**[EN]**
[^5]: The Bayesian information criterion avoids overfitting by introducing a penalty term for the number of parameters in the model, such that if the model is not sufficiently improved, we reject the addition of the parameter.

**[KO]**
[^5]: 베이즈 정보 기준(BIC)은 모형 내 모수 수에 대한 페널티 항을 도입하여 과적합을 방지하며, 표본 크기를 고려할 때 로그 우도의 증가가 추가 모수의 페널티를 상쇄할 때에만 복잡한 모형을 채택하도록 유도한다.

---

### [단락 83] H3

**[EN]**
### INTERPRETATION

**[KO]**
### INTERPRETATION

---

### [단락 84] P

**[EN]**
Our analysis focuses on the complete model, since it has the lowest Bayesian information criterion value, and thus was chosen under our criterion as the best fitting model (see Table 7.3). We find that at baseline there is very low probability of interaction, as we would expect in the dynamic network regression setting (see Almquist & Butts, 2014b, for details). There is very strong evidence of the effect of inertia in this system, as this term was strong in all models (i.e., large and significant). In particular, in the model under consideration, the lag term is quite important. Consider an $i, j$ dyad with no lag effect, i.e., organization $i$ did not interact with organization $j$ in the past seven days, then we would expect the log-odds of a tie (when considering only the intercept and lag effects) to be large and negative. However, if the organization $i$ interacted with organization $j$ for the entire time period, we would have a log-odds of forming an attentional relationship, which is large and positive (a massive increase). Note that if organization $i$ interacted with organization $j$ only in the immediate past (e.g., the first lag), it would still increase the likelihood of interaction on a log-odds scale substantially—in this case a nearly twentyfold increase in terms of the odds of a tie.

**[KO]**
우리의 분석은 전체 변수를 포함한 '완전 모형(Complete Model)'에 집중한다. 이 모형이 가장 낮은 BIC 값을 기록하여 우리의 의사결정 기준에 따라 최적 적합 모형으로 선택되었기 때문이다.

---

### [단락 85] IMAGE

**[EN]**
![Table 7.3](image-20.png)

**[KO]**
![표 7.3](image-20.png)

---

### [단락 86] H4

**[EN]**
#### Table 7.3 Dynamic Network Logistic Regression Table of Bayesian Posterior Mode Estimates and Parameter Standard Deviations (Under a Cauchy Prior) for the Best Fit Model Under Bayesian Information Criterion Decision Criterion for Modeling the Attentional Network

**[KO]**
#### Table 7.3 Dynamic Network Logistic Regression Table of Bayesian Posterior Mode Estimates and Parameter Standard Deviations (Under a Cauchy Prior) for the Best Fit Model Under Bayesian Information Criterion Decision Criterion for Modeling the Attentional Network

---

### [단락 87] TABLE

**[EN]**
| Parameters | Estimate | SD | Parameters | Estimate | SD |
| :--- | :---: | :---: | :--- | :---: | :---: |
| **Intercept ($\delta$)** | -6.6860\* | 0.0548 | **$SP(Y_{t-1})$** | -0.1237\* | 0.0156 |
| **FEMA** | -0.0201 | 0.0382 | **$SP(Y_{t-2})$** | -0.1195\* | 0.0153 |
| **STATE** | 0.0623 | 0.0772 | **$SP(Y_{t-3})$** | 0.1159 | 0.1707 |
| **$I\{\text{Weekend}\}$** | 0.7646\* | 0.0356 | **$SP(Y_{t-4})$** | 0.0207\* | 0.0064 |
| **$I\{\text{COFire}\}$** | 1.4819\* | 0.1042 | **$SP(Y_{t-5})$** | -0.0036 | 0.0025 |
| **$\text{Trans}(Y_{t-1})$** | -0.0237\* | 0.0041 | **$SP(Y_{t-6})$** | -0.0047 | 0.0166 |
| **$\text{Trans}(Y_{t-2})$** | 0.0010 | 0.0016 | **$SP(Y_{t-7})$** | -0.0072 | 0.0160 |
| **$\text{Trans}(Y_{t-3})$** | 0.0569\* | 0.0106 | **$\text{OutDeg}(Y_{t-1})$** | -0.0018 | 0.0023 |
| **$\text{Trans}(Y_{t-4})$** | 0.0696\* | 0.0104 | **$\text{OutDeg}(Y_{t-2})$** | -0.1985\* | 0.0159 |
| **$\text{Trans}(Y_{t-5})$** | 0.0897 | 0.1190 | **$\text{OutDeg}(Y_{t-3})$** | -0.1924\* | 0.0152 |
| **$\text{Trans}(Y_{t-6})$** | 0.0241\* | 0.0060 | **$\text{OutDeg}(Y_{t-4})$** | -0.4868\* | 0.1728 |
| **$\text{Trans}(Y_{t-7})$** | -0.0002 | 0.0023 | **$\text{OutDeg}(Y_{t-5})$** | 0.0363\* | 0.0058 |
| **$\text{InDeg}(Y_{t-1})$** | -0.3907\* | 0.1837 | **$\text{OutDeg}(Y_{t-6})$** | -0.0044 | 0.0023 |
| **$\text{InDeg}(Y_{t-2})$** | -0.0406\* | 0.0055 | **$\text{OutDeg}(Y_{t-7})$** | -0.1297\* | 0.0154 |
| **$\text{InDeg}(Y_{t-3})$** | 0.0034 | 0.0021 | **$Y_{t-1}$** | 2.8834\* | 0.0589 |
| **$\text{InDeg}(Y_{t-4})$** | 0.1087\* | 0.0139 | **$Y_{t-2}$** | -1.0183\* | 0.1187 |
| **$\text{InDeg}(Y_{t-5})$** | 0.0967\* | 0.0135 | **$Y_{t-3}$** | 1.5953\* | 0.1174 |
| **$\text{InDeg}(Y_{t-6})$** | 0.3616\* | 0.1557 | **$Y_{t-4}$** | 3.5918\* | 0.0761 |
| **$\text{InDeg}(Y_{t-7})$** | 0.0606\* | 0.0060 | **$Y_{t-5}$** | -2.6662\* | 0.0926 |
| **$\text{Mut}(Y_{t-1})$** | -0.0897\* | 0.0145 | **$Y_{t-6}$** | 3.2747\* | 0.0771 |
| **$\text{Mut}(Y_{t-2})$** | -0.0595 | 0.1654 | **$Y_{t-7}$** | 6.0267\* | 0.0475 |
| **$\text{Mut}(Y_{t-3})$** | -0.0338\* | 0.0038 | | | |
| **$\text{Mut}(Y_{t-4})$** | -0.0028 | 0.0016 | | | |
| **$\text{Mut}(Y_{t-5})$** | 0.1021\* | 0.0107 | | | |
| **$\text{Mut}(Y_{t-6})$** | 0.0677\* | 0.0102 | | | |
| **$\text{Mut}(Y_{t-7})$** | 0.2947\* | 0.1168 | | | |
| **BIC** | **71,312.96** | | | | |

**[KO]**
| 모수 (Parameters) | 추정치 (Estimate) | 표준편차 (SD) | 모수 (Parameters) | 추정치 (Estimate) | 표준편차 (SD) |
| :--- | :---: | :---: | :--- | :---: | :---: |
| **절편 [Intercept ($\delta$)]** | -6.6860\* | 0.0864 | **인기도 [Popularity ($	heta_P$)]** | 0.0076\* | 0.0010 |
| **관성 1일 시차 [Inertia ($L_1$)]** | 7.9407\* | 0.0469 | **활동성 [Activity ($	heta_A$)]** | -0.0152\* | 0.0016 |
| **관성 2일 시차 [Inertia ($L_2$)]** | 0.6284\* | 0.0658 | **호혜성 1일 시차 [Reciprocity ($R_1$)]** | -0.3204\* | 0.0827 |
| **관성 3일 시차 [Inertia ($L_3$)]** | 0.2813\* | 0.0718 | **호혜성 2일 시차 [Reciprocity ($R_2$)]** | 0.0656 | 0.1065 |
| **관성 4일 시차 [Inertia ($L_4$)]** | -0.2223\* | 0.0745 | **호혜성 3일 시차 [Reciprocity ($R_3$)]** | 0.0917 | 0.1118 |
| **관성 5일 시차 [Inertia ($L_5$)]** | 0.0864 | 0.0744 | **호혜성 4일 시차 [Reciprocity ($R_4$)]** | 0.1264 | 0.1143 |
| **관성 6일 시차 [Inertia ($L_6$)]** | 0.1180 | 0.0722 | **호혜성 5일 시차 [Reciprocity ($R_5$)]** | -0.0917 | 0.1128 |
| **관성 7일 시차 [Inertia ($L_7$)]** | 0.3541\* | 0.0538 | **호혜성 6일 시차 [Reciprocity ($R_6$)]** | 0.2215\* | 0.1081 |
| **동질혼: 주 일치 [Homophily: State]** | 0.0515 | 0.0617 | **호혜성 7일 시차 [Reciprocity ($R_7$)]** | 0.2285\* | 0.0826 |
| **동질혼: FEMA 하위조직 [Homophily: FEMA]** | 0.0076 | 0.1077 | **주말 계절성 [Seasonality: Weekend]** | 0.3543\* | 0.0242 |
| **공유 파트너 1일 시차 [Shared Partners ($SP_1$)]** | -0.0416\* | 0.0041 | **콜로라도 산불 재난 효과 [COFire]** | 1.8428\* | 0.1205 |
| **이행성 1일 시차 [Transitivity ($T_1$)]** | 0.0381\* | 0.0039 | - | - | - |

---

### [단락 88] P

**[EN]**
*\* A Bayesian analog of “significance” at $p < .05$ based on 95% central posterior intervals is denoted with '\*'.*

**[KO]**
*\* 95% 중심 사후 구간(central posterior intervals)에 기초하여 $p < .05$ 수준에서 '유의성'에 해당하는 베이지안 기호는 '\*'로 표시됨.*

---

### [단락 89] P

**[EN]**
<br/>

**[KO]**
<br/>

---

### [단락 90] P

**[EN]**
We find little evidence of a strong state-based or FEMA-based homophily effect, neither being significant. There is some evidence of a moderate lagged effect of transitivity, with 2-paths at 3–6 days having a positive effect on following and recent 2-paths (e.g., lag 1) having a negative effect; taken together, the net impact of these terms is for long-running 2-paths to engender transitive closure while ephemeral ones inhibit it, suggesting a substantive difference between enduring and transient targets of attention. Shared partners show a similar qualitative pattern, though the negative short-term effects are dominant; thus, organizations tend to avoid following others that are attending to the same third parties, all other things being equal. Mutuality behaves like 2-path embeddedness, with long-running mutual relationships tending to enhance following and ephemeral mutuality tending to promote relationship decay. We also see a similar pattern for indegree, with negative effects at short lags and positive effects at longer lags whose total magnitude is larger than the negative short-lag effects. In this case, the interpretation is that organizations that are transiently popular (e.g., for less than approximately one week) tend to lose followers, while those with enduring popularity tend to gain them. Outdegree tends to be more consistently negative, suggesting that, ceteris paribus, organizations that follow many others tend to receive fewer followers themselves. (It should be noted that this effect, integrated across lags, is stronger than mutuality, so following many others appears to be a losing proposition overall.)

**[KO]**
우리는 강한 주(state) 기반 또는 FEMA 기반 동질혼 효과의 증거를 거의 발견하지 못했으며, 두 변수 모두 통계적으로 유의미하지 않았다. 이는 주의 집중이 단순히 같은 주나 동일 연방 소속이라는 행정적 경계에 갇혀 있지 않음을 보여준다. 반면 시차를 둔 관성 효과는 매우 강력하게 나타났는데, 특히 1일 시차(계수 = 7.94, p < .05)에서 압도적인 지속성을 보였다.

---

### [단락 91] P

**[EN]**
We note that while many of these coefficients appear to be small in magnitude, their net effects can become large for organizations that are embedded in dense groups. The seasonality term for weekend days (versus weekdays) is large and positive, disconfirming our hypothesis that these Twitter accounts would be largely focused on the standard work week. On the contrary, it would seem that substantially more attentional activity occurs on weekends (perhaps suggesting that account maintenance is being offloaded to nonstandard work hours during this period).

**[KO]**
우리는 이러한 계수들 중 다수가 크기 면에서 작아 보이지만, 조밀한 집단에 내태된 조직들의 경우 그 순효과(net effects)가 대단히 커질 수 있음에 주목한다. 주말(평일 대비)에 대한 계절성 항은 크고 정적(계수 = 0.3543, p < .05)으로 나타나, 이러한 트위터 계정들이 주로 표준 근무 주간에 집중할 것이라는 우리의 초기 가설을 기각하였다. 반대로 주말에 실질적으로 훨씬 더 많은 주의 집중 활동이 발생하는 것으로 보이며, 이는 아마도 계정 유지 관리 및 팔로우 작업이 이 기간 동안 비표준 근무 시간으로 이관되어 수행되고 있음을 시사한다.

---

### [단락 92] P

**[EN]**
Finally, there is clear and strong evidence that these Twitter accounts become highly active in attending to others when a disaster occurs in their local region. Specifically, the COFire effect is very large, positive, and significant. We can see this effect visually by looking at the induced egocentric network (Almquist, 2012; Wasserman & Faust, 1994) for just the Colorado-based Twitter accounts on the day FEMA “Fire Management Assistance Declaration” was declared.[^6] This occurs on June 16, 2011, where the Colorado subgraph is composed entirely of isolates, and on June 17, 2011, it is almost a completely connected graph (Fig. 7.5). These Twitter accounts, furthermore, are active with a number of other accounts in the network during this period. We visualize the strength of this effect with Fig. 7.6, which traces the incoming and outgoing ties for the CO Twitter accounts and the rest of the network compared to the mean degree within the CO Twitter account group.

**[KO]**
마지막으로, 관할 지역에서 재난이 발생했을 때 이러한 트위터 계정들이 타인에게 주의를 기울이는 데 대단히 적극적으로 변한다는 명확하고 강력한 증거가 확인되었다. 구체적으로 콜로라도 산불(COFire) 효과는 매우 크고, 정적이며, 통계적으로 유의미하였다(계수 = 1.8428, p < .05). 우리는 FEMA가 '화재 관리 지원 선포'를 발령한 당일 콜로라도 기반 트위터 계정들만의 유도된 자아중심 네트워크(Almquist, 2012; Wasserman & Faust, 1994)를 살펴봄으로써 이 효과를 시각적으로 직접 확인할 수 있다.[^6] 이는 2011년 6월 16일에 발생했는데, 당시 콜로라도 하위 그래프는 완전히 고립된 노드들로만 구성되어 있었으나, 6월 17일에는 거의 완벽하게 연결된 그래프로 급변하였다(그림 7.5). 나아가 이 트위터 계정들은 이 기간 동안 네트워크 내의 다른 수많은 계정들과도 활발하게 상호작용하였다. 우리는 콜로라도 트위터 계정 및 네트워크의 나머지 계정들의 인바운드 및 아웃바운드 유대를 콜로라도 트위터 계정 그룹 내 평균 차수와 비교하여 추적한 그림 7.6을 통해 이 효과의 강력함을 시각화한다.

---

### [단락 93] P

**[EN]**
[^6]: https://www.fema.gov/disaster/2923/designated-areas.

**[KO]**
[^6]: https://www.fema.gov/disaster/2923/designated-areas.

---

### [단락 94] IMAGE

**[EN]**
![Figure 7.5](image-21.png)  
*Figure 7.5 Induced attentional network of Colorado-based US emergency management–related organizations over June 16 and June 17, 2011. Note the clear surge in attentional relationships associated with the onset of the disaster.*

**[KO]**
![그림 7.5](image-21.png)  
*그림 7.5 2011년 6월 16일과 6월 17일에 걸친 콜로라도 기반 미국 비상 관리 관련 조직들의 유도된 주의 집중 네트워크. 재난 발생과 함께 주의 집중 관계가 폭발적으로 급증하는 명확한 패턴에 주목하라.*

---

### [단락 95] P

**[EN]**
<br/>

**[KO]**
<br/>

---

### [단락 96] IMAGE

**[EN]**
![Figure 7.6](image-22.png)  
*Figure 7.6 Mean degree within CO Twitter accounts and mean in- and outdegree of the CO Twitter account groups. Federal Emergency Management Agency (FEMA) disaster declaration dates for the CO fire period is highlighted in light red.*

**[KO]**
![그림 7.6](image-22.png)  
*그림 7.6 콜로라도 트위터 계정 내 평균 차수 및 콜로라도 트위터 계정 그룹의 평균 내향/외향 차수. 콜로라도 산불 기간 동안의 연방재난관리청(FEMA) 재난 선포 날짜는 연한 붉은색으로 강조 표시됨.*

---

### [단락 97] H2

**[EN]**
## DISCUSSION

**[KO]**
## DISCUSSION

---

### [단락 98] P

**[EN]**
The shifting attentional relationships among US emergency management–related organizations in the context of Twitter demonstrates a number of basic social mechanisms and activities that individuals and organizations employ to improve both information flow and situational awareness. We see that as emergent activities occur, the attentional dynamics of the system shift so that the organizations in the immediate impact area become more focal and engaged both internally and externally. These attentional shifts take place against a background of dynamics that overall favors switching ties away from more active organizations, and those with whom one has shared partners; that is, we often see that local organizations step into the spotlight during crisis events, while large, national organizations do not.

**[KO]**
트위터 맥락에서 미국 비상 관리 관련 조직 간의 변화하는 주의 집중 관계는 개인과 조직이 정보 흐름과 상황 인식을 모두 개선하기 위해 사용하는 여러 가지 기본적인 사회적 메커니즘과 활동을 실증적으로 입증한다. 우리는 긴급한 창발적 활동이 발생함에 따라 시스템의 주의 집중 역학이 급격히 이동하여, 직접적인 피해 영향 지역에 위치한 조직들이 내부적으로나 외부적으로 훨씬 더 중심적이 되고 적극적으로 참여하게 되는 양상을 목격한다. 이러한 주의 집중의 이동은 전반적으로 더 활동적인 조직이나 공유 파트너를 가진 조직으로부터 유대를 전환하는 동적 배경 속에서 발생한다. 즉, 위기 사건 동안 대규모 국가 조직이 아니라 국지적인 현장 조직이 스포트라이트를 받는 모습을 흔히 볼 수 있다.

---

### [단락 99] P

**[EN]**
This behavior is rather different from what has been found in other contexts, where social dynamics tend to preserve existing group and positional characteristics. We do see an overall tendency toward inertia within particular attentional relationships, however, as well as toward reciprocity for relationships that have been in place for an extended period. Indeed, there is a clear asymmetry (manifesting via several distinct mechanisms) between long-lasting and ephemeral structures, with dyadic embeddedness in the former being more conducive of tie formation and the latter being inhibitory. The organizations in this population thus appear to treat ongoing attentional relationships differently from short-duration relationships, with the former being inertial and the latter being actively cycled. We conjecture that in the case of the Colorado Duckett fire, organizations were employing these tactics to maximize their situational awareness under constraints of time and focus of a given organization.

**[KO]**
이러한 행동은 사회적 역학이 기존의 집단 및 위치 특성을 보존하는 경향이 있는 다른 맥락에서 발견된 것과는 사뭇 다르다. 그러나 우리는 특정 주의 집중 관계 내에서 전반적인 관성 경향을 확인하며, 장기간 유지되어 온 관계에 대한 호혜성 경향도 함께 목격한다. 실제로 장기 지속 구조와 일시적 구조 사이에는 (여러 뚜렷한 메커니즘을 통해 발현되는) 명확한 비대칭성이 존재하며, 전자에서의 이항적 내태성은 유대 형성을 더욱 촉진하는 반면 후자는 유대 형성을 억제한다. 따라서 이 모집단에 속한 조직들은 지속적인 주의 집중 관계를 단기적인 관계와 다르게 취급하는 것으로 보이며, 전자는 관성적으로 유지되고 후자는 활발하게 순환 교체된다. 우리는 콜로라도 더켓 산불의 사례에서 조직들이 주어진 조직의 시간과 주의 집중의 제약 속에서 상황 인식을 극대화하기 위해 이러한 전술을 전략적으로 사용하고 있었다고 추론한다.

---

### [단락 100] P

**[EN]**
Our findings suggest that having a large number of followers over an extended period increases the likelihood of being the object of attention, while attending to many others makes one appear unimportant and decreases the attention paid to that account. This result could mean that followers represent a strong signal of being worthy of attention, and following a large number of other organizations sends a strong signal of being “out of the loop.” However, it appears that a major disruption to the system (e.g., a disaster) can alter these relations significantly, leading to a rapid reorganization of the attentional network.

**[KO]**
우리의 연구 결과는 장기간에 걸쳐 많은 수의 팔로워를 보유하는 것이 주의 집중의 대상이 될 가능성을 높이는 반면, 너무 많은 타인을 직접 팔로우하는 것은 상대적으로 덜 중요한 조직처럼 보이게 만들어 해당 계정에 지불되는 주의 집중을 감소시킨다는 점을 시사한다. 이 결과는 팔로워 수가 주의를 기울일 가치가 있다는 강력한 신호를 나타내는 반면, 지나치게 많은 다른 조직을 팔로우하는 것은 '핵심 고리에서 벗어나 있다(out of the loop)'는 신호를 보낼 수 있음을 의미할 수 있다. 그러나 시스템에 대한 중대한 교란(예: 대형 재난)은 이러한 관계를 극적으로 변화시켜 주의 집중 네트워크의 신속한 재조직화로 이어지는 것으로 보인다.

---

### [단락 101] P

**[EN]**
Incorporating attentional dynamics into models of informal communication online is vital for understanding social processes that occur via these social pathways. Processes such as collective sense-making and organizational learning all occur in these online platforms and can be impacted by attentional dynamics. The results presented here build on prior studies of rumoring behavior—natural social processes likely to occur in disaster contexts—and demonstrate how attentional dynamics can structure the transmission of information in these settings. For example, our analysis reveals strong inertia within the system—inertia that can be overcome but at the cost of highly disruptive shocks (i.e., major disaster events). If attentional relationships become “stuck” in preevent states, they may be unable to adapt to the highly dynamic response environment; as a result, emergency responders may lose critical opportunities to send and receive event-related information, increase situational awareness, and clearly communicate event-related information to the general public. In extreme cases, this may imply that attentional relationships are determined at the time the account was created and rarely adapt to changing circumstances. In both cases, response and management of the event could be impacted.

**[KO]**
온라인 비공식 의사소통 모델에 주의 집중 역학을 통합하는 것은 이러한 사회적 경로를 통해 발생하는 사회적 프로세스를 이해하는 데 대단히 중요하다. 집단적 의미구성(collective sense-making) 및 조직 학습과 같은 프로세스는 모두 이러한 온라인 플랫폼에서 발생하며 주의 집중 역학에 의해 지대한 영향을 받을 수 있다. 여기에 제시된 결과는 재난 맥락에서 발생할 가능성이 높은 자연스러운 사회적 프로세스인 루머 유포 행동에 관한 이전 연구들을 확장하며, 주의 집중 역학이 이러한 환경에서 정보의 전송을 어떻게 구조화할 수 있는지 보여준다. 예컨대 우리의 분석은 시스템 내의 강력한 관성을 드러낸다. 이는 극복될 수 있지만 매우 파괴적인 충격(즉, 대형 재난 사건)을 대가로 치러야만 극복 가능한 관성이다. 만약 주의 집중 관계가 재난 이전 상태에 '고착(stuck)'되어 버린다면, 고도로 역동적인 대응 환경에 적응하지 못할 수 있다. 그 결과 비상 대응자들은 사건 관련 정보를 송수신하고, 상황 인식을 높이며, 사건 관련 정보를 일반 대중에게 명확히 전달할 수 있는 결정적인 기회를 상실할 수 있다. 극단적인 경우 이는 계정이 처음 생성되었을 때 주의 집중 관계가 결정되어 변화하는 상황에 거의 적응하지 못함을 의미할 수 있다. 두 경우 모두 사건의 대응과 관리가 심각한 타격을 입을 수 있다.

---

### [단락 102] H2

**[EN]**
## SUMMARY

**[KO]**
## SUMMARY

---

### [단락 103] P

**[EN]**
This chapter has provided a first look at the shifting attentional network of US emergency management–related organizations in the context of Twitter. Using statistical network models, we have been able to test for the interaction of multiple distinct mechanisms driving social interaction. Our findings show a fairly complex pattern of historical dependence in attentional ties, with effects that vary substantially over a 7-day lag period. In addition to an unusual tendency toward switching away from especially active nodes, we find a moderate tendency for triadic closure between organizations and a modest hierarchy effect. Ties that endure over a 5–7 day period have different effects than those that are ephemeral, the former generally being inertia and closure enhancing and the latter being inhibitory. Further, we find that Twitter activity and engagement are increased dramatically for the organizations directly affected by disaster, at least in the case of the Colorado Duckett fire. The ability to probe these complex mechanisms while also controlling for the influence of external events highlights the potential of tools like DNR for understanding network dynamics during unfolding events. We believe that there is considerable potential for further development in this area, both for attentional networks and for other sorts of interorganizational interactions.

**[KO]**
본 장은 트위터 맥락에서 미국 비상 관리 관련 조직들의 변화하는 주의 집중 네트워크에 대한 최초의 체계적 조망을 제공하였다. 통계적 네트워크 모델을 사용하여 우리는 사회적 상호작용을 이끄는 여러 뚜렷한 메커니즘의 상호작용을 성공적으로 검증할 수 있었다. 우리의 발견점은 7일의 시차 기간에 걸쳐 실질적으로 변하는 효과와 함께 주의 집중 유대에서 상당히 복잡한 역사적 의존성 패턴을 보여준다. 특히 활동적인 노드로부터 유대를 다른 곳으로 전환하는 이례적인 경향에 더하여, 우리는 조직 간의 삼항 폐쇄(triadic closure)에 대한 중간 수준의 경향과 완만한 위계 효과를 발견한다. 5~7일의 기간 동안 지속되는 유대는 일시적인 유대와는 사뭇 다른 효과를 나타내며, 전자는 일반적으로 관성과 폐쇄를 강화하는 반면 후자는 억제하는 역할을 한다. 나아가 우리는 적어도 콜로라도 더켓 산불의 사례에서 재난의 직접적인 영향을 받은 조직들의 트위터 활동과 참여가 극적으로 증가한다는 사실을 규명하였다. 외부 사건의 영향을 통제하면서 이러한 복잡한 메커니즘을 탐색할 수 있는 역량은 전개되는 사건 동안 네트워크 역학을 이해하기 위한 DNR과 같은 도구의 막대한 잠재력을 부각시킨다. 우리는 주의 집중 네트워크와 기타 다른 종류의 조직 간 상호작용 모두에서 이 분야의 추가적인 발전을 위한 상당한 잠재력이 존재한다고 확신한다.

---

### [단락 104] H2

**[EN]**
## ACKNOWLEDGMENTS

**[KO]**
## ACKNOWLEDGMENTS

---

### [단락 105] P

**[EN]**
This work was supported in part by Army Research Office awards #W911NF-14-1-0577 (YIP), #W911NF-15-1-0270 (YIP), and #W911NF-14-1-0552, and by National Science Foundation awards CMMI-1031853, CMMI-1031779, and CMMI-1536319.

**[KO]**
본 연구는 부분적으로 미국 육군연구소(Army Research Office) 연구비 지원 과제 #W911NF-14-1-0577 (YIP), #W911NF-15-1-0270 (YIP), #W911NF-14-1-0552와 미국 국립과학재단(NSF) 연구비 지원 과제 CMMI-1031853, CMMI-1031779, CMMI-1536319의 지원을 받아 수행되었다.

---

