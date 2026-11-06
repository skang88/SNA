import re

with open('scratch/ch10_stage1.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Define Table 10.1 Markdown
table_10_1_md = """### Table 10.1 Communication Network Descriptive Measures

| Period | Average Indegree | Standard Deviation (in/out) | Reciprocity | Clustering |
| :--- | :---: | :---: | :---: | :---: |
| **Communication t1 (Preearthquake)** | 2.7 | 2.9 / 5.2 | 0.11 | 0.17 |
| **Communication t2 (Emergency Response)** | 9.8 | 6.8 / 13.5 | 0.15 | 0.24 |
| **Communication t3 (Disaster Recovery)** | 11.1 | 6.9 / 14.0 | 0.17 | 0.28 |

*“Communication t1” represents preearthquake period. “Communication t2” represents emergency response. “Communication t3” represents disaster recovery.*"""

# Define Table 10.2 Markdown
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

*†p < .10, \*p < .05, \*\*p < .01 (two-sided). “s.e.” stands for standard error. Coefficients from standard SIENA (4.0) analysis implemented in the R statistical system of directed network matrix. All statistics converged with t-statistic < 0.1.*"""

print("Table definitions ready.")
