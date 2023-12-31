import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import secrets

input_path = 'Data/Stage 7/ctg-with-spec.csv'

# load csv data
df = pd.read_csv(input_path)

start_date_list = df["Start Date"].astype(str).to_list()
end_date_list = df["Completion Date"].astype(str).to_list()
phases_list = df["Phases"].astype(str).to_list()

year_start = 1980
year_end = 2040

columns_list = df.columns.tolist()
# print(columns_list)
spec_list = columns_list[15:len(columns_list)]

# line graph axis
fig, ax1 = plt.subplots()

# bar graph axis
ax2 = ax1.twinx()

def is_date_between(start_date_str, end_date_str, check_date_str):
    start_date_str = start_date_str[0:7]
    end_date_str = end_date_str[0:7]
    check_date_str = check_date_str[0:7]
    # convert string dates to datetime objects
    start_date = datetime.strptime(start_date_str, '%Y-%m')
    end_date = datetime.strptime(end_date_str, '%Y-%m')
    date_to_check = datetime.strptime(check_date_str, '%Y-%m')

    # check if date_to_check is between start_date and end_date
    return start_date <= date_to_check <= end_date

def plot_spec_data(spec):
    if spec in spec_list:
        # initialise list length of amount of months between year_start and year_end
        y_values = [0] * (year_end - year_start) * 12
        early_1_values = [0] * (year_end - year_start) * 12
        phase_1_values = [0] * (year_end - year_start) * 12
        phase_2_values = [0] * (year_end - year_start) * 12
        phase_3_values = [0] * (year_end - year_start) * 12
        phase_4_values = [0] * (year_end - year_start) * 12
        # go through each trial
        for i in range(0, len(start_date_list)):
            print("line graph 1 trial " + str(i))
            # if either date values are not equal to nan
            if str(start_date_list[i]) != "nan" and str(end_date_list[i]) != "nan":
                # if the trial contains the specialisation we are graphing
                if df.iat[i, df.columns.get_loc(spec)] == 1:
                    check_date = start_date_list[i]
                    # for each month the trial is running between year_start and year_end, increment the corresponding value in y_values
                    while is_date_between(start_date_list[i], end_date_list[i], check_date) and is_date_between(str(year_start) + "-01", str(year_end) + "-01", check_date):
                        check_values = check_date.split('-')

                        # update frequency values
                        y_values[(int(check_values[0]) - year_start) * 12 + int(check_values[1]) - 2] += 1

                        #update phase values
                        # if phase values are not equal to nan
                        if str(phases_list[i]) != "nan":
                            phases = phases_list[i].split("|")
                            for j in range(0, len(phases)):
                                if phases[j] == "EARLY_PHASE1":
                                    early_1_values[(int(check_values[0]) - year_start) * 12 + int(check_values[1]) - 2] += 1
                                elif phases[j] == "PHASE1":
                                    phase_1_values[(int(check_values[0]) - year_start) * 12 + int(check_values[1]) - 2] += 1
                                elif phases[j] == "PHASE2":
                                    phase_2_values[(int(check_values[0]) - year_start) * 12 + int(check_values[1]) - 2] += 1
                                elif phases[j] == "PHASE3":
                                    phase_3_values[(int(check_values[0]) - year_start) * 12 + int(check_values[1]) - 2] += 1
                                elif phases[j] == "PHASE4":
                                    phase_4_values[(int(check_values[0]) - year_start) * 12 + int(check_values[1]) - 2] += 1

                        # increment check date
                        if int(check_values[1]) + 1 > 12:
                            check_date = str(int(check_values[0]) + 1) + "-01"
                        else:
                            check_date = str(check_values[0]) + "-" + str(int(check_values[1]) + 1).zfill(2)

        # plot line graph
        y = np.array(y_values)
        # set step for each month
        x = np.arange(year_start, year_end, 1/12)

        # plot with random colour
        colour = '#' + secrets.token_hex(3)

        # plt.figure(1)
        ax1.plot(x, y, color=colour, label=spec)

        # plot stacked bar graph
        ax2.bar(x, early_1_values, label='Early Phase 1', alpha=0.4)
        ax2.bar(x, phase_1_values, label='Phase 1', bottom=early_1_values, alpha=0.4)
        ax2.bar(x, phase_2_values, label='Phase 2', bottom=np.add(early_1_values, phase_1_values), alpha=0.4)
        ax2.bar(x, phase_3_values, label='Phase 3', bottom=np.add(np.add(early_1_values, phase_1_values), phase_2_values), alpha=0.4)
        ax2.bar(x, phase_4_values, label='Phase 4', bottom=np.add(np.add(np.add(early_1_values, phase_1_values), phase_2_values), phase_3_values), alpha=0.4)
    
        # set the y-axis limits for both axes to be the same
        y_max = max(np.add(np.add(np.add(early_1_values, phase_1_values), phase_2_values), phase_3_values).max(), y.max())
        y_min = min(np.add(np.add(np.add(early_1_values, phase_1_values), phase_2_values), phase_3_values).min(), y.min())
        ax1.set_ylim(y_min, y_max)
        ax2.set_ylim(y_min, y_max)
    else:
        print("Invalid specialisation")

plot_spec_data('oncology')

plt.title('Specialisation data')
plt.xlabel('Year')
plt.ylabel('No. of trials active')
# set x axis values in a range with step 60
plt.xticks(np.arange(year_start, year_end, 5))

# show the plot
ax1.legend(loc='upper right')
ax2.legend(loc='upper left')
# plt.tight_layout()
plt.show()