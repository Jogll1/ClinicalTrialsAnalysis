# in analyse the conditions column, extract the data from the column
import pandas as pd
import re

pd.options.display.max_colwidth = 1000

# variables
csv_path = 'ctg-studies1.csv'
column_name = 'Conditions'
output_path = 'conditions.txt'

# note - all rows with value 'nan' are withheld trials by the us gov

# read csv file
df = pd.read_csv(csv_path)
# sort the values by condition
df = df.sort_values(column_name)
# get conditions column
column_data = df[column_name].astype(str)
# remove string after comma, hyphen, semicolon or " - " on each row
column_data_cleaned = column_data.str.replace(r'[,;].*| - .*', '', regex=True)
# remove punctuation left over
column_data_cleaned = column_data_cleaned.str.replace(r'[^\w\s]', '', regex=True)
#remove stopwords
stopwords = ['and', 'the', 'in', 'to', 'by', 'due', 'for', 'his', 'of', 'use', 'at', 'all', 'old', 'more', 'than', 'with']
pattern = r'\b(?:{})\b'.format('|'.join(stopwords))
column_data_cleaned = column_data_cleaned.str.replace(pattern, '', regex=True)
#remove with
pattern_with = r'\b{}\b'.format(re.escape('with'))
column_data_cleaned = column_data_cleaned.str.replace(pattern_with, '', regex=True)
# set text to lower
column_data_cleaned = column_data_cleaned.str.lower()
# cast as string without index or header
column_data_str = column_data_cleaned.to_string(index=False, header=False)
# remove leading whitespace
column_data_str = '\n'.join(row.strip() for row in column_data_str.split('\n'))
# split lines with multiple data points by "|"
split_rows = [row.split("|") for row in column_data_str.split('\n')]
# flatten split data into a string with newline chars
split_data = [item for sublist in split_rows for item in sublist]
# join the split data 
split_data_str = '\n'.join(split_data)
# sort the split data alphabetically
sorted_data = sorted(split_data_str.split('\n'))
# join the sorted data into a string
sorted_data_str = '\n'.join(sorted_data)

# create text file
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(sorted_data_str)
