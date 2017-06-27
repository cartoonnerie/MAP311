#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Token:
    def __init__(self, value, comparison_value) :
        self.value = value
        self.comp = comparison_value
        pass
    
    def __lt__(self, other):
        return self.comp < other
    
    def __le__(self, other):
        return self.comp <= other
    
    def __eq__(self, other):
        return self.comp == other
    
    def __ge__(self, other):
        return self.comp >= other
    
    def __gt__(self, other):
        return self > other
        
    def __str__(self):
        return self.value.__str__()
        
    def __rep__(self):
        return self.value.__rep__()
    
        