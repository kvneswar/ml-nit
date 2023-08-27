import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# MATPLOT IS FOR VISUALIZATION
# SEABORN IS FOR ADVANCED VISUALIZATION

plt.plot(
    [2, 4, 6, 8],
    [10, 20, 30, 40],
    c='red',
    ls='--',
    marker='o',
    ms=20
)

plt.plot(
    [2, 4, 6, 8],
    [50, 60, 70, 80],
    c='green',
    ls='-',
    marker='*',
    ms=30
)

#plt.xticks([2, 4, 6, 8], rotation='vertical')

plt.title("TITLE")
plt.rcParams['figure.figsize'] = 1000, 6
plt.legend(loc = 'upper left')

plt.show()
