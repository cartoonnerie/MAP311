#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Token:
    """A class used to redifine the object used for comparison for
    other classes"""
    def __init__(self, value, comparison_value) :
        self.__value = value
        self.__comp = comparison_value
        pass
    
    ##Redifining all comparison to the object to use for comparison
    def __lt__(self, other):
        return self.__comp < other
    
    def __le__(self, other):
        return self.__comp <= other
    
    def __eq__(self, other):
        return self.__comp == other
    
    def __ge__(self, other):
        return self.__comp >= other
    
    def __gt__(self, other):
        return self.__comp > other
    
    ##redirecting all attribute access, functioncal, representation and so on
    ##to the original object
    def __str__(self):
        return self.__value.__str__()
        
    def __repr__(self):
        return self.__value.__repr__()
        
    def __getattr__(self, name):
        return self.__value.__getattribute__(name)
    
    def __hash__(self, *args):
        return self.__value.__hash__(*args)
        
        
        
class HuffTree:
    """Used to construct a Huffman Tree"""
    def __init__(self, value, childs=None):
        self.value = value
        if childs :
            self.left, self.right = childs
            self.__isLeaf = False
        else :
            self.__isLeaf = True #This particular tree is a leaf
            self.left, self.right = None, None
        pass
    
    def toDict(self, prefix=None) :
        """Recursively convert the whole tree to a dict representation
        with keys beeing the encoded word and values being the huffman code for that word"""
        #Prefix represents the first part of the coding, with is given by the parent tree
        if prefix == None:
            #No parent tree, calling with no prefix
            return self.toDict('')
            
        if self.__isLeaf:
            return {self.value: prefix}
        else:
            rep = {}
            rep.update(self.left.toDict(prefix + '0'))
            rep.update(self.right.toDict(prefix + '1'))
            return rep
        
    def __str__(self):
        return '[{value}, {left}, {right}]'.format(self)
    
    def __repr__(self):
        return 'HuffTree(%s, %s, %s)' % (self.value.__repr__(),
            self.left.__repr__(),
            self.right.__repr__())
            
        