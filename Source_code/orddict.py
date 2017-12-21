# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from collections import Counter
cars = (
    ('Tesla', 'Model S'),
    ('BMW', '7 Series'),
    ('Daimler', 'S Class'),
    ('Tesla', 'Model X'),
    ('BMW', '5 Series'),
    ('Honda', 'NSX'),
)

preferred_cars_count = Counter(name for name, model in cars)
print(preferred_cars_count)
















