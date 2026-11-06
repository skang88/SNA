import re

with open('scratch/ch10_stage1.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Headers to split
headers = [
    ("INTRODUCTION", "## INTRODUCTION"),
    ("CIVIL SOCIETY THEORY IN THE CHINESE CONTEXT", "## CIVIL SOCIETY THEORY IN THE CHINESE CONTEXT"),
    ("SOCIAL NETWORKS AND DISASTERS", "## SOCIAL NETWORKS AND DISASTERS"),
    ("RESEARCH DESIGN", "## RESEARCH DESIGN"),
    ("NETWORK BOUNDARY CLARIFICATION", "### Network Boundary Clarification"),
    ("NETWORK CONTENT SPECIFICATION", "### Network Content Specification"),
    ("THE SURVEY QUESTIONNAIRE METHOD", "### The Survey Questionnaire Method"),
    ("DATA TREATMENT", "### Data Treatment"),
    ("LONGITUDINAL MODELING OF NETWORK DYNAMICS USING RSIENA", "### Longitudinal Modeling of Network Dynamics Using RSiena"),
    ("RESULTS", "## RESULTS"),
    ("SOME DESCRIPTIVES", "### Some Descriptives"),
    ("DYNAMICS OF THE EMERGENCY RESPONSE COMMUNICATION NETWORK", "### Dynamics of the Emergency Response Communication Network"),
    ("DYNAMICS OF THE DISASTER RECOVERY COMMUNICATION NETWORK", "### Dynamics of the Disaster Recovery Communication Network"),
    ("EMERGENCE OF STRUCTURAL RESILIENCE", "## EMERGENCE OF STRUCTURAL RESILIENCE"),
    ("CONCLUSIONS AND POLICY IMPLICATIONS", "## CONCLUSIONS AND POLICY IMPLICATIONS")
]

# Find positions
positions = []
for title, md_hdr in headers:
    pos = text.find(title + "\n")
    if pos == -1:
        # try without newline
        pos = text.find(title)
    # Avoid matching in outline
    if pos < 1500:
        pos = text.find(title + "\n", 1500)
    positions.append((pos, title, md_hdr))

positions.sort()
for p in positions:
    print(f"Pos {p[0]}: {p[1]}")
