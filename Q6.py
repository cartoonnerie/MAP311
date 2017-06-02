# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 21:38:11 2017

@author: alice
"""

import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp

#Q6a

#loi de X [a , b, c]
Px = np.array([14/16, 1/16, 1/16])

#entropie d'une variable aléatoire
def Hx(P):
    somme = 0.
    for p in P:
        if p != 0.: 
        #on ne fait rien si p = 0 (convention)
            somme += -p * mp.log(p, 2)
    return somme

#loi de Y|X sous forme de tableau Pxy[0] = P_Y|X = x0
Pxy = np.array([[1., 0.], [0., 1.],[0., 1.]])

def Hxy(Px, P): #len(Px) = len(P)
    somme = 0.
    n = len(P)
    for i in range(n):
        somme += Px[i] * Hx(P[i])
    return somme

Hx(Px)
Xxy(Pxy)

#Q6b Q6c