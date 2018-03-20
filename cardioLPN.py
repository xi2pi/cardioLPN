# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 16:09:56 2018

@author: CatOnTour
"""
from sympy import Matrix
#from sympy import exp, Symbol
from sympy.abc import s, t

#R, L, C = symbols('R L C', positive=True)

def A_R(R_value):
    return Matrix([[1 , R_value], [0 , 1]])
    
def A_L(L_value):
    return Matrix([[1 , L_value*s], [0 , 1]])
    
def A_C(C_value):
    return Matrix([[1 , 0], [C_value*s , 1]])



