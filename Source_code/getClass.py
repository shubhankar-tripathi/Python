# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class SuperApp:
    pass
class App(SuperApp):
    def get_super(self):
        for base in self.__class__.__bases__:
            print (base.__name__)
obj = App()
obj.get_super()









