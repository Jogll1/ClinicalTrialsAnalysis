# # test plotter
# import matplotlib.pyplot as plt
# import numpy as np

# # xpoints = np.array([0, 6])
# # ypoints = np.array([0, 250])

# xpoints1 = np.array([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015])

# ypoints1 = np.array([5, 6, 3, 6, 24, 12, 14, 19, 22, 34, 20, 15, 5, 67, 45, 32])
# ypoints2 = np.array([2, 34, 24, 17, 4, 6, 7, 13, 17, 26, 36, 31, 25, 7, 2, 3])

# # marker|line|color
# plt.plot(xpoints1, ypoints1, marker='o', c='#4caf50')
# plt.plot(xpoints1, ypoints2, marker='o', c='#f4f5ad')
# plt.show()

import matplotlib.pyplot as plt

data = {
    'Oncology': {
        2021: 5025,
        2022: 4580,
        2020: 4484,
        2019: 4258,
        2018: 3692,
        2017: 3489,
        2016: 3092,
        2023: 3033,
        2015: 2768
    },
    'Neurology': {
        2021: 3511,
        2022: 3186,
        2019: 2885,
        2018: 2792
    },
    'Psychiatry': {
        2022: 3501,
        2021: 3423,
        2020: 2924,
        2019: 2844
    },
    'Infectious diseases': {
        2020: 3299
    },
    'Cardiology': {
        2021: 2778
    }
}

colors = ['blue', 'green', 'red', 'orange', 'purple']  # Assign colors to specialties

# Plotting the line graphs
for i, (specialty, values) in enumerate(data.items()):
    years = list(values.keys())
    frequencies = list(values.values())
    plt.plot(years, frequencies, color=colors[i % len(colors)], label=specialty)

plt.xlabel('Year')
plt.ylabel('Frequency')
plt.legend()
plt.title('Specialty Frequencies Over Time')
plt.grid(True)
plt.show()