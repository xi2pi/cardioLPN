# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 11:36:46 2019

@author: CatOnTour
"""

import mpmath as mp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sympy.abc import s
from sympy.integrals.transforms import inverse_laplace_transform
from sympy import symbols, lambdify
from sympy import *
from scipy import signal
from cardioLPN import *

import scipy.optimize as optimization


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



#L = 25
#C = 2.3
#R = 1.5

def error_func(para, y_measured):
    L = para[0]
    C = para[1]
    R = para[2]
    A_CLR = A_C(C) * A_L(L) * A_R(R)
    H = trans_A2H(A_CLR)
    
    
    test_func = sympy_to_dlti(H[1, 1])
    num, den = sympy_to_num_den(H[1, 1])
    
    cont_sys = signal.lti(num, den)
    
    dis_sys = cont_sys.to_discrete(0.1)  
    
    # Input
    t_in = np.linspace(0, 50, 200)
    u_in = np.sin(t_in) + 2
     
    # Output
    u_out = dis_sys.output(u_in, t_in)
    y = [i[0] for i in u_out[1].tolist()]
    
    plt.plot(u_out[0], y_measured, label = "measured signal")
    plt.plot(u_out[0], y, "r", label = "model output")
    plt.legend()
    plt.show()
    
    sum_distance = sum((y-y_measured)**2)
    return sum_distance
    
y_measured = pd.read_csv("u_out.csv")
    
res_opt = optimization.minimize(error_func, [10, 2.3, 1], args=(y_measured["u_out"].values), method='Nelder-Mead')
    
    
    

