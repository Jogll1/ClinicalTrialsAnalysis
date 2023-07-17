import pandas as pd
import numpy as np

# variables
input_path = 'Data/Stage 2/mapped_conditions.txt'
output_path = 'Data/Stage 2/specialisation_frequency.csv'

new_med_spec_path = 'Data/Stage 2/new_medical_specialisations.txt'
cond_freq_path = 'Data/Stage 1/conditions_frequency.csv'

# first strip the conditions so no quotation marks
# then split each line of text file into condition and specialisation
# then create a new list of medical specialisations as chatgpt might have added or changed some
# get the frequency of each condition and add it to the overall frequency of that medical specialisation
# then create a csv file with that data

# idk (strip lines?)
values_added = []
with open(input_path, 'r', encoding='utf-8') as f_in, open(new_med_spec_path, 'w', encoding='utf-8') as f_out:
    for line in f_in:
        values = line.split(':')
        # var1 = values[0].strip()
        var2 = values[1].strip().split('/')[0]
        if var2 not in values_added:
            # line_stripped = ':'.join([var1, var2])
            line_stripped = var2
            f_out.write(line_stripped + '\n')
            values_added.append(var2)

# split each line into condition and specialisation and extract all specialisations
# read csv file
condition_column = pd.read_csv(cond_freq_path)['Conditions']
frequencies_column = pd.read_csv(cond_freq_path)['Frequency']

specialisations = []
frequencies = []
linecount = 0
with open(input_path, 'r', encoding='utf-8') as f_in:
    for line in f_in:
        values = line.split(':')
        if values[1] not in specialisations:
            specialisations.append(values[1])
            frequencies.append(frequencies_column[linecount])
        else:
            # increment frequency
            frequencies[specialisations.index(values[1])] += frequencies_column[linecount]
        linecount += 1

# with open('testing.txt', 'w', encoding='utf-8') as f_out:
#     for i in range(0, len(specialisations)):
#         f_out.write(specialisations[i].strip('\n') + " " + str(frequencies[i]) + '\n')

# clean list
for i in range(0, len(specialisations)):
    specialisations[i] = specialisations[i].strip('\n').strip()

# send to csv
df = pd.DataFrame({'Specialisation': specialisations, 'Frequency': frequencies})
sorted_df = df.sort_values('Frequency', ascending=False)
sorted_df.to_csv(output_path, index=False)
