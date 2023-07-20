import pandas as pd
import json

input_path = 'Data/Stage 7/avg_length_spec_dict.json'
output_path = 'Data/Stage 7/avg_length_spec.csv'

# load json
data = {}

with open(input_path) as json_file:
    data = json.load(json_file)

specialisations_list = list(data.keys())

average_lengths = []
for i in range(0, len(specialisations_list)):
    values = data[specialisations_list[i]]
    average = round(float(values[0]) / float(values[1]), 2)
    average_lengths.append(average)

df = pd.DataFrame({'Specialisation': specialisations_list, 'Average length (days)': average_lengths})
df.to_csv(output_path, index=False)