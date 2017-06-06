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

#loi de Y|X sous forme de tableau Pxy[0] = P_Y|(X = x0)
Pxy = np.array([[1., 0.], [0., 1.],[0., 1.]])

def Hxy(Px, P): #len(Px) = len(P)
    somme = 0.
    n = len(P)
    for i in range(n):
        somme += Px[i] * Hx(P[i])
    return somme


limit = Hxy(Px, Pxy)

#Q6b 

k = 5000
X = np.random.choice(['a', 'b', 'c'], k, p=Px)
Y = np.zeros(X.shape, dtype ='int32')
Y[X != 'a'] = 1
I = np.zeros((k, 3))
for i in range(k) :
    I[i] = Pxy[:, Y[i]] * Px / np.sum(Px * Pxy[:, Y[i]])
H = np.zeros(k)
Prod = I * np.log2(I)
Prod[I == 0.0] = 0
for i in range(k) :
    H[i] = np.sum(Prod)

plt.plot(range(k), H / range(k) + 1)
plt.plot(range(k), np.array(range(k)) * limit)
plt.ymax = 1

plt.show()

#Q6c