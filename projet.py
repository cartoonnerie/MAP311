#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp

#constant
p = 0.5625965771739638
N = 713

limit = (0.1, 1.3, 0.002)
l = np.arange(*limit)
size = l.size
ns = np.zeros(size, dtype='int64')
freqs = np.zeros((size, N))
prod = np.zeros(size)
theo = np.zeros(size)
i = -1

for k in l:
    #n = int(10 ** k)
    print(n)
    i += 1

    ns[i] = n
    #simulation de n variables aléatoires indépendante de loi B(N, p)
    sim = np.random.binomial(N, p, n)
    
    #calcul des fréquences pour approximer les propabilités de chaque réalisation
    freqs[i] = np.bincount(sim, minlength=N) / n
    
    #calcul du produit des frequence, approximation du produit des probabilités
    prod[i] = np.prod(freqs)
    
    #calcul théorique du produit des probabilités
    theo[i] = (p * (1 - p) ) ** (n * (n + 1) / 2) * mp.superfac(n) ** 2 / mp.factorial(n) ** (n +1)
    pass

#plt.hist(sim, normed=1, bins=int(n**(1/3)))
#plt.plot([i for i in range(len(freqs))], freqs)

plt.plot(ns, prod - theo, '-')
plt.draw()