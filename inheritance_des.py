# -*- coding: utf-8 -*-
"""
Created on Fri Feb 05 00:34:38 2016

@author: Geetha Yedida
"""

class Parent(object):
    def __init__(self,last_name,eye_color):
        print "Parent init"
        self.last_name = last_name
        self.eye_color = eye_color
        
    def show_info(self):
        print "LN: "+ self.last_name
        print "eye_color: "+ self.eye_color
        
class Child(Parent):
    def __init__(self,last_name,eye_color,num_of_toys):
        print "Child Class"
        Parent.__init__(self,last_name,eye_color)
        self.num_of_toys = num_of_toys
        
    def show_info(self):
        print "LN: "+ self.last_name
        print "eye_color: "+ self.eye_color
        print "Toys number :" + str(self.num_of_toys)
    
amitab = Parent("Bachan", "Brown")
#print "Parent eye color: " + amitab.eye_color

abhishek = Child("Bachan","Black",4)
#print "Child eye color: "+ abhishek.eye_color
print abhishek.show_info()