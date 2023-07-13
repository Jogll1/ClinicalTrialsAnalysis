# to get a better estimate, perform similarity checking on the rows of text
import pandas as pd
from difflib import SequenceMatcher

pd.options.display.max_colwidth = 1000
similarity_threshold = 0.6

data_path = 'conditions.txt'
invalid_rows = ['nan', '#NAME?']

# calcualte the similarity between two strings using SequenceMatcher
def similarity_score(a, b):
    return SequenceMatcher(None, a, b).ratio()


