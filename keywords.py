# Sample text containing IEEE Keywords and Author Keywords
text = """
IEEE Keywords
Feature extraction
,
Data mining
,
Natural languages
,
Training
,
Python
,
Java
,
Data models
INSPEC: Controlled Indexing
data mining
,
Java
,
learning (artificial intelligence)
,
natural languages
,
neural nets
,
software engineering
,
source code (software)
INSPEC: Non-Controlled Indexing
code synthesis
,
code retrieval
,
code summarization
,
data-driven models
,
parallel data
,
stack overflow
,
heuristic methods
,
NL-code pairs
,
high-quality aligned data
,
neural network model
,
mining methods
,
parallel natural language
,
source code corpora
,
Python
,
Java
Author Keywords
Code Mining
,
Stack Overflow
,
Neural Networks
,
Bimodal Modeling
"""

# Initialize variables to store IEEE Keywords and Author Keywords
ieee_keywords = []
author_keywords = []

# Split the text into lines
lines = text.split("\n")

# Initialize a flag to determine when to collect keywords
collect_keywords = False

# Iterate through the lines to collect keywords
for line in lines:
    line = line.strip()
    
    # Check if the line indicates the start of IEEE Keywords or Author Keywords section
    if line == "IEEE Keywords":
        collect_keywords = True
    elif line == "Author Keywords":
        collect_keywords = False
    
    # Collect keywords if the flag is set
    if collect_keywords and line:
        keywords = line.split(",")
        keywords = [keyword.strip() for keyword in keywords]
        
        if keywords:
            ieee_keywords.extend(keywords)

# Print the extracted IEEE Keywords and Author Keywords
print("IEEE Keywords:", ieee_keywords)
print("Author Keywords:", author_keywords)
