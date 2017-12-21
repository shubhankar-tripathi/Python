# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Car:
    year = 2018
    make = "Tesla"
car = Car()
print('The car is manufactured by:', getattr(car, "make"))
print('The car is manufactured by:', car.make)







