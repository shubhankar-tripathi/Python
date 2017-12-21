# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def outer(func):
    def inner(name):
        return "Hey " + func(name)
    return inner
def f(name):
    return name + "!!!"
f = outer(f)
print (f("Bernie"))










