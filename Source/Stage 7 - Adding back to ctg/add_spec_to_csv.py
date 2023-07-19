import pandas as pd
import json

# script to add the specialisation to a trial
# in form of adding a 1 to the specialisation column

group_spec_path = 'Data/Stage 7/grouped_spec.json'
map_cond_path = 'Data/Stage 2/mapped_conditions.txt'
input_path = 'Data/CTG csv/ctg-studies(all).csv'
output_path = 'Data/Stage 7/ctg-with-spec.csv'

# load csv
df = pd.read_csv(input_path)
conditions_list = df["Conditions"].astype(str).to_list()

# get 2 lists: the condittion and its mapped spec
mapped_cond = []
mapped_spec = []
with open(map_cond_path, 'r', encoding='utf-8') as f:
    for line in f:
        values = line.split(":")
        mapped_cond.append(values[0].lower().strip())
        mapped_spec.append(values[1].lower().strip())

# load json to get specialisations
data = {}

with open(group_spec_path) as json_file:
    data = json.load(json_file)

specialisations_list = list(data.keys())

# get copy of csv
copy_df = df.copy()

# add new column for each speciality to copy of csv
for i in range(0, len(specialisations_list)):
    column_title = specialisations_list[i]
    copy_df[column_title] = ''

# go through each trial and check which conditions it contains
for i in range(0, len(conditions_list)):
    print("trial " + str(i))
    conditions = conditions_list[i].split("|")
    for j in conditions:
        spec = ''
        # map the conditions from mapped_conditions
        if j.lower().strip() in mapped_cond:
            spec = mapped_spec[mapped_cond.index(j.lower().strip())]            
            print(spec)
        # remap the conditions from json

# write the copy df to a csv file
# copy_df.to_csv(output_path, index=False)