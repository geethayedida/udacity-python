# -*- coding: utf-8 -*-
"""
Created on Thu Feb 04 15:41:18 2016

@author: Geetha Yedida
"""

import turtle

def draw_square():
    window = turtle.Screen()
    brad = turtle.Turtle()
    for i in range(36):    
        for i in range(4):
            brad.forward(100)
            brad.right(90)
        brad.right(10)
    window.exitonclick()

draw_square()
    