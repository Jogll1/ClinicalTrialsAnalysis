# plot the values of the spec_year_freq_dict
import matplotlib.pyplot as plt
import numpy as np
import json
import secrets

json_path = 'Data/Stage 3/spec_year_freq_dict.json'

data = {}

# load json data
with open(json_path) as json_file:
    data = json.load(json_file)

year_start = 1980
year_end = 2024

# value = data['oncology']['2001'] = 706

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
        for i in range(year_start, year_end):
            if nested_key_exists(data, [spec, str(i)]):
                # if there is data for that year
                y_values.append(data[spec][str(i)])
            else:
                #if not set it to 0
                y_values.append(0)
        
        # plot values
        # convert list to np array
        y = np.array(y_values)
        x = np.arange(year_start, year_end, 1)

        # plot with random colour
        colour = '#' + secrets.token_hex(3)
        plt.plot(x, y, color=colour, label=spec)
    else:
        print('Invalid key')

# plotting the data
plot_specialisation('oncology')
plot_specialisation('cardiology')
plot_specialisation('psychiatry')
plot_specialisation('neurology')
plot_specialisation('endocrinology')
plot_specialisation('ophthalmology')

# generate list of all keys
# test_list = ['oncology', 'cardiology', 'psychiatry', 'neurology', 'endocrinology', 'infectious disea']
# keys_list = list(data.keys())
# for i in keys_list:
#     if i not in test_list:
#         plot_specialisation(i)

plt.xlabel('Year')
plt.ylabel('Frequency')
plt.title('Frequency of Specialisations by Year')

# set x axis values in a range with step 5
plt.xticks(np.arange(year_start, year_end, 5))

# show graph
plt.legend(loc='upper left')
plt.show()