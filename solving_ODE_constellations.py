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
from sympy import *
from cardioLPN import A_R, A_L, A_C

#R, L, C = symbols('R L C', positive=True)
U_2, I_2 = symbols('U_2 I_2', positive=True)
U, I = symbols('U I', positive=True)

#t = symbols('t', positive=True, real = True)
#s = symbols('s', positive=True)

L = 10
C = 2
R = 1

A_CLR = A_C(C) * A_L(L) * A_R(R)
A_CRL = A_C(C) * A_R(R) * A_L(L)
A_LCR = A_L(L) * A_C(C) * A_R(R)
A_LRC = A_L(L) * A_R(R) * A_C(C)
A_RLC = A_R(R) * A_L(L) * A_C(C)
A_RCL = A_R(R) * A_C(C) * A_L(L)


# defining a function for U_2 and I_2
U_2 = 1/(s*(1+s*5))
#U_2 = 1/(s**2 + 0.5*s + 2)
I_2 = 1/(s*(1+s*15))

# defining
x_2 = Matrix([U_2, I_2])


''' Outputs '''

x_CLR = A_CLR * x_2
x_CRL = A_CRL * x_2

x_LCR = A_LCR * x_2
x_LRC = A_LRC * x_2

x_RLC = A_RLC * x_2
x_RCL = A_RCL * x_2


#
x_CLR_func = lambdify(s, x_CLR[0])
x_CRL_func = lambdify(s, x_CRL[0])

x_LCR_func = lambdify(s, x_LCR[0])
x_LRC_func = lambdify(s, x_LRC[0])

x_RLC_func = lambdify(s, x_RLC[0])
x_RCL_func = lambdify(s, x_RCL[0])


#t = np.linspace(0.01,20,20)
t = np.linspace(0.01,20,50)

X_CLR = []
X_LCR = []
X_CRL = []
X_LRC = []
X_RLC = []
X_RCL = []

for i in t:
    X_CRL.append(mp.invertlaplace(x_CRL_func, i, method = 'dehoog', dps = 10, degree = 18))
    X_CLR.append(mp.invertlaplace(x_CLR_func, i, method = 'dehoog', dps = 10, degree = 18))
    
    X_LCR.append(mp.invertlaplace(x_LCR_func, i, method = 'dehoog', dps = 10, degree = 18))
    X_LRC.append(mp.invertlaplace(x_LRC_func, i, method = 'dehoog', dps = 10, degree = 18))
    
    X_RLC.append(mp.invertlaplace(x_RLC_func, i, method = 'dehoog', dps = 10, degree = 18))
    X_RCL.append(mp.invertlaplace(x_RCL_func, i, method = 'dehoog', dps = 10, degree = 18))


U2_func = lambdify(s,U_2)
U2_time = []
for i in t:
    U2_time.append(mp.invertlaplace(U2_func, i, method = 'dehoog', dps = 10, degree = 18))

plt.plot(t, U2_time, "k", label = "U2")
plt.legend()
plt.savefig("u2.png")
plt.show()


plt.plot(t, X_CLR, "k*", label = "CLR")
plt.plot(t, X_LCR, "g", label = "LCR")
plt.plot(t, X_CRL, "y", label = "CRL")
plt.plot(t, X_LRC, "b", label = "LRC")
plt.plot(t, X_RLC, "r*", label = "RLC")
plt.plot(t, X_RCL, "c", label = "RCL")
plt.legend()
plt.savefig("u1.png")
plt.show()