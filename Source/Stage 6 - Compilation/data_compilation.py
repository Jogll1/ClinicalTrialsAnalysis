import pandas as pd
import json

# aim to make new csv containing all data
# Specialisation, Overall Frequency, Early Phase 1, Phase 1, Phase 2, Phase 3, Phase 4, Academic, Industry, US Gov, Other

specialisations_path = 'Data/Stage 2/new_medical_specialisations.txt'
input_csv1 = 'Data/Stage 2/specialisation_frequency.csv'
input_json1 = 'Data/Stage 4/spec_phase_freq_dict.json'
input_csv3 = 'Data/Stage 5/spec_funder_percent.csv'
output_path = 'Data/Stage 6/compiled_data.csv'

specialisations = [] # 
overall_frequencies = [] # 
early_phase_1 = []
phase_1 = []
phase_2 = []
phase_3 = []
phase_4 = []
academic_fr = []
industry_fr = []
us_gov_fr = []
other_fr = []

# get specialisations list
with open(specialisations_path, 'r', encoding='utf-8') as f:
    for line in f:
        specialisations.append(line.strip().lower())
specialisations = sorted(specialisations)

# get overall frequencies
overall_frequencies = [0] * len(specialisations)
df2 = pd.read_csv(input_csv1)
spec_list = df2["Specialisation"].astype(str).to_list()
spec_list = [item.lower().strip() for item in spec_list]
freq_list = df2["Frequency"].astype(str).to_list()

for i in range(0, len(spec_list)):
    for j in range(0, len(specialisations)):
        if spec_list[i] == specialisations[j] or spec_list[i] in specialisations[j]:
            overall_frequencies[j] = freq_list[i]
            break

# clean list of any empties
new_specialisations = []
new_overall_frequencies = []
for i in range(0, len(overall_frequencies)):
    if overall_frequencies[i] != 0:
        new_specialisations.append(i)
        new_overall_frequencies.append(i)
specialisations = new_specialisations
overall_frequencies = new_overall_frequencies

# phases
data = {}

with open(input_json1) as json_file:
    data = json.load(json_file)

def nested_key_exists(dict, keys):
    try:
        x = dict[keys[0]][keys[1]]
        return True
    except KeyError:
        return False

keys_list = list(data.keys())

phases = ["early_phase1", "phase1", "phase2", "phase3", "phase4"]
for i in range(0, len(keys_list)):
    print("yeah")

# df = pd.DataFrame({'Specialisation': keys_list, 'Academic': academic_fr_list, 'Industry': industry_fr_list, 'Gov': gov_fr_list, 'Other': other_fr_list})
# df.to_csv(output_path, index=False)