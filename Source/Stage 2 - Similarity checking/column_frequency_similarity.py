# to get a better estimate, perform similarity checking on the rows of text
import pandas as pd
from difflib import SequenceMatcher

pd.options.display.max_colwidth = 1000
similarity_threshold = 0.6

# read the text file
# with open('conditions.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()

# calcualte the similarity between two strings using SequenceMatcher
def similarity_score(a, b):
    return SequenceMatcher(None, a, b).ratio()

print(similarity_score('Cough', 'Cough Variant Asthma'))


