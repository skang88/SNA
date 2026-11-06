import re

with open('scratch/ch10_stage1.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Custom paragraph joining function
def smart_join_paragraphs(text_block):
    # Remove figure captions or table references embedded in text if handled separately
    lines = [l.strip() for l in text_block.split('\n') if l.strip()]
    paragraphs = []
    current_p = []
    
    for l in lines:
        # Check if line is a figure caption or metadata
        if l.startswith('Lu, J. (2013)') or l.startswith('Dissertations.'):
            continue
        current_p.append(l)
        if len(l) < 82 and (l.endswith('.') or l.endswith(':') or l.endswith('.”') or l.endswith('."') or l.endswith(')')):
            p_text = ' '.join(current_p)
            # clean up multiple spaces
            p_text = re.sub(r'\s+', ' ', p_text)
            paragraphs.append(p_text)
            current_p = []
    if current_p:
        p_text = re.sub(r'\s+', ' ', ' '.join(current_p))
        paragraphs.append(p_text)
    return paragraphs

# Sections definition with exact ranges
sec_ranges = [
    ("INTRODUCTION", 2278 + len("INTRODUCTION"), 7218, "## INTRODUCTION"),
    ("CIVIL SOCIETY THEORY IN THE CHINESE CONTEXT", 7218 + len("CIVIL SOCIETY THEORY IN THE CHINESE CONTEXT"), 16209, "## CIVIL SOCIETY THEORY IN THE CHINESE CONTEXT"),
    ("SOCIAL NETWORKS AND DISASTERS", 16209 + len("SOCIAL NETWORKS AND DISASTERS"), 19099, "## SOCIAL NETWORKS AND DISASTERS"),
    ("RESEARCH DESIGN", 19099 + len("RESEARCH DESIGN"), 19115, "## RESEARCH DESIGN"),
    ("NETWORK BOUNDARY CLARIFICATION", 19115 + len("NETWORK BOUNDARY CLARIFICATION"), 19992, "### Network Boundary Clarification"),
    ("NETWORK CONTENT SPECIFICATION", 19992 + len("NETWORK CONTENT SPECIFICATION"), 20986, "### Network Content Specification"),
    ("THE SURVEY QUESTIONNAIRE METHOD", 20986 + len("THE SURVEY QUESTIONNAIRE METHOD"), 22458, "### The Survey Questionnaire Method"),
    ("DATA TREATMENT", 22458 + len("DATA TREATMENT"), 25400, "### Data Treatment"),
    ("LONGITUDINAL MODELING OF NETWORK DYNAMICS USING RSIENA", 25400 + len("LONGITUDINAL MODELING OF NETWORK DYNAMICS USING RSIENA"), 31442, "### Longitudinal Modeling of Network Dynamics Using RSiena"),
    ("RESULTS", 31442 + len("RESULTS"), 31450, "## RESULTS"),
    ("SOME DESCRIPTIVES", 31450 + len("SOME DESCRIPTIVES"), 33266, "### Some Descriptives"),
    ("DYNAMICS OF THE EMERGENCY RESPONSE COMMUNICATION NETWORK", 33266 + len("DYNAMICS OF THE EMERGENCY RESPONSE COMMUNICATION NETWORK"), 42869, "### Dynamics of the Emergency Response Communication Network"),
    ("DYNAMICS OF THE DISASTER RECOVERY COMMUNICATION NETWORK", 42869 + len("DYNAMICS OF THE DISASTER RECOVERY COMMUNICATION NETWORK"), 47357, "### Dynamics of the Disaster Recovery Communication Network"),
    ("EMERGENCE OF STRUCTURAL RESILIENCE", 47357 + len("EMERGENCE OF STRUCTURAL RESILIENCE"), 50758, "## EMERGENCE OF STRUCTURAL RESILIENCE"),
    ("CONCLUSIONS AND POLICY IMPLICATIONS", 50758 + len("CONCLUSIONS AND POLICY IMPLICATIONS"), len(text), "## CONCLUSIONS AND POLICY IMPLICATIONS")
]

# Table 10.1 & 10.2 definitions
table_10_1_md = """### Table 10.1 Communication Network Descriptive Measures

| Period | Average Indegree | Standard Deviation (in/out) | Reciprocity | Clustering |
| :--- | :---: | :---: | :---: | :---: |
| **Communication t1 (Preearthquake)** | 2.7 | 2.9 / 5.2 | 0.11 | 0.17 |
| **Communication t2 (Emergency Response)** | 9.8 | 6.8 / 13.5 | 0.15 | 0.24 |
| **Communication t3 (Disaster Recovery)** | 11.1 | 6.9 / 14.0 | 0.17 | 0.28 |

*“Communication t1” represents preearthquake period. “Communication t2” represents emergency response. “Communication t3” represents disaster recovery.*"""

table_10_2_md = """### Table 10.2 Rules Governing Emergency Response and Recovery Periods Communication Network Evolution

| Effect | Response (t1–t2: Pre-Disaster to Response)<br/>Parameter Estimate (s.e.) | Recovery (t2–t3: Response to Recovery)<br/>Parameter Estimate (s.e.) |
| :--- | :---: | :---: |
| **Within Network** | | |
| - Outdegree | −3.30** (0.18) | −4.18** (0.69) |
| - Reciprocity | 0.41† (0.23) | 0.91** (0.17) |
| - Transitive triplets | 0.11** (0.04) | 0.08* (0.05) |
| - Three cycles | −0.12 (0.07) | 0.01 (0.35) |
| - Transitive ties | −0.89** (0.21) | 1.01** (0.01) |
| - Balance | −0.09** (0.01) | −0.01 (0.06) |
| - Indegree popularity (Sqrt) | 0.93** (0.07) | 0.43** (0.12) |
| - Outdegree popularity (Sqrt) | −0.17* (0.08) | −0.29* (0.13) |
| - Outdegree activity (Sqrt) | – (–) | 0.15 (0.27) |
| **Registration** | | |
| - Int. Registration similarity × reciprocity | −1.39** (0.40) | −0.48† (0.13) |
| - Registration alter | – (–) | −0.06 (0.12) |
| - Registration ego | – (–) | 0.41** (0.25) |
| - Registration ego × registration alter | – (–) | 0.12 (0.11) |
| **Activity** | | |
| - Housing alter | – (–) | −0.07 (0.12) |
| - Housing ego | – (–) | 0.03 (0.13) |
| - Housing ego × housing alter | – (–) | −0.28* (0.31) |
| - Elderly_disabled alter | – (–) | 0.84** (0.11) |
| - Elderly_disabled ego | – (–) | 0.00 (0.11) |
| - Elderly_disabled ego × Elderly_disabled alter | – (–) | −0.22† (0.22) |
| - Women_children alter | – (–) | 0.14 (0.15) |
| - Women_children ego | – (–) | 0.06 (0.15) |
| - Women_children ego × Women_children alter | – (–) | 0.74** (0.22) |
| - Environment alter | – (–) | 0.18 (0.11) |
| - Environment ego | – (–) | −0.10 (0.15) |
| - Environment ego × environment alter | – (–) | −0.50** (0.23) |
| - Psychology alter | – (–) | 0.31 (0.13) |
| - Psychology ego | – (–) | −0.16 (0.12) |
| - Psychology ego × psychology alter | – (–) | 0.40** (0.23) |
| - Livelihood alter | – (–) | 0.33 (0.12) |
| - Livelihood ego | – (–) | 0.17 (0.14) |
| - Livelihood ego × livelihood alter | – (–) | −0.02 (0.22) |

*†p < .10, \*p < .05, \*\*p < .01 (two-sided). “s.e.” stands for standard error. Coefficients from standard SIENA (4.0) analysis implemented in the R statistical system of directed network matrix. All statistics converged with t-statistic < 0.1. The use of dashed lines in certain cells indicates that the variable was dropped due to insignificance during the model selection process.*"""

# Build document
doc = """# CHAPTER 10. INTERORGANIZATIONAL NETWORK DYNAMICS IN THE WENCHUAN EARTHQUAKE RECOVERY

**Jia Lu**<sup>1,2</sup>  
<sup>1</sup> *California State University-Los Angeles, Los Angeles, CA, United States*  
<sup>2</sup> *University of Southern California, Los Angeles, CA, United States*  

*Social Network Analysis of Disaster Response, Recovery, and Adaptation.* http://dx.doi.org/10.1016/B978-0-12-805196-2.00010-8  
Copyright © 2017 Elsevier Inc. All rights reserved.

---

## CHAPTER OUTLINE

- **Introduction**
- **Civil Society Theory in the Chinese Context**
- **Social Networks and Disasters**
- **Research Design**
  - Network Boundary Clarification
  - Network Content Specification
  - The Survey Questionnaire Method
  - Data Treatment
  - Longitudinal Modeling of Network Dynamics Using RSiena
- **Results**
  - Some Descriptives
  - Dynamics of the Emergency Response Communication Network
  - Dynamics of the Disaster Recovery Communication Network
- **Emergence of Structural Resilience**
- **Conclusions and Policy Implications**

---

"""

for name, s, e, hdr in sec_ranges:
    raw_sec = text[s:e].strip()
    if not raw_sec:
        continue
    
    doc += f"{hdr}\n\n"
    
    # Specific handling for sections with tables and figures
    if name == "SOME DESCRIPTIVES":
        # Extract text before table 10.1
        t1_idx = raw_sec.find("Table 10.1 Communication Network")
        if t1_idx != -1:
            p_before = raw_sec[:t1_idx]
            for p in smart_join_paragraphs(p_before):
                doc += f"{p}\n\n"
            doc += f"{table_10_1_md}\n\n"
            doc += f"*FIGURE 10.1 Preearthquake communication network.*\n\n"
        else:
            for p in smart_join_paragraphs(raw_sec):
                doc += f"{p}\n\n"
    elif name == "DYNAMICS OF THE EMERGENCY RESPONSE COMMUNICATION NETWORK":
        t2_idx = raw_sec.find("Table 10.2 Rules Governing")
        p_before = raw_sec[:t2_idx] if t2_idx != -1 else raw_sec
        # check if FIGURE 10.2 mentioned
        p_list = smart_join_paragraphs(p_before)
        for p in p_list:
            doc += f"{p}\n\n"
            if "FIGURE 10.2" in p:
                doc += f"*FIGURE 10.2 Disaster response communication network.*\n\n"
        if t2_idx != -1:
            doc += f"{table_10_2_md}\n\n"
            # text after table 10.2
            t2_end = raw_sec.find("counterintuitive because", t2_idx)
            if t2_end != -1:
                p_after = raw_sec[t2_end:]
                for p in smart_join_paragraphs(p_after):
                    doc += f"{p}\n\n"
    elif name == "DYNAMICS OF THE DISASTER RECOVERY COMMUNICATION NETWORK":
        for p in smart_join_paragraphs(raw_sec):
            doc += f"{p}\n\n"
        doc += f"*FIGURE 10.3 Disaster recovery communication network.*\n\n"
    else:
        for p in smart_join_paragraphs(raw_sec):
            doc += f"{p}\n\n"
            
    doc += "---\n\n"

with open('subnote/chapter10-원문.md', 'w', encoding='utf-8') as f:
    f.write(doc)

print("Chapter 10 successfully rebuilt as markdown!")
