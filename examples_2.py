# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 16:28:43 2019

@author: CatOnTour
"""

from sympy import *
from cardioLPN import *
from sympy.utilities.iterables import variations
from functools import reduce

#R1, C, R2= symbols('R1 C R2', positive=True)
#A_RCR = A_R(R1) * A_C(C) * A_R(R2)
#trans_A2Z(A_RCR)


R, L, C = symbols('R L C', positive=True)
#A_CLR = A_C(C) * A_L(L) * A_R(R)

List_variations = list(variations([A_C(C),A_L(L),A_R(R)], 3))


reduce((lambda x, y: x * y), List_variations[0]) 


