# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 11:36:46 2019

@author: CatOnTour
"""

import mpmath as mp
import numpy as np
import matplotlib.pyplot as plt

def f(s):
    return 1 / (s-1)

t = np.linspace(0.01,10,20)

G = []

for i in t:
    G.append(mp.invertlaplace(f, i, method = 'dehoog', dps = 10, degree = 18))


plt.plot(t, G)
plt.show()