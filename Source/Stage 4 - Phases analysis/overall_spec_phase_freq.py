import pandas as pd
import json

input_path = 'Data/Stage 4/spec_phase_frequencies.csv'
output_path = 'Data/Stage 4/overall_spec_phase_freq.csv'

specialisations = []
frequencies = []

df = pd.read_csv(input_path)
spec_list = df["Specialisation-Phase"].astype(str).to_list()
freq_list = df["Frequency"].astype(str).to_list()

# strip phases of specialisations
strip_spec_list = [i.split(':')[0].strip() for i in spec_list]

# count unique specialisations
for i in range(0, len(strip_spec_list)):
    if strip_spec_list[i] in specialisations:
        # increment frequency
        frequencies[specialisations.index(strip_spec_list[i])] = int(frequencies[specialisations.index(strip_spec_list[i])])
        frequencies[specialisations.index(strip_spec_list[i])] += int(freq_list[i])
    else:
        # add to list
        specialisations.append(strip_spec_list[i])
        frequencies.append(freq_list[i])

# write to csv
df = pd.DataFrame({'Specialisation': specialisations, 'Frequency': frequencies})
df.to_csv(output_path, index=False)
