# to get a better estimate, perform similarity checking on the rows of text
import pandas as pd
from difflib import SequenceMatcher

pd.options.display.max_colwidth = 1000

data_path = 'conditions.txt'
invalid_rows = ['nan', '#NAME?']

# read the text file and create a new csv containing the frequency of each individual word
words_frequency = {}
with open(data_path, 'r', encoding='utf-8') as f:
    for row in f:
        if row.strip() not in invalid_rows:
            row = row.strip().split()
            # word_frequency[word] = word_frequency.get(row, 0) + 1
            for i in range(0, len(row)):
                words_frequency[row[i]] = words_frequency.get(row[i], 0) + 1


# create a dataframe from the dictionary
df = pd.DataFrame(list(words_frequency.items()), columns=['Word', 'Frequency'])

# sort the dataframe
# sorted_df = df.sort_values(by='Condition', ascending=True)
sorted_df = df.sort_values(by='Frequency', ascending=False)

# write to csv
sorted_df.to_csv('words_frequency.csv', index=False, header=False)