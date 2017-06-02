# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 21:32:54 2017

@author: alice
"""

import numpy as np
#import m matplotlib.pyplot as plt
#import mpmath as mp

P = np.array([14/16, 1/16, 1/16])

def simulP(P):#P = [[x1...xn], [p0...pn]]
    pCumul = np.cumsum(P[1])
    a = np.random.rand()
    n = len(P[0])
    i = 0
    while i < n and pCumul[i] < a:
        i += 1
    return P[1][i]