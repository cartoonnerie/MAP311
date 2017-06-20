# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 09:30:45 2017

@author: alice
"""
import heapq


def occurencies(s):
    rep = {}
    for char in s :
        rep[0] = rep.setdefault(char, 0) + 1
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

s = 'sckyejvtscloqpcjvovioqzbjhquviydrf'
sunit = set(s)
tas = []
Char = InitTokenClass(occurencies(s))
for i in sunit :
    heapq.heappush(tas, Char(i))
    pass
print(tas)