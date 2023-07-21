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

# Sample data
categories = ['Category A', 'Category B', 'Category C']
data1 = [20, 30, 40]
data2 = [10, 25, 35]
data3 = [5, 15, 25]

# Create an array of positions for the bars
x = np.arange(len(categories))

# Plot the first set of bars
plt.bar(x, data1, label='Data 1')

# Plot the second set of bars on top of the first set
plt.bar(x, data2, bottom=data1, label='Data 2')

# Plot the third set of bars on top of the previous two
plt.bar(x, data3, bottom=np.add(data1, data2), label='Data 3')

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Stacked Bar Chart')
plt.xticks(x, categories)
plt.legend()

# Show the plot
plt.show()