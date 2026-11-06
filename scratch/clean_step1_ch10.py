import re

with open('subnote/chapter10-원문.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Clean header/footer artifacts
# Remove Elsevier header
text = re.sub(r'Social Network Analysis of Disaster Response, Recovery, and Adaptation\.\s+http://dx\.doi\.org/10\.1016/B978-0-12-805196-2\.00010-8\s+Copyright © 2017 Elsevier Inc\. All rights reserved\.', '', text)

# Remove running page numbers and headers
patterns_to_remove = [
    r'\n\d{3}\s*\nCHAPTER 10 INTERORGANIZATIONAL NETWORK DYNAMICS\s*\n',
    r'\nCHAPTER 10 INTERORGANIZATIONAL NETWORK DYNAMICS\s*\n\d{3}\s*\n',
    r'\n\d{3}\s*\n', # standalone 3-digit page numbers
    r'\nRESEARCH DESIGN\s*\n(?=[a-z])', # running header before lowercase continuation
    r'\nRESULTS\s*\n(?=[a-z])',
    r'\nCONCLUSIONS AND POLICY IMPLICATIONS\s*\n(?=[a-z])',
    r'\nCIVIL SOCIETY THEORY IN THE CHINESE CONTEXT\s*\n(?=[a-z])',
]
for p in patterns_to_remove:
    text = re.sub(p, '\n', text)

# Join hyphenated words across lines (e.g., "coun-\ntry" -> "country")
text = re.sub(r'(\b[a-zA-Z]+)-\n([a-zA-Z]+\b)', r'\1\2', text)

# Save intermediate cleaned text
with open('scratch/ch10_stage1.txt', 'w', encoding='utf-8') as f:
    f.write(text)

print("Stage 1 cleaning done. Saved to scratch/ch10_stage1.txt")
