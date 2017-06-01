#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp

p = 0.5625965771739638
N = 7

def simError(n) :
     #simulation de n variables aléatoires indépendante de loi B(N, p)
    sim = np.random.binomial(N, p, n)
    
    #calcul des fréquences pour approximer les propabilités de chaque réalisation
    freqs = np.bincount(sim, minlength=N) / n
    
    #calcul du produit des frequence, approximation du produit des probabilités
    prod = np.prod(freqs)
    
    #calcul théorique du produit des probabilités
    theo = (p * (1 - p) ) ** (N * (N + 1) / 2) * mp.superfac(N) ** 2 / mp.factorial(N) ** (N +1)
    #print(prod, theo)
    return prod - theo
    
    
plt.plot(range(1, 100000, 10), [simError(i) for i in range(1, 100000, 10)])
plt.draw()