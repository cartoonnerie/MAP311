#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import scipy as sps

def ex1a(n) :
    cartes = list(range(n))
    suppr = []
    while len(cartes) > 1 :
        suppr.append(cartes.pop(0))
        cartes.append(cartes.pop(0))
    return cartes, suppr
    pass

def ex1b(a) :
    x = np.arange(-a, a, (2 * a) / 1000)
    y = np.ones(x.size)
    print(x,y)
    y[x != 0.0] = np.sin(x[x!=0.0]) / x[x!=0.0]
    plt.plot(x, y, color='r', label='graph de sin(x) /x')
    plt.title("a random title")
    plt.legend(loc="best")
    plt.show()
    pass

#ex1b(20 * np.pi)

def ex1c(n, m) :
    for j in range(m) :
        fibo = []
        fibo.append(np.random.random())
        fibo.append(np.random.random())
        s = 2 * np.random.binomial(1, .5, n-2) - 1
        for i in range(n - 2) :
            fibo.append(fibo[-1] + s[i] * fibo[-2])
        plt.plot(range(n), fibo)
    plt.show()
    pass

#ex1c(50 ,9)

def gdnb(n) :
    X = np.random.uniform(-1, 1, n)
    S = X.cumsum()
    S = S / np.array(range(n))
    plt.plot(range(n), S)
    plt.show()
    pass

#gdnb(15000)

def gdnbCauchy(n) :
    X = np.random.uniform(-1, 1, n)
    Y = np.tan(np.pi * X / 2)
    S = Y.cumsum()
    S = S / np.array(range(n))
    plt.plot(range(n), S)
    plt.show()
    pass

#gdnbCauchy(150000)


def thCentLim(n, m) :
    X = np.random.uniform(-1, 1, (m, n))
    mu = 0 #np.mean(X, axis=1)
    sigma = 1/ np.sqrt(3) #np.std(X, axis=1)
    S = np.sqrt(n) * (np.sum(X, axis = 1)/ n - mu) / sigma
    plt.hist(S, normed=True, bins=40)
    x = np.arange(-10, 10, 40/10000)
    plt.plot(x, 1/np.sqrt(2*np.pi) * np.exp(- x ** 2 / 2))
    plt.show()
    pass

#thCentLim(10000, 10000)

def ex4a(n):
    X = 2 * np.random.rand(n) - 1
    Y = 2 * np.random.rand(n) - 1
    S = X + Y
    plt.hist(S, normed=1, bins=int(n**(1/3)))
    x = np.arange(-2, 2, 4/ 100)
    plt.plot(x, np.maximum(2 - np.abs(x), 0) / 4)
    plt.show()
    pass

#ex4a(100000)

def ex4b(n) :
    X = np.random.exponential(1, n)
    Y = np.random.exponential(1, n)
    S = X + Y
    plt.hist(S, normed=1, bins=int(n**(1/3)))
    x = np.arange(0, S.max(), S.max() / 1000)
    plt.plot(x, x * np.exp(-x))
    plt.show()
    pass

#ex4b(100000)


def ex4c(n, t) :
    X = np.random.exponential(1, 2 * n)
    Xt = X[X>t] - t
    data = np.vstack([X[:Xt.size], Xt]).T
    #plt.hist(X, normed=1, bins=int(n**(1/3)), alpha=0.5)
    #plt.hist(Xt, normed=1, bins=int(n**(1/3)), alpha=0.5)
    plt.hist(data, normed=1, bins=int(n**(1/3)), label=['X', 'X | X > t'], alpha=0.7 )
    plt.legend(loc='best')
    plt.show()
    pass

#Nex4c(100000, 0.5)

def ex5(n, m) :
    U = np.random.rand(n, m) *4 - 2
    V = np.random.rand(n, m) / np.pi
    t = V[V <= np.sqrt(4 - U ** 2) / np.pi / 2].reshape(n).min(axis=1)
    plt.hist(t, normed=1, bins=int(n**(1/3)))
    x = np.arange(-2,2, 4/10000)
    plt.plot(x, np.sqrt(4 - x ** 2) / np.pi / 2)
    plt.plot()
    pass

#ex5(1000, 1000000)
    




     