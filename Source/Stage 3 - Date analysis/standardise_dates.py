import pandas as pd

# program to standardise dates in a single format (yyyy/mm)

# variables
csv_path = 'ctg-studies(dates).csv'
column_name = 'Completion Date'

# read csv file and get column
df = pd.read_csv(csv_path)
column_data = df[column_name]

# modify column
# column_data_list = '\n'.join(map(str, column_data.tolist()))
column_data_list = column_data.tolist()
column_data_str = [str(value) for value in column_data]

for i in range(len(column_data_str)):
    column_data_str[i] = column_data_str[i][0:7]

# update csv with new column
column_data = pd.DataFrame(column_data_str, columns=[column_name])
df[column_name] = column_data

# write the dataframe back to csv
df.to_csv(csv_path, index=False)
# df.to_csv('updated-dates.csv', index=False)