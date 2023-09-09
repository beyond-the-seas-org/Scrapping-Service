# Sample text
text = """
Conferences >ICASSP 2020 - 2020 IEEE Inter...
Universal Phone Recognition with a Multilingual Allophone System
Publisher: IEEE
Cite This
PDF
Xinjian Li; Siddharth Dalmia; Juncheng Li; Matthew Lee; Patrick Littell
All Authors
27
Cites in
Papers
610
Full
Text Views
Abstract
Document Sections
1.
INTRODUCTION
2.
RELATED WORK
3.
APPROACH
4.
EXPERIMENTS
5.
CONCLUSION
Authors
Figures
References
Citations
Keywords
Metrics
Footnotes
Abstract:
Multilingual models can improve language processing, particularly for low resource situations, by sharing parameters across languages. Multilingual acoustic models, however, generally ignore the difference between phonemes (sounds that can 
support lexical contrasts in a particular language) and their corresponding phones (the sounds that are actually spoken, which are language independent). This can lead to performance degradation when combining a variety of training languages, as identically annotated phonemes can actually correspond to several different underlying phonetic realizations. In this work, we propose a joint model of both language-independent phone and language-dependent phoneme distributions. In multilingual ASR experiments over 11 languages, we find that this model improves testing performance by 2% phoneme error 
rate absolute in low-resource conditions. Additionally, because we are explicitly modeling language-independent phones, 
we can build a (nearly-)universal phone recognizer that, when combined with the PHOIBLE [1] large, manually curated database of phone inventories, can be customized into 2,000 language dependent recognizers. Experiments on two low-resourced indigenous languages, Inuktitut and Tusom, show that our recognizer achieves phone accuracy improvements of more than 17%, moving a step closer to speech recognition for all languages in the world. 1
Published in: ICASSP 2020 - 2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)      
Date of Conference: 04-08 May 2020
Date Added to IEEE Xplore: 09 April 2020
ISBN Information:
ISSN Information:
INSPEC Accession Number: 19788378
DOI: 10.1109/ICASSP40776.2020.9054362
Publisher: IEEE
Conference Location: Barcelona, Spain
1. INTRODUCTION
There is an increasing interest in building speech tools benefiting low-resource languages, specifically multilingual models that can improve low-resource recognition using rich resources available in other languages like English and Mandarin. One standard tool for recognition in low resource languages is multilingual acoustic modeling [2]. Acoustic models are generally trained on parallel data of speech waveforms and phoneme transcriptions. Importantly, phonemes are perceptual units of sound that closely correlate with, but do not exactly correspond to the actual sounds that are spoken, phones. An example of this is shown in Figure 1, which demonstrates two English words that share the same phoneme /p/, but different in the actual phonetic realizations [p] and [ph]. Allophones, the sets of phones that correspond to a particular phoneme, are language specific; distinctions that are important in some languages are not important in others.
Sign in to Continue Reading
Authors
Figures
References
Citations
Keywords
Metrics
Footnotes
More Like This
Speech recognition with deep recurrent neural networks
2013 IEEE International Conference on Acoustics, Speech and Signal Processing
Published: 2013
Context-Dependent Pre-Trained Deep Neural Networks for Large-Vocabulary Speech Recognition
IEEE Transactions on Audio, Speech, and Language Processing
Published: 2012
Show More
"""

# Split the text into lines
lines = text.split("\n")

# Initialize variables to store the extracted information
title = None
date_of_conference = None
doi = None
citations = None

# Iterate through the lines to find the relevant information
for i, line in enumerate(lines):
    if i == 2:
        title = line.strip()
    elif "Date Added to IEEE Xplore:" in line:
        date_of_conference = line.split(":")[1].strip()
    elif "DOI:" in line:
        doi = line.split(":")[1].strip()
    elif "All Authors" in line:
        if i + 1 < len(lines):
            citations = lines[i + 1].strip()

# Print the extracted information
print("Title:", title)
print("Date of Adding to IEEE:", date_of_conference)
print("DOI:", doi)
print("Citations:", citations)