import re

with open('scratch/ch10_stage1.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Clean embedded running headers that split sentences or paragraphs
text = text.replace("established a three-year time limit for\nEMERGENCE of STRUCTURAL RESILIENCE\nearthquake recovery",
                    "established a three-year time limit for earthquake recovery")

text = text.replace("ntral China) in 1556 claimed over 800,000 lives, the most in any known earthquake in human history.\nCIVIL SOCIETY THEORY IN THE CHINESE CONTExt\nCIVIL SOCIETY THEORY IN THE CHINESE CONTEXT",
                    "ntral China) in 1556 claimed over 800,000 lives, the most in any known earthquake in human history.\n\nCIVIL SOCIETY THEORY IN THE CHINESE CONTEXT")

text = text.replace("closure. From Table 10.2, we can see that the transitive triplet effect turns out to be positively\nRESULTS\nFIGURE 10.2 Disaster response communication network.\nLu, J. (2013). The Wenchuan Earthquake Response and Recovery: Social Capital and Civil Society\nOrganizational Networks. Dissertations. Paper 244.\nrelated to tie formation",
                    "closure. From Table 10.2, we can see that the transitive triplet effect turns out to be positively related to tie formation")

text = text.replace("facilitating the coordination among organizations in this sector.\nCONCLUSIONS AND POLICY IMPLICATIONS\nOverall, future research needs to further engage",
                    "facilitating the coordination among organizations in this sector.\n\nOverall, future research needs to further engage")

text = text.replace("the data collection stage.\nNETWORK BOUNDARY CLARIFICATION\nNETWORK CONTENT SPECIFICATION",
                    "the data collection stage.\n\nNETWORK CONTENT SPECIFICATION")

# Separate footnote 1 in INTRODUCTION
# "1China’s deadliest quake in Shaanxi (east-central China) in 1556 claimed over 800,000 lives, the most in any known earthquake in human history."
text = text.replace("deadliest since the 1976 Tangshan earthquake (240,000 + deaths).1",
                    "deadliest since the 1976 Tangshan earthquake (240,000+ deaths).[^1]")

fn1 = "[^1]: China’s deadliest quake in Shaanxi (east-central China) in 1556 claimed over 800,000 lives, the most in any known earthquake in human history."
text = text.replace("1China’s deadliest quake in Shaanxi (east-central China) in 1556 claimed over 800,000 lives, the most in any known earthquake in human history.", "")

# Custom paragraph joining function
def clean_and_join_paragraphs(raw_text):
    raw_lines = [l.strip() for l in raw_text.split('\n') if l.strip()]
    paragraphs = []
    curr = []
    for l in raw_lines:
        # Ignore citation under figures if standalone
        if l.startswith("Lu, J. (2013)") or l.startswith("Organizational Networks. Dissertations."):
            continue
        curr.append(l)
        # Check paragraph ending heuristic
        if len(l) < 80 and (l.endswith('.') or l.endswith(':') or l.endswith('.”') or l.endswith('."') or l.endswith(')')):
            p_text = ' '.join(curr)
            p_text = re.sub(r'\s+', ' ', p_text).strip()
            if p_text:
                paragraphs.append(p_text)
            curr = []
    if curr:
        p_text = ' '.join(curr)
        p_text = re.sub(r'\s+', ' ', p_text).strip()
        if p_text:
            paragraphs.append(p_text)
    return paragraphs

# Tables
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

# Now define sections and locate them in text
sec_defs = [
    ("INTRODUCTION", "## INTRODUCTION", "CIVIL SOCIETY THEORY IN THE CHINESE CONTEXT"),
    ("CIVIL SOCIETY THEORY IN THE CHINESE CONTEXT", "## CIVIL SOCIETY THEORY IN THE CHINESE CONTEXT", "SOCIAL NETWORKS AND DISASTERS"),
    ("SOCIAL NETWORKS AND DISASTERS", "## SOCIAL NETWORKS AND DISASTERS", "RESEARCH DESIGN"),
    ("RESEARCH DESIGN", "## RESEARCH DESIGN", "NETWORK BOUNDARY CLARIFICATION"),
    ("NETWORK BOUNDARY CLARIFICATION", "### Network Boundary Clarification", "NETWORK CONTENT SPECIFICATION"),
    ("NETWORK CONTENT SPECIFICATION", "### Network Content Specification", "THE SURVEY QUESTIONNAIRE METHOD"),
    ("THE SURVEY QUESTIONNAIRE METHOD", "### The Survey Questionnaire Method", "DATA TREATMENT"),
    ("DATA TREATMENT", "### Data Treatment", "LONGITUDINAL MODELING OF NETWORK DYNAMICS USING RSIENA"),
    ("LONGITUDINAL MODELING OF NETWORK DYNAMICS USING RSIENA", "### Longitudinal Modeling of Network Dynamics Using RSiena", "RESULTS"),
    ("RESULTS", "## RESULTS", "SOME DESCRIPTIVES"),
    ("SOME DESCRIPTIVES", "### Some Descriptives", "DYNAMICS OF THE EMERGENCY RESPONSE COMMUNICATION NETWORK"),
    ("DYNAMICS OF THE EMERGENCY RESPONSE COMMUNICATION NETWORK", "### Dynamics of the Emergency Response Communication Network", "DYNAMICS OF THE DISASTER RECOVERY COMMUNICATION NETWORK"),
    ("DYNAMICS OF THE DISASTER RECOVERY COMMUNICATION NETWORK", "### Dynamics of the Disaster Recovery Communication Network", "EMERGENCE OF STRUCTURAL RESILIENCE"),
    ("EMERGENCE OF STRUCTURAL RESILIENCE", "## EMERGENCE OF STRUCTURAL RESILIENCE", "CONCLUSIONS AND POLICY IMPLICATIONS"),
    ("CONCLUSIONS AND POLICY IMPLICATIONS", "## CONCLUSIONS AND POLICY IMPLICATIONS", None)
]

# Find start of body (first INTRODUCTION after outline)
outline_end_pos = text.find("Conclusions and Policy Implications")
body_start = text.find("INTRODUCTION", outline_end_pos + len("Conclusions and Policy Implications"))

# Extract sections
sec_contents = {}
curr_pos = body_start

for name, hdr, next_name in sec_defs:
    s_idx = text.find(name, curr_pos)
    if s_idx == -1:
        print(f"Warning: could not find {name}")
        continue
    content_start = s_idx + len(name)
    if next_name:
        next_idx = text.find(next_name, content_start)
        sec_text = text[content_start:next_idx].strip()
        curr_pos = next_idx
    else:
        sec_text = text[content_start:].strip()
    sec_contents[name] = sec_text

# Header
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

# Build document sections
for name, hdr, next_name in sec_defs:
    raw = sec_contents.get(name, "")
    
    # Handle parent headings that have no body of their own (RESEARCH DESIGN, RESULTS)
    if not raw and name in ["RESEARCH DESIGN", "RESULTS"]:
        doc += f"{hdr}\n\n"
        continue
        
    doc += f"{hdr}\n\n"
    
    if name == "INTRODUCTION":
        for p in clean_and_join_paragraphs(raw):
            doc += f"{p}\n\n"
        doc += f"{fn1}\n\n"
        doc += "---\n\n"
    elif name == "SOME DESCRIPTIVES":
        # Remove raw table 10.1 lines and figure 10.1 lines from raw
        # Figure 10.1 Preearthquake communication network.
        raw_clean = re.sub(r'Table 10\.1 Communication Network Descriptive Measures.*?“Communication t3” represents disaster recovery\.', '', raw, flags=re.DOTALL)
        raw_clean = re.sub(r'FIGURE 10\.1 Preearthquake communication network\..*?(?=As shown in Table)', '', raw_clean, flags=re.DOTALL)
        paragraphs = clean_and_join_paragraphs(raw_clean)
        # We output first paragraph (introducing Table 10.1)
        if len(paragraphs) > 0:
            doc += f"{paragraphs[0]}\n\n"
            doc += f"{table_10_1_md}\n\n"
            doc += f"*FIGURE 10.1 Preearthquake communication network.*\n\n"
            for p in paragraphs[1:]:
                doc += f"{p}\n\n"
        else:
            doc += f"{table_10_1_md}\n\n"
            doc += f"*FIGURE 10.1 Preearthquake communication network.*\n\n"
    elif name == "DYNAMICS OF THE EMERGENCY RESPONSE COMMUNICATION NETWORK":
        # Remove raw table 10.2 text
        raw_clean = re.sub(r'Table 10\.2 Rules Governing Emergency Response.*?model selection process\.', '', raw, flags=re.DOTALL)
        raw_clean = re.sub(r'FIGURE 10\.2 Disaster response communication network\.', '', raw_clean)
        paragraphs = clean_and_join_paragraphs(raw_clean)
        for i, p in enumerate(paragraphs):
            doc += f"{p}\n\n"
            if i == 0:
                doc += f"*FIGURE 10.2 Disaster response communication network.*\n\n"
                doc += f"{table_10_2_md}\n\n"
    elif name == "DYNAMICS OF THE DISASTER RECOVERY COMMUNICATION NETWORK":
        raw_clean = re.sub(r'FIGURE 10\.3 Disaster recovery communication network\.', '', raw)
        paragraphs = clean_and_join_paragraphs(raw_clean)
        doc += f"*FIGURE 10.3 Disaster recovery communication network.*\n\n"
        for p in paragraphs:
            doc += f"{p}\n\n"
    else:
        for p in clean_and_join_paragraphs(raw):
            doc += f"{p}\n\n"
            
    # Add separator if it's a major section
    if hdr.startswith("## ") and name not in ["RESEARCH DESIGN", "RESULTS"]:
        doc += "---\n\n"

with open('subnote/chapter10-원문.md', 'w', encoding='utf-8') as f:
    f.write(doc)

print("Final Chapter 10 successfully generated!")
