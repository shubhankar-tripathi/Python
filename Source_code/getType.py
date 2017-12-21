# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Dummy:
    pass
def import_class(name):
    components = name.split('.')
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    print(mod)
import_class('__main__.Dummy')








