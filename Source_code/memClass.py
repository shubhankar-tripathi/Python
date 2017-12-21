# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class App:
    class InnerApp1:
        pass
    class __InnerApp2__:
        pass
obj = App()
attributes = dir(obj) 
print ([a for a in attributes if not(a.startswith('__') and a.endswith('__'))] )












