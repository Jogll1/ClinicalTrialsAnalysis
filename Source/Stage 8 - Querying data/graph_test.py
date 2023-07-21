import matplotlib.pyplot as plt
import numpy as np

# # Sample data for the first plot
# x1 = np.linspace(0, 10, 100)
# y1 = np.sin(x1)

# # Sample data for the second plot
# x2 = np.linspace(0, 5, 50)
# y2 = np.cos(x2)

# # Create the first figure and plot the first graph
# plt.figure(1)
# plt.plot(x1, y1)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('First Plot: y = sin(x)')

# # Create the second figure and plot the second graph
# plt.figure(2)
# plt.plot(x2, y2, color='orange')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Second Plot: y = cos(x)')

# # Show the figures
# plt.show()

# Sample data for the line graph
x_line = np.linspace(0, 10, 100)
y_line = np.sin(x_line)

# Sample data for the stacked bar graph
categories = ['Category A', 'Category B', 'Category C']
data1 = [20, 30, 40]
data2 = [10, 25, 35]
data3 = [5, 15, 25]

# Create an array of positions for the bars
x_bar = np.arange(len(categories))

# Create the figure and the primary axis for the line graph
fig, ax1 = plt.subplots()

# Plot the line graph on the primary axis
ax1.plot(x_line, y_line, label='Line Graph', color='blue')
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Line Graph', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Create a secondary axis for the stacked bar graph
ax2 = ax1.twinx()

# Plot the stacked bar graph on the secondary axis
ax2.bar(x_bar, data1, label='Data 1', alpha=0.7)
ax2.bar(x_bar, data2, label='Data 2', bottom=data1, alpha=0.7)
ax2.bar(x_bar, data3, label='Data 3', bottom=np.add(data1, data2), alpha=0.7)
ax2.set_ylabel('Stacked Bar Graph')

# Add labels and title
plt.xticks(x_bar, categories)
plt.title('Line and Stacked Bar Graphs')

# Show the legend for both graphs
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()