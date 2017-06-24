# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 09:30:45 2017

@author: alice
"""
import heapq


def occurencies(s):
    rep = {}
    for char in s :
        rep[char] = rep.setdefault(char, 0) + 1
    return rep
    pass


def InitTokenClass(occurence) :
    class Token:
        
        occ = occurence   
        
        def __init__(self, value) :
            if not value in Token.occ.keys() :
                raise ValueError
            self.value = value
            pass
        
        def __lt__(self, other) :
            if isinstance(other, Token) :
                return Token.occ[self.value] < Token.occ[other.value]
            else :
                raise NotImplementedError
                pass
            pass
        
        def __le__(self, other) :
            if isinstance(other, Token) :
                return Token.occ[self.value] <= Token.occ[other.value]
            else :
                raise NotImplementedError
                pass
            pass
        
        def __ge__(self, other) :
            if isinstance(other, Token) :
                return Token.occ[self.value] >= Token.occ[other.value]
            else :
                raise NotImplementedError
                pass
            pass
        
        def __gt__(self, other) :
            if isinstance(other, Token) :
                return Token.occ[self.value] > Token.occ[other.value]
            else :
                raise NotImplementedError
                pass
            pass
        
        def __str__(self) :
            return str(self.value)
        pass
    
        def __repr__(self) :
            return str(self)
    
    return Token

s = 'abebbcdadef'#'sckyejvtscloqpcjvovioqzbjhquviydrf'
sunit = set(s) #pas utilisé, pourquoi ?
tas = []
Char = InitTokenClass(occurencies(s))
for i in sunit :
    heapq.heappush(tas, Char(i))
    pass
print(tas)

def tasOccurences(s):
    sunit = set(s)
    tas = []
    Char = InitTokenClass(occurencies(s))
    for i in sunit :
        heapq.heappush(tas, Char(i))
    return tas

def huffman(s):
    tas = []
    Char = InitTokenClass(occurencies(s))
    for i in sunit :
        heapq.heappush(tas, Char(i))
    res = {}
    def huffAux():
        if len(tas) > 2:
            a = heapq.heappop(tas)
            b = heapq.heappop(tas)
            c = a.value + b.value
            Char.occ[c] = Char.occ[a.value] + Char.occ[b.value]
            heapq.heappsuh(tas, Char(c))
            pass
        