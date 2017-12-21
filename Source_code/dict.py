# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
new_set = {"Acura","Lincoln","Cadillac","BMW","Peugeot", 12}
print ("Length of the new_set is", len(new_set))
new_set.add("Subaru")
print (new_set)
new_set.add("Acura") #Adding a duplicate element
print (new_set.remove("Cadillac"))
print (new_set)
another_set = {"Mercedes", "Porche", "Jaguar", "Acura", "Peugeot"}
print (new_set.difference(another_set))
print (another_set.difference(new_set))
print (new_set.intersection(another_set))
print (new_set.union(another_set))
















