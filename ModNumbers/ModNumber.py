# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 23:28:36 2018

@author: nilsh
"""

class ModNr:
    def __init__(self, new_value, mod):
        self.value = self.getValueFromType(new_value)
        self.mod = mod;
        
    def __neg__(self):
        new_value = (-self.value) % self.mod
        return ModNr(new_value, self.mod)
    
    def __iadd__(self, other_value):
        mn = (self.value + self.getValueFromType(other_value)) % self.mod
        self.value = mn
        return self
    def __add__(self, other_value):
        new_mod = ModNr(self.value, self.mod)
        new_mod += other_value
        return new_mod
    def __radd__(self, other_value):
        return self + other_value
    
    def __isub__(self, other_value):
        self.value = (self.value - self.getValueFromType(other_value)) % self.mod
        return self
    def __sub__(self, other_value):
        new_mod = ModNr(self.value, self.mod)
        new_mod -= other_value
        return new_mod
    def __rsub__(self, other_value):
        return -(self - other_value)
    
    def __imul__(self, other_value):
        self.value = (self.value * self.getValueFromType(other_value)) % self.mod
        return self
    def __mul__(self, other_value):
        new_mod = ModNr(self.value, self.mod)
        new_mod *= other_value
        return new_mod
    def __rmul__(self, other_value):
        return self * other_value
    
    def __str__(self):
        return str(self.value)

    def getValueFromType(self, other_value):
        if type(other_value) is int:
            return other_value
        elif type(other_value) is ModNr:
            if self.mod == other_value.mod:
                return other_value.value
            raise TypeError("Cannot add two ModNrs with different mods. One has " + str(self.mod) + "and other has" + str(other_value.mod))
        else:
            raise TypeError("ModNr cannot be added with type: " + str(type(other_value)))
            
            
if (__name__ == "__main__"):
    m = ModNr(4,10)
    print(m)
    m = m + 11
    print(m)
    m = m - 13
    print(m)
    m = 15 - m
    print(m)
    m = -m
    print(m)
    m = m * 2
    print(m)
    m += 3
    print(m)
    m *= 3
    print(m)
    m -= 9
    print(m)