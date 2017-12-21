# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def startsWithA(name):
    return name[0]=='A'
def startsWithS(name):
    return name[0]=='S'
input = ["Acura", "AMG", "Subaru", "Suzuki"]
print (list(filter(startsWithA,input)))
print (list(filter(startsWithS, input)))

















