# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class OddContainer:
    def __contains__(self, x):
        if not isinstance(x, int) or not x % 2:
            return False
        return True
from collections import Container
odd_container = OddContainer()
print (isinstance(odd_container, Container))
print (issubclass(OddContainer,Container))



