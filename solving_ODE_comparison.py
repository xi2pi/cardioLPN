# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 11:36:46 2019

@author: CatOnTour
"""

import mpmath as mp
import numpy as np
import matplotlib.pyplot as plt
from sympy.abc import s
from sympy.integrals.transforms import inverse_laplace_transform
from sympy import symbols, lambdify

# analytic
f_sdomain = s / (s-1)

time = symbols('time', positive=True, real = True)
f_tdomain = inverse_laplace_transform(f_sdomain, s, time)

f_tdomain_func = lambdify(time, f_tdomain)



# numerical 
def f(s):
    return 100 / (s**2 + 0.5*s + 2)
t = np.linspace(0.01,20,100)

G = []

for i in t:
    G.append(mp.invertlaplace(f, i, method = 'dehoog', dps = 10, degree = 18))
    
# dps: decimal places
# degree: Number of terms used in the approximation


#F = [f_tdomain_func(t_) for t_ in t]

#plt.plot(t, F, "r*")
plt.plot(t, G, "b")
plt.show()