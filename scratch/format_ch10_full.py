import re

with open('scratch/ch10_stage1.txt', 'r', encoding='utf-8') as f:
    raw = f.read()

# Custom paragraph joining function
def smart_join_paragraphs(text_block):
    lines = [l.strip() for l in text_block.split('\n') if l.strip()]
    paragraphs = []
    current_p = []
    
    for l in lines:
        current_p.append(l)
        # If line ends with period/colon/quote and is shorter than standard column width (e.g. < 82 chars)
        if len(l) < 82 and (l.endswith('.') or l.endswith(':') or l.endswith('.”') or l.endswith('."') or l.endswith(')')):
            paragraphs.append(' '.join(current_p))
            current_p = []
    if current_p:
        paragraphs.append(' '.join(current_p))
    return paragraphs

# Split into main sections
sections_dict = {}

# Outline
outline_md = """## CHAPTER OUTLINE

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
- **Conclusions and Policy Implications**"""

print("Helper ready")
