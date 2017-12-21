# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
new_list = ["Acura","Lincoln","Cadillac","BMW","Peugeot", 12]
print ("Length of the new_list is", len(new_list))
# following command prints "None" because append doesn't return any value
print (new_list.append("Verstappan")) 
print (new_list)
print (new_list.remove("Cadillac"))
print (new_list)
new_list.append("Cadillac")
print ("Popped element:", new_list.pop(4))
new_list.sort()
print ("Sorted list:", new_list)
print ("Reversed list:", new_list)













