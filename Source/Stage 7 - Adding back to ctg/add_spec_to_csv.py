import pandas as pd
import json

# script to add the specialisation to a trial by adding an extra column for each specialisation
# in form of adding a 1 to the specialisation column if a condition in the trial matches with one of the specilialisations
# also added no. of locatiosn columns

group_spec_path = 'Data/Stage 7/grouped_spec.json'
# map_cond_path = 'Data/Stage 2/mapped_conditions.txt'
map_cond_path = 'Data/Stage 2/mapped_conditions2.txt'
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

# create number of locations column
copy_df['No. of locations'] = 1
# add new column for each speciality to copy of csv
for column_name in specialisations_list:
    copy_df[column_name] = 0

# go through each trial and check which conditions it contains
for i in range(0, len(conditions_list)):
    print("trial " + str(i))
    conditions = conditions_list[i].split("|")
    # print(conditions)
    specs = []
    for j in conditions:
        # map the conditions from mapped_conditions
        if j.lower().strip() in mapped_cond:
            specs.append(mapped_spec[mapped_cond.index(j.lower().strip())])
            continue
        else:
            for k in range(0, len(mapped_spec)):
                if str(j.lower()).strip() in mapped_spec[k].lower().strip() or mapped_spec[k].lower().strip() in str(j.lower()).strip():
                    specs.append(mapped_spec[k].lower().strip())
                    break
        # remap the conditions from json
        for spec in specs:
            for k in range(0, len(specialisations_list)):
                if spec in data[specialisations_list[k]]:
                    specs[specs.index(spec)] = specialisations_list[k]
                    break
    # increment the value in the column of the dataframe
    for m in range(0, len(specs)):
        if specs[m] in specialisations_list:
            # change row, column value to a 1 if its not already
            col = specialisations_list[specialisations_list.index(specs[m])]
            if copy_df.iat[i, copy_df.columns.get_loc(col)] == 0:
                copy_df.iat[i, copy_df.columns.get_loc(col)] = 1
    # print(copy_df.loc[i].values)

    # get amount of locations
    locations = copy_df.iat[i, copy_df.columns.get_loc("Locations")]
    locations =  locations.split("|") if str(locations) != "nan" else ['1']
    copy_df.iat[i, copy_df.columns.get_loc("No. of locations")] = len(locations)

# write the copy df to a csv file
copy_df.to_csv(output_path, index=False)