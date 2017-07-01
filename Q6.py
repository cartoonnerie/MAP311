# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt

#Q6a

#loi de X à valeur dans {a , b, c}
Px = np.array([14/16, 1/16, 1/16])

#entropie d'une variable aléatoire, où P est l'array des probabilités
def Hx(P):
   return -sum([p*np.log2(p) for p in P if p != 0])

#Entropie de X
H = Hx(Px)
print("H(X) = ", H)


#loi de Y|X sous forme de tableau Pxy[0] = P_Y|(X = x0)
Pxy = np.array([[1., 0.], [0., 1.],[0., 1.]])
#loi de X|Y sous forme de tableau Pxy[0] = P_X|(Y = y0)
Pyx = np.array([[1., 0., 0.], [0., 0.5, 0.5]])

#Py
Py = [14./16, 2./16]

#entropie de X|Y
def Hxy(Px, P): #len(Px) = len(P)
    n = len(P)
    return sum([Px[i] * Hx(P[i]) for i in range(n)])

limit = Hxy(Py, Pyx)
print("H(X|Y) = ", limit)

#Q6b 

#mise en place de k réalisations de X et Y

k = 10000
def simul(k):
    #mise en place de k réalisations de X et Y
    X = np.random.choice([0, 1, 2], k, p=Px)
    Y = np.zeros(X.shape, dtype ='int32')
    Y[X != 0] = 1
    #I sera la loi de X|Y = y_i, H l'entropie de cette loi
    I = np.zeros((k, 3))
    H = np.zeros(k)
    
    I[0] = Pxy[:, Y[0]] * Px / np.sum(Px * Pxy[:, Y[0]])
    H[0] = Hx(I[0])
    
    for i in range(1,k) :
        I[i] = Pxy[:, Y[i]] * Px / np.sum(Px * Pxy[:, Y[i]])
        if Hx(I[i]) > Hx(Px):
            print(Hx(I[i]))
            print(i, I[i])
        H[i] = (Hx(I[i]) + (i-1) * H[i-1])/i
    return H

def Q6b(k):
    simu = simul(k)
    plt.plot(range(k), simu)
    plt.plot(range(k), np.ones(k) * limit)
    plt.ymax = 1
    
    plt.show()
    return None
