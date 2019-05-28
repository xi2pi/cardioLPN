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

def sympy_to_dlti(xpr, s=Symbol('s')):
    """ Convert Sympy transfer function polynomial to Scipy LTI """
    num, den = simplify(xpr).as_numer_denom()  # expressions
    p_num_den = poly(num, s), poly(den, s)  # polynomials
    c_num_den = [expand(p).all_coeffs() for p in p_num_den]  # coefficients
    l_num, l_den = [lambdify((), c)() for c in c_num_den]  # convert to floats
    return signal.dlti(l_num, l_den, dt = 0.1)
    
    
def sympy_to_num_den(xpr, s=Symbol('s')):
    num, den = simplify(xpr).as_numer_denom()  # expressions
    p_num_den = poly(num, s), poly(den, s)  # polynomials
    c_num_den = [expand(p).all_coeffs() for p in p_num_den]  # coefficients
    l_num, l_den = [lambdify((), c)() for c in c_num_den]  # convert to floats
    return l_num, l_den

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


H = trans_A2H(A_CLR)

test_func = sympy_to_dlti(H[1, 1])
num, den = sympy_to_num_den(H[1, 1])

#test_func.to_discrete(0.05)

#signal.cont2discrete(test_func)

#signal.cont2discrete((num, den), 0.2)


#dlti.output()

#tf = ([1.0,], [1.0, -1.0], 1.0)
tf = (num, den, 0.1)
t_in = np.linspace(0, 100)
u = np.ones_like(t_in)
t_out, y = signal.dlsim(tf, u, t=t_in)
#y.T
#dis_sys = signal.dlti(num, den, 0.01).step()
cont_sys = signal.lti(num, den)
cont_sys_out = signal.lti(num, den).step()

dis_sys = cont_sys.to_discrete(1)
dis_sys_out = dis_sys.step()


#plt.plot(dis_sys[0], dis_sys[1][0])
plt.plot(cont_sys_out[0], cont_sys_out[1])
plt.plot(dis_sys_out[0], dis_sys_out[1][0])
#plt.plot(t_in, u, ".")
#plt.plot(t_out, y, ".")
plt.show()



