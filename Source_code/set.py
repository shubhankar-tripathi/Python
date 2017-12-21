# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from collections import defaultdict

cars = (
    ('Tesla', 'Model S'),
    ('BMW', '7 Series'),
    ('Daimler', 'S Class'),
    ('VW', 'Passat'),
    ('Toyota', '86'),
    ('Honda', 'NSX'),
)

preferred_car = defaultdict(list)

for name, model in cars:
    preferred_car[name].append(model)

print(preferred_car)
















