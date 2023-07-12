# convert text file into csv containing values and frequencies

import pandas as pd

data_path = 'conditions.txt'
invalid_rows = ['nan', '#NAME?']

# read the text file and count row frequencies
rows_frequency = {}
with open(data_path, 'r', encoding='utf-8') as f:
    for row in f:
        if row.strip().lower() not in invalid_rows:
            row = row.strip().lower()
            rows_frequency[row] = rows_frequency.get(row, 0) + 1

# create a dataframe from the dictionary
df = pd.DataFrame(list(rows_frequency.items()), columns=['Condition', 'Frequency'])

# sort the dataframe by frequency
# sorted_df = df.sort_values(by='Condition', ascending=True)
sorted_df = df.sort_values(by='Frequency', ascending=False)
# filter the top n most frequent
# filtered_df = sorted_df.head(25)

# write to csv
sorted_df.to_csv('conditions_frequency.csv', index=False, header=False)