import re

with open('subnote/chapter10-원문.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove running headers and footers
# e.g., 'CHAPTER 10 INTERORGANIZATIONAL NETWORK DYNAMICS', 'Social Network Analysis of Disaster Response, Recovery, and Adaptation. http://dx.doi.org/10.1016/B978-0-12-805196-2.00010-8', 'Copyright © 2017 Elsevier Inc. All rights reserved.', page numbers like '143', '144'
text = re.sub(r'Social Network Analysis of Disaster Response, Recovery, and Adaptation\.\s+http://dx\.doi\.org/10\.1016/B978-0-12-805196-2\.00010-8\s+Copyright © 2017 Elsevier Inc\. All rights reserved\.\s+143', '', text)

# Remove running page numbers and headers
text = re.sub(r'\n\d{3}\s*\nCHAPTER 10 INTERORGANIZATIONAL NETWORK DYNAMICS\s*\n', '\n\n', text)
text = re.sub(r'\nCHAPTER 10 INTERORGANIZATIONAL NETWORK DYNAMICS\s*\n\d{3}\s*\n', '\n\n', text)
text = re.sub(r'\n[A-Z\s]{4,}\s*\n\d{3}\s*\n', '\n\n', text)

# Remove hyphenation at line breaks: e.g. "coun-\ntry" -> "country"
text = re.sub(r'(\b[a-zA-Z]+)-\n([a-zA-Z]+\b)', r'\1\2', text)

print("Pre-cleaning done")
