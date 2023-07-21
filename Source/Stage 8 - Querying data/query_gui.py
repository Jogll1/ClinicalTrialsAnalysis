import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pandas as pd
import re
from datetime import datetime

data_path = 'Data/Stage 7/ctg-with-spec.csv'

def is_date_between(start_date_str, end_date_str, date_to_check_str):
    start_date_str = start_date_str[0:7]
    end_date_str = end_date_str[0:7]
    # convert string dates to datetime objects
    start_date = datetime.strptime(start_date_str, '%Y-%m')
    end_date = datetime.strptime(end_date_str, '%Y-%m')
    date_to_check = datetime.strptime(date_to_check_str, '%Y-%m')

    # check if date_to_check is between start_date and end_date
    return start_date <= date_to_check <= end_date

def filter_and_print_data():
    year = year_var.get()
    month = month_var.get()
    if not year or not month:
        print("Please enter both year and month.")
        return
    
    try:
        year = int(year)
    except ValueError:
        print("Invalid year format. Please enter a valid year (e.g., 2023).")
        return

    df = pd.read_csv(data_path)
    start_date_list = df["Start Date"].astype(str).to_list()
    end_date_list = df["Completion Date"].astype(str).to_list()

    # print(df.columns.to_list())

    filtered_data = []

    check_date = str(year) + "-" + str(month)

    for i in range(0, len(start_date_list)):
        if str(start_date_list[i]) != "nan" and str(end_date_list[i]) != "nan":
            if is_date_between(str(start_date_list[i]), str(end_date_list[i]), check_date):
                filtered_data.append(df.iloc[i].values)

    if len(filtered_data) == 0:
        print("No data found for the specified year and month.")
    else:
        for i in range(0, len(filtered_data)):
            print(filtered_data[i][0] + " " + filtered_data[i][11] + " " + filtered_data[i][12])

# tkinter window setup
root = tk.Tk()
root.title("CSV Filter")
# root.geometry("400x200")

# year input
year_label = tk.Label(root, text="Year:")
year_label.pack(side=tk.LEFT)
year_var = tk.StringVar()
year_entry = tk.Entry(root, textvariable=year_var)
year_entry.pack(side=tk.LEFT)

# month selection
month_label = tk.Label(root, text="Month:")
month_label.pack(side=tk.LEFT)
month_var = tk.StringVar()
month_combobox = ttk.Combobox(root, textvariable=month_var, values=[str(i).zfill(2) for i in range(1, 13)])
month_combobox.pack(side=tk.LEFT)

# button to filter and print data
print_button = tk.Button(root, text="Print Data", command=filter_and_print_data)
print_button.pack(side=tk.LEFT)

# root.geometry("600x450")
root.resizable(False, False)

root.mainloop()