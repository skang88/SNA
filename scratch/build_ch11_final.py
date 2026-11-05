import re

# Read current chapter11-원문.md to get the full methodology body and existing clean intro/theory/canterbury
with open('subnote/chapter11-원문.md', 'r', encoding='utf-8') as f:
    full_text = f.read()

# Extract the big body from METHODOLOGY
m = re.search(r'## METHODOLOGY\n\n(.*?)(?=### Case Study Selection)', full_text, re.DOTALL)
meth_body = m.group(1).replace('\xad', '')

# Extract earlier parts
intro_part = re.search(r'## INTRODUCTION\n\n(.*?)(?=---|\n## THEORETICAL FRAMEWORK)', full_text, re.DOTALL).group(1).strip()
theory_part = re.search(r'## THEORETICAL FRAMEWORK\n\n(.*?)(?=---|\n## THE CANTERBURY EARTHQUAKE SEQUENCE)', full_text, re.DOTALL).group(1).strip()
canterbury_part = re.search(r'## THE CANTERBURY EARTHQUAKE SEQUENCE\n\n(.*?)(?=---|\n## METHODOLOGY)', full_text, re.DOTALL).group(1).strip()

# Clean and split paragraphs function
def clean_paragraphs(text_block):
    lines = [l.strip() for l in text_block.split('\n') if l.strip()]
    paragraphs = []
    curr = []
    for l in lines:
        curr.append(l)
        if len(l) < 80 and (l.endswith('.') or l.endswith(':') or l.endswith('.”') or l.endswith('."') or l.endswith(')')):
            p_text = re.sub(r'\s+', ' ', ' '.join(curr)).strip()
            if p_text:
                paragraphs.append(p_text)
            curr = []
    if curr:
        p_text = re.sub(r'\s+', ' ', ' '.join(curr)).strip()
        if p_text:
            paragraphs.append(p_text)
    return paragraphs

# Define markers in meth_body
markers = [
    ("CASE STUDY SELECTION", "### Case Study Selection"),
    ("DOCUMENTING THE CASE STUDIES’ JOURNEYS", "### Documenting the Case Studies’ Journeys"),
    ("NETWORK DATA COLLECTION", "### Network Data Collection"),
    ("FINDINGS", "## FINDINGS"),
    ("TYPES OF SUPPORT ORGANIZATIONS ACCESSED TO AID RECOVERY", "### Types of Support Organizations Accessed to Aid Recovery"),
    ("THE RELATIONSHIPS THAT MAKE UP SUPPORT NETWORKS", "### The Relationships That Make Up Support Networks"),
    ("POSTEARTHQUAKE NETWORKING BEHAVIORS", "### Postearthquake Networking Behaviors"),
    ("ASSESSING ORGANIZATIONAL PERFORMANCE", "#### Assessing Organizational Performance"),
    ("Sensors in the Community", "#### Sensors in the Community"),
    ("Trust and Decision Evaluation", "#### Trust and Decision Evaluation"),
    ("Network Density and Understanding Connectivity", "#### Network Density and Understanding Connectivity"),
    ("Managing Reciprocity", "#### Managing Reciprocity"),
    ("Devolved Responsibilities", "#### Devolved Responsibilities"),
    ("DISCUSSION AND CONCLUSIONS", "## DISCUSSION AND CONCLUSIONS"),
    ("RELATIONAL RESILIENCE", "### Relational Resilience"),
    ("FUTURE WORK AND IMPLICATIONS", "### Future Work and Implications")
]

# Find indices of all markers in meth_body
slice_points = []
for token, heading in markers:
    idx = meth_body.find(token)
    if idx == -1:
        print(f"ERROR: Token '{token}' not found!")
    slice_points.append((idx, token, heading))

# Sort by index
slice_points.sort(key=lambda x: x[0])

sections_dict = {}
for i in range(len(slice_points)):
    idx, token, heading = slice_points[i]
    start = idx + len(token)
    if i + 1 < len(slice_points):
        end = slice_points[i+1][0]
    else:
        end = len(meth_body)
    raw_content = meth_body[start:end].strip()
    sections_dict[heading] = raw_content

# Tables definition
table_11_1_md = """### Table 11.1 Types of Support Organizations Accessed Following the Earthquakes

| Type of Support | Description | Proportion of All Received Support (%) |
| :--- | :--- | :---: |
| **Services, assistance, and labor provided to the organization** | Retail shop assistance, construction, doing taxes, assisting with relocation, cleaning | 37 |
| **Support given to aid emotional coping of people within the organization** | “Checking in,” sympathy, supportive emails or calls | 31 |
| **Monetary/financial support given to the organization or staff** | Loans, donations, grants, purchasing from participant organization, insurance payouts, employee wage subsidies, bank overdrafts, debt forgiveness, credit, discounts | 30 |
| **Nonmonetary material resources** | Accommodations, storage space, vehicles, equipment, furnishings, office supplies, food/drinks, staff housing | 25 |
| **Advice or information offered to the organization** | Business mentoring; legal/financial advice; where to apply for aid | 23 |
| **Social influence exerted by the tie** | Brokerage, ie, bridging (socially “horizontal”) or linking (socially “vertical”) the organization to a wider range of people/organizations. Also included advocacy for the organization. | 10 |

*Note: Across the organizations, participants reported receiving a range of support types, and these were coded into six categories. Each supporter could provide between one and six types of support.*"""

table_11_2_md = """### Table 11.2 Network Relationship Attributes

| Attribute | % of Supporters |
| :--- | :---: |
| **Location of supporter (n = 372)** | |
| - Within Canterbury | > 70% |
| - Outside Canterbury | < 30% |
| **Duration of relationship with supporter (n = 372)** | |
| - More than 10 years | ~47% |
| - Formed at least a year before earthquakes | > 80% |
| - New / No prior interaction before earthquakes | ~17% |
| **Role of supporter (n = 457)** | |
| - Suppliers of goods and services | Most common source |
| - Government agencies & Community groups | Common source |
| - Friends and Family members | Common source |

*Note: Data derived from participant-aided sociograms across 32 case study organizations. Each network member could provide between one and six types of support.*"""

# Now assemble full markdown document
doc = """# CHAPTER 11. ORGANIZATIONAL SUPPORT NETWORKS AND RELATIONAL RESILIENCE AFTER THE 2010/11 EARTHQUAKES IN CANTERBURY, NEW ZEALAND

**Joanne R. Stevenson**<sup>1,2</sup>, **David Conradson**<sup>2</sup>  
<sup>1</sup> *Resilient Organisations Ltd., Sheffield, New Zealand*  
<sup>2</sup> *University of Canterbury, Christchurch, New Zealand*  

*Social Network Analysis of Disaster Response, Recovery, and Adaptation.* http://dx.doi.org/10.1016/B978-0-12-805196-2.00011-X  
Copyright © 2017 Elsevier Inc. All rights reserved.

---

## CHAPTER OUTLINE

- **Introduction**
- **Theoretical Framework**
- **The Canterbury Earthquake Sequence**
- **Methodology**
  - Case Study Selection
  - Documenting the Case Studies’ Journeys
  - Network Data Collection
- **Findings**
  - Types of Support Organizations Accessed to Aid Recovery
  - The Relationships That Make Up Support Networks
  - Postearthquake Networking Behaviors
    - Assessing Organizational Performance
    - Sensors in the Community
    - Trust and Decision Evaluation
    - Network Density and Understanding Connectivity
    - Managing Reciprocity
    - Devolved Responsibilities
- **Discussion and Conclusions**
  - Relational Resilience
  - Future Work and Implications

---

## INTRODUCTION

"""

for p in clean_paragraphs(intro_part):
    # bullet format if needed for research questions
    if "What kinds of support did organizations mobilize" in p:
        p = p.replace("• What kinds of support did organizations mobilize post disaster to aid their recovery? • What kinds of relationships comprised postdisaster support networks? • In what ways do the networking behaviors of organizations experiencing positive postdisaster trajectories differ from those with degenerative trajectories?",
                      "\n\n- What kinds of support did organizations mobilize post disaster to aid their recovery?\n- What kinds of relationships comprised postdisaster support networks?\n- In what ways do the networking behaviors of organizations experiencing positive postdisaster trajectories differ from those with degenerative trajectories?\n\n")
    doc += f"{p}\n\n"

doc += "---\n\n## THEORETICAL FRAMEWORK\n\n"
for p in clean_paragraphs(theory_part):
    doc += f"{p}\n\n"

doc += "---\n\n## THE CANTERBURY EARTHQUAKE SEQUENCE\n\n"
canterbury_paras = clean_paragraphs(canterbury_part)
for i, p in enumerate(canterbury_paras):
    doc += f"{p}\n\n"
    if i == 0:
        doc += "*FIGURE 11.1 Canterbury earthquake sequence 2010/2011.*\n*Source: GeoNet (2011). Canterbury quakes. Retrieved from http://info.geonet.org.nz/display/home/Canterbury+Quakes.*\n\n"

doc += "---\n\n## METHODOLOGY\n\n"

# Methodology subsections
for h in ["### Case Study Selection", "### Documenting the Case Studies’ Journeys", "### Network Data Collection"]:
    doc += f"{h}\n\n"
    raw_s = sections_dict.get(h, "")
    if h == "### Network Data Collection":
        raw_s = re.sub(r'FIGURE 11\.2.*?\(network data collection tool\)\.', '', raw_s, flags=re.DOTALL)
        raw_s = re.sub(r'work\s*\(ie responding organization\)\s*Least important', '', raw_s)
        doc += "*FIGURE 11.2 Schematic diagram of participant-aided sociogram (network data collection tool).*\n\n"
    for p in clean_paragraphs(raw_s):
        doc += f"{p}\n\n"

doc += "---\n\n## FINDINGS\n\n"

# Findings subsections
findings_subsections = [
    "### Types of Support Organizations Accessed to Aid Recovery",
    "### The Relationships That Make Up Support Networks",
    "### Postearthquake Networking Behaviors",
    "#### Assessing Organizational Performance",
    "#### Sensors in the Community",
    "#### Trust and Decision Evaluation",
    "#### Network Density and Understanding Connectivity",
    "#### Managing Reciprocity",
    "#### Devolved Responsibilities"
]

for h in findings_subsections:
    doc += f"{h}\n\n"
    raw_s = sections_dict.get(h, "")
    
    if h == "### Types of Support Organizations Accessed to Aid Recovery":
        raw_s = re.sub(r'Table 11\.1 Types of Support Organizations Accessed.*?Proportion of All Received Support.*?10', '', raw_s, flags=re.DOTALL)
        doc += f"{table_11_1_md}\n\n"
    elif h == "### The Relationships That Make Up Support Networks":
        raw_s = re.sub(r'Table 11\.2 Network Relationship Attributes\s*Attribute % of Supporters.*?Role of supporter \( n\s*=\s*457\)', '', raw_s, flags=re.DOTALL)
        paras = clean_paragraphs(raw_s)
        if len(paras) > 1:
            doc += f"{paras[0]}\n\n{paras[1]}\n\n{table_11_2_md}\n\n"
            for p in paras[2:]:
                doc += f"{p}\n\n"
            continue
    elif h == "#### Assessing Organizational Performance":
        raw_s = re.sub(r'FIGURE 11\.3.*?degenerative trajectories\.', '', raw_s, flags=re.DOTALL)
        raw_s = re.sub(r'2009 2010 2011 2012 2007 2008 2009 2010 2011 2012\s*Excellent\s*Above\s*average\s*Average\s*Below\s*average\s*Poor', '', raw_s)
        doc += "*FIGURE 11.3 Representative drawings made by case study organization participants of their financial performance before and after the 2010/2011 earthquakes. Examples of (A) developmental change, (B) recovery to pre-earthquake trends, and (C) degenerative trajectories.*\n\n"
    elif h == "#### Managing Reciprocity":
        raw_s = re.sub(r'FIGURE 11\.4\s+Percent of support reciprocated by trajectory group\.', '', raw_s)
        raw_s = re.sub(r'to\s*Pre-EQ Trends\s*Trajectory\s*Developmental\s*Change', '', raw_s)
        paras = clean_paragraphs(raw_s)
        if len(paras) > 1:
            doc += f"{paras[0]}\n\n*FIGURE 11.4 Percent of support reciprocated by trajectory group.*\n\n"
            for p in paras[1:]:
                doc += f"{p}\n\n"
            continue

    for p in clean_paragraphs(raw_s):
        doc += f"{p}\n\n"

doc += "---\n\n## DISCUSSION AND CONCLUSIONS\n\n"

for h in ["### Relational Resilience", "### Future Work and Implications"]:
    doc += f"{h}\n\n"
    raw_s = sections_dict.get(h, "")
    for p in clean_paragraphs(raw_s):
        doc += f"{p}\n\n"

# Footnotes
fn4 = "[^1]: To be reported on the sociogram, “support,” in the participant’s opinion, had to have aided their organization’s response and recovery at some point between September 2010 and mid-2012."
fn5 = "[^2]: Each network member could provide between one and six types of support. Cross-tabulation and chi-squared analyses were run for each support type separately."

doc += f"---\n\n### FOOTNOTES\n\n{fn4}\n\n{fn5}\n"

with open('subnote/chapter11-원문.md', 'w', encoding='utf-8') as f:
    f.write(doc)

print("Chapter 11 rebuilt successfully with all sections populated!")
