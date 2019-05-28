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
    



A_result = A_L(0.1) 
Y_result = simplify(trans_A2Y(A_result))

num00, den00 = sympy_to_num_den(Y_result[0, 0])
cont_sys_00 = signal.lti(num00, den00)

num01, den01 = sympy_to_num_den(Y_result[0, 1])
cont_sys_01 = signal.lti(num01, den01)


I1 = cont_sys_00.output([2,2,2,2], [0,1,2,3])[1] + cont_sys_01.output([1,1,1,1], [0,1,2,3])[1]

plt.plot(I1)
plt.show()

'''variation of L'''
# step 1
A_result = A_L(0.1) 
Y_result = simplify(trans_A2Y(A_result))

num00, den00 = sympy_to_num_den(Y_result[0, 0])
cont_sys_00 = signal.lti(num00, den00)

num01, den01 = sympy_to_num_den(Y_result[0, 1])
cont_sys_01 = signal.lti(num01, den01)


I1_1 = cont_sys_00.output([2,2,2,2], [0,1,2,3])[1] + cont_sys_01.output([1,1,1,1], [0,1,2,3])[1]

# step 2
A_result = A_L(0.2) 
Y_result = simplify(trans_A2Y(A_result))

num00, den00 = sympy_to_num_den(Y_result[0, 0])
cont_sys_00 = signal.lti(num00, den00)

num01, den01 = sympy_to_num_den(Y_result[0, 1])
cont_sys_01 = signal.lti(num01, den01)


I1_2 = cont_sys_00.output([2,2,2,2], [3,4,5,6])[1] + cont_sys_01.output([1,1,1,1], [3,4,5,6])[1]

I1 = np.append(I1_1[:-1], I1_2 + I1_1[-1]) 
plt.plot(I1)
plt.show()

#num10, den10 = sympy_to_num_den(Y_result[1, 0])
#cont_sys_10 = signal.lti(num10, den10)
#
#num11, den11 = sympy_to_num_den(Y_result[1, 1])
#cont_sys_11 = signal.lti(num11, den11)
#
#
#I2 = cont_sys_10.output([2,2,2,2], [0,1,2,3])[1] + cont_sys_11.output([1,1,1,1], [0,1,2,3])[1]
#
#plt.plot(-I2)
#plt.show()








'''old'''
# inputs

#plt.plot(signal.unit_impulse(100))
#plt.show()
#
#plt.plot(np.append([0], np.linspace(0,100,101)),np.append([0], np.ones(101)))
#plt.show()

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


