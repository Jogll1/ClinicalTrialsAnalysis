import pandas as pd
import json
from datetime import datetime

# get a list of all specialisations and list the average time of trials under that spec

group_spec_path = 'Data/Stage 7/grouped_spec.json'
input_path = 'Data/Stage 7/ctg-with-spec.csv'
output_path_json = 'Data/Stage 7/avg_length_spec_dict.json'

# load csv
df = pd.read_csv(input_path)
start_dates_list = df["Start Date"].astype(str).to_list()
end_dates_list = df["Completion Date"].astype(str).to_list()

# load json
data = {}

with open(group_spec_path) as json_file:
    data = json.load(json_file)

specialisations_list = list(data.keys())

# generate dictionary where each key is a specialisation holding a list
# each key should be "spec_name": [running_total_of_lengths, frequency_of_spec]
spec_dict = {spec: [0, 0] for spec in specialisations_list}

# function to calculate number of days between two dates
def days_between_dates(date_str1, date_str2):
    # convert date strings to datetime objects
    date1 = datetime.strptime(date_str1, "%Y-%m-%d")
    date2 = datetime.strptime(date_str2, "%Y-%m-%d")
    # calculate the time difference
    time_difference = date2 - date1
    # extract the number of days from the time difference
    days_difference = time_difference.days
    return days_difference

# generate lengths
for i in range(0, len(start_dates_list)):
    print("running " + str(i))
    # only get valid dates
    if str(start_dates_list[i]) != "nan" and str(end_dates_list[i]) != "nan":
        # calculate length between dates
        start_date = start_dates_list[i] if len(start_dates_list[i]) == 10 else start_dates_list[i] + "-01"
        end_date = end_dates_list[i] if len(end_dates_list[i]) == 10 else end_dates_list[i] + "-01"
        length = days_between_dates(start_date, end_date)
        # print(str(start_date) + ":" + str(end_date) + " = " + str(length))

        # get the specialisations this trial covers
        selected_values = df.iloc[i, len(df.columns.tolist()) - len(specialisations_list):len(df.columns.tolist())].values
        for j in range(0, len(selected_values)):
            if selected_values[j] == 1:
                spec = specialisations_list[j]
                spec_dict[spec][0] += length
                spec_dict[spec][1] += 1

with open(output_path_json, 'w') as json_file:
    json.dump(spec_dict, json_file, indent=4)

# get the averages using get_avg.py