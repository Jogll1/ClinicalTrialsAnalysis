import numpy as np
import pandas as pd
import json
import secrets

# get percentage of academically-led vs commercially led trials

json_path = 'Data/Stage 5/spec_funder_freq_dict.json'
output_path = 'Data/Stage 5/spec_funder_percent.csv'

data = {}

# load json data
with open(json_path) as json_file:
    data = json.load(json_file)

# generate list of all keys (specialisations) and fractions
keys_list = list(data.keys())

academic_fr_list = []
industry_fr_list = []
gov_fr_list = []
other_fr_list = []

# function to check if a key is in the data dictionary
def nested_key_exists(dict, keys):
    try:
        x = dict[keys[0]][keys[1]]
        return True
    except KeyError:
        return False

gov_types = ["FED", "NIH", "OTHER_GOV"]
for i in range(0, len(keys_list)):
    nested_keys_list = list(data[keys_list[i]].keys())
    total_value = 0
    for j in nested_keys_list:
        total_value += data[keys_list[i]][j]

    other_append = round(float(data[keys_list[i]]["OTHER"]) / float(total_value), 4) if "OTHER" in nested_keys_list else 0
    academic_fr_list.append(other_append)

    industry_append = round(float(data[keys_list[i]]["INDUSTRY"]) / float(total_value), 4) if "INDUSTRY" in nested_keys_list else 0
    industry_fr_list.append(industry_append)

    numerator = 0
    for k in gov_types:
        if k in gov_types:
            if nested_key_exists(data, [keys_list[i], k]):
                numerator += data[keys_list[i]][k]
    gov_append = round(float(numerator) / float(total_value), 4) if numerator != 0 else 0
    gov_fr_list.append(gov_append)

    other_fr_list.append(abs(round(1 - other_append - industry_append - gov_append, 4)))

# print(str(len(keys_list)) + " " + str(len(academic_fr_list)) + " " + str(len(industry_fr_list)) + " " + str(len(gov_fr_list)))
df = pd.DataFrame({'Specialisation': keys_list, 'Academic': academic_fr_list, 'Industry': industry_fr_list, 'Gov': gov_fr_list, 'Other': other_fr_list})
# df = df.sort_values('Academic', ascending=False)
df.to_csv(output_path, index=False)
            