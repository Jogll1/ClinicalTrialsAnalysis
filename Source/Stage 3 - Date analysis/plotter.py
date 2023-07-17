# plot the values of the spec_year_freq_dict
import matplotlib.pyplot as plt
import numpy as np
import json
import secrets

# region Test
# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])

# xpoints1 = np.array([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015])

# ypoints1 = np.array([5, 6, 3, 6, 24, 12, 14, 19, 22, 34, 20, 15, 5, 67, 45, 32])
# ypoints2 = np.array([2, 34, 24, 17, 4, 6, 7, 13, 17, 26, 36, 31, 25, 7, 2, 3])

# # marker|line|color
# plt.plot(xpoints1, ypoints1, marker='o', c='#4caf50')
# plt.plot(xpoints1, ypoints2, marker='o', c='#f4f5ad')
# plt.show()
#endregion

json_path = 'spec_year_freq_dict.json'

data = {}

# Load JSON data from a file
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

        colour = '#' + secrets.token_hex(3)
        plt.plot(x, y, color=colour, label=spec)
    else:
        print('Invalid key')

# Plotting the data
plot_specialisation('oncology')
plot_specialisation('cardiology')
plot_specialisation('psychiatry')
plot_specialisation('neurology')
plot_specialisation('endocrinology')

plt.xlabel('Year')
plt.ylabel('Frequency')
plt.title('Frequency of Specialisations by Year')

# set x axis values in a range with step 5
plt.xticks(np.arange(year_start, year_end, 5))

# show graph
plt.legend()
plt.show()