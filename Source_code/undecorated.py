# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def outer(func):
    def inner(name):
        return "Hey " + func(name)
    return inner
@outer
def f(name):
    return name + "!!!"
print (f("Bernie"))











