# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:43:24 2019

@author: CatOnTour
"""

from sympy import *
from cardioLPN import *
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

def sympy_to_num_den(xpr, s=Symbol('s')):
    num, den = simplify(xpr).as_numer_denom()  # expressions
    p_num_den = poly(num, s), poly(den, s)  # polynomials
    c_num_den = [expand(p).all_coeffs() for p in p_num_den]  # coefficients
    l_num, l_den = [lambdify((), c)() for c in c_num_den]  # convert to floats
    return l_num, l_den
    

#R1, C, R2= symbols('R1 C R2', positive=True)

A_RCR = A_R(0.1) * A_C(0.01) * A_R(0.03)

A_result = simplify(A_RCR**5)
A_result = simplify(trans_A2H(A_RCR))

num00, den00 = sympy_to_num_den(A_result[0, 0])
cont_sys_00 = signal.lti(num00, den00)

num01, den01 = sympy_to_num_den(A_result[0, 1])
cont_sys_01 = signal.lti(num01, den01)


u1 = cont_sys_00.impulse()[1] + cont_sys_01.step()[1]

plt.plot(u1)
plt.show()

num10, den10 = sympy_to_num_den(A_result[1, 0])
cont_sys_10 = signal.lti(num10, den10)

num11, den11 = sympy_to_num_den(A_result[1, 1])
cont_sys_11 = signal.lti(num11, den11)


i2 = cont_sys_10.impulse()[1] + cont_sys_11.step()[1]

plt.plot(-i2)
plt.show()


# inputs

plt.plot(signal.unit_impulse(100))
plt.show()

plt.plot(np.append([0], np.linspace(0,100,101)),np.append([0], np.ones(101)))
plt.show()

#A_result = simplify(A_RCR)
#
#num00, den00 = sympy_to_num_den(A_result[0, 0])
#cont_sys_00 = signal.lti(num00, den00)
#
#num01, den01 = sympy_to_num_den(A_result[0, 1])
#cont_sys_01 = signal.lti(num01, den01)
#
#
#u1 = cont_sys_00.step()[1] - cont_sys_01.impulse()[1]
#
#plt.plot(u1)
#plt.show()
#
#num10, den10 = sympy_to_num_den(A_result[1, 0])
#cont_sys_10 = signal.lti(num10, den10)
#
#num11, den11 = sympy_to_num_den(A_result[1, 1])
#cont_sys_11 = signal.lti(num11, den11)


#i2 = cont_sys_10.step()[1] - cont_sys_11.impulse()[1]
#
#plt.plot(i2)
#plt.show()


