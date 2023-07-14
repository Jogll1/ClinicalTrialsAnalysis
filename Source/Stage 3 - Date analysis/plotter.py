# test plotter
import matplotlib.pyplot as plt
import numpy as np

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])

xpoints1 = np.array([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015])

ypoints1 = np.array([5, 6, 3, 6, 24, 12, 14, 19, 22, 34, 20, 15, 5, 67, 45, 32])
ypoints2 = np.array([2, 34, 24, 17, 4, 6, 7, 13, 17, 26, 36, 31, 25, 7, 2, 3])

# marker|line|color
plt.plot(xpoints1, ypoints1, marker='o', c='#4caf50')
plt.plot(xpoints1, ypoints2, marker='o', c='#f4f5ad')
plt.show()