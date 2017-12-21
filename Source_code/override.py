# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Employee:
    def __init__(self,name):
        self.emp =name
    def getSalary(self):
        return 3000
class Lawyer(Employee):
    def __init__(self, name):
        super().__init__(name)
    def getSalary(self):
        baseSalary = super().getSalary()
        return baseSalary + 5000.00
guy = Lawyer("The New Guy")
print (guy.getSalary())

