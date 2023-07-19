# plot the values of the spec_phase_freq_dict
import matplotlib.pyplot as plt
import numpy as np
import json
import secrets

json_path = 'Data/Stage 4/spec_phase_freq_dict.json'

# phase
phases = ['early_phase1', 'phase1', 'phase2', 'phase3', 'phase4']
titles = ['Early Phase 1', 'Phase 1', 'Phase 2', 'Phase 3', 'Phase 4']

data = {}

# load json data
with open(json_path) as json_file:
    data = json.load(json_file)

# create a figure and axis
fig, ax = plt.subplots()

# function to check if a key is in the data dictionary
def nested_key_exists(dict, keys):
    try:
        x = dict[keys[0]][keys[1]]
        return True
    except KeyError:
        return False

def plot_specialisation(spec):
    # check if spec exists
    if spec in data and data[spec] is not None:
        y_values = []
        for i in range(0, 5):
            if nested_key_exists(data, [spec, phases[i]]):
                # if there is data for that phase
                y_values.append(data[spec][phases[i]])
            else:
                y_values.append(0)

        # plot values
        # convert list to np array
        y = np.array(y_values)

        # plot with random colour
        colour = '#' + secrets.token_hex(3)
        plt.plot(titles, y, color=colour, label=spec)
    else:
        print('Invalid key')

# plotting the data
plot_specialisation('ophthalmology')
plot_specialisation('hematology')
plot_specialisation('neurology')
plot_specialisation('gastroenterology')
plot_specialisation('infectious disea')
plot_specialisation('ophthalmology')

# generate list of all keys
# test_list = ['oncology', 'hematology', 'neurology', 'gastroenterology', 'infectious disea']
# keys_list = list(data.keys())
# for i in keys_list:
#     if i not in test_list:
#         plot_specialisation(i)

plt.xlabel('Phase')
plt.ylabel('Frequency')
plt.title('Frequency of Specialisations by Phase')

# show graph
plt.legend(loc='upper left')
plt.show()