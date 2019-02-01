
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

# from sklearn import svm

import matplotlib.pyplot as plt
import seaborn as sns
# import create_data
from mpl_toolkits import mplot3d

sns.set(font_scale=1)


recipies = pd.read_csv('data.csv')

fig = plt.figure()
ax = plt.axes(projection='3d')

# Data for a three-dimensional line
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'gray')

# Data for three-dimensional scattered points
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')


plt.show()
