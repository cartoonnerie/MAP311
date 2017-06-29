# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 09:30:45 2017

@author: alice
"""
import heapq
import random
import numpy as np
from CustomObjects import Token, HuffTree

import Q6


def occurencies(s):
    rep = {}
    for char in s :
        rep[char] = rep.setdefault(char, 0) + 1
    return rep
    pass

def huffman(s):
    tas = []
    occ = occurencies(s)
    for char in set(s) :
        heapq.heappush(tas, Token(char, occ[char]))
        
    def aux(tas):
        


for i in sunit :
    heapq.heappush(tas, Char(i))
    pass
print(tas)

def tasOccurences(s):
    sunit = set(s)
    tas = []
    for i in sunit :
        heapq.heappush(tas, Token(i, ))
    return tas

def huffman(s): #tentative non aboutie

    tas = []
    Char = InitTokenClass(occurencies(s))
    for i in sunit :
        heapq.heappush(tas, Char(i))
    res = {}
    
    

#questionD

def genererMot(size, chars): 
#https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
    return ''.join(random.choice(chars) for _ in range(size))

longueur = 13
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
d = len(alphabet)
texte = id_generator(longueur, alphabet)
print(texte)
#codage = huffman(texte) #attendu un dicttionnaire de la forme {char : codage}
freq = np.array([x for x in occurencies(texte).values()])
freq = freq / longueur
entropie = Q6.Hx(freq)

#avg = np.average(np.array([x for x in codage.values()]))
#print((avg, entropie/np.log2(d) + 1))
        