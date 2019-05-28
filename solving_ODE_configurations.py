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
from scipy import signal
from cardioLPN import *

def sympy_to_lti(xpr, s=Symbol('s')):
    """ Convert Sympy transfer function polynomial to Scipy LTI """
    num, den = simplify(xpr).as_numer_denom()  # expressions
    p_num_den = poly(num, s), poly(den, s)  # polynomials
    c_num_den = [expand(p).all_coeffs() for p in p_num_den]  # coefficients
    l_num, l_den = [lambdify((), c)() for c in c_num_den]  # convert to floats
    return signal.lti(l_num, l_den)

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


Z_CLR = simplify(trans_A2Z(A_CLR))
Y_CLR = simplify(trans_A2Y(A_CLR))
H_CLR = simplify(trans_A2H(A_CLR))
P_CLR = simplify(trans_A2P(A_CLR))
B_CLR = simplify(trans_A2B(A_CLR))


# defining a function for U_2 and I_2
x_21 = 1/(s*(1+s*5))
#U_2 = 1/(s**2 + 0.5*s + 2)
x_22 = 1/(s*(1+s*15))

# defining
x_2 = Matrix([x_21, x_22])


''' Outputs '''

x_A = A_CLR * x_2
x_Z = Z_CLR * x_2
x_Y = Y_CLR * x_2
x_H = H_CLR * x_2
x_P = P_CLR * x_2
x_B = B_CLR * x_2


#
x_A_func = lambdify(s, x_A[0])
x_Z_func = lambdify(s, x_Z[0])
x_Y_func = lambdify(s, x_Y[0])
x_H_func = lambdify(s, x_H[0])
x_P_func = lambdify(s, x_P[0])
x_B_func = lambdify(s, x_B[0])



#t = np.linspace(0.01,20,20)
t = np.linspace(0.01,20,50)

X_A = []
X_Z = []
X_Y = []
X_H = []
X_P = []
X_B = []

for i in t:
    X_A.append(mp.invertlaplace(x_A_func, i, method = 'dehoog', dps = 10, degree = 18))
    X_Z.append(mp.invertlaplace(x_Z_func, i, method = 'dehoog', dps = 10, degree = 18))
    X_Y.append(mp.invertlaplace(x_Y_func, i, method = 'dehoog', dps = 10, degree = 18)) 
    X_H.append(mp.invertlaplace(x_H_func, i, method = 'dehoog', dps = 10, degree = 18))
    X_P.append(mp.invertlaplace(x_P_func, i, method = 'dehoog', dps = 10, degree = 18))    
    X_B.append(mp.invertlaplace(x_B_func, i, method = 'dehoog', dps = 10, degree = 18))


x_21_func = lambdify(s, x_21)
x_21_time = []
for i in t:
    x_21_time.append(mp.invertlaplace(x_21_func, i, method = 'dehoog', dps = 10, degree = 18))

plt.plot(t, x_21_time, "k", label = "U2")
plt.legend()
plt.savefig("constellation_x_21.png")
plt.show()


plt.plot(t, X_A, "k*", label = "A")
plt.plot(t, X_Z, "c", label = "Z")
plt.plot(t, X_Y, "g", label = "Y")
plt.plot(t, X_H, "y", label = "H")
plt.plot(t, X_P, "b", label = "P")
plt.plot(t, X_B, "r*", label = "B")

plt.legend()
plt.savefig("constellation_X.png")
plt.show()


