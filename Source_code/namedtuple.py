# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from collections import namedtuple
from enum import Enum

class Vehicles(Enum):
    Tesla= 1
    Bmw= 2
    Daimler = 3
cars = namedtuple('cars', 'make model')
car1 = cars(make=Vehicles.Tesla, model="ModelX")
car2 = cars(make=Vehicles.Bmw, model="M5")
car3 = cars(make=Vehicles.Daimler, model="E63AMG")
car4 = cars(make=Vehicles.Bmw, model="6Series")
print (car2.make==car4.make)
print (car2.make)

















