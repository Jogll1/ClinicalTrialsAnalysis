import pandas as pd
import json

# overview
# gather a list of all conditions:phase ('condition_with_phase.txt')
# go through this list and
# if the condition is not in mapped_conditions just remove for now
# this then means we can map the left over conditions to their specialisation and include the phase
# then for each specialisation count the amount of different phases
# (this is basically the same as get_year_freq.py)

# paths
input_path = 'Data/CTG csv/ctg-studies(phases).csv'
map_cond_path = 'Data/Stage 2/mapped_conditions.txt'
output_txt_path1 = 'Data/Stage 4/condition_with_phase.txt'
output_txt_path2 = 'Data/Stage 4/spec_with_phase.txt'
output_csv_path1 = 'Data/Stage 4/spec_phase_frequencies.csv'
output_json_path1 = 'Data/Stage 4/spec_phase_freq_dict.json'

df = pd.read_csv(input_path)
conditions_list = df["Conditions"].astype(str).to_list()
phases_list = df["Phases"].astype(str).to_list()

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

# write conditions and phase to a text file
print("Write to condition_with_phase.txt")
with open(output_txt_path1, 'w', encoding='utf-8') as f_out:
    for i in range(0, len(conditions_list)):
        #split phases seperated by '|' and add to list 
        phase = phases_list[i].strip().split('|')
        #split conditions seperated by '|' and add to list 
        conditions = conditions_list[i].split('|')
        # if phase valid
        if "phase" in phase[0].lower():
            for i in range(0, len(conditions)):
                for j in range(0, len(phase)):
                    f_out.write(conditions[i].strip('"').split(':')[0].lower() + ":" 
                                + phase[j].strip('"').lower() + '\n')
                    
# check each condition and remove ones which aren't in mapped_conditions
# then create new file and add the specialisation paired with the phase
print("Write to spec_with_phase.txt")
with open(output_txt_path1, "r", encoding='utf-8') as f_in, open(output_txt_path2, "w", encoding='utf-8') as f_out:
    for line in f_in:
        values = line.split(':')
        cond = values[0].split(':')[0]
        phase = values[1]
        if cond in map_cond_list:
            spec = map_spec_list[map_cond_list.index(cond)].strip('\n')
            # some specialisations are like spec1/spec2 so split at / and count them as 2 seperate
            specs = spec.split('/')
            if len(specs) > 1:
                f_out.write(specs[0] + ":" + phase)
                f_out.write(specs[1] + ":" + phase)
            else:
                # some also have (not listed) at the end so remove that
                spec = spec.rstrip(' (not listed)')
                f_out.write(spec + ":" + phase)

# now collect all repeated instances of speciality:phase with freqeuncies
spec_and_phase_tokens = []
spec_and_phase_frequency = []
print("Write lists for frequencies of spec and phase")
with open(output_txt_path2, "r", encoding='utf-8') as f_in:
    for line in f_in:
        if line not in spec_and_phase_tokens:
            spec_and_phase_tokens.append(line)
            spec_and_phase_frequency.append(1)
        else:
            # increment the frequencies
            spec_and_phase_frequency[spec_and_phase_tokens.index(line)] += 1

# clean spec_and_phase_tokens
print("Clean spec_and_phase_tokens")
for i in range(0, len(spec_and_phase_tokens)):
    spec_and_phase_tokens[i] = spec_and_phase_tokens[i].strip('"').strip('\n')

# add these values to a csv
print("Write to spec_phase_frequencies.csv")
df = pd.DataFrame({'Specialisation-Phase': spec_and_phase_tokens, 'Frequency': spec_and_phase_frequency})
sorted_df = df.sort_values('Frequency', ascending=False)
sorted_df.to_csv(output_csv_path1, index=False)

# now generate a 2d array csv
print("Write to nested dictionary object")
data_for_plotting = {}

# read the CSV file using pandas
df = pd.read_csv(output_csv_path1)

# iterate over each row in the dataframe
for index, row in df.iterrows():
    values = row['Specialisation-Phase'].split(':')
    spec = values[0]
    phase = values[1]
    frequency = int(row['Frequency'])

    if spec not in data_for_plotting:
        data_for_plotting[spec] = {}

    data_for_plotting[spec][phase] = frequency

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