# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 16:09:56 2018

@author: CatOnTour
"""
from sympy import *
#from sympy.integrals.transforms import inverse_laplace_transform
#from sympy import exp, Symbol
from sympy.abc import s, t
from sympy.integrals.transforms import inverse_laplace_transform

from cardioLPN import A_R, A_L, A_C
from sympy import symbols

"""
a = Symbol('a', positive=True)

inv_solv = inverse_laplace_transform(exp(-a*s)/s, s, t)

print(inv_solv)
"""

R_p, R_d, R, L, C = symbols('R_p, R_d R L C', positive=True)
U_2, I_2 = symbols('U_2 I_2', positive=True)
U, I = symbols('U I', positive=True)

# testing

A_result = A_C(C)*A_L(L)*A_R(R)
print(A_result)

#x_2 = Matrix([U_2, -I_2])
x_2 = Matrix([1/(s*(1+s*5)), 1/(s*(1+s*5))])


x_1 = A_result * x_2
print(x_1)

#u_1 = inverse_laplace_transform(x_1[0], s, t)

x = Matrix([U, -I])
ODE = A_result * x - x


## Beispiel aus der Pub 0D/3D coupling
A_result_2 = A_R(R_p)*A_C(C)*A_R(R_d)
#x_val = Matrix([0, -I])
x_val = Matrix([0, -(1/(2*s**3+2*s))])
res = A_result_2  * x_val

P_ex = inverse_laplace_transform(res[0], s, t)

#
#A_ex = A_L(L)*A_R(R)*A_R(R)*A_C(C)*A_L(L)
#
#A_ex_2 = A_R(R)*A_C(C)*A_L(L)*A_L(L)*A_R(R)
#
#A_ex_3 = A_C(C)*A_L(L)*A_R(R)
#
#A_ex_4 = A_L(L)*A_R(R)*A_C(C)
#
#eig = A_ex.eigenvals()
#
#factor_list(expand(A_ex[1]))
#testing = expand(A_ex[1])
#a = Poly(testing, s)
#
#a.coeffs()