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
    #Creation du tas
    tas = []
    #Creation du dictionnaire des occurences
    occ = occurencies(s)
    #Initialisation du tas :
    #chaque lettre est ajoutée une fois,
    #sous la forme d'une feuille d'un arbre de Huffman
    #La classe Token redéfinie les comparaisons afin de pouvoir utiliser
    #le module heapq sans recoder les tas.
    for char in set(s) :
        heapq.heappush(tas, Token(HuffTree(char), occ[char]))
    
    #Fonction auxiliaire récursive        
    def aux(tas):
        #extraction des des plus petits éléments
        small = heapq.heappop(tas)
        big = heapq.heappop(tas)
        if len(tas) == 0:
            #si le tas ne contenait que deux elements, on a atteint la dernière etape
            return HuffTree(small.value + big.value, (small, big))
        else :
            #s'il reste des elements, alors :
            #  - On construit l'arbre de huffman des deux plus petit elements:
            #  - On lui donne une probabilité égale à la somme des probabilités
            #    des elements qu'il represente
            #  - On continue la construction de l'arbre
            heapq.heappush(tas, Token(HuffTree(small.value + big.value,
                                               (small,big)),
                                      small._Token__comp + big._Token__comp))
            return aux(tas)
    #la fonction récursive construit un HuffTree, il n'y a plus qu'a le convertir
    #sous une forme plus utile pour l'encodage, un dictionnaire.
    return aux(tas).toDict('')

    
#questionD

def genererMot(size, chars): 
#https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
    return ''.join(random.choice(chars) for _ in range(size))

longueur = 26
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
d = len(alphabet)
texte = genererMot(longueur, alphabet)
print(texte)
codage = huffman(texte) #attendu un dicttionnaire de la forme {char : codage}
freq = np.array([x for x in occurencies(texte).values()])
freq = freq / longueur
#entropie = Q6.Hx(freq)

#avg = np.average(np.array([x for x in codage.values()]))
#print((avg, entropie/np.log2(d) + 1))
        