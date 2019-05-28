# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 16:09:56 2018

@author: CatOnTour
"""
from sympy import Matrix
from sympy import exp, Symbol, symbols
from sympy.abc import s, t

R_1, R_2, L, C = symbols('R1 R2 L C', positive=True)

'''Resistance'''
def A_R(R_value):
    return Matrix([[1 , R_value], [0 , 1]])

def Y_R(R_value):
    return Matrix([[1/R_value , -1/R_value], [-1/R_value , 1/R_value]])
    
def H_R(R_value):
    return Matrix([[R_value, 1], [-1 , 0]])
    
def P_R(R_value):
    return Matrix([[0 , 1], [-1 , R_value]])
    
def B_R(R_value):
    return Matrix([[1 , -R_value], [0 , 1]])

'''Inductance'''   
def A_L(L_value):
    return Matrix([[1 , L_value*s], [0 , 1]])
    
def Y_L(L_value):
    return Matrix([[1/L_value , -1/L_value], [-1/L_value , 1/L_value]])
    
def H_L(L_value):
    return Matrix([[L_value, 1], [-1 , 0]])
    
def P_L(L_value):
    return Matrix([[0 , 1], [-1 , L_value]])
    
def B_L(L_value):
    return Matrix([[1 , -L_value], [0 , 1]])
  
'''Conductance'''  
def A_C(C_value):
    return Matrix([[1 , 0], [C_value*s , 1]])
    
def Z_C(C_value):
    return Matrix([[1/(C_value*s) , 1/(C_value*s)], [1/(C_value*s), 1/(C_value*s)]])
    
def H_C(C_value):
    return Matrix([[1, 1], [-1 , C_value*s]])
    
def P_C(C_value):
    return Matrix([[C_value*s , -1], [1 , 0]])
    
def B_C(C_value):
    return Matrix([[1 , 0], [-C_value*s , 1]])
    
    
##########################################
##### Transformations
    
    
def trans_A2Z(A):
    A10 = A[1,0]
    Z = Matrix([[A[0,0]/A10 , A.det()/A10], [1/A10, A[1,1]/A10]])
    return Z

def trans_A2Y(A):
    A01 = A[0,1]
    Y = Matrix([[A[1,1]/A01 , -A.det()/A01], [-1/A01, A[0,0]/A01]])
    return Y

def trans_A2H(A):
    A11 = A[1,1]
    H = Matrix([[A[0,1]/A11 , A.det()/A11], [-1/A11, A[1,0]/A11]])
    return H   
    
def trans_A2P(A):
    A00 = A[0,0]
    P = Matrix([[A[1,0]/A00 , -A.det()/A00], [1/A00, A[0,1]/A00]])
    return P    

def trans_A2B(A):
    A_det = A.det()
    B = Matrix([[A[1,1]/A_det , -A[0,1]/A_det], [-A[1,0]/A_det, A[0,0]/A_det]])
    return B

