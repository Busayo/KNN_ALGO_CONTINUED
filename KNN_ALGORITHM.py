# import numpy as np
import matplotlib.pyplot as plt
# import warnings
# from math import sqrt
# from collections import Counter

from matplotlib import style

style.use('fivethirtyeight')

dataset = {'K': [[1, 2], [2, 3], [3, 1]],
           'r': [[6, 5], [7, 7], [8, 6]]
           }

new_features = [5, 7]

[[plt.scatter(ii[0], ii[1], s=100, color=i) for ii in dataset[i]] for i in dataset]

plt.scatter(new_features[0], new_features[1])
plt.show()
