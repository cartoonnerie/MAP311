#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
#import mpmath as mp
from scipy.special import binom

#loi binomiale B(N,p)
N = 7
p = 0.562

#Nombre de simulation
n=50


def simError(n) :
     #simulation de n variables aléatoires indépendante de loi B(N, p)
    sim = np.random.binomial(N, p, n)
    
    #calcul des fréquences pour approximer les propabilités de chaque réalisation
    freqs = np.bincount(sim, minlength=N) / n
    
    #calcul du produit des frequence, approximation du produit des probabilités
    prod = np.prod(freqs)
    
    #[INUTILE][ERREUR] calcul théorique du produit des probabilités
    #theo = (p * (1 - p) ) ** (N * (N + 1) / 2) * mp.superfac(N) ** 2 / mp.factorial(N) ** (N +1)
    
    #Calcul de la probabilité p(x)
    def pX(x):
        return binom(N, x)  * p**x * (1-p)**(N-x)
    
    #calcul de l'entropie theorique
    H = - sum([pX(k) * np.log2(pX(k)) for k in range(N+1)])
    
    #print(prod, theo)
    return prod - 2**(-n*H)
    
    
plt.plot(range(1, n, max(n//100,1)),
         [simError(i) for i in range(1, n, max(n//100,1))],
         label="Produit[p(x)] - 2^(-nH)")
plt.title("Approche intuitive de l'entropie")
plt.xlabel('Nombre de simulation')
plt.legend(loc='best')
#plt.savefig('Q1.jpg', dpi=600)
plt.draw()