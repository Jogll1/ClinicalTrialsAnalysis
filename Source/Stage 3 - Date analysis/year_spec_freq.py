import pandas as pd
import json

# overview
# gather a list of all conditions:year ('condition_with_year.txt')
# go through this list and
# if the condition is not in mapped_conditions just remove for now
# this then means we can map the left over conditions to their specialisation and include the year
# then for each year count the amount of specialisations for that year

# paths
input_path = 'Data/CTG csv/ctg-studies(dates).csv'
map_cond_path = 'Data/Stage 2/mapped_conditions.txt'
output_txt_path1 = 'Data/Stage 3/condition_with_year.txt'
output_txt_path2 = 'Data/Stage 3/spec_with_year.txt'
output_csv_path1 = 'Data/Stage 3/spec_year_frequencies.csv'
output_json_path1 = 'Data/Stage 3/spec_year_freq_dict.json'

df = pd.read_csv(input_path)
conditions_list = df["Conditions"].astype(str).to_list()
start_years_list = df["Start Date"].astype(str).to_list()

# get the conditions in mapped_conditions
map_cond_list = [] # list of all conditions in mapped_condition
map_spec_list = [] # list of all specialities in mapped_condition
print("Get unqiue conditions and specialisations")
with open(map_cond_path, 'r', encoding='utf-8') as f:
    for line in f:
        strip_line_cond = line.split(':')[0].lower()
        strip_line_spec = line.split(':')[1].lower()
        if strip_line_cond not in map_cond_list:
            map_cond_list.append(strip_line_cond)
            map_spec_list.append(strip_line_spec)

# write conditions and start year to a text file
print("Write to condition_with_year.txt")
with open(output_txt_path1, 'w', encoding='utf-8') as f_out:
    for i in range(0, len(conditions_list)):
        #split conditions seperated by '|' and add to list 
        year = start_years_list[i][0:4]
        conditions = conditions_list[i].split('|')
        for i in range(0, len(conditions)):
            f_out.write(conditions[i].strip('"').split(':')[0].lower() + ":" + year + '\n')

# check each condition and remove ones which aren't in mapped_conditions
# then create new file and add the specialisation paired with the year
print("Write to spec_with_year.txt")
with open(output_txt_path1, "r", encoding='utf-8') as f_in, open(output_txt_path2, "w", encoding='utf-8') as f_out:
    for line in f_in:
        values = line.split(':')
        cond = values[0].split(':')[0]
        year = values[1]
        if cond in map_cond_list and year != 'nan\n':
            spec = map_spec_list[map_cond_list.index(cond)].strip('\n')
            # some specialisations are like spec1/spec2 so split at / and count them as 2 seperate
            specs = spec.split('/')
            if len(specs) > 1:
                f_out.write(specs[0] + ":" + year)
                f_out.write(specs[1] + ":" + year)
            else:
                # some also have (not listed) at the end so remove that
                spec = spec.rstrip(' (not listed)')
                f_out.write(spec + ":" + year)

# now collect all repeated instances of speciality:year with freqeuncies
spec_and_year_tokens = []
spec_and_year_frequency = []
print("Write lists for frequencies of spec and year")
with open(output_txt_path2, "r", encoding='utf-8') as f_in:
    for line in f_in:
        if line not in spec_and_year_tokens:
            spec_and_year_tokens.append(line)
            spec_and_year_frequency.append(1)
        else:
            # increment the frequencies
            spec_and_year_frequency[spec_and_year_tokens.index(line)] += 1

# clean spec_and_year_tokens
print("Clean spec_and_year_tokens")
for i in range(0, len(spec_and_year_tokens)):
    spec_and_year_tokens[i] = spec_and_year_tokens[i].strip('"').strip('\n')

# add these values to a csv
print("Write to spec_year_frequencies.csv")
df = pd.DataFrame({'Specialisation-Year': spec_and_year_tokens, 'Frequency': spec_and_year_frequency})
sorted_df = df.sort_values('Frequency', ascending=False)
sorted_df.to_csv(output_csv_path1, index=False)

# now generate a 2d array csv
print("Write to nested dictionary object")
data_for_plotting = {}

# read the CSV file using pandas
df = pd.read_csv(output_csv_path1)

# iterate over each row in the dataframe
for index, row in df.iterrows():
    values = row['Specialisation-Year'].split(':')
    spec = values[0]
    year = values[1]
    frequency = int(row['Frequency'])

    if spec not in data_for_plotting:
        data_for_plotting[spec] = {}

    data_for_plotting[spec][year] = frequency

def sort_dict(dictionary):
    if isinstance(dictionary, dict):
        sorted_dict = {}
        for key in sorted(dictionary.keys()):
            sorted_dict[key] = sort_dict(dictionary[key])
        return sorted_dict
    else:
        return dictionary

data_for_plotting = sort_dict(data_for_plotting)

with open(output_json_path1, 'w') as json_file:
    json.dump(data_for_plotting, json_file, indent=4)